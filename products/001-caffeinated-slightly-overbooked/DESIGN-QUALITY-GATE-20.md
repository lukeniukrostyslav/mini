# DESIGN QUALITY GATE — 20/20

## Purpose
A commercial collection must pass a human-style visual and marketplace review in addition to automated rendering tests.

## Per-design gates

Each design must pass all applicable checks:

- [ ] message understood in 1–2 seconds
- [ ] visual hook identifiable without reading every line
- [ ] primary text readable as a mobile thumbnail
- [ ] no accidental collisions or awkward spacing
- [ ] no unnecessary micro-text
- [ ] strong silhouette on a T-shirt
- [ ] works independently of shirt color
- [ ] composition feels intentional, not template-generated
- [ ] visually distinct from the other 19 designs
- [ ] print geometry is safe
- [ ] original artwork/composition
- [ ] no unverified third-party brand/logo/character/likeness
- [ ] phrase risk reviewed before release
- [ ] final PNG render verified
- [ ] actual final asset used for mockup

## Collection-level gates

- [ ] 20/20 masters exist
- [ ] 20/20 final PNG renders exist
- [ ] contact sheet reviewed
- [ ] no obvious duplicate concepts
- [ ] coffee does not dominate every design
- [ ] office/calendar/adult-life categories are visibly differentiated
- [ ] typography systems have enough variation
- [ ] collection looks coherent as one paid bundle
- [ ] strongest designs remain readable in marketplace thumbnails
- [ ] weak designs are revised or removed before packaging

## Important release rule

Automated CI passing is necessary but not sufficient.

A design is not commercially accepted merely because:
- the SVG is valid;
- the PNG has correct dimensions;
- the workflow is green.

Final acceptance requires asset-level, visual, print, originality, packaging and listing QA.

## Current status — 2026-09-26

Masters: 20/20
Automated rendering pipeline: implemented
Full verified 20-file workflow result: pending verification
Human visual review: pending
Mockups: pending
Packaging: in progress
Marketplace listing: pending
Final acceptance: pending
