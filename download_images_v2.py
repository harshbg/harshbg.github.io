import os
import requests
import time
import urllib.parse
from bs4 import BeautifulSoup
import json

assets_dir = 'oregon-assets'
images = sorted([f for f in os.listdir(assets_dir) if f.endswith('.jpg')])

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

def get_google_image(query):
    url = f"https://www.google.com/search?q={urllib.parse.quote(query)}&tbm=isch"
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'html.parser')
            for img in soup.find_all("img"):
                src = img.get('src')
                if src and src.startswith('http') and 'images' in src:
                    return src
                elif src and src.startswith('http') and 'gstatic' in src:
                    return src
    except Exception as e:
        pass
    return None

def get_unsplash_image(query):
    url = f"https://unsplash.com/napi/search/photos?query={urllib.parse.quote(query)}&per_page=1"
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            if data.get('results'):
                return data['results'][0]['urls']['regular']
    except Exception:
        pass
    return None

for image in images:
    filepath = os.path.join(assets_dir, image)
    keyword = image.replace('.jpg', '').replace('-', ' ') + ' Oregon'
    print(f"Searching for: {keyword} ...")
    
    # Try google image first (often returns a thumbnail, but it's specific)
    img_url = get_google_image(keyword)
    
    if not img_url:
        print("  Falling back to Unsplash")
        img_url = get_unsplash_image(keyword)
        
    if img_url:
        try:
            img_resp = requests.get(img_url, headers=headers, timeout=10)
            if img_resp.status_code == 200:
                with open(filepath, 'wb') as f:
                    f.write(img_resp.content)
                print(f"  [OK] Saved {filepath}")
            else:
                print(f"  [FAIL] Download failed {img_resp.status_code}")
        except Exception as e:
            print(f"  [ERROR] {e}")
    else:
        print("  [FAIL] No image found")
        
    time.sleep(0.5)

print("Finished replacing images.")
