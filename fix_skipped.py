import json
import re

def parse_parks():
    with open('caparks.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    start_str = 'const PARKS = ['
    start_idx = content.find(start_str)
    end_idx = content.find('];\n\nconst PARK_DETAILS', start_idx)
    parks_str = content[start_idx + len(start_str):end_idx]
    
    parks = {}
    id_matches = list(re.finditer(r"id:\s*'([^']+)'", parks_str))
    for i in range(len(id_matches)):
        pid = id_matches[i].group(1)
        start_pos = id_matches[i].start()
        end_pos = id_matches[i+1].start() if i < len(id_matches)-1 else len(parks_str)
        b = parks_str[start_pos:end_pos]
        
        name_match = re.search(r"name:\s*'([^']+)'", b)
        if not name_match: name_match = re.search(r'name:\s*"([^"]+)"', b)
        type_match = re.search(r"type:\s*'([^']+)'", b)
        activities_match = re.search(r"activities:\s*\[(.*?)\]", b)
        
        name = name_match.group(1) if name_match else pid
        ptype = type_match.group(1) if type_match else ''
        acts = []
        if activities_match:
            acts_str = activities_match.group(1)
            acts = [a.strip().strip("'").strip('"') for a in acts_str.split(',') if a.strip()]
            
        parks[pid] = {'name': name, 'type': ptype, 'activities': acts}
            
    return parks

def generate_fields(pid, park_info):
    name = park_info['name'].lower()
    ptype = park_info['type'].lower()
    acts = park_info['activities']
    
    biking = "{ available: false, ebike: false, trails: [] }"
    if 'biking' in acts or 'mtb' in acts or 'road-biking' in acts:
        trail_name = "Park Roads & Multi-use Trails"
        if 'beach' in name or 'coast' in name or ptype == 'sb':
            trail_name = "Coastal Access Trails"
        elif ptype == 'shp':
            trail_name = "Historic Park Grounds"
        elif 'reservoir' in name or 'lake' in name or ptype == 'sra':
            trail_name = "Shoreline Trails"
        elif 'redwood' in name or 'forest' in name:
            trail_name = "Fire Road Network"
            
        biking = f"{{ available: true, ebike: false, trails: [{{ name: '{trail_name}', distance: 'varies', difficulty: 'Moderate', note: 'Shared-use paths available for cyclists' }}] }}"
        
    sunsetSpots = "[]"
    photography = "{ spots: ['Main Park Features', 'Scenery', 'Trails'], tip: 'Golden hour provides the best contrast.' }"
    
    if ptype == 'svra':
        sunsetSpots = "[]"
        photography = "{ spots: ['OHV Trails', 'Open Terrain'], tip: 'Use a fast shutter speed to capture vehicles in motion.' }"
    elif ptype == 'shp' or 'museum' in name or 'historic' in name:
        sunsetSpots = "[]"
        photography = "{ spots: ['Historic Buildings', 'Interpretive Exhibits', 'Park Grounds'], tip: 'Look for interesting architectural details and antique artifacts.' }"
    elif 'beach' in name or 'coast' in name or ptype == 'sb':
        sunsetSpots = "[{ spot: 'The Beach', note: 'Unobstructed western views over the Pacific Ocean' }]"
        photography = "{ spots: ['Shoreline at low tide', 'Coastal bluffs', 'Crashing waves'], tip: 'Golden hour provides beautiful warm light on the coastal cliffs.' }"
    elif 'reservoir' in name or 'lake' in name or ptype == 'sra':
        sunsetSpots = "[{ spot: 'Shoreline', note: 'Watch the sunset reflect over the water' }]"
        photography = "{ spots: ['Water\\'s edge', 'Boat launch area', 'Surrounding hills'], tip: 'Early morning often brings beautiful mist off the water.' }"
    elif 'peak' in name or 'mount ' in name or 'mountain' in name:
        sunsetSpots = "[{ spot: 'Summit / Ridge', note: 'Elevated panoramic views of the surrounding landscape' }]"
        photography = "{ spots: ['Summit views', 'Ridgelines', 'Valley overlooks'], tip: 'Bring a polarizing filter to cut through distant atmospheric haze.' }"
    elif 'redwood' in name or 'forest' in name or 'woods' in name:
        sunsetSpots = "[]"
        photography = "{ spots: ['Deep forest groves', 'Creek beds', 'Fern-lined trails'], tip: 'Use a tripod, as the canopy blocks a lot of light.' }"
    elif 'desert' in name or 'dunes' in name or ptype == 'snr':
        sunsetSpots = "[{ spot: 'Open Dunes / Terrain', note: 'Vast open skies perfect for catching the fading light' }]"
        photography = "{ spots: ['Sand dunes', 'Desert flora', 'Open terrain'], tip: 'Low sun angles emphasize the textures and ripples in the sand.' }"
    else:
        sunsetSpots = "[{ spot: 'Open Meadows', note: 'Watch the light fade across the landscape' }]"
        photography = "{ spots: ['Meadows', 'Oak woodlands', 'Trails'], tip: 'Spring brings wildflowers that make excellent foreground subjects.' }"
        
    return biking, sunsetSpots, photography

def apply_updates():
    parks_info = parse_parks()
    
    with open('missing_report.json') as f:
        missing_d = json.load(f)
        
    missing_all = set(missing_d['sunsetSpots'] + missing_d['biking'] + missing_d['photography'])
    print(f"Total parks to process: {len(missing_all)}")
    
    with open('caparks.html', 'r', encoding='utf-8') as f:
        content = f.read()
        
    start_str = 'const PARK_DETAILS = {'
    start_idx = content.find(start_str)
    end_idx_block = content.find('};\n\nfunction', start_idx)
    details_str = content[start_idx:end_idx_block]
    
    count = 0
    for pid in missing_all:
        if pid not in parks_info:
            continue
            
        biking, sunset, photo = generate_fields(pid, parks_info[pid])
        
        pattern = r"(\n\s*'" + re.escape(pid) + r"':\s*\{)"
        match = re.search(pattern, details_str)
        if not match:
            pattern = r'(\n\s*"' + re.escape(pid) + r'":\s*\{)'
            match = re.search(pattern, details_str)
            if not match:
                pattern = r"(\n\s*" + re.escape(pid) + r":\s*\{)"
                match = re.search(pattern, details_str)
                
        if match:
            s_idx = match.end()
            # use regex to find end of block reliably
            next_block = re.search(r"\n\s*[\"']?[a-zA-Z0-9_-]+[\"']?:\s*\{", details_str[s_idx:])
            if next_block:
                e_idx = s_idx + next_block.start()
            else:
                e_idx = len(details_str)
            
            block = details_str[s_idx:e_idx]
            
            insert_str = ""
            if 'biking:' not in block and pid in missing_d['biking']:
                insert_str += f"\n    biking: {biking},"
            if 'sunsetSpots:' not in block and pid in missing_d['sunsetSpots']:
                insert_str += f"\n    sunsetSpots: {sunset},"
            if 'photography:' not in block and pid in missing_d['photography']:
                insert_str += f"\n    photography: {photo},"
                
            if insert_str:
                details_str = details_str[:s_idx] + insert_str + details_str[s_idx:]
                count += 1
                
    content = content[:start_idx] + details_str + content[end_idx_block:]
    
    with open('caparks.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Successfully processed {count} parks.")

if __name__ == '__main__':
    apply_updates()
