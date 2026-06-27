import os
import time
import urllib.parse
import subprocess
import json

assets_dir = 'oregon-assets'
images = sorted([f for f in os.listdir(assets_dir) if f.endswith('.jpg')])

def get_unsplash_image(query):
    url = f"https://unsplash.com/napi/search/photos?query={urllib.parse.quote(query)}&per_page=1"
    try:
        # Use curl to avoid python requests being blocked by Cloudflare/Unsplash
        result = subprocess.run(["curl", "-s", url], capture_output=True, text=True)
        if result.returncode == 0:
            data = json.loads(result.stdout)
            if data.get('results'):
                return data['results'][0]['urls']['regular']
    except Exception as e:
        print("Error with curl Unsplash API:", e)
    return None

for image in images:
    filepath = os.path.join(assets_dir, image)
    keyword = image.replace('.jpg', '').replace('-', ' ') + ' Oregon'
    print(f"Searching for: {keyword} ...")
    
    img_url = get_unsplash_image(keyword)
        
    if img_url:
        try:
            # Download image using curl
            print(f"  Downloading {img_url}")
            subprocess.run(["curl", "-s", "-o", filepath, img_url])
            print(f"  [OK] Saved {filepath}")
        except Exception as e:
            print(f"  [ERROR] {e}")
    else:
        print("  [FAIL] No image found")
        
    time.sleep(0.5)

print("Finished replacing images.")
