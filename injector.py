import re
import json

def get_blocks(content):
    start_str = 'const PARK_DETAILS = {'
    start_idx = content.find(start_str)
    end_idx = content.find('};\n\nfunction', start_idx)
    details_str = content[start_idx + len(start_str):end_idx]
    
    matches = list(re.finditer(r"\n\s*'([^']+)':\s*\{", details_str))
    if not matches:
        matches = list(re.finditer(r'\n\s*"([^"]+)":\s*\{', details_str))
    if not matches:
        matches = list(re.finditer(r'\n\s*([a-zA-Z0-9_-]+):\s*\{', details_str))
        
    blocks = {}
    for i in range(len(matches)):
        park_id = matches[i].group(1)
        start_pos = matches[i].end()
        if i < len(matches) - 1:
            end_pos = matches[i+1].start()
        else:
            end_pos = len(details_str)
            
        blocks[park_id] = {
            'start_idx': start_idx + len(start_str) + start_pos,
            'end_idx': start_idx + len(start_str) + end_pos,
            'text': details_str[start_pos:end_pos]
        }
    return blocks

def inject_data(park_data):
    with open('caparks.html', 'r', encoding='utf-8') as f:
        content = f.read()
        
    blocks = get_blocks(content)
    
    # We apply from bottom to top so indices don't shift!
    sorted_parks = sorted([p for p in park_data.keys() if p in blocks], key=lambda x: blocks[x]['start_idx'], reverse=True)
    
    for park_id in sorted_parks:
        new_d = park_data[park_id]
        block = blocks[park_id]['text']
        start_idx = blocks[park_id]['start_idx']
        
        insert_str = ""
        if 'biking:' not in block and 'biking' in new_d:
            insert_str += f"\n    biking: {new_d['biking']},"
        if 'photography:' not in block and 'photography' in new_d:
            insert_str += f"\n    photography: {new_d['photography']},"
        if 'sunsetSpots:' not in block and 'sunsetSpots' in new_d:
            insert_str += f"\n    sunsetSpots: {new_d['sunsetSpots']},"
        if 'googleRating:' not in block and 'googleRating' in new_d:
            insert_str += f"\n    googleRating: {new_d['googleRating']},"
        if 'googleReviews:' not in block and 'googleReviews' in new_d:
            insert_str += f"\n    googleReviews: {new_d['googleReviews']},"
            
        content = content[:start_idx] + insert_str + content[start_idx:]
        
    with open('caparks.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Injected data for {len(sorted_parks)} parks cleanly.")

if __name__ == '__main__':
    from enrich_grounded_1 import data as data1
    inject_data(data1)
