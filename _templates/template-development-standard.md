---
title: "{{title}}"
aliases: ["{{title}}"]  # required when title differs from filename - makes Obsidian resolve title-based wikilinks
type: standard
tags: ["juris/{{state-slug}}/{{city-slug}}", "standard/{{slug}}", stub, needs-verification]
created: "{{date}}"
updated: "{{date}}"
status: stub
ai_summary: "{{one-sentence summary, <=30 words}}"
jurisdiction: "{{City of ___}}"
state: "{{XX}}"
applies_to: []                  # zones or use types the standard governs
source_url: "TBD"
source_last_verified: ""
related: []
---

# {{title}}

## Summary
*1–2 paragraphs: what this standard regulates (e.g., citywide parking, landscaping, signage, walls/fences), why it exists, and its scope.*

## Applicability
*Which zones, use types, or geographies the standard applies to, and any exemptions in scope. Mirror in `applies_to:` frontmatter.*

## Requirement Detail
*The actual requirements, using the FIXED column order below for any tabular values so AI can parse reliably.*

| Standard | Requirement | Units | Code Citation | Notes |
|----------|-------------|-------|---------------|-------|
| {{standard}} | TBD | {{units}} | | |

## Exceptions
*Waivers, reductions, administrative adjustments, and how they're obtained.*

## Calculation Examples
*Worked examples showing how to apply the standard (e.g., required parking for a 200-unit project). Label figures as illustrative.*

## Related Zones
*Zones governed by this standard. Wikilink and mirror in `related:` frontmatter.*

## Sources
*Direct ordinance link in source_url; inline-cite figures. Add to 00-meta/data-sources.md.*

<!--
AI FILL-IN INSTRUCTIONS (type: standard)
- Filename: standards/{slug}.md within a city folder. Required frontmatter per §3 standard block.
- Requirement Detail table uses the SAME fixed column order as the zone template: | Standard | Requirement | Units | Code Citation | Notes |.
- NEVER fabricate numeric requirements — use "TBD — verify against {section}" + needs-verification tag + status: stub until confirmed.
- Populate applies_to: with the zones/use types governed; populate related: with zone note TITLES.
- source_last_verified stays blank until human verification.
- SUCCESS CRITERIA: a reader knows exactly what the standard requires, where it applies, how to calculate compliance, and how to get relief — with sourced figures.
-->
