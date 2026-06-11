---
title: "Yield on Cost"
aliases: ["Yield on Cost"]
type: concept
tags: [cre/concepts]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Yield on cost measures a development project's stabilized NOI divided by total project cost, serving as the primary feasibility test for ground-up and value-add investments.
domain: concepts
formula: true
related:
  - "Cap Rate"
  - "Going-In Cap Rate"
  - "Net Operating Income (NOI)"
  - "Stabilized NOI"
  - "Replacement Cost"
  - "Development Spread"
  - "Yield-on-Cost vs. Market Cap Spread"
  - "Ground-Up Development"
  - "Development Feasibility Test"
---

# Yield on Cost

## Definition

Yield on cost (YOC) is the ratio of a project's stabilized net operating income to its total all-in development or renovation cost. It is the foundational feasibility metric for development and value-add underwriting: it answers the question "given everything it costs to build or renovate this project, what unlevered income yield do I earn at stabilization?" When the yield on cost exceeds the prevailing acquisition cap rate for comparable stabilized assets, the developer has created value through construction or repositioning.

The concept applies equally to ground-up development and value-add repositioning. For a developer building a new apartment complex, the yield on cost tells them whether the spread over market cap rates justifies the development risk, carry cost, and execution uncertainty. For a value-add buyer, it benchmarks the post-renovation income yield against what the market would pay for a stabilized version of the asset. See [[Development Feasibility Test]] and [[Yield-on-Cost vs. Market Cap Spread]] for the analytical frameworks built around this metric.

Yield on cost is an unlevered, stabilized, point-in-time metric — like a cap rate applied to a cost basis rather than a transaction price. It does not capture the time value of money, lease-up risk, or the path to stabilization. For those dimensions, a full DCF model with levered IRR is needed.

## Formula

- Plain text: `Yield on Cost = Stabilized NOI / Total Project Cost`
- LaTeX: $$ \text{Yield on Cost} = \frac{\text{Stabilized NOI}}{\text{Total Project Cost}} $$

**Where:**
- **Stabilized NOI** — the net operating income the property is expected to generate at full market occupancy (typically 90–95% for most asset classes), using market-rate rents and normalized expenses. See [[Stabilized NOI]].
- **Total Project Cost** — the fully loaded project cost including land acquisition, hard costs, soft costs, financing costs (carry interest), developer fee, and all contingencies. See [[Hard Costs]], [[Soft Costs]], and [[Construction Loan]].

The development spread is computed as: `Development Spread = Yield on Cost − Market Cap Rate`. A positive spread (YOC exceeds going-in cap rates for stabilized comparable assets) indicates value creation. Most institutional developers require a minimum spread of 100–200 basis points over market cap rates to justify ground-up development risk (varies by market and vintage; current as of 2026-05-24).

## When It's Used

Yield on cost is the primary go/no-go metric evaluated at every stage of development underwriting. Before land acquisition, a developer runs a "back-of-envelope" feasibility test: what NOI is achievable, and does that NOI divided by estimated total cost clear the required spread? If not, the land price must be lower or the project redesigned. See [[Residual Land Value Method]] for the land pricing analog.

Lenders also use yield on cost as a underwriting input for construction loans: they want to confirm that at stabilization, the borrower will be able to refinance into permanent debt at a cap rate that produces acceptable LTV and DSCR — which depends on the project producing sufficient NOI relative to total cost. Equity investors use yield on cost to evaluate the sponsor's underwriting credibility and compare projected returns across competing development opportunities.

## Variations & Edge Cases

**Gross YOC vs. net YOC:** Some practitioners compute YOC on gross scheduled income rather than NOI. This is uncommon in institutional practice but may appear in quick pro formas. Always confirm the NOI basis.

**In-place YOC:** For a value-add acquisition, practitioners sometimes quote a "day-one yield on cost" using current NOI divided by total all-in cost (purchase price plus planned capex). This is lower than stabilized YOC and reflects the drag of lease-up and renovation. Distinguish clearly.

**Developer fee inclusion:** Whether or not the developer fee is included in total project cost varies. Including it is the more conservative (and more common institutional) convention — the developer earns the fee as a project expense, not an equity return, and it belongs in the cost basis.

**Carry costs during construction:** Total project cost should include interest carry on the construction loan through the projected lease-up period. Understating carry costs inflates yield on cost and is a common underwriting error.

## Common Mistakes

**Using pro forma NOI that exceeds achievable market rents.** If the stabilized NOI assumption is aggressive, the yield on cost will appear to clear the hurdle when it does not in practice. Ground the NOI assumption in current [[Comparable Rents (Rent Comps)]] with modest growth assumptions.

**Excluding soft costs or contingency from total project cost.** A yield on cost that omits developer overhead, financing fees, soft-cost contingency, or lease-up costs is artificially high. Institutional lenders and equity partners will insist on full-cost inclusion.

**Comparing to the wrong market cap rate.** The relevant benchmark is the stabilized acquisition cap rate for a newly completed comparable asset in the same submarket — not an average or stale figure. Using a cap rate that is too high makes the development spread appear wider than it actually is.

## Related Concepts

- [[Cap Rate]] — the benchmark against which yield on cost is compared to assess development spread
- [[Going-In Cap Rate]] — the acquisition-day cap rate for stabilized comparables
- [[Net Operating Income (NOI)]] — the numerator; stabilized NOI quality is critical
- [[Stabilized NOI]] — the income projection applied at the YOC denominator's stabilization date
- [[Replacement Cost]] — a complementary feasibility check: if purchase price exceeds replacement cost, new supply becomes competitive
- [[Development Spread]] — the explicit spread: YOC minus market cap rate
- [[Yield-on-Cost vs. Market Cap Spread]] — the framework for interpreting and applying the spread
- [[Ground-Up Development]] — the primary deal type where YOC is the core feasibility metric

## Sources

Yield on cost methodology is discussed in ULI's *Real Estate Development* (6th ed.) and CCIM's development underwriting curriculum. NCREIF and institutional fund managers publish return hurdles that frame required development spreads. Market spread requirements vary by asset class, market cycle phase, and risk profile (varies by market and vintage; current as of 2026-05-24).
