---
title: "Oro Valley, Arizona"
type: jurisdiction
tags: [juris/az/oro-valley, needs-verification]
created: "2026-05-24"
updated: "2026-06-07"
status: draft
ai_summary: Affluent master-planned community north of Tucson in Pima County; high-income demographics, conservative growth posture, and primarily residential and professional-office CRE character.
level: city
state: AZ
parent_jurisdiction: "Pima County, Arizona"
population: "TBD"
zoning_authority: "Town of Oro Valley Planning and Zoning Division"
code_url: "https://www.orovalleyaz.gov/town/departments/planning-and-zoning"
gis_url: "TBD"
source_url: "https://www.orovalleyaz.gov/town/departments/planning-and-zoning"
source_last_verified: ""
related:
  - "Pima County, Arizona"
  - "Arizona State Overview"
  - "Entitlement Play"
  - "Zone Change (Rezoning)"
  - "Highest and Best Use Analysis"
children: []
---

# Oro Valley, Arizona

## Overview

Oro Valley is an incorporated town immediately north of Tucson in Pima County, widely regarded as one of the most affluent and desirable communities in Southern Arizona. The town was developed primarily through master-planned communities and has a well-established character: high-quality residential neighborhoods, premium retail and restaurant corridors (particularly around Oracle Road and the Oro Valley Marketplace), and a concentration of medical, healthcare, and professional office uses.

The town's growth posture is notably conservative compared to Phoenix-area peer cities. It has been largely built out in terms of major undeveloped land, and its planning culture emphasizes preserving community character, scenic desert views, and high design standards. This posture affects CRE: speculative industrial or high-density residential are not natural fits; professional office, medical office, and high-quality retail and restaurant are more aligned with local entitlement sentiment.

Bioscience and healthcare are significant economic drivers, with facilities linked to the broader Tucson bioscience corridor. The town's proximity to the Tucson Motorsports Park (formerly Rillito Park area) and recreational tourism assets adds a niche hospitality dimension.

## Primary Sources

Primary-source documents for the Town of Oro Valley are held in the `Pima County development standards/` library:

- **Zoning code:** Oro Valley Zoning Code (OVZC) — General Code — https://orovalley.town.codes/ZC
- **General plan:** Your Voice, Our Future General Plan — local PDF `OroValley_GeneralPlan_YourVoiceOurFuture.pdf`
- **Subdivision street standards:** local PDF `OroValley_SubdivisionStreetStandardsPolicyManual.pdf`
- **Drainage:** local PDF `OroValley_DrainageCriteriaManual.pdf`

Base zoning districts and dimensional standards were extracted from the OVZC (§ 23.1 districts; Table 23-2A residential, Table 23-2B nonresidential) into `40-data/zones/az-oro-valley.json` and feed the data-linked Zone Standards table below. All values are AI-`extracted` and `needs-verification` until human-confirmed.

## Governing Body

Oro Valley is a town governed by a Mayor and Town Council. The Planning and Zoning Commission reviews land-use applications and makes recommendations; the Town Council makes final decisions on rezonings and general plan amendments. The town has historically maintained tight design and compatibility standards that influence entitlement outcomes.

## Planning Department

**Town of Oro Valley — Planning and Zoning Division**
The Planning and Zoning Division manages current and long-range planning, zoning administration, and development review.

Website: https://www.orovalleyaz.gov/town/departments/planning-and-zoning

## General Plan / Comprehensive Plan

Oro Valley maintains an adopted General Plan that guides land use, growth management, and community character. The plan's horizon year is TBD — verify against the current Oro Valley General Plan document. Given the largely built-out character of the town, the General Plan is primarily a framework for infill, redevelopment, and compatibility standards rather than greenfield expansion.

_(General Plan horizon year: needs-verification)_

## Zoning Code Citation

Oro Valley's zoning regulations are codified in the **Oro Valley Zoning Code** within the Oro Valley Town Code. The exact title/chapter citation is TBD — verify against the current town code. Oro Valley's code reflects its master-planned origins and includes design standards oriented toward community character preservation.

_(Exact code citation: needs-verification)_

## Zoning Map URL

TBD — verify via the Town of Oro Valley GIS or Planning portal.

## Zone Districts Index

Overview-only note — zone roster and detailed standards deferred to a later buildout pass.

## Overlay Districts

TBD — deferred to later buildout pass.

## Subdivision Standards

TBD — governed by the Oro Valley Subdivision and Development Standards and Arizona Revised Statutes; verify via Planning Division.

## Impact Fees & Exactions

TBD — verify current development impact fee schedule with the Town of Oro Valley. _(needs-verification)_

## Permit Timelines

TBD — verify current entitlement and building-permit timeline estimates with the Planning Division.

## Notable Recent Code Changes

TBD — verify any recent zoning or general plan amendments with the Planning Division.

## Sources

- Town of Oro Valley Planning and Zoning: https://www.orovalleyaz.gov/town/departments/planning-and-zoning
- Oro Valley Town Code / Zoning Code: TBD — verify URL
- Oro Valley GIS / Zoning Map: TBD — verify URL
- Oro Valley General Plan: TBD — verify URL

<!-- BEGIN:zones-table (generated by 40-data/_tools/sync.py — do not edit) -->

## Zone Standards (data-linked)

*Generated from `40-data/zones/az-oro-valley.json` via `sync.py`. `—` = not yet extracted. Full data: `40-data/zoning_standards.csv`. Do not edit between the markers.*

| Zone | Name | Category | Min Lot (sf) | Density (du/ac) | FAR | Height (ft) | Front | Side | Rear | Parking | Conf. |
|------|------|----------|--------------|-----------------|-----|-------------|-------|------|------|---------|-------|
| C-1 | C-1 Commercial District | commercial | — | — | 0.3 | 25 | 20 | — | — | — | extracted |
| C-2 | C-2 Commercial District | commercial | — | — | 0.4 | 30 | 20 | — | — | — | extracted |
| C-N | C-N Neighborhood Commercial District | commercial | 0 | — | 0.25 | 25 | 20 | — | — | — | extracted |
| PAD | PAD Planned Area Development | planned | — | — | — | — | — | — | — | — | tbd |
| POS | POS Parks and Open Space District | open-space | — | — | 0.15 | — | — | — | — | — | extracted |
| PRD | PRD Planned Residential District | planned | — | — | — | — | — | — | — | — | tbd |
| PS | PS Private Schools District | special | — | — | — | — | — | — | — | — | extracted |
| R-4 | R-4 Townhouse Residential District | residential | — | — | — | 25 | — | — | — | — | extracted |
| R-4R | R-4R Resort District | residential | — | — | — | 34 | — | — | — | — | extracted |
| R-6 | R-6 Multifamily Residential District | residential | — | — | — | 25 | 30 | 20 | 20 | — | extracted |
| R-S | R-S Residential Service District | residential | — | — | — | 25 | — | — | — | — | extracted |
| R1-10 | R1-10 Single-Family Residential District | residential | 10000 | — | — | 25 | 25 | 10 | 25 | — | extracted |
| R1-144 | R1-144 Single-Family Residential District | residential | 144000 | — | — | 18 | 50 | 20 | 50 | — | extracted |
| R1-20 | R1-20 Single-Family Residential District | residential | 20000 | — | — | 18 | 30 | 15 | 30 | — | extracted |
| R1-300 | R1-300 Single-Family Residential District | residential | 300000 | — | — | 34 | 50 | 20 | 50 | — | extracted |
| R1-36 | R1-36 Single-Family Residential District | residential | 36000 | — | — | 18 | 30 | 15 | 40 | — | extracted |
| R1-43 | R1-43 Single-Family Residential District | residential | 43560 | — | — | 18 | 30 | 20 | 40 | — | extracted |
| R1-7 | R1-7 Single-Family Residential District | residential | 7000 | — | — | 25 | 20 | 7.5 | 20 | — | extracted |
| R1-72 | R1-72 Single-Family Residential District | residential | 72000 | — | — | 22 | 50 | 35 | 50 | — | extracted |
| SDH-6 | SDH-6 Site Delivered Housing District | residential | 6000 | — | — | 18 | 20 | 15 | 25 | — | extracted |
| T-P | T-P Technological Park District | industrial | — | — | 0.5 | 36 | 20 | — | — | — | extracted |

<!-- END:zones-table -->
