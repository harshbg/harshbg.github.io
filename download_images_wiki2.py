import os
import requests
import time
import urllib.parse
import subprocess

assets_dir = 'oregon-assets'
images = sorted([f for f in os.listdir(assets_dir) if f.endswith('.jpg')])

headers = {"User-Agent": "TravelPlannerBot/2.0 (learning@example.com)"}

def get_wiki_image(keyword):
    search_url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(keyword)}&utf8=&format=json"
    try:
        r = requests.get(search_url, headers=headers, timeout=10).json()
        if r.get('query') and r['query'].get('search'):
            title = r['query']['search'][0]['title']
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
    if 'wfh' in image.lower() or 'drive-back' in image.lower():
        continue
        
    filepath = os.path.join(assets_dir, image)
    
    # Check if the file is a generic placeholder or an Unsplash image (Unsplash images were downloaded in a previous script, we want to replace ALL of them with Wiki OR we just replace the ones that we didn't get from Wiki)
    # Actually let's just get the ones that still need replacing.
    size = os.path.getsize(filepath)
    # The wiki images successfully downloaded so far have various sizes. Unsplash sizes vary too.
    # The ones that failed on the last run are currently either generic placeholders or Unsplash photos.
    # We want ALL of them to be accurate Wikipedia photos. Let's just check if it's one of the ones that failed Wikipedia earlier.
    # I'll just check the file modify time! If it was modified in the last 2 minutes, it's a Wiki image.
    if time.time() - os.path.getmtime(filepath) < 120:
        continue # Already updated by Wiki script

    keyword = image.replace('.jpg', '').replace('-', ' ') + ' Oregon'
    print(f"Searching Wikipedia for: {keyword} ...")
    
    img_url = get_wiki_image(keyword)
        
    if img_url:
        try:
            print(f"  Downloading {img_url}")
            subprocess.run(["curl", "-s", "-A", "Mozilla/5.0", "-L", "-o", filepath, img_url])
            print(f"  [OK] Saved {filepath}")
        except Exception as e:
            print(f"  [ERROR] {e}")
    else:
        print("  [FAIL] No image found on Wikipedia")
        
    time.sleep(1)

print("Finished replacing remaining images.")
