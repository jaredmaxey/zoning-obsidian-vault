---
title: "{{title}}"
type: asset-class
tags: [cre, "asset/{{slug}}", stub]
created: "{{date}}"
updated: "{{date}}"
status: stub
ai_summary: "{{one-sentence summary, <=30 words}}"
asset_class: multifamily    # one of: multifamily | office | retail | industrial | hospitality | self-storage | mixed-use | ground-up-development | land | specialty
subtypes: []                # list of subtype names
related: []
---

# {{title}}

## Overview
*1–3 paragraphs: what this asset class is, its role in institutional portfolios, current sentiment, and the headline thesis for/against it.*

## Subtypes
*Break down the subtypes within the class (e.g., multifamily: garden, mid-rise, high-rise, BTR/SFR, student, senior). One short paragraph or bullet each. Mirror names in the `subtypes:` frontmatter list.*

## Demand Drivers
*What creates tenant/user demand — demographics, employment, e-commerce, tourism, etc. What to watch as leading indicators.*

## Supply Dynamics
*How new supply is delivered, typical development timelines, barriers to entry, and how supply tends to overshoot/undershoot in cycles.*

## Underwriting Norms
*Typical ranges as a table. Present as ranges with explicit "varies by market" qualifiers. Do not invent precise figures.*

| Metric | Typical Range | Notes |
|--------|---------------|-------|
| Going-in cap rate | X.X% – Y.Y% | Class A urban core tighter; class B suburban wider |
| Stabilized vacancy | X% – Y% | |
| Operating expense ratio | X% – Y% | |
| Exit cap (spread to going-in) | +X bps – +Y bps | |

*Ranges current as of {{date}}. Verify against current market data before underwriting.*

## Key Operating Metrics
*The class-specific metrics that matter most (e.g., RevPAR/ADR/occupancy for hotels, sales per SF for retail, $/SF/year NNN for industrial, RevPAU for self-storage). Define each briefly.*

## Common Deal Structures
*Typical ownership, financing, and JV structures for this class; lease structures (gross, NNN, modified gross); brand/management arrangements where relevant.*

## Major Risks
*Class-specific risks (e.g., obsolescence for office, tenant concentration for STNL retail, RevPAR volatility for hotels) and mitigants.*

## Regulatory Considerations
*Class-specific regulatory issues — rent control (multifamily), ADA (retail), healthcare/licensing (MOB/senior), entitlement intensity (industrial), etc.*

## Notable Markets
*Markets where this class is concentrated or notable, and why. Qualitative only.*

## Related Notes
*Wikilink to relevant concepts, deal types, frameworks, and the subtype notes in this folder. Mirror in `related:` frontmatter.*

<!--
AI FILL-IN INSTRUCTIONS (type: asset-class)
- This template is the asset-class folder's 00-overview.md entry point.
- Required frontmatter: title, type=asset-class, tags (cre + asset/<slug> + stub), created, updated, status, ai_summary, asset_class, subtypes, related.
- asset_class must be one of the enumerated values; the slug in the asset/ tag matches it.
- Populate subtypes: with the subtype note names you create alongside this overview.
- Underwriting Norms MUST be a table with ranges + "varies by market" qualifiers + the "Ranges current as of {date}" footer. NEVER fabricate precise cap rates or expense ratios.
- Set status: draft when sections carry substantive (1–3 paragraph) content.
- SUCCESS CRITERIA: a reader gets a complete institutional picture of the asset class — what it is, what drives it, how it underwrites, its risks, and its regulatory landscape — with all quantitative claims hedged as ranges and dated.
-->
