from injector import inject_data

data = {
    'jedediah-smith': {
        'sunsetSpots': "[]", 
        'photography': "{ spots: ['Stout Grove', 'Smith River', 'Howland Hill Road'], tip: 'Use a tripod in the deep redwood groves as light is very dim.' }",
        'biking': "{ available: true, ebike: false, trails: [{ name: 'Howland Hill Road', distance: '10.0 mi', difficulty: 'Easy', note: 'Scenic, unpaved road through old-growth redwoods' }] }"
    },
    'del-norte-coast': {
        'sunsetSpots': "[{ spot: 'Damnation Creek Trailhead', note: 'Coastal views before the trail descends into the forest' }]",
        'photography': "{ spots: ['Damnation Creek', 'Coastal Bluffs', 'Mill Creek Campground'], tip: 'Fog often rolls in during summer, creating atmospheric redwood shots.' }",
        'biking': "{ available: true, ebike: false, trails: [{ name: 'Hobbs Wall Trail', distance: '4.0 mi', difficulty: 'Moderate', note: 'Shared-use trail through second-growth forest' }] }"
    },
    'pelican-sb': {
        'sunsetSpots': "[{ spot: 'Pelican Beach', note: 'Remote beach offering uninterrupted Pacific sunsets' }]",
        'photography': "{ spots: ['Sandy Beach', 'Driftwood', 'Ocean horizon'], tip: 'Strong winds are common—protect your lens from flying sand.' }",
        'biking': "{ available: false, ebike: false, trails: [] }"
    },
    'tolowa-dunes': {
        'sunsetSpots': "[{ spot: 'Kellogg Beach', note: 'Wide open beaches perfect for sunset colors' }]",
        'photography': "{ spots: ['Sand Dunes', 'Lake Earl', 'Kellogg Beach'], tip: 'Look for shorebirds and waterfowl in the wetlands during migration.' }",
        'biking': "{ available: true, ebike: false, trails: [{ name: 'Tolowa Coast Trail', distance: '4.5 mi', difficulty: 'Easy', note: 'Sandy and dirt paths suited for fat-tire bikes' }] }"
    },
    'azalea-snr': {
        'sunsetSpots': "[]",
        'photography': "{ spots: ['Azalea blooms', 'Forested edges'], tip: 'Visit in April/May with a macro lens for the Western Azalea blooms.' }",
        'biking': "{ available: false, ebike: false, trails: [] }"
    },
    'benbow-lake': {
        'sunsetSpots': "[]",
        'photography': "{ spots: ['Eel River', 'Historic Benbow Inn exterior', 'Campsite'], tip: 'Summers are very hot; photograph early in the morning for best light.' }",
        'biking': "{ available: true, ebike: false, trails: [{ name: 'Campground roads', distance: 'varies', difficulty: 'Easy', note: 'Paved paths suitable for families' }] }"
    },
    'fort-humboldt': {
        'sunsetSpots': "[]",
        'photography': "{ spots: ['Historic hospital building', 'Logging equipment display', 'Bluff overlooking Humboldt Bay'], tip: 'Capture the antique steam donkeys and locomotives.' }",
        'biking': "{ available: true, ebike: false, trails: [{ name: 'Park grounds', distance: '1.0 mi', difficulty: 'Easy', note: 'Paved paths around the historic buildings' }] }"
    },
    'grizzly-creek': {
        'sunsetSpots': "[]",
        'photography': "{ spots: ['Cheatham Grove', 'Van Duzen River'], tip: 'Cheatham Grove is famous as the \"Endor\" filming location—great for deep forest photography.' }",
        'biking': "{ available: false, ebike: false, trails: [] }"
    },
    'harry-merlo': {
        'sunsetSpots': "[]",
        'photography': "{ spots: ['Big Lagoon', 'Coastal forest'], tip: 'It\\'s an undeveloped park, so natural undisturbed shots abound.' }",
        'biking': "{ available: false, ebike: false, trails: [] }"
    },
    'humboldt-lagoon': {
        'sunsetSpots': "[{ spot: 'Dry Lagoon Beach', note: 'Sunset over the vast, isolated stretch of sand and surf' }]",
        'photography': "{ spots: ['Stone Lagoon', 'Dry Lagoon', 'Agate Beach'], tip: 'Roosevelt Elk are often wandering near the lagoons; use a telephoto lens.' }",
        'biking': "{ available: false, ebike: false, trails: [] }"
    },
    'dewitt-redwoods': {
        'sunsetSpots': "[]",
        'photography': "{ spots: ['Redwood groves', 'Eel River banks'], tip: 'Mostly a small drive-through grove.' }",
        'biking': "{ available: false, ebike: false, trails: [] }"
    },
    'little-river-sb': {
        'sunsetSpots': "[{ spot: 'Little River Beach', note: 'Expansive sandy beach facing west' }]",
        'photography': "{ spots: ['Little River mouth', 'Dunes', 'Ocean surf'], tip: 'Great for reflection shots on the wet sand at low tide.' }",
        'biking': "{ available: false, ebike: false, trails: [] }"
    },
    'sinkyone-wilderness': {
        'sunsetSpots': "[{ spot: 'Needle Rock Visitor Center', note: 'Cliffs face the ocean for dramatic sunsets' }]",
        'photography': "{ spots: ['Lost Coast Trail', 'Needle Rock', 'Bear Harbor'], tip: 'Rugged landscapes require exploring; Roosevelt Elk often graze near Needle Rock.' }",
        'biking': "{ available: false, ebike: false, trails: [] }"
    },
    'sue-meg': {
        'sunsetSpots': "[{ spot: 'Wedding Rock', note: 'Rocky point offering incredible views of the sun setting over the ocean' }, { spot: 'Mussel Rocks', note: 'Great tidepool and sunset viewing spot' }]",
        'photography': "{ spots: ['Wedding Rock', 'Agate Beach', 'Sumeg Village'], tip: 'Capture the crashing waves at Wedding Rock using a fast shutter speed.' }",
        'biking': "{ available: true, ebike: false, trails: [{ name: 'Rim Trail', distance: '2.0 mi', difficulty: 'Easy', note: 'Parallels the park road along the coastal bluffs' }] }"
    },
    'trinidad-sb': {
        'sunsetSpots': "[{ spot: 'Trinidad Head Point', note: 'Elevated views of the Pacific and surrounding rocky coves' }]",
        'photography': "{ spots: ['Trinidad Head', 'Pewetole Island offshore', 'College Cove'], tip: 'The memorial lighthouse area provides a great elevated vantage point.' }",
        'biking': "{ available: false, ebike: false, trails: [] }"
    },
    'admiral-standley': {
        'sunsetSpots': "[]",
        'photography': "{ spots: ['Redwood Groves'], tip: 'Small and undeveloped; focus on the ancient trees lining the road.' }",
        'biking': "{ available: false, ebike: false, trails: [] }"
    },
    'caspar-headlands-sb': {
        'sunsetSpots': "[{ spot: 'Caspar Beach', note: 'Quiet cove tucked between bluffs, facing West' }]",
        'photography': "{ spots: ['Caspar Beach cove', 'Headlands'], tip: 'Beautiful sheltered beach, great for golden hour photography.' }",
        'biking': "{ available: false, ebike: false, trails: [] }"
    },
    'caspar-headlands-snr': {
        'sunsetSpots': "[{ spot: 'The Headlands', note: 'Exposed rocky bluffs facing the setting sun' }]",
        'photography': "{ spots: ['Coastal Bluffs', 'Wildflower fields (spring)'], tip: 'Very small reserve, but excellent for stormy wave photography.' }",
        'biking': "{ available: false, ebike: false, trails: [] }"
    },
    'greenwood-sb': {
        'sunsetSpots': "[{ spot: 'Greenwood Creek Beach', note: 'Driftwood-strewn beach facing the sunset' }]",
        'photography': "{ spots: ['Creek mouth', 'Historic lumber town bluffs', 'Beach'], tip: 'Follow the short trail down to the cove for the best angles.' }",
        'biking': "{ available: false, ebike: false, trails: [] }"
    },
    'hendy-woods': {
        'sunsetSpots': "[]",
        'photography': "{ spots: ['Big Hendy Grove', 'Navarro River', 'Hermit Hut'], tip: 'The Navarro River provides great reflections of the surrounding redwoods in autumn.' }",
        'biking': "{ available: true, ebike: false, trails: [{ name: 'Park Roads', distance: 'varies', difficulty: 'Easy', note: 'Paved paths suitable for casual rides' }] }"
    }
}

if __name__ == '__main__':
    inject_data(data)
