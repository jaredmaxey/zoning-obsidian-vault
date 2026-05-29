---
title: "{{title}}"
type: jurisdiction
tags: ["juris/{{state-slug}}", stub]
created: "{{date}}"
updated: "{{date}}"
status: stub
ai_summary: "{{one-sentence summary, <=30 words}}"
level: county
state: "{{XX}}"
parent_jurisdiction: "{{state title}}"
population: "TBD"
zoning_authority: "{{county planning/zoning authority}}"
code_url: "TBD"
gis_url: "TBD"
source_url: "TBD"
source_last_verified: ""
related: []
children: []                    # city note titles within the county
---

# {{title}}

## Overview
*1–3 paragraphs: the county's role in the metro, growth posture, and what distinguishes its unincorporated-area regulation.*

## Governing Body
*Board of supervisors/commissioners structure, how land-use decisions are made, meeting cadence.*

## Planning Department
*Name, role, and URL of the planning/development department. What it handles vs. what cities handle.*

## Unincorporated Area Zoning
*How the county zones unincorporated land — the code reference, the zone district families, and where the code lives. This is the county's core land-use product.*

## Subdivision Regulations
*County subdivision/plat process and standards for unincorporated land.*

## Building Code Adoption
*Which building codes the county has adopted and the edition year.*

## Permit Process
*The development permit path at the county level — typical steps and sequencing.*

## Impact Fees
*County impact/development fees and what they fund. Note amounts as "TBD — verify" unless confirmed.*

## Cities Within
*The incorporated cities in the county. Link to each city's `00-overview.md`. Mirror titles in `children:` frontmatter.*

## Sources
*County code, planning dept, and GIS URLs. Add to 00-meta/data-sources.md.*

<!--
AI FILL-IN INSTRUCTIONS (type: jurisdiction, level: county)
- Filename: counties/county-{slug}.md. Required frontmatter per §3; level=county, parent_jurisdiction = the state's note title.
- Populate children: with the city note TITLES within this county.
- Focus content on UNINCORPORATED-area regulation (that's what counties control); cities have their own notes.
- Put URLs in frontmatter + data-sources.md; leave source_last_verified blank until verified. Use "TBD — verify" for unconfirmed fees/figures + needs-verification tag.
- SUCCESS CRITERIA: a reader knows how the county regulates unincorporated land, its permit/subdivision process, and which cities sit within it.
-->
