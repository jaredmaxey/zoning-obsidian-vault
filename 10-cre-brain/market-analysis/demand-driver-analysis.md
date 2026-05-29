---
title: "Demand Driver Analysis"
type: framework
tags: [cre/market-analysis]
created: "2026-05-24"
updated: "2026-05-24"
status: draft
ai_summary: Framework for identifying, quantifying, and stress-testing the economic forces that generate occupancy demand for a specific property type in a defined submarket.
inputs_required:
  - Defined submarket boundary (from Submarket Definition and Selection)
  - Employment data by sector (BLS Quarterly Census of Employment and Wages, QCEW)
  - Population and household growth projections (Census/ACS, ESRI, local MPO)
  - Historical absorption data by property type (CoStar, CBRE, JLL market reports)
  - Anchor tenant or demand generator locations (ESRI, CoStar)
  - GDP and income growth forecasts (BLS, Moody's Analytics, Woods & Poole)
  - Industry concentration and employer headcount (BLS, ESRI Business Analyst)
outputs:
  - Demand driver narrative identifying primary and secondary drivers
  - Quantified demand forecast (SF or units per year) with low/base/high scenarios
  - Demand-driver risk assessment (sensitivity to key economic assumptions)
  - Absorption projection table for use in supply-demand modeling
related:
  - "Submarket Definition and Selection"
  - "Supply Pipeline Analysis"
  - "Absorption Rate"
  - "Demographic Analysis"
  - "Employment and Jobs Analysis"
  - "Trade Area Analysis (Retail)"
  - "Four-Quadrant Model"
  - "Absorption Modeling"
---

# Demand Driver Analysis

## Purpose

Demand driver analysis identifies and quantifies the underlying economic forces that generate occupancy demand for a specific property type in a defined market or submarket. While vacancy and absorption statistics describe what has happened, demand driver analysis explains why it happened and projects what is likely to happen next. For office space, the primary driver is typically professional and business services employment growth. For industrial space, it is e-commerce penetration, trade flows, and manufacturing activity. For multifamily, it is household formation, in-migration, and the rent-vs.-own affordability ratio. For retail, it is population density, disposable income, and consumer spending patterns. This framework forces the analyst to name the drivers explicitly and link them to measurable, forecastable variables — rather than extrapolating historical absorption trends without understanding what caused them.

Analysts reach for this framework when building a market study for a new development, when underwriting an acquisition with above-market assumptions, or when a sponsor's rent growth projection requires justification. It pairs tightly with [[Supply Pipeline Analysis]] (the supply side of the same supply-demand balance) and [[Employment and Jobs Analysis]] (which quantifies one of the most frequently used driver variables). The output feeds directly into [[Absorption Modeling]] and serves as the demand-side input to a supply-demand gap calculation.

## Inputs Required

- **Defined submarket boundary:** Established via [[Submarket Definition and Selection]]; all demand metrics must be calibrated to the same geographic area.
- **Employment data by sector:** BLS Quarterly Census of Employment and Wages (QCEW) at the county or MSA level, segmented by NAICS supersector. For office, focus on professional and business services, financial activities, and information sectors. For industrial, focus on transportation/warehousing, manufacturing, and wholesale trade.
- **Population and household growth projections:** Census/ACS current estimates; ESRI Tapestry or Business Analyst for submarket-level projections; local Metropolitan Planning Organization (MPO) long-range projections for 5–20 year horizons.
- **Historical absorption data:** CoStar gross and net absorption by property type and submarket, ideally 10+ years to capture a full cycle.
- **Anchor tenant or demand generator locations:** Hospital campuses, university campuses, major corporate HQ, port and intermodal facilities, or major retail anchors as applicable.
- **GDP and income growth forecasts:** BLS, Moody's Analytics, or Woods & Poole at the MSA level for macro context.
- **Industry concentration ratios:** Location quotient data (BLS or ESRI) to identify whether the local economy is over- or under-represented in the sectors that drive demand for the subject property type.

## Method

1. **Identify the property-type demand equation.** Start by naming the 2–3 primary demand drivers for the subject's property type. Use established rule-of-thumb ratios as a starting framework (e.g., office space per employee in the knowledge economy is commonly cited in the 150–225 SF/employee range, varying by market and vintage; current as of 2026-05-24) but verify against local historical data before projecting.

2. **Pull historical employment or population growth.** Source BLS QCEW at the relevant geography (county or MSA) for the past 10 years. Calculate compound annual growth rates (CAGR) over the full period and over the most recent 3–5 years to identify trend direction and acceleration/deceleration.

3. **Source independent projections.** Gather 5-year forward projections from at least two independent sources (MPO long-range transportation plan, ESRI Business Analyst, Moody's Analytics, or a third-party economist report). Note the range across sources as an indicator of forecast uncertainty.

4. **Calculate implied demand.** Multiply the employment or household growth forecast by the applicable space-per-unit ratio to produce annual gross demand in SF (or units). For example: projected 500-employee gain in professional services × 180 SF/employee = 90,000 SF annual gross demand (illustrative).

5. **Adjust for demand elasticity and market-specific factors.** Consider whether the market is emerging (demand elasticity is high — new supply attracts new tenants) or mature (demand is largely replacement-driven). Adjust for remote work penetration, hybrid schedules, or other structural shifts affecting space-per-employee ratios where relevant.

6. **Build low/base/high scenarios.** Use the low-end employment/population growth forecast for the stress case, the consensus forecast for the base case, and the high-end forecast for the upside. Each scenario should produce a corresponding annual absorption projection in SF or units.

7. **Validate against historical absorption.** Compare the model's base-case demand projection to actual historical net absorption from CoStar over the past 5–10 years. If the model's output is materially higher than historical absorption, identify whether that reflects a supply shortage (demand was higher but couldn't be filled) or an overly optimistic assumption. Reconcile the discrepancy in writing.

8. **Document risk factors.** Identify the 2–3 assumptions the demand forecast is most sensitive to, and describe the scenarios under which demand would fall materially below the base case (employer consolidation, remote work acceleration, trade policy change for industrial, etc.).

## Outputs

The primary output is a **demand driver narrative** — a 2–3 page summary identifying primary and secondary demand drivers, supporting data, and the analyst's qualitative assessment of demand quality and durability. This is accompanied by a **quantified demand forecast table** showing annual absorption projections in SF or units under low/base/high scenarios over a 3–5 year horizon. A **demand-driver risk assessment** (one page) identifies the top 2–3 sensitivities. These outputs feed directly into the supply-demand gap calculation within [[Absorption Modeling]].

## Example Walkthrough

The following numbers are illustrative and hypothetical, labeled as such throughout.

Suppose the subject is a hypothetical 300-unit Class A multifamily development in a growing Sun Belt metro. The analyst identifies three demand drivers: (1) net household formation from in-migration, (2) the rent-vs.-own affordability ratio (renters priced out of for-sale housing remain renters longer), and (3) job growth in professional services and technology sectors. Pulling hypothetical BLS QCEW data, the analyst finds the MSA added approximately 8,000–12,000 jobs annually over the prior five years in the target sectors, with MPO projections showing a similar pace over the next five years. Using a hypothetical renter-household-per-job conversion ratio of 0.25 (varies by market and vintage; current as of 2026-05-24), the model implies roughly 2,000–3,000 new renter households per year in the MSA. Against a hypothetical competitive submarket inventory of 8,000 units, this implies an annual demand rate of roughly 25–37% of inventory — consistent with the historical net absorption data the analyst pulls from CoStar for the submarket. The base-case scenario implies the subject's 300 units can be absorbed within 9–14 months post-delivery, supporting a 12-month lease-up assumption in the pro forma.

## Limitations

Demand driver analysis is forward-looking, and all forecasts carry error. Employment forecasts are notoriously sensitive to macroeconomic shocks, and space-per-unit ratios are structurally shifting for office (remote and hybrid work) and potentially for retail (e-commerce displacement). The framework does not capture cyclical demand volatility well — most of the inputs are trend-based, not cyclical. For markets with thin historical data or rapidly evolving economic bases, the historical-absorption validation step may give false confidence. Analysts should always pair this framework with a conservative sensitivity analysis and should never rely on a single demand projection as a basis for underwriting.

## Related Frameworks

[[Submarket Definition and Selection]] establishes the geographic boundaries that contain this analysis. [[Supply Pipeline Analysis]] provides the supply side of the equation. [[Employment and Jobs Analysis]] supports the employment growth input in detail. [[Demographic Analysis]] provides the population and household formation inputs for residential demand. [[Absorption Modeling]] applies the demand and supply outputs to project lease-up and stabilization timing. The [[Four-Quadrant Model]] provides a theoretical framework for understanding how demand shocks propagate through rent levels and new supply decisions.
