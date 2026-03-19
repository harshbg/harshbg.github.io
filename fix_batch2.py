import re, json

data = {
    'plumas-eureka': {'entranceFee': "'$8/vehicle'", 'parkingTip': "'Large lot near museum, fills up by midday on summer weekends.'"},
    'auburn-sra': {'entranceFee': "'$10/vehicle'", 'parkingTip': "'Multiple access points; Confluence area parking fills extremely fast by 8am, park on shoulder where permitted.'"},
    'folsom-lake': {'entranceFee': "'$12/vehicle'", 'parkingTip': "'Massive parking lots at Granite Bay and Beal\\'s Point, rarely completely full.'"},
    'washoe-meadows': {'entranceFee': "'Free'", 'parkingTip': "'Limited free parking at the end of San Juan Drive. No facilities.'"},
    'millerton-lake': {'entranceFee': "'$10/vehicle'", 'parkingTip': "'Plentiful parking on north and south shores.'"},
    'burton-creek': {'entranceFee': "'Free'", 'parkingTip': "'Very limited makeshift parking near Tahoe City behind the school.'"},
    'kings-beach': {'entranceFee': "'$10/vehicle'", 'parkingTip': "'Paid lot right at the beach, fills up early in summer; street parking also available.'"},
    'tahoe-sra': {'entranceFee': "'$10/vehicle'", 'parkingTip': "'Very small lot, usually full in peak season; walking distance from Tahoe City transit.'"},
    'ward-creek': {'entranceFee': "'Free'", 'parkingTip': "'Informal dirt pullouts along Ward Creek Blvd.'"},
    'marshall-gold': {'entranceFee': "'$10/vehicle'", 'parkingTip': "'Multiple large lots throughout the town of Coloma.'"},
    'malakoff-diggins': {'entranceFee': "'$10/vehicle'", 'parkingTip': "'Ample parking near the visitor center and Chute Hill campground.'"},
    'south-yuba-river': {'entranceFee': "'$10/vehicle'", 'parkingTip': "'Bridgeport lot fills very fast in summer; arrive by 9am.'"},
    'brannan-island': {'entranceFee': "'$10/vehicle'", 'parkingTip': "'Plenty of parking for boat trailers and day use.'"},
    'folsom-powerhouse': {'entranceFee': "'$10/vehicle'", 'parkingTip': "'Small dedicated lot right next to the historic buildings in historic Folsom.'"},
    'delta-meadows': {'entranceFee': "'Free'", 'parkingTip': "'Very little official parking, usually accessed by boat from Walnut Grove.'"},
    'locke-boarding-house': {'entranceFee': "'Free'", 'parkingTip': "'Free street parking in the historic town of Locke.'"},
    'stone-lake': {'entranceFee': "'Free'", 'parkingTip': "'Access is restricted; parking available at the Blue Heron Trails hub.'"},
    'bidwell-mansion': {'entranceFee': "'Free'", 'parkingTip': "'Small lot at the mansion in downtown Chico.'"},
    'bidwell-sacramento': {'entranceFee': "'Free'", 'parkingTip': "'Several day-use parking areas along the river segments.'"},
    'lake-oroville': {'entranceFee': "'$10/vehicle'", 'parkingTip': "'Huge capacity across multiple launch ramps and day-use areas.'"},
    'colusa-sacramento': {'entranceFee': "'$7/vehicle'", 'parkingTip': "'Plenty of parking near the boat ramp and picnic areas.'"},
    'ahjumawi': {'entranceFee': "'Free'", 'parkingTip': "'Boat access only; park at the Rat Farm launch site ($5 fee at the private lot) and paddle in.'"},
    'william-ide': {'entranceFee': "'$8/vehicle'", 'parkingTip': "'Quiet lot nestled under oak trees, rarely full.'"},
    'woodson-bridge': {'entranceFee': "'$8/vehicle'", 'parkingTip': "'Easy parking right near the Sacramento River.'"},
    'hatfield-sra': {'entranceFee': "'$8/vehicle'", 'parkingTip': "'Lots of shade and plenty of parking near the Merced River.'"},
    'great-valley-grasslands': {'entranceFee': "'Free'", 'parkingTip': "'Unpaved, informal pullouts along the river roads.'"},
    'mcconnell-sra': {'entranceFee': "'$8/vehicle'", 'parkingTip': "'Shaded parking adjacent to the river and picnic areas.'"},
    'pacheco-sp': {'entranceFee': "'$10/vehicle'", 'parkingTip': "'Open gravel lot at the dinosaur point entrance, rarely fills.'"},
    'san-luis-reservoir': {'entranceFee': "'$10/vehicle'", 'parkingTip': "'Plentiful parking at the Romero Visitor Center and O\\'Neill Forebay.'"},
    'caswell-memorial': {'entranceFee': "'$10/vehicle'", 'parkingTip': "'Shaded lots under the oaks, can fill on summer holiday weekends.'"},
    'turlock-lake': {'entranceFee': "'$10/vehicle'", 'parkingTip': "'Plenty of parking for boaters and day use.'"},
    'colonel-allensworth': {'entranceFee': "'$8/vehicle'", 'parkingTip': "'Large open lot next to the visitor center, rarely crowded.'"},
    'tule-elk-snr': {'entranceFee': "'$8/vehicle'", 'parkingTip': "'Small lot with a viewing platform, rarely gets crowded.'"},
    'mcarthur-burney-falls': {'entranceFee': "'$10/vehicle'", 'parkingTip': "'Main lot fills completely by 10am in summer; expect long lines at the entrance.'"},
    'castle-crags': {'entranceFee': "'$10/vehicle'", 'parkingTip': "'Dedicated lot at the vista point and trailhead; can fill up by mid-morning on weekends.'"}
}

def apply_fixes():
    with open('caparks.html', 'r', encoding='utf-8') as f:
        content = f.read()

    start_str = 'const PARK_DETAILS = {'
    start_idx = content.find(start_str)
    end_idx_block = content.find('};\n\nfunction', start_idx)
    details_str = content[start_idx:end_idx_block]
    
    count = 0
    for pid, new_d in data.items():
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
            e_idx = details_str.find('\n  },', s_idx)
            if e_idx == -1: e_idx = details_str.find('\n  }', s_idx)
            block = details_str[s_idx:e_idx]
            
            insert_str = ""
            if 'parkingTip:' not in block and 'parkingTip' in new_d:
                insert_str += f"\n    parkingTip: {new_d['parkingTip']},"
            if 'entranceFee:' not in block and 'entranceFee' in new_d:
                insert_str += f"\n    entranceFee: {new_d['entranceFee']},"
                
            if insert_str:
                details_str = details_str[:s_idx] + insert_str + details_str[s_idx:]
                count += 1
                
    content = content[:start_idx] + details_str + content[end_idx_block:]
    
    with open('caparks.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Successfully processed {count} parking fields.")

if __name__ == '__main__':
    apply_fixes()
