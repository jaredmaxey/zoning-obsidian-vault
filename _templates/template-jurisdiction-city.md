---
title: "{{title}}"
aliases: ["{{title}}"]  # required when title differs from filename - makes Obsidian resolve title-based wikilinks
type: jurisdiction
tags: ["juris/{{state-slug}}/{{city-slug}}", stub]
created: "{{date}}"
updated: "{{date}}"
status: stub
ai_summary: "{{one-sentence summary, <=30 words}}"
level: city
state: "{{XX}}"
parent_jurisdiction: "{{county title}}"
population: "TBD"
zoning_authority: "{{city planning dept / zoning administrator}}"
code_url: "TBD"
gis_url: "TBD"
source_url: "TBD"
source_last_verified: ""
related: []
children: []                    # zone, overlay, standard, process note titles
---

# {{title}}

## Overview
*1–3 paragraphs: the city's development posture, growth areas, and what makes its zoning regime distinctive.*

## Governing Body
*City council structure, planning commission, zoning administrator/hearing officer — who decides what.*

## Planning Department
*Department name, role, and URL.*

## General Plan / Comprehensive Plan
*The adopted general/comprehensive plan, its horizon year, and how it steers zoning and entitlement.*

## Zoning Code Citation
*The zoning ordinance citation (title/chapter), adoption authority, and where it lives online (code_url).*

## Zoning Map URL
*Link to the official zoning map / GIS (gis_url).*

## Zone Districts Index
*Table of base zone districts, each linking to its `zones/zone-{code}.md` note. This is the spine of the city's zoning tree.*

| Zone Code | Zone Name | Category | Note |
|-----------|-----------|----------|------|
| R1-6 | Single-Family Residence | Residential | [[Zone R1-6 — City]] |
| ... | ... | ... | ... |

## Overlay Districts
*The overlay districts in force, each linking to its `overlays/overlay-{slug}.md` note.*

## Subdivision Standards
*The city's subdivision/platting standards and process.*

## Impact Fees & Exactions
*Development impact fees, dedications, and exactions. Amounts as "TBD — verify" unless confirmed.*

## Permit Timelines
*Typical entitlement and building-permit timelines by application type.*

## Notable Recent Code Changes
*Recent or pending zoning code amendments (e.g., adoption of a form-based/walkable-urban code) that affect development.*

## Sources
*Zoning ordinance, general plan, GIS, and fee schedule URLs. Add each to 00-meta/data-sources.md.*

<!--
AI FILL-IN INSTRUCTIONS (type: jurisdiction, level: city)
- Filename: cities/{city-slug}/00-overview.md. Required frontmatter per §3; level=city, parent_jurisdiction = county title.
- Zone Districts Index table must link to every base zone note you create under zones/. Mirror all child note TITLES (zones, overlays, standards, processes) in children:.
- Tag includes the nested juris/<state>/<city> namespace.
- Put ordinance/GIS/fee URLs in frontmatter + data-sources.md; leave source_last_verified blank until verified.
- Do NOT fabricate fee amounts or timelines — use "TBD — verify against {source}" + needs-verification when unsure.
- SUCCESS CRITERIA: a reader can navigate the city's entire zoning tree from this hub and knows the plan, code citation, map, fees, and process at a glance.
-->
