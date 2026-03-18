import re

data = {
    'yosemite': {
        'biking': "{ available: true, ebike: true, trails: [{ name: 'Yosemite Valley Loop', distance: '12.0 mi', difficulty: 'Easy', note: 'Paved, relatively flat loop taking in the classic valley views' }] }",
        'photography': "{ spots: ['Tunnel View', 'Glacier Point', 'Valley View', 'Taft Point', 'Sentinel Bridge'], tip: 'Early morning light cuts through valley haze best; use a tripod for sunset at Tunnel View.' }",
        'sunsetSpots': "[{ spot: 'Glacier Point', note: 'Provides an iconic, elevated view of Half Dome turning orange as the sun sets' }, { spot: 'Tunnel View', note: 'Classic sweeping view of the valley; watch the light fade on El Capitan' }]",
        'googleRating': '4.8',
        'googleReviews': "'68.2K'"
    },
    'henry-coe': {
        'biking': "{ available: true, ebike: false, trails: [{ name: 'Hunting Hollow to Coe Headquarters', distance: '15.0 mi', difficulty: 'Hard', note: 'Challenging steep fire roads but incredible spring views' }] }",
        'photography': "{ spots: ['Hunting Hollow', 'Coe Headquarters ridge', 'Mississippi Lake'], tip: 'Spring brings brilliant green hills and wildflowers, best photographed in the morning.' }",
        'sunsetSpots': "[{ spot: 'Coe Headquarters Ridge', note: 'Expansive views to the west over the Santa Clara Valley' }]",
        'googleRating': '4.7',
        'googleReviews': "'2.1K'"
    },
    'mount-diablo': {
        'biking': "{ available: true, ebike: true, trails: [{ name: 'South Gate Road to Summit', distance: '11.0 mi', difficulty: 'Hard', note: 'Iconic road cycling climb' }, { name: 'Mitchell Canyon', distance: '8.0 mi', difficulty: 'Moderate', note: 'Good dirt trails for mountain biking' }] }",
        'photography': "{ spots: ['Summit observation deck', 'Rock City', 'Mitchell Canyon'], tip: 'Winter days right after a rain offer the clearest views, sometimes all the way to the Sierra.' }",
        'sunsetSpots': "[{ spot: 'Summit', note: 'Incredible 360-degree views as the sun drops behind the coastal ranges' }, { spot: 'Rock City', note: 'Interesting sandstone formations glow in the late afternoon light' }]",
        'googleRating': '4.8',
        'googleReviews': "'3.2K'"
    },
    'big-basin': {
        'biking': "{ available: true, ebike: false, trails: [{ name: 'Skyline to the Sea (Fire Road sections)', distance: 'varies', difficulty: 'Moderate', note: 'Bikes allowed on designated fire roads only' }] }",
        'photography': "{ spots: ['Berry Creek Falls', 'Redwood Loop', 'Sempervirens Falls'], tip: 'Cloudy or foggy days are best for photographing redwoods to avoid harsh contrast.' }",
        'sunsetSpots': "[{ spot: 'Buzzard\\'s Roost', note: 'A climb above the canopy provides a view toward the ocean for sunset' }]",
        'googleRating': '4.7',
        'googleReviews': "'5.4K'"
    },
    'castle-rock': {
        'biking': "{ available: false, ebike: false, trails: [] }",
        'photography': "{ spots: ['Castle Rock', 'Goat Rock', 'Saratoga Gap'], tip: 'Late afternoon light illuminates the sandstone formations against the forest backdrop.' }",
        'sunsetSpots': "[{ spot: 'Goat Rock Overlook', note: 'Unobstructed views looking west toward the Santa Cruz Mountains and the Pacific' }]",
        'googleRating': '4.8',
        'googleReviews': "'1.5K'"
    },
    'portola-redwoods': {
        'biking': "{ available: true, ebike: false, trails: [{ name: 'Old Haul Road', distance: '10.0 mi', difficulty: 'Moderate', note: 'Wide dirt road winding through deep second-growth redwoods' }] }",
        'photography': "{ spots: ['Peters Creek', 'Old Tree Trail', 'Slate Creek'], tip: 'Use a polarizing filter to make the lush green ferns and creek water pop.' }",
        'sunsetSpots': "[{ spot: 'Slate Creek Trail ridge', note: 'One of the few spots where you gain enough elevation to see the evening sky' }]",
        'googleRating': '4.7',
        'googleReviews': '450'
    },
    'butano': {
        'biking': "{ available: true, ebike: false, trails: [{ name: 'Olmo Fire Road', distance: '6.0 mi', difficulty: 'Hard', note: 'Steep climbs through mixed evergreen and redwood forest' }] }",
        'photography': "{ spots: ['Little Butano Creek', 'Ano Nuevo Overlook', 'Jackson Flats'], tip: 'Fog often rolls in during the late afternoon, creating moody forest shots.' }",
        'sunsetSpots': "[{ spot: 'Ano Nuevo Overlook', note: 'Distant views of the Pacific Ocean and Point Ano Nuevo as the sun goes down' }]",
        'googleRating': '4.7',
        'googleReviews': '500'
    },
    'ano-nuevo': {
        'biking': "{ available: false, ebike: false, trails: [] }",
        'photography': "{ spots: ['Elephant Seal Viewing Area', 'Cove Beach', 'Point Ano Nuevo'], tip: 'Bring a telephoto lens (200mm+) to safely photograph the elephant seals.' }",
        'sunsetSpots': "[{ spot: 'Point Ano Nuevo', note: 'Spectacular coastal sunsets, just be sure to leave before the reserve closes' }]",
        'googleRating': '4.8',
        'googleReviews': "'1.8K'"
    },
    'half-moon-bay': {
        'biking': "{ available: true, ebike: true, trails: [{ name: 'Coastside Trail', distance: '7.0 mi', difficulty: 'Easy', note: 'Paved, flat, and highly scenic oceanfront riding' }] }",
        'photography': "{ spots: ['Francis Beach', 'Venice Beach', 'Pillar Point Harbor'], tip: 'Great for golden hour beach portraits and surfing action shots.' }",
        'sunsetSpots': "[{ spot: 'Francis Beach', note: 'Direct west-facing beach for unobstructed ocean sunsets' }]",
        'googleRating': '4.7',
        'googleReviews': "'3K'"
    },
    'mount-tamalpais': {
        'biking': "{ available: true, ebike: false, trails: [{ name: 'Railroad Grade', distance: '7.5 mi', difficulty: 'Moderate', note: 'Historic rail route with a steady climb to the East Peak area' }] }",
        'photography': "{ spots: ['East Peak', 'Trojan Point', 'Cataract Falls'], tip: 'Get above the marine layer in summer for surreal \"sea of clouds\" images at sunset.' }",
        'sunsetSpots': "[{ spot: 'Trojan Point', note: 'Panoramic views of the Pacific' }, { spot: 'East Peak', note: 'Look down on the entire Bay Area at dusk' }]",
        'googleRating': '4.8',
        'googleReviews': "'5K'"
    },
    'china-camp': {
        'biking': "{ available: true, ebike: false, trails: [{ name: 'Shoreline Trail', distance: '5.0 mi', difficulty: 'Easy', note: 'Beginner-friendly flowing singletrack skirting the bay' }] }",
        'photography': "{ spots: ['China Camp Village', 'Point San Pedro', 'Shoreline Trail'], tip: 'The historic village is photogenic at high tide in the early morning.' }",
        'sunsetSpots': "[{ spot: 'Point San Pedro', note: 'Views north to San Pablo Bay catching evening light' }]",
        'googleRating': '4.7',
        'googleReviews': "'1.2K'"
    },
    'samuel-taylor': {
        'biking': "{ available: true, ebike: true, trails: [{ name: 'Cross Marin Trail', distance: '5.0 mi', difficulty: 'Easy', note: 'Flat, partly paved trail following Lagunitas Creek through redwoods' }] }",
        'photography': "{ spots: ['Lagunitas Creek', 'Pioneer Tree Trail', 'Campground Redwoods'], tip: 'Look for spawning salmon in the creek during winter months.' }",
        'sunsetSpots': "[{ spot: 'Barnabe Peak', note: 'A steep hike up the fire road rewards you with sweeping views of the Marin hills at dusk' }]",
        'googleRating': '4.8',
        'googleReviews': "'1.6K'"
    },
    'tomales-bay': {
        'biking': "{ available: false, ebike: false, trails: [] }",
        'photography': "{ spots: ['Heart\\'s Desire Beach', 'Shell Beach', 'Jepson Trail'], tip: 'The calm, sheltered waters of the bay are perfect for morning reflection shots.' }",
        'sunsetSpots': "[{ spot: 'Heart\\'s Desire Beach', note: 'Looks east, but the sky glows beautifully over the water as the sun sets behind you' }]",
        'googleRating': '4.8',
        'googleReviews': '850'
    },
    'henry-cowell': {
        'biking': "{ available: true, ebike: false, trails: [{ name: 'Pipeline Road', distance: '4.0 mi', difficulty: 'Easy', note: 'Paved and dirt sections winding alongside the San Lorenzo River' }] }",
        'photography': "{ spots: ['Redwood Grove Loop', 'San Lorenzo River', 'Observation Deck'], tip: 'Bring a fast lens (f/2.8 or wider) for the dark old-growth loop.' }",
        'sunsetSpots': "[{ spot: 'Observation Deck', note: 'The highest point in the park offers 360-degree views, including Monterey Bay' }]",
        'googleRating': '4.8',
        'googleReviews': "'5K'"
    },
    'nisene-marks': {
        'biking': "{ available: true, ebike: false, trails: [{ name: 'Aptos Creek Fire Road', distance: '14.0 mi', difficulty: 'Moderate', note: 'Long, steady fire road climb deep into the redwood canyon' }] }",
        'photography': "{ spots: ['Loma Prieta Grade', 'Twisted Grove', 'Aptos Creek'], tip: 'Capture the remnants of the old logging operations overgrown with lush forest.' }",
        'sunsetSpots': "[{ spot: 'Sand Point Overlook', note: 'A long hike or ride up the fire road to a viewpoint looking out to the ocean' }]",
        'googleRating': '4.8',
        'googleReviews': "'1.2K'"
    },
    'fremont-peak': {
        'biking': "{ available: false, ebike: false, trails: [] }",
        'photography': "{ spots: ['Summit', 'Observatory area', 'Valley overlook'], tip: 'Famous for astrophotography and stunningly clear views above the Salinas Valley fog.' }",
        'sunsetSpots': "[{ spot: 'Fremont Peak Summit', note: 'One of the best sunsets in the region, watching the sun sink into Monterey Bay from 3,169 ft' }]",
        'googleRating': '4.8',
        'googleReviews': '400'
    },
    'albany-smr': {
        'biking': "{ available: true, ebike: true, trails: [{ name: 'Bay Trail', distance: '2.0 mi', difficulty: 'Easy', note: 'Paved shoreline path leading out to the bulb' }] }",
        'photography': "{ spots: ['Albany Bulb art', 'Shoreline', 'Bay bridge views'], tip: 'The eclectic driftwood and scrap metal art makes for unique foregrounds against the SF skyline.' }",
        'sunsetSpots': "[{ spot: 'Albany Bulb', note: 'Unmatched views of the Golden Gate and SF skyline silhouetted against the sunset' }]",
        'googleRating': '4.6',
        'googleReviews': '500'
    },
    'bethany-reservoir': {
        'biking': "{ available: true, ebike: true, trails: [{ name: 'California Aqueduct Bikeway', distance: '8.0+ mi', difficulty: 'Easy', note: 'Paved, very flat path following the aqueduct' }] }",
        'photography': "{ spots: ['Reservoir banks', 'Windmills on the hills', 'Aqueduct intake'], tip: 'Best photographed in spring when the surrounding hills are green.' }",
        'sunsetSpots': "[{ spot: 'Reservoir shoreline', note: 'The water reflects the sky, framed by the Altamont Pass windmills' }]",
        'googleRating': '4.3',
        'googleReviews': '200'
    },
    'emeryville-crescent': {
        'biking': "{ available: true, ebike: true, trails: [{ name: 'SF Bay Trail', distance: '3.0 mi', difficulty: 'Easy', note: 'Paved multi-use trail bridging Emeryville and Oakland' }] }",
        'photography': "{ spots: ['Marsh grass', 'Bay Bridge views', 'Shorebirds'], tip: 'Bring a telephoto lens to capture shorebirds without disturbing the protected marsh.' }",
        'sunsetSpots': "[{ spot: 'Bay Trail', note: 'Direct views of the Bay Bridge spanning the water at sunset' }]",
        'googleRating': '4.5',
        'googleReviews': '120'
    },
    'mclaughlin-eastshore': {
        'biking': "{ available: true, ebike: true, trails: [{ name: 'Bay Trail', distance: '8.5 mi', difficulty: 'Easy', note: 'Long, continuous paved path tracing the East Bay shoreline' }] }",
        'photography': "{ spots: ['Berkeley Marina', 'César Chávez Park', 'Richmond shoreline'], tip: 'Great kite-flying photography at César Chávez Park.' }",
        'sunsetSpots': "[{ spot: 'César Chávez Park', note: 'Broad, grassy hills with clear views of the Golden Gate Bridge and SF skyline' }, { spot: 'Berkeley Pier', note: 'A classic foreground element stretching into the bay for sunset' }]",
        'googleRating': '4.6',
        'googleReviews': '600'
    }
}

def inject():
    with open('caparks.html', 'r', encoding='utf-8') as f:
        content = f.read()

    for park_id, new_data in data.items():
        pattern = r"(\n\s*'" + re.escape(park_id) + r"':\s*\{)"
        match = re.search(pattern, content)
        if not match:
            # try double quotes or unquoted
            pattern = r'(\n\s*"' + re.escape(park_id) + r'":\s*\{)'
            match = re.search(pattern, content)
            if not match:
                pattern = r"(\n\s*" + re.escape(park_id) + r":\s*\{)"
                match = re.search(pattern, content)
                
        if not match:
            print(f"Count not find park_id {park_id}")
            continue
            
        start_idx = match.end()
        block_text = content[start_idx:start_idx+15000] 
        
        insert_str = ""
        if 'biking:' not in block_text:
            insert_str += f"\n    biking: {new_data['biking']},"
        if 'photography:' not in block_text:
            insert_str += f"\n    photography: {new_data['photography']},"
        if 'sunsetSpots:' not in block_text:
            insert_str += f"\n    sunsetSpots: {new_data['sunsetSpots']},"
        if 'googleRating:' not in block_text:
            insert_str += f"\n    googleRating: {new_data['googleRating']},"
        if 'googleReviews:' not in block_text:
            insert_str += f"\n    googleReviews: {new_data['googleReviews']},"
            
        content = content[:start_idx] + insert_str + content[start_idx:]

    with open('caparks.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
if __name__ == '__main__':
    inject()
