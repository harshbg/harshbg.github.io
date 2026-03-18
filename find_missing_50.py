import json
import re

def get_missing():
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
        
    missing_parks = []
    
    for i in range(len(matches)):
        park_id = matches[i].group(1)
        start_pos = matches[i].end()
        end_pos = matches[i+1].start() if i < len(matches)-1 else len(details_str)
        c = details_str[start_pos:end_pos]
        
        missing = False
        if 'biking:' not in c: missing = True
        elif 'photography:' not in c: missing = True
        elif 'sunsetSpots:' not in c: missing = True
        elif 'googleRating:' not in c: missing = True
        elif 'googleReviews:' not in c: missing = True
        elif "gain:'—'" in c or "gain: '—'" in c: missing = True
        
        if missing:
            missing_parks.append(park_id)
            
    return missing_parks

print(json.dumps(get_missing()[:50], indent=2))
