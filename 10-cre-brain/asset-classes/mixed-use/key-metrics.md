---
title: Mixed-Use — Key Metrics
aliases: ["Mixed-Use — Key Metrics"]
type: asset-class
tags: [cre, asset/mixed-use]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Defines six key metrics specific to mixed-use underwriting and operations — blended cap rate, component NOI contribution, shared parking ratio, cost allocation method, placemaking premium, and structured parking cost per stall.
asset_class: mixed-use
subtypes: []
related:
  - Mixed-Use
  - Mixed-Use — Underwriting Norms
  - Mixed-Use — Risks & Considerations
  - Multifamily
  - Retail
  - Office
  - Cap Rate
  - Going-In Cap Rate
  - Net Operating Income (NOI)
  - Stabilized NOI
  - Effective Gross Income (EGI)
  - Yield on Cost
  - Price per Square Foot
  - Price per Unit
  - Replacement Cost
  - Direct Capitalization
  - Discounted Cash Flow (DCF)
  - Weighted Average Cost of Capital (WACC)
---

# Mixed-Use — Key Metrics

Mixed-use underwriting and asset management require both the standard metrics of each component class (see [[Multifamily]], [[Retail]], [[Office]]) and a set of project-level metrics that exist only in the multi-use context. The six metrics below are the most important mixed-use-specific measures for deal analysis, financing, and ongoing asset management.

### Blended Cap Rate

**Definition:** The NOI-weighted average capitalization rate across all income-producing components of a mixed-use project. Because each component (residential, retail, office) is valued at a different cap rate reflecting its risk profile and income stability, a single blended cap rate is required to produce a unified asset valuation via direct capitalization.

**Use:** Applied to stabilized project-level NOI to derive a single-asset value; used in financing, disposition underwriting, and portfolio attribution. Also used to compare mixed-use acquisitions to single-use alternatives.

**Formula (plain):** Blended Cap Rate = Total Stabilized NOI ÷ Total Property Value

Where Total Property Value is the sum of component values (each component's NOI capitalized at its own market cap rate), and the blended cap rate is the implied rate on the aggregated NOI.

**Formula (LaTeX):**

$$\text{Blended Cap Rate} = \frac{\sum_{i} \text{NOI}_i}{\sum_{i} \frac{\text{NOI}_i}{r_i}}$$

Where $\text{NOI}_i$ is the stabilized NOI of component $i$ and $r_i$ is the market cap rate for that component. The denominator is the sum of individual component values.

**Typical range:** 4.5%–6.5% for residential-heavy projects in major markets; wider (6.0%–8.0%+) for retail- or office-heavy programs. Varies by market and vintage.

### Component-Level NOI Contribution

**Definition:** Each income-producing component's NOI expressed as a percentage of total project NOI. Measures programmatic concentration and identifies which uses drive value, income stability, and risk.

**Use:** Guides capital-stack structuring (lenders focus on the dominant component), sensitivity analysis (a residential-heavy project is more resilient to retail vacancy than a retail-heavy one), and operational priority-setting. Required for any component-level financing split (e.g., agency debt on the multifamily tranche).

**Formula (plain):** Component NOI Share (%) = Component Stabilized NOI ÷ Total Project Stabilized NOI × 100

**Typical range:** In contemporary residential-led mixed-use, the residential component typically contributes 60%–85% of total NOI; ground-floor retail 10%–25%; office (where present) 5%–20%. Projects with larger retail or office programs carry greater exposure to the cyclicality and leasing risk of those components.

### Shared Parking Ratio

**Definition:** The ratio of total parking stalls provided to the aggregate peak-hour demand of all uses if each use were operated independently (i.e., required by individual parking standards). A shared parking ratio below 1.0 means the project provides fewer stalls than single-use standards would require, taking advantage of staggered peak demand across uses.

**Use:** Quantifies the parking efficiency benefit of mixed-use programming. A favorable shared parking ratio reduces required stall count, lowering structured parking construction cost — one of the largest drivers of mixed-use project cost and feasibility. Required for municipal approvals in jurisdictions that use shared-parking analysis in lieu of standard minimum parking ratios.

**Formula (plain):** Shared Parking Ratio = Stalls Provided ÷ Sum of Individual Use Parking Requirements (each use at its peak demand time)

**Typical range:** 0.70–0.90x in well-programmed mixed-use projects (i.e., providing 70–90% of stalls that would be required if each use were standalone). Varies by use mix and peak demand profiles. Residential peaks evenings/weekends; retail peaks weekday noon and weekend afternoons; office peaks weekday mornings.

### Cost Allocation Method

**Definition:** The methodology used to allocate shared project costs — structured parking, lobby, building core and shell, building systems, landscaping, and common-area maintenance — among the individual use components of a mixed-use project.

**Use:** Drives per-component NOI (by determining each component's operating expense load), affects tax assessment (in jurisdictions that assess by use), and governs financial obligations in condo regimes or reciprocal easement agreements (REAs). Lenders and appraisers will require a clear, defensible cost allocation to underwrite component-level loans. See [[Mixed-Use — Underwriting Norms]] for the three primary methods (GLA pro-rata, unit-count basis, benefit-based).

**No single formula** — method must be selected based on project structure, ownership, and financing requirements. The key discipline is consistency: apply the same method across budget, appraisal, and financing documentation.

### Cross-Use Synergy / Placemaking Premium

**Definition:** The rent premium — in residential, retail, or office units — attributable to the activated mixed-use environment versus comparable single-use product in the same submarket. A well-executed mixed-use project generates foot traffic, amenity density, and sense-of-place that allow residential units to command above-comparable rents and ground-floor retail to achieve faster lease-up at market rates.

**Use:** Supports underwriting above-market residential rents in pro forma; justifies higher project cost by demonstrating value creation beyond the sum of standalone components. Must be validated against actual comparable mixed-use projects in the submarket — a common underwriting error is assuming a placemaking premium without comps support.

**Formula (plain):** Placemaking Premium (%) = (Mixed-Use Project Rent PSF − Comparable Single-Use Rent PSF) ÷ Comparable Single-Use Rent PSF × 100

**Typical range:** 3%–10% premium for well-located, well-executed mixed-use residential versus comparable single-use multifamily in the same submarket; range varies widely and can be negative in projects with chronic ground-floor vacancy or poor retail activation. Verify against current comps; do not assume premium without evidence.

### Structured Parking Cost Per Stall

**Definition:** The all-in construction cost to deliver one parking stall in a structured (above-grade or below-grade) parking facility integrated into a mixed-use project. Structured parking is almost always required in urban and TOD mixed-use because surface parking is land-inefficient. Cost per stall is a primary driver of overall project cost and feasibility.

**Use:** Appears in the development budget as a [[Hard Costs]] line item; used in shared-cost allocation (stall costs allocated to each use based on its parking demand); evaluated against the "parking subsidy" — the extent to which structured parking costs exceed what the project's parking revenue (if any) and the indirect benefit to residents/tenants can justify. Parking cost that cannot be recovered through rents or allocated costs reduces yield-on-cost and may impair feasibility.

**Formula (plain):** Structured Parking Cost Per Stall = Total Parking Structure Cost ÷ Total Stalls

**Typical range:** $25,000–$45,000 per stall for above-grade structured parking; $40,000–$80,000+ per stall for below-grade (underground) parking. Wide variation by market, structure depth, soil conditions, and construction type. Varies by market and vintage — verify against current contractor bids and comparable projects before budgeting.
