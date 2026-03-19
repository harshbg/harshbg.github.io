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
        # Match from pid to the next '},' or end of string
        pattern = r"(\n\s*['\"]?" + re.escape(pid) + r"['\"]?:\s*\{)(.*?)(?=\n\s*\},|\n\},|\n\s*[a-zA-Z0-9_-]+:)"
        match = re.search(pattern, content, re.DOTALL)
        if not match:
            print("Block not found:", pid)
            continue

        prefix = match.group(1)
        block = match.group(2)

        # Process trails
        def replacer(t_match):
            nonlocal count
            t_inner = t_match.group(1)
            
            if 'gain:' in t_inner: return t_match.group(0)
                
            n_match = re.search(r"name:\s*'([^']+)'", t_inner)
            d_match = re.search(r"distance:\s*'([^']+)'", t_inner)
            df_match = re.search(r"difficulty:\s*'([^']+)'", t_inner)
            
            if not (n_match and d_match and df_match): return t_match.group(0)
                
            name = n_match.group(1)
            dist = d_match.group(1)
            diff = df_match.group(1)
            
            gain_val = get_biking_gain(dist, diff, name)
            dist_full = d_match.group(0)
            
            new_inner = t_inner.replace(dist_full, f"{dist_full}, gain: '{gain_val}'")
            count += 1
            return "{" + new_inner + "}"

        # only process the biking trails array so we don't accidentally modify hikes
        biking_match = re.search(r"(biking:\s*\{.*?trails:\s*\[)([^\]]*)(\])", block, re.DOTALL)
        if biking_match:
            b_prefix = biking_match.group(1)
            b_array = biking_match.group(2)
            b_suffix = biking_match.group(3)
            
            new_b_array = re.sub(r"\{([^}]+)\}", replacer, b_array)
            new_block = block.replace(b_prefix + b_array + b_suffix, b_prefix + new_b_array + b_suffix)
            
            content = content.replace(prefix + block, prefix + new_block)

    with open('caparks.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Injected gain for {count} biking trails.")

if __name__ == '__main__':
    process()
