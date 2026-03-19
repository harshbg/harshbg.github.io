import re

def process_inflated():
    with open('caparks.html', 'r', encoding='utf-8') as f:
        content = f.read()

    def replacer(match):
        full_str = match.group(0)
        name = match.group(1)
        dist_str = match.group(2)
        gain = int(match.group(3).replace(',', ''))
        
        try:
            dist = float(dist_str.replace(' mi', '').replace('+', ''))
        except:
            dist = 5.0
            
        new_gain = gain
        
        # Hardcodes based on user feedback and general knowledge
        name_lower = name.lower()
        if 'mt. st. helena' in name_lower or 'mount st. helena' in name_lower:
            new_gain = 2100
        elif 'south gate road' in name_lower and 'summit' in name_lower:
            new_gain = 3300
        elif 'avenue of the giants' in name_lower:
            new_gain = 300
        elif 'pinto basin' in name_lower:
            new_gain = 500
        elif 'titus canyon' in name_lower:
            new_gain = 2000
        elif 'park boulevard' in name_lower:
            new_gain = 400
        elif 'bridge to nowhere' in name_lower:
            new_gain = 1000
        elif 'hunting hollow' in name_lower and 'coe' in name_lower:
            new_gain = 2500
        elif gain >= 3000:
            # Overly aggressive multiplier fix for long trails
            # Max realistic gain per mile for a generic 'hard' trail is ~300 ft/mi
            max_gain = int(dist * 300)
            if 'road' in name_lower:
                max_gain = int(dist * 150)
                
            if gain > max_gain:
                new_gain = max_gain
                # round to 50
                new_gain = max(50, round(new_gain / 50) * 50)
                
        if new_gain != gain:
            new_str = full_str.replace(f"gain: '~{match.group(3)}", f"gain: '~{new_gain:,}")
            new_str = new_str.replace(f"gain: '~{match.group(3)}'", f"gain: '~{new_gain:,}'")
            return new_str
            
        return full_str

    # Match hikename, distance, and gain
    # name: '...', distance: '...', gain: '~5,550 ft'
    pattern = r"name:\s*'([^']+)'[^}]*distance:\s*'([^']+)'[^}]*gain:\s*'~([0-9,]+)\s*ft'"
    content = re.sub(pattern, replacer, content)

    with open('caparks.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Fixed inflated gains.")

if __name__ == '__main__':
    process_inflated()
