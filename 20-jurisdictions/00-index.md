---
title: Jurisdictions Index
aliases: ["Jurisdictions Index"]
type: index
tags: [juris, index]
created: 2026-05-24
updated: 2026-05-24
status: draft
covers: The zoning and development-standards half of the vault, organized by state → county → city → zone, plus the canonical pattern for adding new states.
ai_summary: Hub note for the jurisdiction/zoning knowledge base, linking to each state and the state-addition pattern.
---

# Jurisdictions Index

The zoning and development-standards knowledge base. Structure is **pattern-driven** so adding a new state is mechanical: see `_jurisdiction-pattern.md` (the canonical recipe, written in Prompt 4).

The hierarchy is **state → county → city → (zones, overlays, standards, processes)**, plus state statutes and special districts.

## Canonical pattern

- **`_jurisdiction-pattern.md`** — the recipe for scaffolding any state. Give a future session this file plus a state name and it can build the state. _(Written in Prompt 4.)_

## States

### Arizona ✅ _(Prompt 4)_

[[Arizona State Overview]] — enabling statutes, agencies, water, programs.

> **Maricopa County primary-source migration (2026-06-06).** The `Maricopa County development standards/` library (official PDFs + live-code links + `INDEX.html`) is now the source of truth for Maricopa jurisdictions, and dimensional standards are mirrored into the machine-readable [[Structured Data Layer]] (`40-data/`). Each jurisdiction overview carries an auto-generated **Zone Standards (data-linked)** table; the cross-jurisdiction projection is `40-data/zoning_standards.csv`. Base-zone extraction is **complete for all 26 Maricopa jurisdictions** (534 zones, 533 from official sources) — Tucson excepted (Pima County). Values are AI-`extracted` from official sources and remain `needs-verification` until a human confirms them.

- **State statutes:** [[A.R.S. Title 9 — Cities and Towns (Municipal Zoning)]], [[A.R.S. Title 11 — Counties (County Zoning)]], [[A.R.S. Title 32 — Professions and Occupations (Real Estate Licensing)]], [[A.R.S. Title 33 — Property]], [[A.R.S. Title 45 — Waters]], [[Assured Water Supply Program (Arizona)]]
- **Counties (7):** [[Maricopa County, Arizona]], [[Pima County, Arizona]], [[Pinal County, Arizona]], [[Yavapai County, Arizona]], [[Coconino County, Arizona]], [[Mohave County, Arizona]], [[Yuma County, Arizona]]
- **Cities — full buildout** (overview + enumerated zones + overlays + standards + processes): [[Phoenix, Arizona]] (22), [[Scottsdale, Arizona]] (35), [[Mesa, Arizona]] (34), [[Tempe, Arizona]] (31), [[Tucson, Arizona]] (28), [[Gilbert, Arizona]] (28), [[Chandler, Arizona]] (18). **196 zone notes total.** Zone codes/names are web-sourced (draft); dimensional standards are `TBD` pending verification.
- **Cities — overview only:** [[Glendale, Arizona]], [[Peoria, Arizona]], [[Surprise, Arizona]], [[Goodyear, Arizona]], [[Buckeye, Arizona]], [[Queen Creek, Arizona]], [[Avondale, Arizona]], [[Oro Valley, Arizona]], [[Marana, Arizona]], [[Sahuarita, Arizona]], [[Casa Grande, Arizona]], [[Maricopa (City), Arizona]], [[Prescott, Arizona]], [[Prescott Valley, Arizona]], [[Flagstaff, Arizona]], [[Sedona, Arizona]], [[Lake Havasu City, Arizona]], [[Yuma, Arizona]]
- **Maricopa cities — new scaffolds** (added 2026-06-06 from the primary-source set; overview + Primary Sources, zones queued): [[City of El Mirage]], [[City of Tolleson]], [[City of Litchfield Park]], [[Town of Youngtown]], [[Town of Wickenburg]], [[Town of Gila Bend]], [[Town of Fountain Hills]], [[Town of Cave Creek]], [[Town of Carefree]], [[Town of Paradise Valley]], [[Town of Guadalupe]], [[City of Apache Junction]]
- **Special districts:** [[Arizona Tribal Lands Overview]], [[Arizona Military Installations and Compatibility]], [[Community Facilities Districts (Arizona)]], [[Domestic Water Improvement Districts (Arizona)]]
- **Note:** [[Tucson, Arizona]] is in **Pima County** — outside the Maricopa primary-source set; its standards retain their prior sourcing.

### Nevada ⬜ _(stub)_

[[Nevada State Overview]] — stub only (NRS Chapter 278 enabling statutes). Full buildout follows the Arizona pattern (`_jurisdiction-pattern.md`) in a later prompt.

## Related indexes

- [[CRE Brain Index]] — the CRE development knowledge half.
- [[Reference Index]] — cross-jurisdictional lookup tables (parking ratios, density metrics).
