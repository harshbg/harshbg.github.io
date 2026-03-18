import re
from injector import inject_data

data = {
    'ventana-wilderness': {
        'biking': "{ available: false, ebike: false, trails: [] }",
        'photography': "{ spots: ['Sykes Hot Springs', 'Big Sur River', 'Pine Ridge Trail'], tip: 'Capture the dense oak and redwood canopies transitioning to chaparral ridges.' }",
        'sunsetSpots': "[{ spot: 'Cone Peak', note: 'One of the steepest coastal gradients in the contiguous US, offering unmatched Pacific sunsets' }]",
        'googleRating': '4.8',
        'googleReviews': "'1.2K'"
    },
    'candlestick-point': {
        'biking': "{ available: true, ebike: true, trails: [{ name: 'SF Bay Trail', distance: 'varies', difficulty: 'Easy', note: 'Paved bayside loop' }] }",
        'photography': "{ spots: ['Fishing piers', 'Windsurf launch', 'Tidal flats'], tip: 'Great views of the East Bay hills on clear winter days.' }",
        'sunsetSpots': "[{ spot: 'Sunrise Point', note: 'Despite the name, affords beautiful evening light over the bay skyline' }]",
        'googleRating': '4.3',
        'googleReviews': "'1K'"
    },
    'benicia-sra': {
        'biking': "{ available: true, ebike: true, trails: [{ name: 'Carquinez Strait Scenic Loop', distance: 'varies', difficulty: 'Easy', note: 'Paved path passing through marshes' }] }",
        'photography': "{ spots: ['Southampton Bay', 'Dillon Point', 'Tidal marshes'], tip: 'A fantastic spot to photograph huge cargo ships passing through the strait.' }",
        'sunsetSpots': "[{ spot: 'Dillon Point', note: 'Look straight down the Carquinez Strait as the sun sets over the water' }]",
        'googleRating': '4.6',
        'googleReviews': "'1.1K'"
    },
    'benicia-capitol': {
        'biking': "{ available: false, ebike: false, trails: [] }",
        'photography': "{ spots: ['Capitol exterior', 'Historic desk replicas', 'Fischer-Hanlon House gardens'], tip: 'The brick facade of the 1852 capitol looks best in late afternoon light.' }",
        'sunsetSpots': "[{ spot: 'First Street waterfront (nearby)', note: 'Walk just down the street from the capitol to watch the sunset over the strait' }]",
        'googleRating': '4.7',
        'googleReviews': "'220'"
    },
    'franks-tract': {
        'biking': "{ available: false, ebike: false, trails: [] }",
        'photography': "{ spots: ['Flooded island waters', 'Remnant levees', 'Waterfowl'], tip: 'Requires a boat — best photographed on calm mornings when the Delta water reflects perfectly.' }",
        'sunsetSpots': "[{ spot: 'Open water', note: 'Unobstructed delta sunsets reflecting in the flooded tract' }]",
        'googleRating': '4.3',
        'googleReviews': "'95'"
    },
    'sugarloaf-ridge': {
        'biking': "{ available: true, ebike: false, trails: [{ name: 'Bald Mountain Fire Road', distance: '2.5 mi', difficulty: 'Hard', note: 'Steep climb rewarding with 360-degree views of wine country' }] }",
        'photography': "{ spots: ['Bald Mountain summit', 'Sonoma Creek waterfall', 'Robert Ferguson Observatory'], tip: 'Amazing dark sky location; the observatory parking lot is ideal for astrophotography.' }",
        'sunsetSpots': "[{ spot: 'Bald Mountain', note: 'Views stretch all the way to the Golden Gate and Sierras on a clear evening' }]",
        'googleRating': '4.8',
        'googleReviews': "'1.5K'"
    },
    'trione-annadel': {
        'biking': "{ available: true, ebike: false, trails: [{ name: 'Lawndale-Schultz-Ridge loop', distance: '12.0 mi', difficulty: 'Moderate', note: 'Legendary mountain bike singletrack through volcanic rocks and oaks' }] }",
        'photography': "{ spots: ['Lake Ilsanjo', 'Ledson Marsh', 'Cobblestone Quarry'], tip: 'Spring brings brilliant green grasses and wildflower blooms among the volcanic rocks.' }",
        'sunsetSpots': "[{ spot: 'Buena Vista Trail', note: 'Elevated views looking west over the Santa Rosa plain' }]",
        'googleRating': '4.8',
        'googleReviews': "'1.8K'"
    },
    'bothe-napa': {
        'biking': "{ available: false, ebike: false, trails: [] }",
        'photography': "{ spots: ['Ritchey Creek', 'Pioneer Cemetery', 'Redwood canopy'], tip: 'One of the furthest inland coastal redwood stands—capture the mix of redwoods and oaks.' }",
        'sunsetSpots': "[{ spot: 'Coyote Peak', note: 'Hike to the top for dusk views of the Napa Valley floor' }]",
        'googleRating': '4.7',
        'googleReviews': "'650'"
    },
    'jack-london': {
        'biking': "{ available: true, ebike: false, trails: [{ name: 'Sonoma Mountain Ridge', distance: '8.0 mi', difficulty: 'Moderate', note: 'Multi-use dirt trail winding up the slopes of Sonoma Mountain' }] }",
        'photography': "{ spots: ['Wolf House ruins', 'Beauty Ranch', 'Pig Palace'], tip: 'The massive stone ruins of the burnt Wolf House are most dramatic in overcast light.' }",
        'sunsetSpots': "[{ spot: 'Sonoma Mountain Trail', note: 'High vantage point over the Valley of the Moon turning golden' }]",
        'googleRating': '4.8',
        'googleReviews': "'2.5K'"
    },
    'robert-louis-stevenson': {
        'biking': "{ available: true, ebike: false, trails: [{ name: 'Mt. St. Helena Fire Road', distance: '10.0 mi', difficulty: 'Hard', note: 'Steady 2,000+ ft climb to the summit on dirt fire road' }] }",
        'photography': "{ spots: ['Mt. St. Helena summit', 'Palisades', 'Silverado Mine ruins'], tip: 'Winter offers the clearest views; sometimes Mt. Shasta is visible 190 miles away.' }",
        'sunsetSpots': "[{ spot: 'Mt. St. Helena', note: 'The highest peak in wine country catches the absolute last light of the day' }]",
        'googleRating': '4.8',
        'googleReviews': "'800'"
    },
    'austin-creek': {
        'biking': "{ available: false, ebike: false, trails: [] }",
        'photography': "{ spots: ['Bullfrog Pond', 'Rolling meadows', 'Backcountry oak woodlands'], tip: 'Accessible via Armstrong Redwoods, the contrast from redwoods to open oaks is striking.' }",
        'sunsetSpots': "[{ spot: 'Campground ridge', note: 'Looks out over the rugged, rolling coastal range as the sun sets' }]",
        'googleRating': '4.7',
        'googleReviews': "'220'"
    },
    'kruse-rhododendron': {
        'biking': "{ available: false, ebike: false, trails: [] }",
        'photography': "{ spots: ['Understory blooms', 'Regrowth redwoods', 'Fern canyons'], tip: 'Visit in April or May to photograph the spectacular pink rhododendron blooms.' }",
        'sunsetSpots': "[{ spot: 'Trail breaks', note: 'Mostly dense forest, but filtered evening light through the pink flowers is magical' }]",
        'googleRating': '4.8',
        'googleReviews': "'400'"
    },
    'bale-grist-mill': {
        'biking': "{ available: false, ebike: false, trails: [] }",
        'photography': "{ spots: ['Wooden water wheel', 'Historic mill stones', 'Forested creek'], tip: 'The massive 36-foot wooden water wheel is fully operational; use a slow shutter to blur the dripping water.' }",
        'sunsetSpots': "[{ spot: 'Mill exterior', note: 'The historic wood structure catches beautiful dappled afternoon light' }]",
        'googleRating': '4.7',
        'googleReviews': "'850'"
    },
    'anderson-marsh': {
        'biking': "{ available: false, ebike: false, trails: [] }",
        'photography': "{ spots: ['Cache Creek', 'Historic Ranch House', 'Tule marshlands'], tip: 'A premier birding spot—bring your longest lens to capture bald eagles and herons.' }",
        'sunsetSpots': "[{ spot: 'Audubon Trail boardwalk', note: 'Watch the sunset over the tule reeds of Clear Lake' }]",
        'googleRating': '4.4',
        'googleReviews': "'150'"
    },
    'clear-lake': {
        'biking': "{ available: true, ebike: false, trails: [] }",
        'photography': "{ spots: ['Cole Creek', 'Dorn Trail', 'Lake shoreline'], tip: 'The oldest lake in North America; photograph the ancient volcanic silhouettes reflected in the water.' }",
        'sunsetSpots': "[{ spot: 'Kelsey Creek area', note: 'Unobstructed western views across the massive lake body' }]",
        'googleRating': '4.4',
        'googleReviews': "'900'"
    },
    'armstrong-redwoods': {
        'biking': "{ available: false, ebike: false, trails: [] }",
        'photography': "{ spots: ['Colonel Armstrong Tree', 'Parson Jones Tree', 'Forest theater'], tip: 'Foggiest in the morning; shoot straight up to capture the 310-foot giants converging.' }",
        'sunsetSpots': "[{ spot: 'Canopy gaps', note: 'Deep within the canyon, sunset comes early as light retreats up the colossal trunks' }]",
        'googleRating': '4.8',
        'googleReviews': "'6K'"
    },
    'salt-point': {
        'biking': "{ available: false, ebike: false, trails: [] }",
        'photography': "{ spots: ['Tafoni sandstone rocks', 'Gerstle Cove', 'Pygmy Forest'], tip: 'The honeycomb-like \"tafoni\" rock formations along the coastline create otherworldly foregrounds.' }",
        'sunsetSpots': "[{ spot: 'Fisk Mill Cove', note: 'Dramatic cliffs dropping straight into the crashing Pacific surf' }]",
        'googleRating': '4.8',
        'googleReviews': "'1.1K'"
    },
    'sonoma-coast': {
        'biking': "{ available: false, ebike: false, trails: [] }",
        'photography': "{ spots: ['Goat Rock', 'Bodega Head', 'Blind Beach', 'Russian River mouth'], tip: 'Spectacular sea stacks dot the ocean; long exposures (30+ seconds) smooth out the crashing surf.' }",
        'sunsetSpots': "[{ spot: 'Goat Rock Beach', note: 'One of the most iconic sunset beaches in California, with massive arched rocks framing the sun' }]",
        'googleRating': '4.8',
        'googleReviews': "'8.5K'"
    },
    'fort-ross': {
        'biking': "{ available: false, ebike: false, trails: [] }",
        'photography': "{ spots: ['Russian Orthodox Chapel', 'Wooden palisades', 'Cove and cannons'], tip: 'The stark wooden chapel set against the moody, foggy coastline is incredibly photogenic.' }",
        'sunsetSpots': "[{ spot: 'Fort compound', note: 'Watch the sunset behind the wooden stockade walls looking out to the Pacific' }]",
        'googleRating': '4.7',
        'googleReviews': "'1.4K'"
    },
    'van-damme': {
        'biking': "{ available: true, ebike: false, trails: [{ name: 'Fern Canyon Trail', distance: '5.0 mi', difficulty: 'Easy', note: 'Lush, flat dirt trail following Little River; paved at the beginning' }] }",
        'photography': "{ spots: ['Fern Canyon', 'Pygmy Forest boardwalk', 'Little River beach'], tip: 'The dense, wet fern canyon is a macro photographer\\'s dream for mosses and fungi.' }",
        'sunsetSpots': "[{ spot: 'Van Damme Beach', note: 'A protected cove where the river meets the sea, catching the western evening light' }]",
        'googleRating': '4.7',
        'googleReviews': "'1.2K'"
    },
    'russian-gulch': {
        'biking': "{ available: true, ebike: true, trails: [{ name: 'Bike path to waterfall', distance: '2.5 mi', difficulty: 'Easy', note: 'Paved multi-use trail leading deep into the forested canyon' }] }",
        'photography': "{ spots: ['Devil\\'s Punchbowl', 'Panther Bridge', 'Russian Gulch Falls'], tip: 'The 36-foot waterfall cascading through ferns is best captured with a 1-second exposure.' }",
        'sunsetSpots': "[{ spot: 'Headlands Trail', note: 'Look down into the Devil\\'s Punchbowl sinkhole as the sun sets over the ocean' }]",
        'googleRating': '4.8',
        'googleReviews': "'1.6K'"
    },
    'mackerricher': {
        'biking': "{ available: true, ebike: true, trails: [{ name: 'Haul Road Trail', distance: '3.0 mi', difficulty: 'Easy', note: 'Old paved logging road running right along the coastal cliffs' }] }",
        'photography': "{ spots: ['Glass Beach (nearby)', 'Laguna Point boardwalk', 'Lake Cleone'], tip: 'Harbor seals often haul out on the rocks at Laguna Point; bring a zoom lens.' }",
        'sunsetSpots': "[{ spot: 'Laguna Point', note: 'Unobstructed 180-degree ocean views and a prime spot to photograph whales at sunset' }]",
        'googleRating': '4.8',
        'googleReviews': "'2.2K'"
    },
    'humboldt-redwoods': {
        'biking': "{ available: true, ebike: true, trails: [{ name: 'Avenue of the Giants', distance: '31.0 mi', difficulty: 'Moderate', note: 'World-famous paved scenic highway riding alongside the colossal trees' }] }",
        'photography': "{ spots: ['Founders Grove', 'Eel River', 'Rockefeller Forest'], tip: 'The largest contiguous old-growth redwood forest on earth. Use a person in frame for scale.' }",
        'sunsetSpots': "[{ spot: 'Eel River sandbars', note: 'Sunset reflects on the river surface framed by 300-foot tall shadows' }]",
        'googleRating': '4.9',
        'googleReviews': "'5K'"
    },
    'richardson-grove': {
        'biking': "{ available: false, ebike: false, trails: [] }",
        'photography': "{ spots: ['Dawn Redwood path', 'South Fork Eel River', 'Visitor Center'], tip: 'Often the first redwood park visitors hit driving north; great afternoon light cutting through the canopy.' }",
        'sunsetSpots': "[{ spot: 'River shoreline', note: 'Calm water near the swimming hole reflects the evening sky' }]",
        'googleRating': '4.7',
        'googleReviews': "'1.5K'"
    },
    'prairie-creek': {
        'biking': "{ available: true, ebike: true, trails: [{ name: 'Newton B. Drury Parkway', distance: '10.0 mi', difficulty: 'Moderate', note: 'Paved road through immense redwoods (often closed to cars, making it a cycling paradise)' }] }",
        'photography': "{ spots: ['Fern Canyon', 'Elk Prairie', 'Big Tree wayside'], tip: 'Fern Canyon (where Jurassic Park was filmed) is spectacular, but herds of Roosevelt Elk in the meadow provide the best wildlife shots.' }",
        'sunsetSpots': "[{ spot: 'Gold Bluffs Beach', note: 'Crashing Pacific waves backed by steep redwood bluffs' }]",
        'googleRating': '4.9',
        'googleReviews': "'2.8K'"
    }
}

if __name__ == '__main__':
    inject_data(data)
