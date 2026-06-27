import requests
import urllib.parse
from bs4 import BeautifulSoup
import re
import json

url = "https://www.bing.com/images/search?q=" + urllib.parse.quote("multnomah falls oregon")
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
for a in soup.find_all('a', class_='iusc'):
    m = json.loads(a.get('m', '{}'))
    if 'murl' in m:
        print(m['murl'])
        break
