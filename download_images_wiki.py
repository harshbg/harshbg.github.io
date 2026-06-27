import os
import requests
import time
import urllib.parse

assets_dir = 'oregon-assets'
images = sorted([f for f in os.listdir(assets_dir) if f.endswith('.jpg')])

headers = {"User-Agent": "AntigravityBot/1.0 (contact@example.com)"}

def get_wiki_image(keyword):
    # 1. Search Wikipedia for the best matching article
    search_url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(keyword)}&utf8=&format=json"
    try:
        r = requests.get(search_url, headers=headers, timeout=10).json()
        if r.get('query') and r['query'].get('search'):
            title = r['query']['search'][0]['title']
            # 2. Get the main image thumbnail for that article
            img_url = f"https://en.wikipedia.org/w/api.php?action=query&prop=pageimages&titles={urllib.parse.quote(title)}&pithumbsize=1000&format=json"
            r2 = requests.get(img_url, headers=headers, timeout=10).json()
            if r2.get('query') and r2['query'].get('pages'):
                pages = r2['query']['pages']
                for p_id, p_data in pages.items():
                    if 'thumbnail' in p_data:
                        return p_data['thumbnail']['source']
    except Exception as e:
        print(f"    [Error] {e}")
    return None

for image in images:
    # Skip dummy stops
    if 'wfh' in image.lower() or 'drive-back' in image.lower():
        continue
        
    filepath = os.path.join(assets_dir, image)
    # The image filename uses hyphens, let's make it a clean search phrase
    keyword = image.replace('.jpg', '').replace('-', ' ') + ' Oregon'
    print(f"Searching Wikipedia for: {keyword} ...")
    
    img_url = get_wiki_image(keyword)
        
    if img_url:
        try:
            print(f"  Downloading {img_url}")
            img_resp = requests.get(img_url, headers=headers, timeout=10)
            if img_resp.status_code == 200:
                with open(filepath, 'wb') as f:
                    f.write(img_resp.content)
                print(f"  [OK] Saved {filepath}")
            else:
                print(f"  [FAIL] Could not download image {img_resp.status_code}")
        except Exception as e:
            print(f"  [ERROR] {e}")
    else:
        print("  [FAIL] No image found on Wikipedia")
        
    time.sleep(0.5)

print("Finished replacing images with Wikipedia accurate photos.")
