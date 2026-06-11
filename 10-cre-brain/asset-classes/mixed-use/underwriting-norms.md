---
title: Mixed-Use — Underwriting Norms
aliases: ["Mixed-Use — Underwriting Norms"]
type: asset-class
tags: [cre, asset/mixed-use]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Component-level and blended underwriting ranges for mixed-use, including cap rates by use, vacancy assumptions, shared-cost allocation, and the methodology for aggregating component NOIs into a project-level valuation.
asset_class: mixed-use
subtypes: []
related:
  - Mixed-Use
  - Mixed-Use — Key Metrics
  - Mixed-Use — Risks & Considerations
  - Multifamily
  - Retail
  - Office
  - Cap Rate
  - Going-In Cap Rate
  - Exit Cap Rate
  - Net Operating Income (NOI)
  - Stabilized NOI
  - Effective Gross Income (EGI)
  - Vacancy and Collection Loss
  - Operating Expense Ratio
  - Reserves for Replacement
  - Yield on Cost
  - Yield-on-Cost vs. Market Cap Spread
  - Direct Capitalization
  - Discounted Cash Flow (DCF)
  - Pro Forma Construction Method
  - Expense Normalization
  - Sensitivity Analysis
  - Debt Service Coverage Ratio (DSCR)
  - Loan-to-Value (LTV)
  - Construction Loan
  - Permanent Loan
  - Senior Debt
---

# Mixed-Use — Underwriting Norms

## Overview

Underwriting mixed-use requires treating each income-producing component — residential, retail, office, or other use — as a separate pro forma with its own market-driven rent, vacancy, expense, and cap-rate assumptions, then aggregating the results into a project-level NOI and value conclusion. The temptation to apply a single blended cap rate to a blended NOI without component-level decomposition produces inaccurate valuations and conceals the risk profile of weaker components behind stronger ones. Best practice is to underwrite each component by the standards of its own asset class (see [[Multifamily]], [[Retail]], [[Office]]), allocate shared costs explicitly, and derive the blended cap rate as an NOI-weighted average of component cap rates.

A critical underwriting judgment in mixed-use is the shared-cost allocation — how parking structure costs, lobby and common-area maintenance, building systems, and other costs shared between uses are charged to each component. The allocation method (by GLA share, by unit count, by use-specific benefit) materially affects per-component NOI and, in condo or parcelized structures, has legal and tax implications. Lenders will scrutinize cost-allocation methodology carefully, particularly for cross-collateralized or component-financed structures.

Construction feasibility underwriting uses [[Yield on Cost]] (stabilized NOI ÷ total project cost) benchmarked against a target market cap rate spread — typically 100–200 basis points above the stabilized cap rate to justify development risk. Because mixed-use projects carry higher all-in costs (structured parking, podium construction, MEP complexity, longer lease-up) than comparable single-use residential, the feasibility hurdle is meaningful. Projects that cannot achieve a positive spread between yield-on-cost and market cap rate will fail the [[Development Feasibility Test]] unless land cost, public subsidy, or density bonuses improve the margin.

## Typical Ranges by Component

| Metric | Residential Component | Retail Component | Office Component | Notes |
|--------|-----------------------|-----------------|-----------------|-------|
| Going-in cap rate | 4.0% – 5.5% | 6.0% – 8.5% | 6.0% – 9.0% | Class A urban tighter; secondary market / Class B wider |
| Stabilized vacancy | 4% – 8% | 5% – 15% | 8% – 18% | Ground-floor mixed-use retail historically elevated vs. freestanding |
| Operating expense ratio | 30% – 40% | 10% – 25% (NNN) | 35% – 50% (gross) | Retail NNN recovery shifts OpEx to tenant; office gross is landlord-heavy |
| TI/LC allowance — new lease | N/A | $15 – $75 PSF | $40 – $100 PSF | Market and space condition dependent |
| Reserves for replacement | $200 – $500/unit/yr | $0.10 – $0.30 PSF | $0.15 – $0.40 PSF | Varies by age and quality |
| Exit cap (spread to going-in) | +25 bps – +75 bps | +50 bps – +100 bps | +50 bps – +125 bps | Retail and office carry wider exit spread due to lease-term burn-off |

## Blended Cap Rate and Project-Level Metrics

| Metric | Typical Range | Notes |
|--------|---------------|-------|
| Blended going-in cap rate | 4.5% – 6.5% | NOI-weighted by component; residential-heavy projects track multifamily pricing |
| Blended stabilized vacancy | 5% – 12% | Residential typically stabilizes faster; retail and office may drag project vacancy higher |
| Blended OER | 28% – 42% | Depends heavily on lease structure mix (NNN retail vs. gross office vs. residential) |
| Yield on cost — target | 5.0% – 7.5% | Must exceed stabilized market cap rate by 100–200 bps to justify development risk |
| DSCR at stabilization | 1.20x – 1.35x | Lender requirement; component-level debt may require higher coverage on weaker-performing use |
| LTC — construction | 55% – 70% | Lower than single-use residential due to mixed-program complexity and lease-up risk |
| LTV — permanent (stabilized) | 55% – 70% | Per-component takeout financing may achieve higher LTV on residential tranche |

*Ranges current as of 2026-05-24. Verify against current market data before underwriting.*

## Component Underwriting Approach

**Residential component:** Apply [[Multifamily]] underwriting methodology. Use [[Comparable Rents (Rent Comps)]] to establish per-unit market rent by bedroom type; apply a mixed-use placemaking premium (typically 3–10% above comparable single-use multifamily in the same submarket, but verify against actual market comps). Model vacancy and collection loss, operating expenses (management fee, payroll, utilities, insurance, taxes, repairs and maintenance), and [[Reserves for Replacement]]. Cap residential NOI at the market rate for comparable multifamily product type and submarket.

**Retail component:** Apply [[Retail]] underwriting methodology for the applicable format (ground-floor neighborhood service NNN is most common). Establish market rent per SF using [[Comparable Rents (Rent Comps)]] for ground-floor mixed-use retail in comparable infill locations — note that ground-floor mixed-use retail frequently trades at a discount to freestanding retail in the same trade area due to activation risk and less favorable access/visibility. Apply stabilized vacancy, landlord-responsibility operating expenses, TI/LC reserves, and cap at the applicable retail cap rate (neighborhood-service NNN, likely 6.5–8.5% in most markets). Do not assume 100% retail occupancy at pro forma stabilization; model a conservative stabilized vacancy of 5–15%.

**Office component:** Where present, apply [[Office]] underwriting methodology. Establish market rent using office [[Comparable Rents (Rent Comps)]], model lease-up (office absorption is slower and lumpier than residential), apply appropriate operating expenses (gross or modified-gross), and cap at office market rates for the applicable class and submarket. Office components in mixed-use projects are increasingly rare outside of owner-occupied or medical-office programs given post-2020 office demand uncertainty.

## Shared-Cost Allocation

Shared costs — structured parking construction and operation, lobby and common area, building systems, landscaping, building management — must be allocated among components before per-component NOI can be derived. The most common methods:

- **Gross leasable area (GLA) pro-rata:** Allocate by each component's share of total rentable SF. Simple and auditable; may overcharge retail (which occupies lower floors with higher shell cost per SF) or undercharge residential.
- **Unit-count basis:** For residential-heavy projects, allocate shared costs on a per-unit basis to the residential component and PSF basis to commercial. Reflects that management and operational intensity scales with unit count.
- **Benefit-based allocation:** Assign parking costs based on each component's estimated parking demand; assign lobby costs based on building access; allocate MEP costs based on metered usage. Most accurate but operationally complex; required in condo regimes with separate ownership.

Parking is often the largest shared-cost item. Structured parking at $25,000–$60,000+ per stall (varies by market and structure type) is a primary driver of project cost and must be allocated among users. Shared parking ratio analysis — modeling peak parking demand by component by time-of-day — often demonstrates that a mixed-use project requires 15–30% fewer total stalls than the sum of single-use requirements, a key feasibility advantage. See [[Mixed-Use — Key Metrics]] for the shared parking ratio metric.

---

*Ranges current as of 2026-05-24. Verify against current market data before underwriting.*
