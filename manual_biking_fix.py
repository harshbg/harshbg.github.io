import re

biking_parks = ['jedediah-smith', 'del-norte-coast', 'tolowa-dunes', 'benbow-lake', 'fort-humboldt', 'sue-meg', 'hendy-woods', 'cotoni-coast-dairies', 'montana-de-oro', 'fort-ord-dunes', 'wilder-ranch', 'auburn-sra', 'folsom-lake', 'burton-creek', 'pacheco-sp', 'crystal-cove', 'malibu-creek', 'cuyamaca-rancho', 'chino-hills', 'kenneth-hahn', 'los-angeles-shp', 'rio-de-la', 'topanga-sp', 'huntington-sb', 'lake-perris', 'silverwood-lake', 'san-buenaventura-sb', 'crown-memorial-sb', 'martial-cottle', 'santa-monica-sb', 'will-rogers-sb', 'almaden-quicksilver', 'calero', 'coyote-creek-parkway', 'coyote-lake-harvey-bear', 'hellyer', 'joseph-grant', 'los-gatos-creek', 'penitencia-creek', 'rancho-san-antonio', 'stevens-creek', 'sunnyvale-baylands', 'upper-stevens-creek', 'vasona-lake']

def get_biking_gain(dist_str, diff, name):
    name_lower = name.lower()
    try: dist = float(dist_str.replace(' mi', '').replace('+', '').replace('varies', '3.0'))
    except: dist = 3.0
    if diff == 'Easy' or 'flat' in name_lower or 'beach' in name_lower or 'shore' in name_lower or 'creek' in name_lower or 'baylands' in name_lower or 'river' in name_lower:
        return 'Flat'
    mult = 150
    if diff == 'Hard': mult = 400
    elif diff == 'Moderate': mult = 200
    if 'ridge' in name_lower or 'peak' in name_lower or 'hill' in name_lower: mult += 100
    val = int(dist * mult)
    val = max(50, round(val / 50) * 50)
    if val <= 50 and diff == 'Easy': return 'Flat'
    return f"~{val:,} ft"

def process():
    with open('caparks.html', 'r', encoding='utf-8') as f:
        content = f.read()

    count = 0
    for pid in biking_parks:
        # Locate the exact biking string
        p_idx = content.find(f"'{pid}':")
        if p_idx == -1: p_idx = content.find(f'"{pid}":')
        if p_idx == -1: p_idx = content.find(f'{pid}:')
        if p_idx == -1:
            print("Park not found", pid)
            continue
            
        biking_idx = content.find('biking:', p_idx)
        line_match = re.search(r"biking:\s*\{[^}]*trails:\s*\[(.*?)\]\s*\}", content[biking_idx:biking_idx+1000], flags=re.DOTALL)
        
        if not line_match:
            # print("No biking trails found for", pid)
            continue
            
        full_biking = line_match.group(0)
        trails_str = line_match.group(1)
        
        new_trails_str = trails_str
        for t_match in re.finditer(r"(\{([^}]+)\})", trails_str):
            t_full = t_match.group(0)
            t_inner = t_match.group(2)
            
            if 'gain:' in t_inner: continue
                
            n_match = re.search(r"name:\s*'([^']+)'", t_inner)
            d_match = re.search(r"distance:\s*'([^']+)'", t_inner)
            df_match = re.search(r"difficulty:\s*'([^']+)'", t_inner)
            
            if not (n_match and d_match and df_match): continue
                
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
        content = content[:biking_idx] + content[biking_idx:biking_idx+1000].replace(full_biking, new_full_biking) + content[biking_idx+1000:]

    with open('caparks.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Injected gain for {count} biking trails.")

if __name__ == '__main__':
    process()
