import re
import json

def analyze():
    with open('caparks.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    start_str = 'const PARK_DETAILS = {'
    start_idx = content.find(start_str)
    end_idx = content.find('};\n\nfunction', start_idx)
    details_str = content[start_idx + len(start_str):end_idx]
    
    matches = list(re.finditer(r"\n\s*'([^']+)':\s*\{", details_str))
    if not matches:
        matches = list(re.finditer(r'\n\s*"([^"]+)":\s*\{', details_str))
    if not matches:
        matches = list(re.finditer(r'\n\s*([a-zA-Z0-9_-]+):\s*\{', details_str))
        
    missing = {
        'googleRating': [],
        'googleReviews': [],
        'parkingTip': [],
        'entranceFee': [],
        'gain': [],
        'sunsetSpots': [],
        'biking': [],
        'photography': []
    }
    
    for i in range(len(matches)):
        park_id = matches[i].group(1)
        start_pos = matches[i].end()
        end_pos = matches[i+1].start() if i < len(matches)-1 else len(details_str)
        c = details_str[start_pos:end_pos]
        
        if 'googleRating:' not in c: missing['googleRating'].append(park_id)
        if 'googleReviews:' not in c: missing['googleReviews'].append(park_id)
        if 'parkingTip:' not in c: missing['parkingTip'].append(park_id)
        if 'entranceFee:' not in c: missing['entranceFee'].append(park_id)
        if 'sunsetSpots:' not in c: missing['sunsetSpots'].append(park_id)
        if 'biking:' not in c: missing['biking'].append(park_id)
        if 'photography:' not in c: missing['photography'].append(park_id)
        
        # for gain, it's specific to the 'hikes' array if it exists.
        # the prompt says "95 hike entries missing `gain` field" ... "Some hike objects have {name, ...} but missing `gain`"
        # Let's count how many hike entries are actually missing gain.
        hikes_match = re.search(r'hikes:\s*\[(.*?)\]', c, re.DOTALL)
        if hikes_match:
            hikes_str = hikes_match.group(1)
            # Find all objects in hikes_str
            hike_objs = re.findall(r'\{[^\}]+\}', hikes_str)
            for ho in hike_objs:
                if 'gain:' not in ho:
                    missing['gain'].append(park_id)
                    break # just record the park for now
                    
    for k, v in missing.items():
        print(f"{k}: {len(v)} missing")
        
    with open('missing_report.json', 'w') as f:
        json.dump(missing, f, indent=2)

if __name__ == '__main__':
    analyze()
