import os
import requests
from duckduckgo_search import DDGS
import time
import socket

# Set timeout for socket
socket.setdefaulttimeout(10)

assets_dir = 'oregon-assets'
images = sorted([f for f in os.listdir(assets_dir) if f.endswith('.jpg')])

ddgs = DDGS()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

for image in images:
    filepath = os.path.join(assets_dir, image)
    keyword = image.replace('.jpg', '').replace('-', ' ') + ' Oregon'
    print(f"Searching for: {keyword} ...")
    
    try:
        results = ddgs.images(keywords=keyword, max_results=5)
        success = False
        if results:
            for result in results:
                image_url = result.get('image')
                if not image_url: continue
                
                print(f"  Trying {image_url} ...")
                try:
                    resp = requests.get(image_url, headers=headers, timeout=10)
                    if resp.status_code == 200 and 'image' in resp.headers.get('Content-Type', ''):
                        with open(filepath, 'wb') as f:
                            f.write(resp.content)
                        print(f"  [OK] Saved {filepath}")
                        success = True
                        break
                    else:
                        print(f"  [FAIL] HTTP {resp.status_code} or not an image.")
                except Exception as e:
                    print(f"  [ERROR] {e}")
                time.sleep(0.5)
        
        if not success:
            print(f"  [WARN] Could not find or download an image for {keyword}")
            
    except Exception as e:
        print(f"  [FATAL ERROR] {e}")
    
    time.sleep(1)

print("Finished replacing images.")
