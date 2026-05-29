---
title: "Stabilized NOI"
type: concept
tags: [cre/concepts]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Stabilized NOI is the normalized, market-occupancy net operating income a property is expected to produce once fully leased at market rents with normal vacancy and no extraordinary items.
domain: concepts
formula: true
related:
  - "Net Operating Income (NOI)"
  - "Cap Rate"
  - "Vacancy and Collection Loss"
  - "Effective Gross Income (EGI)"
  - "Operating Expense Ratio"
  - "Debt Service Coverage Ratio (DSCR)"
  - "Yield on Cost"
  - "Going-In Cap Rate"
  - "Exit Cap Rate"
  - "Direct Capitalization"
  - "Expense Normalization"
---

# Stabilized NOI

## Definition

Stabilized NOI is the normalized net operating income a property is expected to generate under market-rate, steady-state operating conditions — meaning market-level occupancy (not temporary peak or trough occupancy), market rents (not above- or below-market leases at expiration), and normal, recurring operating expenses without extraordinary items. It is the income assumption used in direct capitalization valuation, loan sizing, and long-term return projections, because it represents the sustainable earnings power of the asset rather than a snapshot of a potentially unusual operating period.

The "stabilization" concept addresses two fundamental challenges in income property analysis. First, properties frequently operate at occupancies that differ from long-run equilibrium — a newly delivered project is in lease-up, a value-add acquisition is intentionally under-occupied, or a recently churned tenant roster has left some space temporarily vacant. In each case, current NOI misrepresents the asset's long-run income potential, and valuation based on in-place NOI alone would either understate (for lease-up assets) or occasionally overstate (for assets with temporarily high occupancy) the property's economic value. Second, operating expenses in any given year may include one-time items — a large insurance claim, an unusual legal expense, a one-time management contract termination fee — that distort the run-rate expense baseline. Stabilized NOI normalizes both revenue and expenses to reflect repeatable, sustainable performance.

Stabilized NOI is a forward-looking, pro forma concept. Unlike T-12 NOI (trailing twelve months, which reflects actual historical operations), stabilized NOI is derived by projecting normalized revenue and expense assumptions. A skilled underwriter builds stabilized NOI by analyzing current rent roll versus market rents, applying market vacancy assumptions, and normalizing expenses against market benchmarks — not by simply accepting the most recent full year of actuals. See [[T-12 and T-3 Analysis]] and [[Expense Normalization]].

## Formula

- Plain text: `Stabilized NOI = Stabilized EGI − Normalized Operating Expenses`
- LaTeX:
$$
\text{Stabilized NOI} = \text{Stabilized EGI} - \text{Normalized Operating Expenses}
$$
$$
\text{Stabilized EGI} = \text{GPR at Market Rents} \times (1 - \text{Market Vacancy Rate}) + \text{Normalized Other Income}
$$

**Where:**
- **GPR at Market Rents** — gross potential rent using either: (a) current contract rents for tenants with long remaining terms, or (b) market rents for units/space at or near rollover
- **Market Vacancy Rate** — the stabilized, long-run vacancy rate for the specific submarket and asset type (not current actual vacancy)
- **Normalized Other Income** — recurring ancillary income streams at normalized run-rate levels
- **Normalized Operating Expenses** — operating expenses with one-time items removed, management fees imputed at market rates, and expense growth projected at normal escalation assumptions

## When It's Used

Stabilized NOI is the primary input to the [[Direct Capitalization]] valuation method: dividing stabilized NOI by the market cap rate yields the property's estimated stabilized market value. It is also the NOI basis for permanent loan sizing: lenders size loans on stabilized NOI because they are underwriting the property's long-run debt service capability, not its current temporarily elevated or depressed performance.

In value-add acquisition underwriting, stabilized NOI is the target state — the destination that the business plan aims to achieve through renovation, re-leasing, and repositioning. The investment thesis is quantified as the spread between in-place NOI at acquisition and projected stabilized NOI at execution, divided by the total capital invested (acquisition + renovation). See [[Value-Add Acquisition]].

For development projects, stabilized NOI is the income projection at the end of the lease-up period, typically 12–24 months after building delivery, when occupancy has reached market equilibrium. The yield on cost test divides stabilized NOI by total project cost to assess development feasibility. See [[Yield on Cost]].

## Variations & Edge Cases

**Stabilization timeline:** For a new development, stabilization is typically defined as reaching 90–95% occupancy at market rents, often projected 12–24 months after building delivery depending on submarket absorption rates. For a value-add acquisition, stabilization may be defined as the completion of renovations and re-leasing of the renovated units — often a 2–4 year process.

**Lease-up NOI vs. stabilized NOI:** In a development pro forma, there is typically a transition period between delivery and stabilization where NOI is building from near-zero toward the stabilized level. The cash flows during lease-up are modeled explicitly on a month-by-month basis; stabilized NOI is the terminal run-rate applied at the stabilization date.

**Rent growth:** Whether stabilized NOI is projected in current-year dollars (flat rent assumption) or in year-of-stabilization dollars (including market rent growth from today to stabilization) affects the calculation. Be clear about the rent assumption basis.

## Common Mistakes

**Using T-12 NOI as a proxy for stabilized NOI without adjustment.** Historical T-12 NOI is an important input but should be normalized, not assumed to equal stabilized NOI. Properties with above-market leases rolling, or temporarily low vacancy due to unusual conditions, may have T-12 NOI that overstates sustainable stabilized NOI.

**Assuming current occupancy is stabilized occupancy.** A property at 97% occupancy in a market where 93% is a stable long-run level should be underwritten at 93% — the current peak may not persist through the hold period.

**Failing to normalize expenses to market rates.** Self-managed properties often have below-market management fees; recently renovated properties may have temporarily low maintenance costs. Stabilized NOI requires market-rate expenses, not the current exceptional conditions.

## Related Concepts

- [[Net Operating Income (NOI)]] — stabilized NOI is a normalized, forward-looking version of NOI
- [[Cap Rate]] — the rate applied to stabilized NOI to derive value
- [[Direct Capitalization]] — the valuation method that divides stabilized NOI by the market cap rate
- [[Yield on Cost]] — development feasibility test: stabilized NOI / total project cost
- [[Going-In Cap Rate]] — cap rate applied to stabilized NOI at acquisition to establish entry pricing
- [[Exit Cap Rate]] — cap rate applied to projected stabilized NOI at disposition
- [[Expense Normalization]] — the analytical process that produces the normalized expense basis for stabilized NOI

## Sources

Stabilized NOI methodology is addressed in CCIM's income property analysis curriculum, the Appraisal Institute's income approach standards, and lender underwriting guidelines from Fannie Mae, Freddie Mac, and institutional program lenders. Specific vacancy and expense normalization assumptions vary by market, asset class, and vintage (varies by market and vintage; current as of 2026-05-24).
