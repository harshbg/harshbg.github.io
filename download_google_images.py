import os
import requests
import time
import urllib.parse
from bs4 import BeautifulSoup
import base64

assets_dir = 'oregon-assets'
images = sorted([f for f in os.listdir(assets_dir) if f.endswith('.jpg')])

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

for image in images:
    filepath = os.path.join(assets_dir, image)
    keyword = image.replace('.jpg', '').replace('-', ' ') + ' Oregon'
    print(f"Searching for: {keyword} ...")
    
    url = f"https://www.google.com/search?q={urllib.parse.quote(keyword)}&tbm=isch"
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'html.parser')
            # The first few images are often base64 embedded or use gstatic.
            # We look for the first <img> tag that actually contains an image, skipping the google logo.
            img_src = None
            for img in soup.find_all('img'):
                src = img.get('src')
                if not src:
                    continue
                if 'nav_logo' in src or 'text' in src or 'branding' in src:
                    continue
                if src.startswith('data:image'):
                    img_src = src
                    break
                elif src.startswith('https://encrypted-tbn0.gstatic.com/images'):
                    img_src = src
                    break
            
            if img_src:
                print(f"  Found Google Image thumbnail")
                if img_src.startswith('data:image'):
                    # decode base64
                    header, encoded = img_src.split(",", 1)
                    with open(filepath, 'wb') as f:
                        f.write(base64.b64decode(encoded))
                    print(f"  [OK] Saved base64 {filepath}")
                else:
                    img_resp = requests.get(img_src, headers=headers, timeout=10)
                    if img_resp.status_code == 200:
                        with open(filepath, 'wb') as f:
                            f.write(img_resp.content)
                        print(f"  [OK] Saved url {filepath}")
                    else:
                        print(f"  [FAIL] Could not download image url {img_resp.status_code}")
            else:
                print(f"  [FAIL] No image found in Google Images HTML")
        else:
            print(f"  [FAIL] Google returned {resp.status_code}")
    except Exception as e:
        print(f"  [ERROR] {e}")
        
    time.sleep(1)

print("Finished replacing images.")
