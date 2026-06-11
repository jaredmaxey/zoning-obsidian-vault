---
title: "Maricopa (City), Arizona"
type: jurisdiction
tags: [juris/az/maricopa-city, needs-verification]
created: "2026-05-24"
updated: "2026-06-08"
status: draft
ai_summary: Pinal County bedroom community south of the Phoenix metro; one of the fastest-growing US cities in the 2000s, with primarily residential CRE character and limited commercial base relative to population.
level: city
state: AZ
parent_jurisdiction: "Pinal County, Arizona"
population: "TBD"
zoning_authority: "City of Maricopa Planning Division"
code_url: "https://www.maricopa-az.gov/planning"
gis_url: "TBD"
source_url: "https://www.maricopa-az.gov/planning"
source_last_verified: ""
related:
  - "Pinal County, Arizona"
  - "Arizona State Overview"
  - "Entitlement Play"
  - "Zone Change (Rezoning)"
  - "General Plan Amendment (GPA)"
  - "Subdivision Approval"
children: []
---

# Maricopa (City), Arizona

> **Note:** This note covers the **City of Maricopa** in Pinal County — not Maricopa County. The title uses "(City)" to disambiguate the two. The city is distinct from and governed independently of Maricopa County.

## Overview

The City of Maricopa is a Pinal County municipality located south of the Phoenix metropolitan area, accessible via State Route 347 and with partial access to SR 347/I-10. The city experienced explosive residential growth in the mid-2000s — briefly ranking among the fastest-growing cities in the United States — driven by affordable large-lot single-family homes attracting commuters to the Phoenix metro. The 2008 housing crisis hit the city hard, but it has recovered and continued steady growth.

Maricopa is predominantly a residential bedroom community: its residents largely commute to jobs in the Phoenix metro or Casa Grande, and its commercial base has historically lagged its population size. This imbalance is a known planning challenge, and the city has actively sought to attract retail, healthcare, and employment uses to reduce commute dependency.

For CRE, the primary plays are residential development and retail/service commercial serving a growing but underserved population. Healthcare and grocery-anchored retail are high-demand uses. Industrial and office are limited by the city's commuter character and access constraints, though SR 347 and ongoing road improvements may expand opportunity over time.

## Primary Sources

Primary-source documents for the City of Maricopa (Pinal County) are held in the `Pinal County development standards/` library:

- **Zoning code:** Maricopa City Code, Title 18 (Zoning) — General Code — https://maricopa.municipal.codes/MCC/18
- **General plan:** City of Maricopa General Plan (Planning Maricopa) — https://www.maricopa-az.gov/departments/development-services/planning-maricopa-general-plan
- **Design standards:** City of Maricopa Design Standards Manual (2020) — local PDF `MaricopaCity_DesignStandardsManual_2020.pdf`

Base zoning districts and dimensional standards were extracted from Title 18 (Ch. 18.30–18.55 districts + development-standards tables) into `40-data/zones/az-maricopa-city.json` and feed the data-linked Zone Standards table below — 22 base districts. All values are AI-`extracted` and `needs-verification` until human-confirmed. *(Note: this is the **City of Maricopa in Pinal County**, tracked as `az-maricopa-city` — distinct from `az-maricopa-county`.)*

## Governing Body

The City of Maricopa operates under a Mayor-Council government. The Planning and Zoning Commission reviews applications and makes recommendations; the City Council makes final decisions on rezonings and general plan amendments.

## Planning Department

**City of Maricopa — Planning Division**
The Planning Division manages current and long-range planning, zoning administration, and development review.

Website: https://www.maricopa-az.gov/planning

## General Plan / Comprehensive Plan

Maricopa maintains a General Plan guiding long-range land use and growth. The plan's horizon year is TBD — verify against the current City of Maricopa General Plan. A key policy thrust of the plan is diversifying the employment and commercial base relative to the large residential population.

_(General Plan horizon year: needs-verification)_

## Zoning Code Citation

Maricopa's zoning regulations are codified in the **City of Maricopa Zoning Ordinance** within the City of Maricopa Code. The exact title/chapter citation is TBD — verify against the current city code.

_(Exact code citation: needs-verification)_

## Zoning Map URL

TBD — verify via the City of Maricopa GIS or Planning portal.

## Zone Districts Index

Overview-only note — zone roster and detailed standards deferred to a later buildout pass.

## Overlay Districts

TBD — deferred to later buildout pass.

## Subdivision Standards

TBD — governed by the City of Maricopa Subdivision Ordinance and Arizona Revised Statutes; verify via Planning Division. Large-lot residential subdivisions are the dominant development type historically.

## Impact Fees & Exactions

TBD — verify current development impact fee schedule with the City of Maricopa. _(needs-verification)_

## Permit Timelines

TBD — verify current entitlement and building-permit timeline estimates with the Planning Division.

## Notable Recent Code Changes

TBD — verify any recent zoning or general plan amendments focused on commercial/employment land diversification.

## Sources

- City of Maricopa Planning: https://www.maricopa-az.gov/planning
- Maricopa City Code / Zoning Ordinance: TBD — verify URL
- Maricopa GIS / Zoning Map: TBD — verify URL
- Maricopa General Plan: TBD — verify URL

<!-- BEGIN:zones-table (generated by 40-data/_tools/sync.py — do not edit) -->

## Zone Standards (data-linked)

*Generated from `40-data/zones/az-maricopa-city.json` via `sync.py`. `—` = not yet extracted. Full data: `40-data/zoning_standards.csv`. Do not edit between the markers.*

| Zone | Name | Category | Min Lot (sf) | Density (du/ac) | FAR | Height (ft) | Front | Side | Rear | Parking | Conf. |
|------|------|----------|--------------|-----------------|-----|-------------|-------|------|------|---------|-------|
| GC | General Commercial | commercial | 10000 | — | — | 40 | 20 | 0 | 30 | — | extracted |
| GI | General Industrial | industrial | 10000 | — | — | 40 | 35 | 0 | 20 | — | extracted |
| GO | General Office | commercial | 10000 | — | — | 40 | 20 | 0 | 30 | — | extracted |
| GR | General Rural | agricultural | 54450 | — | — | 30 | 40 | 20 | 40 | — | extracted |
| IP | Industrial Park | industrial | 20000 | — | — | 40 | 25 | 0 | 15 | — | extracted |
| LI | Light Industrial | industrial | 10000 | — | — | 40 | 25 | 0 | 15 | — | extracted |
| MU-G | General Mixed Use | mixed-use | 7000 | 30 | 1.2 | 60 | 10 | 0 | 20 | — | extracted |
| MU-N | Neighborhood Mixed Use | mixed-use | 7000 | 16 | 0.8 | 30 | 10 | 0 | 20 | — | extracted |
| NC | Neighborhood Commercial | commercial | 5000 | 20 | — | 40 | 10 | 0 | 20 | — | extracted |
| OS-C | Conservation Open Space | open-space | — | — | — | — | — | — | — | — | extracted |
| OS-POS | Privately Owned Open Space | open-space | — | — | — | 35 | 25 | 25 | 25 | — | extracted |
| OS-PR | Parks and Recreation Open Space | open-space | — | — | — | 45 | 20 | 20 | 20 | — | extracted |
| PI | Public-Institutional | special | — | — | — | 45 | 20 | 15 | 20 | — | extracted |
| RA | Rural Agricultural | agricultural | 130680 | — | — | 35 | 50 | 30 | 50 | — | extracted |
| RH | High Density Residential | residential | 7000 | 24 | — | 42 | 20 | 5 | 20 | — | extracted |
| RM | Multiple Unit Residential | residential | 7000 | 12 | — | 36 | 20 | 5 | 20 | — | extracted |
| RMHP | Residential Manufactured Home Park | residential | 2500 | 12 | — | 15 | 20 | 5 | 10 | — | extracted |
| RS-1 | Low Density Residential | residential | 12000 | — | — | 30 | 25 | 10 | 25 | — | extracted |
| RS-3 | Medium Density Residential | residential | 9000 | — | — | 30 | 20 | 7.5 | 20 | — | extracted |
| RS-4 | Medium Density Residential | residential | 7000 | — | — | 30 | 20 | 5 | 20 | — | extracted |
| RS-5 | Medium Density Residential | residential | 5000 | — | — | 30 | 15 | 5 | 15 | — | extracted |
| SC | Shopping Center | commercial | 20000 | — | — | 40 | 20 | 0 | 40 | — | extracted |

<!-- END:zones-table -->
