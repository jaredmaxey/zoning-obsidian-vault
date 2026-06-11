---
title: Density Metrics
aliases: ["Density Metrics"]
type: reference
tags: [reference, standard/far]
created: 2026-05-24
updated: 2026-05-25
status: draft
ai_summary: Definitions and formulas for the density and intensity metrics used in zoning and feasibility — FAR, DUA, lot coverage, open-space ratio, and how they interrelate.
---

# Density Metrics

The measures zoning codes use to cap how much can be built on a site, and how they translate into developable program. These are standard, jurisdiction-neutral definitions; the *limits* themselves are set per zone (see the zone notes). Formulas are given in plain text and LaTeX.

## Purpose

Density/intensity metrics convert a parcel's area into a permitted building program. The binding constraint varies by use: residential is usually capped by **DUA** (and sometimes height/setbacks), while commercial/mixed-use is usually capped by **FAR** (and lot coverage/height). Feasibility work backs program out of whichever limit binds first.

## Table

| Metric | Definition | Formula | Notes |
|--------|------------|---------|-------|
| Floor Area Ratio (FAR) | Ratio of total gross building floor area to lot area. | `FAR = Gross Floor Area ÷ Lot Area`  ·  $$FAR = \frac{GFA}{A_{lot}}$$ | Dimensionless. FAR 2.0 on a 20,000 SF lot ⇒ 40,000 SF of building. What counts as "floor area" (e.g., exclusion of parking/mechanical) is defined per code. |
| Buildable Area | Maximum gross floor area permitted by FAR. | `Buildable GFA = FAR × Lot Area`  ·  $$GFA = FAR \times A_{lot}$$ | The starting point for a commercial/mixed-use program before efficiency losses. |
| Dwelling Units per Acre (DUA) | Permitted residential units per acre of land. | `Units = DUA × Acres`  ·  $$U = DUA \times A_{ac}$$ | Distinguish **gross** DUA (over the whole site incl. roads/open space) from **net** DUA (developable land only). |
| Lot Coverage | Share of the lot that may be covered by building footprint (sometimes all impervious structures). | `Coverage % = Building Footprint ÷ Lot Area`  ·  $$Cov = \frac{A_{footprint}}{A_{lot}}$$ | Caps footprint, not total floor area; interacts with height to determine achievable FAR. |
| Open Space Ratio (OSR) | Required open/landscaped area as a share of lot (or per unit). | `OSR = Open Space Area ÷ Lot Area` | May be expressed as a % of lot or as SF per dwelling unit. |
| Density (gross vs. net) | Units or FAR measured over gross site vs. net developable land. | `Net density = Units ÷ Net Developable Acres` | Net excludes rights-of-way, easements, undevelopable slopes, and dedicated open space — net density is always ≥ gross. |
| Floor Plate Efficiency | Ratio of rentable/usable area to gross floor area. | `Efficiency = Rentable Area ÷ Gross Floor Area` | Converts FAR-driven GFA into leasable SF; varies by building type (high-rise less efficient than big-box). |

## How to Use

1. Identify the binding limit for the intended use (DUA for residential; FAR/coverage/height for commercial).
2. Apply it to **net developable** acreage, not gross, unless the code specifies gross.
3. For mixed-use, allocate FAR across components, then convert each to a program (units via avg unit size; leasable SF via efficiency).
4. Cross-check against height and setback envelopes — the *physically* achievable building is the lesser of the FAR/DUA cap and what the height/setback/coverage envelope allows.

## Worked example (illustrative)

A 1.0-acre (43,560 SF) commercial lot with FAR 1.5 and 50% max lot coverage:
- Max GFA = 1.5 × 43,560 = **65,340 SF**.
- Max footprint = 0.50 × 43,560 = 21,780 SF ⇒ to reach 65,340 SF GFA needs ≈ **3 stories** (65,340 ÷ 21,780).
- At 85% efficiency ⇒ ≈ **55,500 leasable SF**. *(Figures illustrative; confirm code definitions and exclusions.)*

## Source / Methodology

Standard land-planning definitions; the numeric *limits* per zone live in the zone notes (currently `TBD — verify`). See [[Glossary]], [[Unit Conversions]], [[Yield on Cost]], and [[Highest and Best Use Analysis]].
