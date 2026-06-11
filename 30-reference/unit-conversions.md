---
title: Unit Conversions
aliases: ["Unit Conversions"]
type: reference
tags: [reference]
created: 2026-05-24
updated: 2026-05-25
status: draft
ai_summary: Quick-reference conversions for CRE and zoning math — area (acres↔SF), density (DUA↔units), intensity (FAR↔buildable area), and common rate conversions.
---

# Unit Conversions

Standard conversions used in site, zoning, and underwriting math. Constants are exact unless noted.

## Area

| From | To | Factor / Formula | Notes |
|------|----|------------------|-------|
| Acre | Square feet | × 43,560 | Exact. 1 acre = 43,560 SF. |
| Square feet | Acres | ÷ 43,560 | |
| Square mile | Acres | × 640 | 1 section = 1 sq mi = 640 ac. |
| Acre | Hectares | × 0.404686 | |
| Square meter | Square feet | × 10.7639 | |

## Intensity & buildable area

| From | To | Factor / Formula | Notes |
|------|----|------------------|-------|
| Lot area + FAR | Max gross floor area | `GFA = FAR × Lot Area` | See [[Density Metrics]]. |
| Gross floor area | Leasable area | `× efficiency (≈0.80–0.92)` | Efficiency varies by building type. |
| Max GFA + footprint | Stories needed | `Stories = GFA ÷ Max Footprint` | Footprint = coverage% × lot area. |

## Density & units

| From | To | Factor / Formula | Notes |
|------|----|------------------|-------|
| Acres + DUA | Unit count | `Units = DUA × Acres` | Use net developable acres unless code says gross. |
| Unit count + acres | Achieved DUA | `DUA = Units ÷ Acres` | |
| Units + avg unit size | Residential GFA | `GFA ≈ Units × Avg Unit SF ÷ efficiency` | Add circulation/amenity load via efficiency. |

## Parking & rates

| From | To | Factor / Formula | Notes |
|------|----|------------------|-------|
| Ratio "per 1,000 SF" | Required stalls | `Stalls = (GLA ÷ 1,000) × ratio` | Commercial parking minimums (see [[Parking Ratios by Use]]). |
| Ratio "per unit" | Required stalls | `Stalls = Units × ratio` | Residential parking minimums. |
| Stall count | Surface parking area | `× ≈300–350 SF/stall` | Includes drive aisles; structured parking ≈ 325–400 SF/stall. |
| Annual rent ($/SF/yr) | Monthly rent | `÷ 12` | NNN vs. gross must match the comparison. |
| % (e.g., cap rate) | Decimal | `÷ 100` | 6.5% = 0.065. |
| Basis points | Percent | `÷ 100` | 25 bps = 0.25%. |

## How to Use

Chain conversions left-to-right: e.g., raw land → net acres → (× DUA) → units → (× avg SF ÷ efficiency) → residential GFA → program. Always confirm whether a code limit applies to **gross** or **net** site area, and whether FAR floor-area definitions exclude parking/mechanical.

## Source / Methodology

Standard conversion constants and CRE planning math. Related: [[Density Metrics]], [[Parking Ratios by Use]], [[Replacement Cost]], [[Glossary]].
