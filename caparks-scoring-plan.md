# CA Parks Scoring Plan

## Goal

Create a scoring system for each location in `caparks.html` that helps answer:

- How good is this place overall?
- How good is it for me right now?
- How much do I personally care about it?
- How trustworthy is the score based on available data?

The scoring system should support trip planning, not just data ranking.

## Recommended Score Model

Use four separate scores:

- `destinationScore`: how inherently strong the place is as a destination
- `fitScore`: how well it fits current conditions and Bay Area access
- `manualScore`: personal preference / bucket-list pull
- `confidenceScore`: how complete and trustworthy the data is

Then compute:

```text
overallScore =
  0.45 * destinationScore +
  0.35 * fitScore +
  0.20 * manualScore
```

Keep `confidenceScore` separate. Do not fold it into the main score.

## Why This Model

- Great places should still score highly even when they are far away.
- Nearby places should not automatically win just because they are easy.
- Personal preference matters and should be explicit.
- Data completeness is uneven, so users should see how much to trust a score.

## Score Breakdown

All scores should be normalized to `0-100`.

### 1. destinationScore

This should be mostly stable and based on the place itself.

```text
destinationScore =
  0.30 * activityScore +
  0.25 * hikeScore +
  0.15 * campingScore +
  0.15 * uniquenessScore +
  0.10 * detailRichnessScore +
  0.05 * publicSentimentScore
```

#### activityScore

Use existing `activities` tags from `PARKS`.

Suggested activity weights:

- `12`: `backpacking`, `waterfalls`, `redwoods`, `giant-trees`, `hot-springs`, `tide-pools`, `island`, `caving`, `lava-tubes`
- `9`: `rock-climbing`, `kayaking`, `stargazing`, `wildflowers`, `wildlife`, `whale-watching`
- `7`: `hiking`, `camping`, `snowshoeing`, `photography`
- `5`: `swimming`, `surfing`, `fishing`, `biking`, `mtb`, `boating`, `horses`
- `3`: `historic`

Formula:

```text
activityScore = min(100, sum(unique activity weights))
```

#### hikeScore

Use `PARK_DETAILS[id].hikes`.

```text
base = min(70, hikes.length * 14)
difficultyBonus = 0 / 10 / 20 depending on whether hikes cover 1 / 2 / 3 difficulty levels
backpackingBonus = 10 if activities include backpacking
hikeScore = min(100, base + difficultyBonus + backpackingBonus)
```

#### campingScore

```text
60 if both car + tent camping
40 if only one is available
15 if no camping but strong day-use destination
0 if neither and weak stay potential
```

#### uniquenessScore

Suggested base by place type:

- `95`: `np`, `wilderness`
- `90`: `nm`, `nca`, `nsa`
- `82`: `snr`, `reserve`
- `75`: `sp`, `sra`
- `68`: `sb`
- `60`: `shp`, `nhs`

Then add `+5` to `+10` for especially distinctive features like:

- `redwoods`
- `waterfalls`
- `hot-springs`
- `giant-trees`
- `island`
- `whale-watching`
- `lava-tubes`

Cap at `100`.

#### detailRichnessScore

Measure how much useful structured data exists.

Suggested scoring:

- `15` each for: `things`, `hikes`, `photoSpots`, `wildlife`
- `10` each for: `bestMonths`, `parkingTip`, `nearbyFood`, `entranceFee`, `elevation`

Cap at `100`.

#### publicSentimentScore

Use `googleRating` lightly.

```text
if no googleRating: 60
else publicSentimentScore = clamp((googleRating - 3.5) / 1.5 * 100, 0, 100)
```

### 2. fitScore

This should answer: how good is this place for me right now?

Use current month, current home base, and planning practicality.

```text
fitScore =
  0.40 * seasonScore +
  0.30 * distanceScore +
  0.15 * costScore +
  0.15 * planningScore
```

#### seasonScore

```text
100 if current month is in bestMonths
75 if adjacent to a best month
45 if two months away
20 otherwise
50 if no bestMonths data
```

#### distanceScore

Use `p.distance`.

```text
100 if <= 60 mi
85 if <= 120
70 if <= 200
55 if <= 300
40 if <= 450
25 otherwise
```

#### costScore

```text
100 if libraryPass
90 if entranceFee is Free
75 if fee is modest
55 if fee is high
65 if unknown
```

#### planningScore

```text
100 if full PARK_DETAILS exists
70 if partial details exist
40 if only basic PARKS row exists
```

### 3. manualScore

This is the user-preference layer and should be explicit.

Add three manual fields per park:

- `wow`: `1-5`
- `priority`: `1-5`
- `repeatability`: `1-5`

Formula:

```text
manualScore =
  0.45 * wow +
  0.35 * priority +
  0.20 * repeatability
```

Then scale the result to `0-100`.

This is the part that captures:

- bucket-list pull
- emotional appeal
- places worth revisiting

### 4. confidenceScore

This should measure data quality only.

```text
confidenceScore =
  presentFields / expectedFields * 100
```

Suggested expected fields:

- `bestMonths`
- `entranceFee`
- `carCamping`
- `tentCamping`
- `parkingTip`
- `nearbyFood`
- `things`
- `hikes`
- `photoSpots`
- `wildlife`
- `elevation`

Example interpretation:

- `overallScore = 84`, `confidenceScore = 95`: strong and trustworthy
- `overallScore = 84`, `confidenceScore = 35`: attractive but weakly supported

## Important Rule

Do not include `visited` in the core score.

Visited should be treated as a filter or a separate planning adjustment, not a quality signal.

If needed later:

```text
nextTripScore = visited ? overallScore - 25 : overallScore
```

Or simply filter visited places out when ranking future trips.

## Data To Add Per Park

When implementing scoring, attach a score object to each park:

```js
p.scores = {
  destination: 0,
  fit: 0,
  manual: 0,
  overall: 0,
  confidence: 0,
}
```

Suggested optional manual defaults for parks without user input yet:

```text
wow = 3
priority = 3
repeatability = 3
```

This keeps the system usable before manual tuning.

## Recommended UI Usage

Short-term:

- Add a new sort option: `Best Overall`
- Optionally show a small score pill on cards
- Optionally show `overall + confidence` together

Example:

```text
84 overall · 91 confidence
```

Longer-term:

- Add a dedicated filter for `Top Picks`
- Add editable manual fields in the modal
- Add separate ranking views for:
  - best overall
  - best this month
  - best weekend trip
  - best bucket-list park

## Practical Notes For This Repo

This model fits the current `caparks.html` structure because it already has:

- `PARKS.activities`
- `p.distance`
- `libraryPass`
- `bestMonths`
- camping data
- `googleRating`
- `hikes`
- `photoSpots`
- `wildlife`

The current dataset is not fully complete, so `confidenceScore` is important from day one.

## Recommended First Implementation

1. Add a central scoring config object for weights and thresholds.
2. Compute all park scores during page initialization.
3. Add `Best Overall` to the sort dropdown.
4. Sort by `p.scores.overall` when that mode is selected.
5. Show the score in cards and the modal.
6. Add manual score fields later, after the base model feels right.

## Default Assumptions

- Home base remains the current Milpitas-area coordinate already used by the page.
- Current month drives `fitScore`.
- Missing manual data should default to neutral values.
- Missing detail data should reduce `fitScore` and `confidenceScore`, not destroy `destinationScore`.

## Open Review Questions

Before implementation, review these:

- Are the activity weights too hiking/backpacking-heavy or correct for current priorities?
- Should historic sites stay in the same scoring pool as outdoor destinations?
- Should `manualScore` remain a separate layer or be more heavily weighted?
- Should there eventually be multiple ranking modes instead of one main score?
