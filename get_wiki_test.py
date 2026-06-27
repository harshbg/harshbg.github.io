import requests
import urllib.parse
headers = {"User-Agent": "AntigravityBot/1.0 (contact@example.com)"}
def get_wiki(keyword):
    search_url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(keyword)}&utf8=&format=json"
    try:
        r = requests.get(search_url, headers=headers).json()
        if r['query']['search']:
            title = r['query']['search'][0]['title']
            img_url = f"https://en.wikipedia.org/w/api.php?action=query&prop=pageimages&titles={urllib.parse.quote(title)}&pithumbsize=1000&format=json"
            r2 = requests.get(img_url, headers=headers).json()
            pages = r2['query']['pages']
            for p in pages.values():
                if 'thumbnail' in p:
                    return p['thumbnail']['source']
    except Exception:
        pass
    return None

print("Phantom Ship:", get_wiki('Phantom Ship Crater Lake Oregon'))
print("Yaquina Head:", get_wiki('Yaquina Head Lighthouse Oregon'))
print("Trillium Lake:", get_wiki('Trillium Lake Oregon'))
