# CA Parks Data Quality Review

Reviewed file: `caparks.html`

Status:
- Refreshed after the March 23 cleanup pass and legacy-schema normalization
- `PARK_DETAILS` currently contains 353 entries
- Numeric `sites` and numeric `googleReviews` source values have now been canonicalized

## Verification

- Inline script syntax parses successfully.
- Headless Chrome rendered the page and produced 353 park cards.
- Sidebar progress populated to `12 / 353 visited` and `3% complete`, which confirms init still runs.
- The sidebar now includes a rendered `Data Checks` panel.
- Current rendered check counts:
  - detail coverage: `353 / 353`
  - missing hikes: `0`
  - intentional no-hike entries: `3`
  - missing wildlife: `0`
  - camping `N/A`: `0`
  - bike distance `varies`: `48`
  - generic wildlife: `0`

## Fixed Since Prior Review

### High-confidence park-data fixes completed

These previously flagged entries were corrected in `caparks.html`:

- `half-moon-bay`
- `tomales-bay`
- `albany-smr`
- `emeryville-crescent`
- `mclaughlin-eastshore`
- `olompali`
- `ishxenta`
- `desolation-wilderness`
- `ansel-adams-wilderness`
- `hoover-wilderness`
- `emigrant-wilderness`
- `trinity-alps`
- `benicia-sra`
- `trione-annadel`

Summary of what changed:

- wrong-park / wrong-region coastal and urban content was rewritten
- placeholder wilderness hike gains were replaced with plausible real values
- contradictory trail metrics were corrected
- obviously generic or misleading content was reduced in several new entries

### Legacy source-schema normalization completed

The source data no longer depends on old key names for current content:

- `top5`: `0` remaining
- `thingsToDo`: `0` remaining
- `fee`: `0` remaining
- `parking`: `0` remaining
- `photos`: `0` remaining
- `camping`: `0` remaining

### Camping-block coverage normalized

- Entries missing explicit `carCamping` / `tentCamping` blocks: `0`
- Entries still using camping `N/A` placeholders: `0`

This includes the older legacy entries plus the previously missing beach / county-park entries.

### Generic wildlife cleanup completed

- Entries still using broad generic wildlife labels like `Gull` or `Fox`: `0`

## Current Open Issues

### 1. Intentional no-hike entries

These entries still have no `hikes` array content:

- `franks-tract`
- `field-sports`
- `metcalf-motorcycle`

Decision:

- `franks-tract` should remain no-hike because it is a flooded, boat-access Delta unit.
- `field-sports` should remain no-hike because it is a shooting-range facility, not a trail destination.
- `metcalf-motorcycle` should remain no-hike because it is an OHV riding facility, not a hiking park.

These are now treated as intentional exceptions rather than data-quality defects.

### 2. Remaining low-information values are now narrower

The broad camping `N/A` and generic-wildlife cleanup is complete. The main legacy residue is now the biking metadata.

Primary remaining example:

- bike trail distances recorded as `varies`

Current count:

- `48` entries still have at least one biking trail with `distance: 'varies'`

Lower-priority residue that may still deserve a later pass:

- general low-information wording in some older legacy-authored notes

This is now a lower-priority cleanup than the original factual / wrong-park issues.

## Structural Notes

### Runtime normalization has been removed

The source data is now canonical enough that the old `normalizeParkDetail()` helper has been removed entirely.

Current dependency counts are all `0`:

- `photography -> photoSpots`
- wildlife string-to-object normalization
- camping site count coercion
- `googleReviews` formatting

This is no longer compensating for the old `top5` / `thingsToDo` / `fee` / `parking` / `photos` / `camping` source schema.

### Browser / UI notes

Verified:

- page renders
- cards render
- sidebar stats populate
- `Data Checks` renders with live counts

Not verified in a live interactive browser session:

- console output
- weather fetch behavior
- map network behavior

## Recommended Next Fix Order

1. Tighten the `48` biking entries that still use `distance: 'varies'`.
2. Spot-check older parks for plausible but still unverified trail metrics or ratings.
3. Split the CA Parks page into static data / JS / CSS files once you want the structural refactor.
