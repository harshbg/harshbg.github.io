import re
from injector import inject_data

data = {
    'olompali': {
        'biking': "{ available: false, ebike: false, trails: [] }",
        'photography': "{ spots: ['Miwok Village replica', 'Historic Adobe ruins', 'Burleigh Murray Ranch trail'], tip: 'Afternoon light filtering through the oak trees brings out the textures of the stone ruins.' }",
        'sunsetSpots': "[{ spot: 'Mt. Burdell Ridge', note: 'Expansive views over the Petaluma River valley as the sun sets' }]",
        'googleRating': '4.6',
        'googleReviews': "'120'"
    },
    'old-sacramento-shp': {
        'biking': "{ available: true, ebike: true, trails: [{ name: 'Jedediah Smith Memorial Trail', distance: '32.0 mi', difficulty: 'Easy', note: 'Paved trail starting at Old Sac and following the American River' }] }",
        'photography': "{ spots: ['Tower Bridge', 'Delta King Riverboat', 'Historic wooden boardwalks'], tip: 'Night photography here is excellent when the vintage streetlamps and Tower Bridge are illuminated.' }",
        'sunsetSpots': "[{ spot: 'Sacramento River waterfront', note: 'Watch the sunset reflect off the water and the golden Tower Bridge' }]",
        'googleRating': '4.7',
        'googleReviews': "'12.5K'"
    },
    'state-capitol-museum': {
        'biking': "{ available: false, ebike: false, trails: [] }",
        'photography': "{ spots: ['Capitol Dome exterior', 'Rotunda interior', 'World Peace Rose Garden'], tip: 'Bring a wide-angle lens to capture the full grandeur of the rotunda\\'s interior dome.' }",
        'sunsetSpots': "[{ spot: 'Capitol Mall', note: 'Facing west down the mall provides a perfect alignment with the setting sun' }]",
        'googleRating': '4.7',
        'googleReviews': "'4K'"
    },
    'dos-rios': {
        'biking': "{ available: false, ebike: false, trails: [] }",
        'photography': "{ spots: ['Tuolumne and San Joaquin River confluence', 'Restored floodplains', 'Riparian forests'], tip: 'Early morning is best for capturing the heavy mist rolling off the river.' }",
        'sunsetSpots': "[{ spot: 'Riverbanks', note: 'Quiet, flat horizon views over the wetlands' }]",
        'googleRating': '4.5',
        'googleReviews': "'40'"
    },
    'ishxenta': {
        'biking': "{ available: false, ebike: false, trails: [] }",
        'photography': "{ spots: ['Garrapata Creek watershed', 'Santa Lucia Mountains backdrop', 'Coastal terraces'], tip: 'Fog creates dramatic, moody atmospheres against the steep mountains in the morning.' }",
        'sunsetSpots': "[{ spot: 'Coastal terrace', note: 'Unobstructed views looking straight out into the Pacific Ocean' }]",
        'googleRating': '4.8',
        'googleReviews': "'15'"
    },
    'old-town-san-diego': {
        'biking': "{ available: false, ebike: false, trails: [] }",
        'photography': "{ spots: ['Casa de Estudillo', 'Fiesta de Reyes courtyard', 'Seeley Stables'], tip: 'The colorful adobes and vibrant courtyards look best in bright, midday sun or vibrant golden hour.' }",
        'sunsetSpots': "[{ spot: 'Presidio Park', note: 'Slightly elevated view looking west over San Diego and the ocean' }]",
        'googleRating': '4.6',
        'googleReviews': "'28K'"
    },
    'alcatraz-island': {
        'biking': "{ available: false, ebike: false, trails: [] }",
        'photography': "{ spots: ['Main Cellhouse', 'Lighthouse', 'Parade Grounds'], tip: 'The night tour offers incredible, moody lighting and spectacular views of the illuminated SF skyline.' }",
        'sunsetSpots': "[{ spot: 'West side of the island', note: 'Direct views of the Golden Gate Bridge silhouetted against the sinking sun' }]",
        'googleRating': '4.7',
        'googleReviews': "'42K'"
    },
    'fort-point-nhs': {
        'biking': "{ available: true, ebike: true, trails: [{ name: 'San Francisco Bay Trail', distance: 'varies', difficulty: 'Easy', note: 'Paved path running right up to the fort along the water' }] }",
        'photography': "{ spots: ['Inside the brick casemates', 'Rooftop battery', 'Hopper\\'s Hands'], tip: 'The geometric brick arches inside the fort combined with the massive steel of the bridge above create incredible leading lines.' }",
        'sunsetSpots': "[{ spot: 'Marine Drive outside the fort', note: 'Watch the sunset behind the Golden Gate Bridge just steps away' }]",
        'googleRating': '4.7',
        'googleReviews': "'6.5K'"
    },
    'presidio-sf': {
        'biking': "{ available: true, ebike: true, trails: [{ name: 'Golden Gate Promenade', distance: '4.3 mi', difficulty: 'Easy', note: 'Iconic paved trail along Crissy Field to the Golden Gate Bridge' }] }",
        'photography': "{ spots: ['Crissy Field shoreline', 'Inspiration Point', 'Andy Goldsworthy\\'s Wood Line'], tip: 'Morning fog receding from the Golden Gate Bridge offers the most classic San Francisco shots.' }",
        'sunsetSpots': "[{ spot: 'Baker Beach', note: 'The ultimate sunset spot with the Golden Gate Bridge glowing in the background' }]",
        'googleRating': '4.8',
        'googleReviews': "'14K'"
    },
    'rosie-riveter': {
        'biking': "{ available: true, ebike: true, trails: [{ name: 'SF Bay Trail', distance: 'varies', difficulty: 'Easy', note: 'Paved bayside trail passing right by the visitor center and memorial' }] }",
        'photography': "{ spots: ['Rosie Memorial at Marina Bay', 'Visitor Center Oil Houses', 'SS Red Oak Victory ship'], tip: 'The memorial\\'s structural elements align beautifully with the San Francisco skyline across the bay.' }",
        'sunsetSpots': "[{ spot: 'Marina Bay Park', note: 'Great views across the bay towards the hills of Marin and Mount Tamalpais' }]",
        'googleRating': '4.7',
        'googleReviews': "'1K'"
    },
    'sf-maritime': {
        'biking': "{ available: true, ebike: true, trails: [{ name: 'SF Bay Trail', distance: 'varies', difficulty: 'Easy', note: 'Paved waterfront path connecting to Fisherman\\'s Wharf' }] }",
        'photography': "{ spots: ['Hyde Street Pier historic ships', 'Aquatic Park cove', 'Maritime Museum building'], tip: 'The historic ships framed against Alcatraz make for stunning nautical photography.' }",
        'sunsetSpots': "[{ spot: 'Aquatic Park Pier', note: 'The curved pier offers a panoramic view of the bay and the setting sun behind the Golden Gate' }]",
        'googleRating': '4.7',
        'googleReviews': "'5.2K'"
    },
    'eugene-oneill': {
        'biking': "{ available: false, ebike: false, trails: [] }",
        'photography': "{ spots: ['Tao House exterior', 'Courtyard gates', 'Las Trampas hills view'], tip: 'The stark white walls and dark wood accents of Tao House photograph beautifully in soft afternoon light.' }",
        'sunsetSpots': "[{ spot: 'Tao House grounds', note: 'Elevated views of the San Ramon Valley turning golden at dusk' }]",
        'googleRating': '4.8',
        'googleReviews': '300'
    },
    'tule-lake-nm': {
        'biking': "{ available: false, ebike: false, trails: [] }",
        'photography': "{ spots: ['Camp segregation center remains', 'Jail building', 'Castle Rock (nearby)'], tip: 'A stark, solemn place. Black and white photography often captures the historic weight of the site effectively.' }",
        'sunsetSpots': "[{ spot: 'Monument landscape', note: 'The wide open Modoc basin provides unobstructed horizon skies' }]",
        'googleRating': '4.6',
        'googleReviews': '150'
    },
    'castle-mountains': {
        'biking': "{ available: true, ebike: false, trails: [{ name: 'Desert dirt roads', distance: 'varies', difficulty: 'Moderate', note: 'Rugged, remote dirt vehicle roads open to bikes' }] }",
        'photography': "{ spots: ['Joshua tree forests', 'Castle Peaks silhouettes', 'Hart Mine ruins'], tip: 'Spring wildflower superblooms (when they happen) contrast incredibly against the red volcanic peaks.' }",
        'sunsetSpots': "[{ spot: 'Lanfair Valley', note: 'Vast desert landscape where the horizon turns neon pink and purple at dusk' }]",
        'googleRating': '4.6',
        'googleReviews': '85'
    },
    'cesar-chavez-nm': {
        'biking': "{ available: false, ebike: false, trails: [] }",
        'photography': "{ spots: ['Visitor Center exhibits', 'Memorial Gardens', 'Historic UFW buildings'], tip: 'The memorial garden provides a peaceful, shaded area with beautiful landscaping.' }",
        'sunsetSpots': "[{ spot: 'Tehachapi Mountains overlook', note: 'Quiet golden hour views of the surrounding oak-studded hills' }]",
        'googleRating': '4.8',
        'googleReviews': '450'
    },
    'desolation-wilderness': {
        'biking': "{ available: false, ebike: false, trails: [] }",
        'photography': "{ spots: ['Lake Aloha', 'Eagle Lake', 'Mt. Tallac summit', 'Dick\\'s Peak'], tip: 'The granite basins reflect the deep blue sky. Use a polarizing filter to cut the glare on the many alpine lakes.' }",
        'sunsetSpots': "[{ spot: 'Mt. Tallac', note: 'Iconic, though challenging to reach at sunset, offering sweeping views of Lake Tahoe' }]",
        'googleRating': '4.9',
        'googleReviews': "'1.8K'"
    },
    'ansel-adams-wilderness': {
        'biking': "{ available: false, ebike: false, trails: [] }",
        'photography': "{ spots: ['Minaret Vista', 'Thousand Island Lake', 'Ediza Lake', 'Ritter Range'], tip: 'Named after the legendary photographer for a reason—the jagged Minarets reflected in alpine lakes are some of the most photogenic peaks in the world.' }",
        'sunsetSpots': "[{ spot: 'Thousand Island Lake', note: 'The alpenglow on Banner Peak reflecting in the island-dotted lake is legendary' }]",
        'googleRating': '4.9',
        'googleReviews': '900'
    },
    'hoover-wilderness': {
        'biking': "{ available: false, ebike: false, trails: [] }",
        'photography': "{ spots: ['Virginia Lakes', 'Saddlebag Lake area', 'Lundy Canyon'], tip: 'Lundy Canyon in October offers some of the best fall color (aspen trees) in the Eastern Sierra.' }",
        'sunsetSpots': "[{ spot: 'Green Creek Valley', note: 'The fading light hitting the steep granite walls of the high Sierra' }]",
        'googleRating': '4.9',
        'googleReviews': '120'
    },
    'emigrant-wilderness': {
        'biking': "{ available: false, ebike: false, trails: [] }",
        'photography': "{ spots: ['Relief Reservoir', 'Kennedy Meadows', 'Emigrant Lake'], tip: 'The vast, rolling granite expanses are perfect for wide-angle landscape shots, especially when afternoon thunderstorms roll in.' }",
        'sunsetSpots': "[{ spot: 'Kennedy Point', note: 'Sweeping views of the Stanislaus River drainage as the sun dips below the Sierra foothills' }]",
        'googleRating': '4.8',
        'googleReviews': '350'
    },
    'trinity-alps': {
        'biking': "{ available: false, ebike: false, trails: [] }",
        'photography': "{ spots: ['Canyon Creek Lakes', 'Emerald Lake', 'Sawtooth Ridge'], tip: 'The white granite of the Alps contrasts beautifully with the deep green forests. Early summer offers spectacular rushing waterfalls.' }",
        'sunsetSpots': "[{ spot: 'Weaverville Bally', note: 'High lookout providing massive panoramic views of the entire wilderness area as it glows in the evening' }]",
        'googleRating': '4.9',
        'googleReviews': "'1.1K'"
    }
}

if __name__ == '__main__':
    inject_data(data)
