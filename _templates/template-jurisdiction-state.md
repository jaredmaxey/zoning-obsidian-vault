---
title: "{{title}}"
aliases: ["{{title}}"]  # required when title differs from filename - makes Obsidian resolve title-based wikilinks
type: jurisdiction
tags: ["juris/{{state-slug}}", stub]
created: "{{date}}"
updated: "{{date}}"
status: stub
ai_summary: "{{one-sentence summary, <=30 words}}"
level: state
state: "{{XX}}"                 # two-letter postal, e.g., AZ
parent_jurisdiction: null
population: "TBD"
zoning_authority: "{{enabling statutes / authority}}"
code_url: "TBD"
gis_url: "TBD"
source_url: "TBD"
source_last_verified: ""        # blank until a human verifies
related: []
children: []                    # county note titles
---

# {{title}}

## Overview
*1–3 paragraphs: the state's land-use posture, growth context, and what an out-of-state developer most needs to know first.*

## Statutory Framework
*Which statutory titles/chapters govern municipal and county land use (cite them). Link to the `state-statutes/` notes. Identify the enabling authority for zoning.*

## Home Rule vs. Dillon's Rule
*Is this a home-rule or Dillon's Rule state? How much independent authority do charter cities have? Practical implications for entitlement.*

## State-Level Agencies
*The agencies a developer interacts with — DOT, Real Estate Department, State Land Department, water/environmental agencies, housing finance agency. One line each on role.*

## Tax Environment
*Property tax structure, transfer taxes, relevant incentives (Opportunity Zones, abatements, TIF equivalents).*

## Disclosure & Closing Norms
*State-specific disclosure requirements, title/escrow norms, and anything unusual about how deals close here.*

## Key Counties
*The counties that matter most (major MSAs). Link to each `counties/county-{slug}.md`. Mirror titles in `children:` frontmatter.*

## Notable Statewide Programs
*LIHTC allocator, Opportunity Zones, brownfield programs, water-adequacy programs, etc.*

## Sources
*Official statute URLs and agency links. Add each to 00-meta/data-sources.md. Use inline citation format from _CONVENTIONS.md §6.*

<!--
AI FILL-IN INSTRUCTIONS (type: jurisdiction, level: state)
- Filename: 00-state-overview.md inside the state folder. Required frontmatter per _CONVENTIONS.md §3 jurisdiction block; level=state, parent_jurisdiction=null.
- Populate children: with the county note TITLES you create.
- Put official statute/agency URLs in source_url/code_url and in 00-meta/data-sources.md; leave source_last_verified BLANK until a human verifies.
- Populate qualitative content from general knowledge; do NOT fabricate specific tax rates or program caps — use "TBD — verify" + needs-verification tag if unsure.
- Set status: draft when substantive; never self-promote to reviewed/authoritative.
- SUCCESS CRITERIA: an analyst new to the state understands who regulates land use, under what statutes, the tax/closing landscape, and which counties to drill into.
-->
