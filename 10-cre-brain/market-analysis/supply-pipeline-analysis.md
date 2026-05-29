---
title: "Supply Pipeline Analysis"
type: framework
tags: [cre/market-analysis]
created: "2026-05-24"
updated: "2026-05-24"
status: draft
ai_summary: Framework for inventorying, phasing, and risk-adjusting all competitive new supply under construction or in permitting to forecast near-term market conditions.
inputs_required:
  - Defined submarket boundary (from Submarket Definition and Selection)
  - Properties under construction (CoStar, local building permits, MPO data)
  - Properties in planning or permitting (CoStar, county planning department records)
  - Delivered/absorbed supply for prior 3–5 years (CoStar)
  - Current submarket vacancy rate and net absorption trend (CoStar)
  - Entitlement and construction lead times by property type
  - Known anchor tenant pre-leasing activity (broker interviews, CoStar)
outputs:
  - Supply pipeline table with project name, size, delivery date, pre-leasing status, and probability weight
  - Risk-adjusted pipeline total (SF or units) by year over 3-year horizon
  - Supply-demand gap analysis (when combined with Demand Driver Analysis output)
  - Narrative commentary on pipeline risk and implications for submarket vacancy
related:
  - "Submarket Definition and Selection"
  - "Demand Driver Analysis"
  - "Absorption Rate"
  - "Absorption Modeling"
  - "Ground-Up Development"
  - "Development Feasibility Test"
  - "Real Estate Cycle and Phases"
---

# Supply Pipeline Analysis

## Purpose

Supply pipeline analysis inventories all competitive space under construction or in the planning/permitting stage within a defined submarket, assigns probability-weighted delivery timelines, and projects the pace at which new supply will hit the market over the next 3–5 years. It is the supply-side counterpart to [[Demand Driver Analysis]], and together the two form the core of a supply-demand gap calculation. Understanding the pipeline is essential because announced projects frequently slip, stall, or are cancelled; an unadjusted list of planned projects will consistently overstate the near-term supply threat and produce overly conservative absorption forecasts.

Analysts use this framework in acquisition underwriting to judge whether a submarket is at risk of oversupply during the projected hold period, in development feasibility to assess whether a new project can be absorbed without competing deliveries depressing rents, and in portfolio monitoring to anticipate lease-up headwinds at existing assets. The framework is closely linked to [[Absorption Modeling]] and informs the [[Real Estate Cycle and Phases]] positioning of the submarket.

## Inputs Required

- **Defined submarket boundary:** From [[Submarket Definition and Selection]]; only projects within or adjacent to (and clearly competitive with) the subject's submarket are included.
- **Under-construction inventory:** CoStar's "under construction" filter by property type and submarket; cross-reference with local building permit data from the county building department for projects not yet in CoStar.
- **Planned/proposed inventory:** CoStar's "proposed" filter; city or county planning commission agendas and approved-project lists for recently entitled projects; MPO permit data.
- **Historical delivery pace:** CoStar annual new deliveries by submarket for the prior 5–10 years, to calibrate how much of the proposed pipeline historically converts to delivered product.
- **Pre-leasing status:** CoStar lease comps filtered to under-construction buildings; broker interviews to confirm anchor tenant activity not yet public.
- **Lead time benchmarks:** Typical construction periods by property type (e.g., garden multifamily: 18–24 months; Class A high-rise multifamily: 30–42 months; industrial tilt-wall: 8–14 months; ground-up retail anchor: 18–30 months; varies by market and vintage; current as of 2026-05-24).
- **Entitlement status:** Approved/entitled (higher certainty) vs. in entitlement review (moderate certainty) vs. concept-stage (low certainty).

## Method

1. **Pull the raw pipeline.** Export CoStar under-construction and proposed properties for the submarket, filtering to the subject's property type and quality tier. Add any projects identified from county permitting records or planning commission agendas not in CoStar.

2. **Assign delivery dates.** For under-construction projects, use CoStar's reported delivery date as a starting point, then add a slippage buffer of 2–6 months (varies; larger for complex projects or constrained labor markets). For proposed projects, assign estimated delivery dates using typical construction lead times from entitlement approval.

3. **Score pipeline certainty.** Assign each project a probability weight based on its stage:
   - Under construction + anchor pre-lease: 90–100%
   - Under construction, no pre-lease: 70–85%
   - Entitled, vertical construction not started: 40–60%
   - In entitlement: 15–35%
   - Concept/planning stage: 5–20%
   These ranges vary by market cycle position; in a tight financing environment, even entitled projects may face higher attrition.

4. **Calculate risk-adjusted supply by year.** Multiply each project's SF (or unit count) by its probability weight and group by expected delivery year to produce a risk-adjusted supply schedule.

5. **Compare to historical delivery pace.** Divide the risk-adjusted annual pipeline by the historical average annual delivery in the submarket. A ratio significantly above 1.0 signals potential oversupply risk; below 1.0 suggests constrained supply.

6. **Calculate the supply-demand gap.** Subtract risk-adjusted annual supply from the base-case annual demand (from [[Demand Driver Analysis]]). A positive gap (demand > supply) supports tightening vacancy and rent growth. A negative gap (supply > demand) signals potential occupancy or rent headwinds.

7. **Identify pre-leasing offset.** Subtract confirmed pre-leased SF from speculative supply for purposes of vacancy impact modeling. Pre-leased space that leaves an existing building creates "shadow vacancy" — capture this in the analysis.

8. **Write the pipeline narrative.** Summarize the pipeline in 2–3 paragraphs: total pipeline size, phasing, pre-leasing level, key risks (construction cost inflation, financing gaps, anchor tenant uncertainty), and the analyst's overall read on supply risk over the projection horizon.

## Outputs

The primary output is a **supply pipeline table** with one row per project, showing property name or address, size (SF or units), property type, quality class, current stage, estimated delivery date, pre-leasing percentage, and probability weight. This feeds a **risk-adjusted annual supply schedule** (a one-page summary table by year). When combined with the demand forecast from [[Demand Driver Analysis]], it produces a **supply-demand gap analysis** showing projected vacancy trajectory and the implied timing of market tightening or softening. The pipeline narrative is typically a 2–3 paragraph section in an investment memo or market study.

## Example Walkthrough

The following numbers are illustrative and hypothetical, labeled as such throughout.

Suppose the subject is a hypothetical 250,000 SF Class A industrial building in a mid-size Sun Belt metro, with a projected delivery 18 months from today. The analyst pulls CoStar and identifies a hypothetical pipeline of 6 projects totaling 2.1 million SF in the submarket over the next 36 months. After applying probability weights (two projects under construction at 80% confidence, two entitled at 50%, two proposed at 20%), the risk-adjusted pipeline is approximately 1.1 million SF. Against a hypothetical historical annual absorption pace of 600,000–800,000 SF, the risk-adjusted pipeline implies roughly 1.5–1.8 years of supply absorption — elevated but not alarming in a growing market. However, the analyst notes that 40% of the pipeline is speculative (no confirmed pre-leasing), creating downside risk if demand falters. The supply-demand gap in the base case shows the market remaining in moderate balance during the subject's projected lease-up window, supporting a 12-month absorption assumption with a 6-month contingency buffer.

## Limitations

Supply pipeline data from CoStar and public records has meaningful coverage gaps: small projects, owner-user buildings, and municipally driven projects (affordable housing, public-private development) are frequently underreported. Probability weights are subjective and can be gamed to support a preferred conclusion. The framework does not model the competitive behavior of existing supply — in a rising market, shadow vacancy (space freed when tenants upgrade to new product) can dampen the benefit of net demand growth. For markets with severe land or entitlement constraints, the pipeline will systematically understate true supply risk from adaptive reuse or conversion projects. Pipeline analysis is a point-in-time snapshot; conditions can change rapidly when capital markets shift.

## Related Frameworks

[[Submarket Definition and Selection]] establishes the boundary. [[Demand Driver Analysis]] provides the demand-side counterpart. [[Absorption Modeling]] synthesizes supply and demand to project lease-up. [[Real Estate Cycle and Phases]] provides the macro context for interpreting pipeline risk. [[Development Feasibility Test]] uses pipeline data to stress-test whether a proposed project pencils given likely competition at delivery.
