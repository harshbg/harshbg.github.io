import re

biking_parks = ['jedediah-smith', 'del-norte-coast', 'tolowa-dunes', 'benbow-lake', 'fort-humboldt', 'sue-meg', 'hendy-woods', 'cotoni-coast-dairies', 'montana-de-oro', 'fort-ord-dunes', 'wilder-ranch', 'auburn-sra', 'folsom-lake', 'burton-creek', 'pacheco-sp', 'crystal-cove', 'malibu-creek', 'cuyamaca-rancho', 'chino-hills', 'kenneth-hahn', 'los-angeles-shp', 'rio-de-la', 'topanga-sp', 'huntington-sb', 'lake-perris', 'silverwood-lake', 'san-buenaventura-sb', 'crown-memorial-sb', 'martial-cottle', 'santa-monica-sb', 'will-rogers-sb', 'almaden-quicksilver', 'calero', 'coyote-creek-parkway', 'coyote-lake-harvey-bear', 'hellyer', 'joseph-grant', 'los-gatos-creek', 'penitencia-creek', 'rancho-san-antonio', 'stevens-creek', 'sunnyvale-baylands', 'upper-stevens-creek', 'vasona-lake']

def get_biking_gain(dist_str, diff, name):
    name_lower = name.lower()
    
    try:
        dist = float(dist_str.replace(' mi', '').replace('+', '').replace('varies', '3.0'))
    except:
        dist = 3.0
        
    if diff == 'Easy' or 'flat' in name_lower or 'beach' in name_lower or 'shore' in name_lower or 'creek' in name_lower or 'baylands' in name_lower or 'river' in name_lower:
        return 'Flat'
        
    mult = 150
    if diff == 'Hard': mult = 400
    elif diff == 'Moderate': mult = 200
    
    if 'ridge' in name_lower or 'peak' in name_lower or 'hill' in name_lower:
        mult += 100
        
    val = int(dist * mult)
    val = max(50, round(val / 50) * 50)
    
    if val <= 50 and diff == 'Easy': return 'Flat'
    return f"~{val:,} ft"

def process():
    with open('caparks.html', 'r', encoding='utf-8') as f:
        content = f.read()
        
    start_str = 'const PARK_DETAILS = {'
    start_idx = content.find(start_str)
    end_idx_block = content.find('};\n\nfunction', start_idx)
    details_str = content[start_idx:end_idx_block]
    
    count = 0
    # For each park, find its block
    for pid in biking_parks:
        # Find start of block
        pattern = r"(\n\s*['\"]?" + re.escape(pid) + r"['\"]?:\s*\{)"
        match = re.search(pattern, details_str)
        
        if not match:
            # print(f"Not found: {pid}")
            continue
            
        s_idx = match.start()
        
        # Find the next park to set e_idx
        next_block = re.search(r"\n\s*[\"']?[a-zA-Z0-9_-]+[\"']?:\s*\{", details_str[s_idx+10:])
        if next_block: 
            e_idx = s_idx + 10 + next_block.start()
        else: 
            e_idx = len(details_str)
            
        block = details_str[s_idx:e_idx]
        
        # Find biking line
        biking_match = re.search(r"(biking:\s*\{.*?trails:\s*\[([^\]]*)\][^\}]*\})", block, re.DOTALL)
        if not biking_match:
            continue
            
        full_biking = biking_match.group(1)
        trails_str = biking_match.group(2)
        
        new_trails_str = trails_str
        
        # Extract trail objects using a more generic regex
        # Each trail object looks like { name: '...', distance: '...', difficulty: '...', note: '...' }
        trail_objects = list(re.finditer(r"\{([^}]+)\}", trails_str))
        
        for t_match in trail_objects:
            t_full = t_match.group(0)
            t_inner = t_match.group(1)
            
            if 'gain:' in t_inner:
                continue
                
            n_match = re.search(r"name:\s*'([^']+)'", t_inner)
            d_match = re.search(r"distance:\s*'([^']+)'", t_inner)
            df_match = re.search(r"difficulty:\s*'([^']+)'", t_inner)
            
            if not (n_match and d_match and df_match):
                continue
                
            name = n_match.group(1)
            dist = d_match.group(1)
            diff = df_match.group(1)
            
            gain_val = get_biking_gain(dist, diff, name)
            
            dist_full = d_match.group(0)
            new_t_inner = t_inner.replace(dist_full, f"{dist_full}, gain: '{gain_val}'")
            new_t_full = t_full.replace(t_inner, new_t_inner)
            
            new_trails_str = new_trails_str.replace(t_full, new_t_full)
            count += 1
            
        new_full_biking = full_biking.replace(trails_str, new_trails_str)
        # We must carefully replace just the full_biking string in the details_str so we don't mess up indices
        details_str = details_str[:s_idx] + block.replace(full_biking, new_full_biking) + details_str[e_idx:]
        
    content = content[:start_idx] + details_str + content[end_idx_block:]
    
    with open('caparks.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Injected gain for {count} biking trails.")

if __name__ == '__main__':
    process()
