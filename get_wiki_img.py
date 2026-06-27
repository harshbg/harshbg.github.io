import requests
import urllib.parse
headers = {"User-Agent": "AntigravityBot/1.0 (contact@example.com)"}
def get_wiki(keyword):
    # Search for the page title first
    search_url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(keyword)}&utf8=&format=json"
    try:
        r = requests.get(search_url, headers=headers).json()
        if r['query']['search']:
            title = r['query']['search'][0]['title']
            # Now get the main image for this page
            img_url = f"https://en.wikipedia.org/w/api.php?action=query&prop=pageimages&titles={urllib.parse.quote(title)}&pithumbsize=1000&format=json"
            r2 = requests.get(img_url, headers=headers).json()
            pages = r2['query']['pages']
            for p in pages.values():
                if 'thumbnail' in p:
                    return p['thumbnail']['source']
    except Exception as e:
        pass
    return None

print(get_wiki('Multnomah Falls Oregon'))
print(get_wiki('Crater Lake Rim Village Oregon'))
print(get_wiki('Bandon Beach Oregon'))
