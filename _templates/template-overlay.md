---
title: "{{title}}"
type: overlay
tags: ["juris/{{state-slug}}/{{city-slug}}", zoning/overlay, stub]
created: "{{date}}"
updated: "{{date}}"
status: stub
ai_summary: "{{one-sentence summary, <=30 words}}"
jurisdiction: "{{City of ___}}"
state: "{{XX}}"
base_zones_affected: []         # base zones the overlay can sit on top of
source_url: "TBD"
source_last_verified: ""
related: []
---

# {{title}}

## Summary
*1–2 paragraphs: the overlay's purpose (historic, transit, hillside, downtown, etc.) and what triggers its application.*

## Geographic Extent
*Where the overlay applies — boundaries, map reference, and how to determine if a parcel is within it.*

## Modifications to Base Zoning
*How the overlay changes the underlying base zone's standards — height, density, setbacks, use, parking. Be specific about what's added vs. relaxed. Mirror affected base zones in `base_zones_affected:` frontmatter.*

## Additional Requirements
*New requirements the overlay imposes beyond the base zone (design review, materials, frontage, etc.).*

## Process Changes
*How the overlay changes the approval process (e.g., additional design review, historic board sign-off).*

## Sources
*Direct ordinance link in source_url; inline-cite. Add to 00-meta/data-sources.md.*

<!--
AI FILL-IN INSTRUCTIONS (type: overlay)
- Filename: overlays/overlay-{slug}.md within a city folder. Required frontmatter per §3 overlay block.
- Populate base_zones_affected: with the base zone TITLES the overlay can apply over; cross-link from those zone notes' Overlay Interactions sections.
- Be precise about MODIFICATIONS — an overlay adds/relaxes specific standards; never fabricate the specifics, use "TBD — verify" + needs-verification when unsure.
- source_last_verified blank until verified.
- SUCCESS CRITERIA: a reader can tell whether a parcel is in the overlay, exactly how it changes the base zoning, and what extra process applies.
-->
