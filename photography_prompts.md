---

# Batch 1 of 5 — Copy everything below this line

I'm building a California parks explorer app. For each park listed below, I need two pieces of data:

**1. `photography` — Best photography spots and a tip**
```js
photography: { spots: ['Named Spot 1', 'Named Spot 2', 'Named Spot 3'], tip: 'One practical photography tip specific to this park' },
```
- List 2-5 real, named viewpoints, landmarks, or scenic locations within the park that are known for great photos
- The tip should be specific to this park's conditions (best time of day, best season, lighting conditions, what lens to bring, etc.)

**2. `sunsetSpots` — Best places to watch the sunset**
```js
sunsetSpots: [{ spot: 'Real Place Name', note: 'Why this spot is great for sunset' }],
```
- List 1-3 real named locations within the park where you can watch the sunset
- If the park has no good sunset views (east-facing only, dense canopy, indoor historic site, etc.), return an empty array: `sunsetSpots: [],`

**Output format** — for each park, output ONLY this:
```js
// park-id
photography: { spots: [...], tip: '...' },
sunsetSpots: [...],
```

**Rules:**
- Use real place names that actually exist in the park — not generic labels like "Open Meadows" or "Trail Overlook"
- Escape apostrophes in single-quoted JS strings: `'McArthur\'s Point'` not `'McArthur's Point'`
- Be honest — if you don't know specific spots for a small/obscure park, use the most notable feature (e.g., the main beach, the historic building, the dam overlook)


## Parks (50 parks):

Find the best photography spots and sunset viewing spots for each of these California parks:

- `tule-lake-nm` — Tule Lake National Monument
- `manchester-sp` — Manchester State Park
- `mendocino-headlands` — Mendocino Headlands State Park
- `mendocino-woodlands` — Mendocino Woodlands State Park
- `king-range` — King Range National Conservation Area
- `alabama-hills` — Alabama Hills National Scenic Area
- `carrizo-plain` — Carrizo Plain National Monument
- `sand-to-snow-nm` — Sand to Snow National Monument
- `california-coastal-nm` — California Coastal National Monument
- `point-arena-stornetta` — Point Arena-Stornetta Unit
- `cotoni-coast-dairies` — Cotoni-Coast Dairies Unit
- `elkhorn-slough-reserve` — Elkhorn Slough Reserve
- `reynolds-wc` — Reynolds Wayside Campground
- `schooner-gulch` — Schooner Gulch State Beach
- `westport-landing` — Westport-Union Landing State Beach
- `pfeiffer-big-sur` — Pfeiffer Big Sur State Park
- `julia-pfeiffer-burns` — Julia Pfeiffer Burns State Park
- `andrew-molera` — Andrew Molera State Park
- `montana-de-oro` — Montaña de Oro State Park
- `morro-bay` — Morro Bay State Park
- `asilomar` — Asilomar State Beach
- `carmel-river-sb` — Carmel River State Beach
- `marina-sb` — Marina State Beach
- `monterey-sb` — Monterey State Beach
- `moss-landing-sb` — Moss Landing State Beach
- `salinas-river-sb` — Salinas River State Beach
- `zmudowski-sb` — Zmudowski State Beach
- `san-juan-bautista` — San Juan Bautista State Historic Park
- `estero-bluffs` — Estero Bluffs State Park
- `harmony-headlands` — Harmony Headlands State Park
- `hearst-san-simeon` — Hearst San Simeon State Park
- `morro-strand` — Morro Strand State Beach
- `pismo-sb` — Pismo State Beach
- `chumash-painted-cave` — Chumash Painted Cave SHP
- `el-capitan-sb` — El Capitán State Beach
- `gaviota` — Gaviota State Park
- `la-purisima` — La Purísima Mission State Historic Park
- `point-sal` — Point Sal State Beach
- `refugio-sb` — Refugio State Beach
- `carpinteria-sb` — Carpinteria State Beach
- `lighthouse-field` — Lighthouse Field State Beach
- `manresa-sb` — Manresa State Beach
- `natural-bridges` — Natural Bridges State Beach
- `new-brighton-sb` — New Brighton State Beach
- `santa-cruz-mission` — Santa Cruz Mission SHP
- `seacliff-sb` — Seacliff State Beach
- `sunset-sb` — Sunset State Beach
- `wilder-ranch` — Wilder Ranch State Park
- `bean-hollow` — Bean Hollow State Beach
- `burleigh-murray` — Burleigh H. Murray Ranch


---

---

# Batch 2 of 5 — Copy everything below this line

I'm building a California parks explorer app. For each park listed below, I need two pieces of data:

**1. `photography` — Best photography spots and a tip**
```js
photography: { spots: ['Named Spot 1', 'Named Spot 2', 'Named Spot 3'], tip: 'One practical photography tip specific to this park' },
```
- List 2-5 real, named viewpoints, landmarks, or scenic locations within the park that are known for great photos
- The tip should be specific to this park's conditions (best time of day, best season, lighting conditions, what lens to bring, etc.)

**2. `sunsetSpots` — Best places to watch the sunset**
```js
sunsetSpots: [{ spot: 'Real Place Name', note: 'Why this spot is great for sunset' }],
```
- List 1-3 real named locations within the park where you can watch the sunset
- If the park has no good sunset views (east-facing only, dense canopy, indoor historic site, etc.), return an empty array: `sunsetSpots: [],`

**Output format** — for each park, output ONLY this:
```js
// park-id
photography: { spots: [...], tip: '...' },
sunsetSpots: [...],
```

**Rules:**
- Use real place names that actually exist in the park — not generic labels like "Open Meadows" or "Trail Overlook"
- Escape apostrophes in single-quoted JS strings: `'McArthur\'s Point'` not `'McArthur's Point'`
- Be honest — if you don't know specific spots for a small/obscure park, use the most notable feature (e.g., the main beach, the historic building, the dam overlook)


## Parks (50 parks):

Find the best photography spots and sunset viewing spots for each of these California parks:

- `gray-whale-cove` — Gray Whale Cove State Beach
- `montara-sb` — Montara State Beach
- `pescadero-sb` — Pescadero State Beach
- `pigeon-point` — Pigeon Point Light Station SHP
- `pomponio-sb` — Pomponio State Beach
- `san-gregorio-sb` — San Gregorio State Beach
- `thornton-sb` — Thornton State Beach
- `calaveras-big-trees` — Calaveras Big Trees State Park
- `emerald-bay` — Emerald Bay State Park
- `dl-bliss` — D.L. Bliss State Park
- `sugar-pine-point` — sugar-pine-point
- `donner-memorial` — Donner Memorial State Park
- `grover-hot-springs` — Grover Hot Springs State Park
- `plumas-eureka` — Plumas-Eureka State Park
- `washoe-meadows` — Washoe Meadows State Park
- `burton-creek` — Burton Creek State Park
- `kings-beach` — Kings Beach State Recreation Area
- `ward-creek` — Ward Creek
- `marshall-gold` — Marshall Gold Discovery State Historic Park
- `malakoff-diggins` — Malakoff Diggins State Historic Park
- `south-yuba-river` — South Yuba River State Park
- `folsom-powerhouse` — Folsom Powerhouse State Historic Park
- `delta-meadows` — Delta Meadows
- `locke-boarding-house` — Locke Boarding House Museum
- `bidwell-mansion` — Bidwell Mansion State Historic Park
- `bidwell-sacramento` — Bidwell-Sacramento River State Park
- `ahjumawi` — Ahjumawi Lava Springs State Park
- `william-ide` — William B. Ide Adobe State Historic Park
- `great-valley-grasslands` — Great Valley Grasslands State Park
- `pacheco-sp` — Pacheco State Park
- `caswell-memorial` — Caswell Memorial State Park
- `colonel-allensworth` — Colonel Allensworth State Historic Park
- `mcarthur-burney-falls` — McArthur-Burney Falls Memorial State Park
- `castle-crags` — Castle Crags State Park
- `columbia-shp` — Columbia State Historic Park
- `indian-grinding-rock` — Indian Grinding Rock State Historic Park
- `crystal-cove` — Crystal Cove State Park
- `malibu-creek` — Malibu Creek State Park
- `leo-carrillo` — Leo Carrillo State Park
- `point-mugu` — Point Mugu State Park
- `cuyamaca-rancho` — Cuyamaca Rancho State Park
- `red-rock-canyon` — Red Rock Canyon State Park
- `chino-hills` — Chino Hills State Park
- `los-angeles-shp` — Los Angeles State Historic Park
- `malibu-lagoon` — Malibu Lagoon State Beach
- `robert-meyer-sb` — Robert H. Meyer Memorial State Beach
- `saddleback-butte` — Saddleback Butte State Park
- `topanga-sp` — Topanga State Park
- `will-rogers` — Will Rogers State Historic Park
- `bolsa-chica` — Bolsa Chica State Beach


---

---

# Batch 3 of 5 — Copy everything below this line

I'm building a California parks explorer app. For each park listed below, I need two pieces of data:

**1. `photography` — Best photography spots and a tip**
```js
photography: { spots: ['Named Spot 1', 'Named Spot 2', 'Named Spot 3'], tip: 'One practical photography tip specific to this park' },
```
- List 2-5 real, named viewpoints, landmarks, or scenic locations within the park that are known for great photos
- The tip should be specific to this park's conditions (best time of day, best season, lighting conditions, what lens to bring, etc.)

**2. `sunsetSpots` — Best places to watch the sunset**
```js
sunsetSpots: [{ spot: 'Real Place Name', note: 'Why this spot is great for sunset' }],
```
- List 1-3 real named locations within the park where you can watch the sunset
- If the park has no good sunset views (east-facing only, dense canopy, indoor historic site, etc.), return an empty array: `sunsetSpots: [],`

**Output format** — for each park, output ONLY this:
```js
// park-id
photography: { spots: [...], tip: '...' },
sunsetSpots: [...],
```

**Rules:**
- Use real place names that actually exist in the park — not generic labels like "Open Meadows" or "Trail Overlook"
- Escape apostrophes in single-quoted JS strings: `'McArthur\'s Point'` not `'McArthur's Point'`
- Be honest — if you don't know specific spots for a small/obscure park, use the most notable feature (e.g., the main beach, the historic building, the dam overlook)


## Parks (50 parks):

Find the best photography spots and sunset viewing spots for each of these California parks:

- `doheny-sb` — Doheny State Beach
- `huntington-sb` — Huntington State Beach
- `san-clemente-sb` — San Clemente State Beach
- `san-onofre-sb` — San Onofre State Beach
- `california-citrus` — California Citrus State Historic Park
- `indio-hills` — Indio Hills Palms
- `san-timoteo` — San Timoteo Canyon
- `wildwood-canyon` — Wildwood Canyon
- `border-field` — Border Field State Park
- `cardiff-sb` — Cardiff State Beach
- `carlsbad-sb` — Carlsbad State Beach
- `san-elijo-sb` — San Elijo State Beach
- `san-pasqual` — San Pasqual Battlefield SHP
- `silver-strand-sb` — Silver Strand State Beach
- `south-carlsbad-sb` — South Carlsbad State Beach
- `tijuana-estuary` — Tijuana Estuary
- `torrey-pines-sb` — Torrey Pines State Beach
- `emma-wood` — Emma Wood State Beach
- `mandalay-sb` — Mandalay State Beach
- `mcgrath-sb` — McGrath State Beach
- `san-buenaventura-sb` — San Buenaventura State Beach
- `sequoia` — Sequoia National Park
- `kings-canyon` — Kings Canyon National Park
- `joshua-tree` — Joshua Tree National Park
- `death-valley` — Death Valley National Park
- `pinnacles` — Pinnacles National Park
- `channel-islands` — Channel Islands National Park
- `lassen-volcanic` — Lassen Volcanic National Park
- `point-reyes` — Point Reyes National Seashore
- `golden-gate` — Golden Gate National Recreation Area
- `whiskeytown` — Whiskeytown National Recreation Area
- `devils-postpile` — Devils Postpile National Monument
- `lava-beds` — Lava Beds National Monument
- `mojave-preserve` — Mojave National Preserve
- `cabrillo` — Cabrillo National Monument
- `john-muir-nhs` — John Muir National Historic Site
- `manzanar` — Manzanar National Historic Site
- `angel-island` — Angel Island State Park
- `crown-memorial-sb` — Robert W. Crown Memorial State Beach
- `pacifica-sb` — Pacifica State Beach
- `marconi-conference-center` — Marconi Conference Center SHP
- `marsh-creek-shp` — Marsh Creek State Historic Park
- `petaluma-adobe` — Petaluma Adobe State Historic Park
- `sonoma-shp` — Sonoma State Historic Park
- `point-cabrillo` — Point Cabrillo Light Station SHP
- `bodie` — Bodie State Historic Park
- `empire-mine` — Empire Mine State Historic Park
- `governors-mansion` — governors-mansion
- `leland-stanford-mansion` — Leland Stanford Mansion State Historic Park
- `ca-mining-museum` — California State Mining and Mineral Museum


---

---

# Batch 4 of 5 — Copy everything below this line

I'm building a California parks explorer app. For each park listed below, I need two pieces of data:

**1. `photography` — Best photography spots and a tip**
```js
photography: { spots: ['Named Spot 1', 'Named Spot 2', 'Named Spot 3'], tip: 'One practical photography tip specific to this park' },
```
- List 2-5 real, named viewpoints, landmarks, or scenic locations within the park that are known for great photos
- The tip should be specific to this park's conditions (best time of day, best season, lighting conditions, what lens to bring, etc.)

**2. `sunsetSpots` — Best places to watch the sunset**
```js
sunsetSpots: [{ spot: 'Real Place Name', note: 'Why this spot is great for sunset' }],
```
- List 1-3 real named locations within the park where you can watch the sunset
- If the park has no good sunset views (east-facing only, dense canopy, indoor historic site, etc.), return an empty array: `sunsetSpots: [],`

**Output format** — for each park, output ONLY this:
```js
// park-id
photography: { spots: [...], tip: '...' },
sunsetSpots: [...],
```

**Rules:**
- Use real place names that actually exist in the park — not generic labels like "Open Meadows" or "Trail Overlook"
- Escape apostrophes in single-quoted JS strings: `'McArthur\'s Point'` not `'McArthur's Point'`
- Be honest — if you don't know specific spots for a small/obscure park, use the most notable feature (e.g., the main beach, the historic building, the dam overlook)


## Parks (50 parks):

Find the best photography spots and sunset viewing spots for each of these California parks:

- `ca-railroad-museum` — California State Railroad Museum
- `sutters-fort` — sutters-fort
- `state-indian-museum` — State Indian Museum
- `railtown-1897` — Railtown 1897 State Historic Park
- `wassama-round-house` — Wassama Round House State Historic Park
- `shasta-shp` — Shasta State Historic Park
- `weaverville-joss-house` — Weaverville Joss House State Historic Park
- `woodland-opera-house` — Woodland Opera House State Historic Park
- `sutter-buttes` — Sutter Buttes State Park
- `hearst-castle` — Hearst San Simeon State Historical Monument
- `limekiln-sp` — Limekiln State Park
- `point-sur-shp` — Point Sur State Historic Park
- `monterey-shp` — Monterey State Historic Park
- `el-presidio` — El Presidio de Santa Barbara SHP
- `cambria-smp` — Cambria State Marine Park
- `cayucos-sb` — Cayucos State Beach
- `twin-lakes-sb` — Twin Lakes State Beach
- `antelope-valley-indian` — Antelope Valley Indian Museum SHP
- `tomo-kahni` — Tomo-Kahni State Historic Park
- `fort-tejon` — Fort Tejon State Historic Park
- `placerita-canyon` — Placerita Canyon State Park
- `los-encinos` — Los Encinos State Historic Park
- `santa-susana-pass` — Santa Susana Pass State Historic Park
- `dockweiler-sb` — Dockweiler State Beach
- `santa-monica-sb` — Santa Monica State Beach
- `will-rogers-sb` — Will Rogers State Beach
- `point-dume-sb` — Point Dume State Beach
- `pio-pico` — Pío Pico State Historic Park
- `watts-towers` — Watts Towers of Simon Rodia SHP
- `corona-del-mar` — Corona del Mar State Beach
- `leucadia-sb` — Leucadia State Beach
- `moonlight-sb` — Moonlight State Beach
- `almaden-quicksilver` — Almaden Quicksilver County Park
- `alviso-marina` — Alviso Marina County Park
- `calero` — Calero County Park
- `chitactac-adams` — Chitactac-Adams Heritage County Park
- `coyote-creek-parkway` — Coyote Creek Parkway
- `ed-levin` — Ed R. Levin County Park
- `field-sports` — Field Sports Park
- `hellyer` — Hellyer County Park
- `joseph-grant` — Joseph D. Grant County Park
- `los-gatos-creek` — Los Gatos Creek County Park
- `metcalf-motorcycle` — Metcalf Motorcycle County Park
- `mt-madonna` — Mt. Madonna County Park
- `penitencia-creek` — Penitencia Creek
- `rancho-san-antonio` — Rancho San Antonio County Park and Open Space Preserve
- `sanborn` — Sanborn County Park
- `santa-teresa` — Santa Teresa County Park
- `stevens-creek` — Stevens Creek County Park
- `sunnyvale-baylands` — Sunnyvale Baylands Park


---

---

# Batch 5 of 5 — Copy everything below this line

I'm building a California parks explorer app. For each park listed below, I need two pieces of data:

**1. `photography` — Best photography spots and a tip**
```js
photography: { spots: ['Named Spot 1', 'Named Spot 2', 'Named Spot 3'], tip: 'One practical photography tip specific to this park' },
```
- List 2-5 real, named viewpoints, landmarks, or scenic locations within the park that are known for great photos
- The tip should be specific to this park's conditions (best time of day, best season, lighting conditions, what lens to bring, etc.)

**2. `sunsetSpots` — Best places to watch the sunset**
```js
sunsetSpots: [{ spot: 'Real Place Name', note: 'Why this spot is great for sunset' }],
```
- List 1-3 real named locations within the park where you can watch the sunset
- If the park has no good sunset views (east-facing only, dense canopy, indoor historic site, etc.), return an empty array: `sunsetSpots: [],`

**Output format** — for each park, output ONLY this:
```js
// park-id
photography: { spots: [...], tip: '...' },
sunsetSpots: [...],
```

**Rules:**
- Use real place names that actually exist in the park — not generic labels like "Open Meadows" or "Trail Overlook"
- Escape apostrophes in single-quoted JS strings: `'McArthur\'s Point'` not `'McArthur's Point'`
- Be honest — if you don't know specific spots for a small/obscure park, use the most notable feature (e.g., the main beach, the historic building, the dam overlook)


## Parks (3 parks):

Find the best photography spots and sunset viewing spots for each of these California parks:

- `upper-stevens-creek` — Upper Stevens Creek County Park
- `uvas-canyon` — Uvas Canyon County Park
- `villa-montalvo` — Villa Montalvo


---

