---
title: "{{title}}"
aliases: ["{{title}}"]  # required when title differs from filename - makes Obsidian resolve title-based wikilinks
type: zone
tags: ["juris/{{state-slug}}/{{city-slug}}", "zoning/{{category}}", stub, needs-verification]
created: "{{date}}"
updated: "{{date}}"
status: stub
ai_summary: "{{one-sentence summary, <=30 words}}"
jurisdiction: "{{City of ___}}"
state: "{{XX}}"
zone_code: "{{R1-6}}"
zone_name: "{{Single-Family Residence District}}"
permitted_uses: []              # high-level use categories permitted by-right
max_height_ft: "TBD"
max_density_dua: "TBD"          # dwelling units per acre
max_far: "TBD"                  # floor area ratio
min_lot_size_sf: "TBD"
setbacks:
  front: "TBD"
  side: "TBD"
  rear: "TBD"
parking_ratio: "TBD"           # e.g., "2 per unit"
source_url: "TBD"
source_last_verified: ""
related: []                     # adjacent/compatible zones, governing standards
parent: "{{city overview title}}"
---

# {{title}}

## Summary
*1–2 paragraphs: the zone's purpose/intent statement (paraphrased from the ordinance), the character of development it produces, and where it's typically applied.*

## Permitted Uses
*Use table. Mark each use as By-Right (P), CUP (C — conditional use permit required), or Prohibited (—). Mirror the by-right categories into the `permitted_uses:` frontmatter list.*

| Use | By-Right | CUP | Prohibited |
|-----|----------|-----|------------|
| {{use}} | P | | |
| {{use}} | | C | |
| {{use}} | | | — |

## Development Standards
*The dimensional standards, using the FIXED column order below so AI can parse reliably. Cover every row listed; use "TBD — verify against {section}" for any value you can't confirm. Mirror the key numeric values into frontmatter.*

| Standard | Requirement | Units | Code Citation | Notes |
|----------|-------------|-------|---------------|-------|
| Max density | TBD | du/acre | | |
| Max FAR | TBD | ratio | | |
| Min lot size | TBD | sf | | |
| Min lot width | TBD | ft | | |
| Max lot coverage | TBD | % | | |
| Max building height | TBD | ft | | |
| Front setback | TBD | ft | | |
| Side setback | TBD | ft | | |
| Rear setback | TBD | ft | | |
| Parking | TBD | spaces/unit or /1,000 sf | | |
| Landscaping | TBD | % or other | | |
| Open space | TBD | % or sf/unit | | |
| Signage | TBD | per sign code | | |

## Subdivision Standards
*If subdivision standards specific to this zone apply, summarize them. Otherwise note "Governed by citywide subdivision standards — see [[...]]" and delete the rest.*

## Overlay Interactions
*How overlays modify this base zone where they apply. Link to relevant `overlay-{slug}.md` notes.*

## Process & Approvals Required
*What approvals development in this zone typically requires (site plan review, design review, CUP for certain uses). Link to the relevant `process` notes.*

## Adjacent / Compatible Zones
*Zones commonly adjacent or used as step-downs/transitions. Wikilink them and mirror in `related:` frontmatter.*

## Recent Amendments
*Recent or pending amendments affecting this zone.*

## Sources
*Direct link to the ordinance section in source_url. Inline-cite every numeric standard: (Source: {Ordinance} § {x}, verified {date}) — or "— UNVERIFIED" until checked. Add the ordinance to 00-meta/data-sources.md.*

<!--
AI FILL-IN INSTRUCTIONS (type: zone) — THE CRITICAL TEMPLATE
- Filename: zones/zone-{code-lowercased-hyphenated}.md (e.g., zone-r1-6.md). parent = city overview title.
- Required frontmatter per _CONVENTIONS.md §3 zone block, including the nested setbacks map and ALL numeric fields.
- DEVELOPMENT STANDARDS TABLE: keep the EXACT column order | Standard | Requirement | Units | Code Citation | Notes | and keep all listed rows.
- NEVER fabricate numeric standards. For any value you cannot confirm against the live ordinance, write "TBD — verify against {section}", keep the value "TBD" in frontmatter, keep the needs-verification tag, and keep status: stub (or draft if qualitative content is solid but numbers pending).
- Populate qualitative content (purpose, permitted-use categories, process) from general knowledge of how the jurisdiction zones.
- Mirror confirmed numeric values from the table into frontmatter (max_height_ft, max_far, setbacks, etc.) AND into 30-reference/parking-ratios-by-use.md (parking) when verified.
- source_last_verified stays BLANK until a human verifies; only a human promotes to reviewed/authoritative.
- SUCCESS CRITERIA: the note states the zone's intent, a complete permitted-use table, a fully-structured standards table (verified values cited, unverified clearly flagged), and links to overlays/processes/adjacent zones — usable directly in a highest-and-best-use analysis.
-->
