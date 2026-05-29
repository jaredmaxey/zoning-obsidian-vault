---
title: "Yield-on-Cost vs. Market Cap Spread"
type: concept
tags: [cre/underwriting]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: The spread between a development's yield on cost and the prevailing market cap rate for comparable stabilized assets, used to measure development return adequacy and feasibility.
domain: underwriting
formula: true
related:
  - "Development Spread"
  - "Yield on Cost"
  - "Cap Rate"
  - "Exit Cap Rate"
  - "Going-In Cap Rate"
  - "Net Operating Income (NOI)"
  - "Stabilized NOI"
  - "Residual Land Value Method"
  - "Direct Capitalization"
  - "Ground-Up Development"
  - "Development Feasibility Test"
---

# Yield-on-Cost vs. Market Cap Spread

## Definition

The yield-on-cost vs. market cap spread (often called the "development spread") is the difference between a development project's yield on cost (YoC) and the prevailing market capitalization rate for stabilized comparable assets. Yield on cost is the stabilized NOI the completed development will generate divided by the total all-in development cost, including land. The market cap rate is what the stabilized asset would trade at in the current transaction market. The spread between the two is the fundamental measure of whether building makes sense versus buying a stabilized equivalent.

When the spread is wide — YoC meaningfully exceeds the market cap rate — development creates value: the developer builds something worth more (at the stabilized cap rate) than it cost to build. This is the core logic of development profitability. When the spread narrows or inverts — YoC approaches or falls below the prevailing cap rate — development no longer creates sufficient value to justify the construction risk, leasing risk, and time risk involved. A developer accepting zero spread is effectively being paid no premium for those risks.

Institutional development underwriting typically targets a minimum spread of 150–250 basis points between YoC and the stabilized exit cap rate (varies by asset class, market, submarket, and development risk as of 2026-05-24). Higher-risk, longer-duration projects (large mixed-use, ground-up office, luxury residential in new submarkets) command the wider end of that range. Stabilized build-to-suit or pre-leased industrial development with creditworthy tenants may underwrite to tighter spreads because leasing risk is largely eliminated. The spread required by institutional equity is sometimes framed as the "risk premium for development" — compensation over and above simply buying a stabilized asset.

## Formula

- Plain text: `Development Spread = YoC − Exit Cap Rate`
- LaTeX: $$ Spread = YoC - R_{exit} $$

Where:
- YoC (Yield on Cost) = Stabilized NOI / Total Development Cost (including land)
- R_exit = prevailing market cap rate for comparable stabilized assets
- Spread = percentage points (e.g., 200 bps = 2.00%)

The YoC formula:
- Plain text: `YoC = Stabilized NOI / Total Development Cost`
- LaTeX: $$ YoC = \frac{NOI_{stab}}{TDC} $$

Where:
- NOI_stab = projected net operating income at stabilization (dollars)
- TDC = total all-in development cost including land acquisition, hard costs, soft costs, financing costs, and carry

## When It's Used

This concept is applied at every stage of development feasibility analysis. In pre-acquisition screening, a developer computes a preliminary YoC using parametric cost estimates and market rent benchmarks to check whether the project is worth pursuing before spending money on detailed design and entitlement. During the full feasibility underwrite, the spread drives the land valuation via the [[Residual Land Value Method]] — the required spread determines what land price the developer can pay. In the capital-raising phase, the spread communicates return adequacy to equity investors and differentiates the development opportunity from simply buying stabilized assets in the same market.

The spread also calibrates the developer's response to changes in market conditions. Rising construction costs compress the spread from below (same NOI, higher TDC). Rising interest rates push up stabilized cap rates, potentially narrowing the spread if market caps widen faster than the developer can raise rents. A falling cap rate environment widens the spread and makes development more attractive — this dynamic drove the development boom of the 2010s in many multifamily markets where cap rates compressed to 4–5% while construction costs were rising but still generating 150–200 bps of spread.

## Variations & Edge Cases

The spread can be measured against the going-in (current) market cap rate or the projected exit cap rate at completion, typically 12–24+ months in the future. Many developers use the projected exit cap — which may be higher or lower than today's cap depending on rate cycle outlook — making the spread forecast-dependent. Conservatively, underwriters stress-test the spread against a cap rate 25–75 bps above their base exit cap assumption to see whether the project still justifies land basis.

In for-sale residential development (condos, single-family land development), the spread concept is replaced by gross development margin — the difference between aggregate sale proceeds and total development cost as a percentage of proceeds. The concept is analogous but the execution differs because there is no stabilized NOI; value is realized through unit sales rather than income capitalization.

## Common Mistakes

The most common mistake is computing YoC on a budget that excludes key cost items — particularly financing costs (construction loan interest carry), developer overhead, or the full land basis including all transaction costs. Any exclusion inflates the apparent YoC and artificially widens the spread, making a marginal project look more compelling than it is. A second error is using the current in-place market cap rate without accounting for likely cap rate movement over the development timeline. If a project takes 36 months to stabilize and the market cap rate is currently compressed, the developer may be underestimating the exit cap at completion.

Analysts also sometimes compare YoC to the going-in cap rate for a stabilized acquisition in the same market — which is an apples-to-oranges comparison because the stabilized acquisition has no construction or leasing risk. The development spread should be measured against the exit cap rate for a stabilized equivalent asset, not the going-in cap rate on current value-add acquisitions, which already embeds a return premium of its own.

## Related Concepts

[[Development Spread]] — this concept is the formal definition; the two notes are closely related. [[Yield on Cost]] — the development return metric that is the numerator of the spread. [[Cap Rate]] and [[Exit Cap Rate]] — the market denominator of the spread comparison. [[Residual Land Value Method]] — the framework that uses the required spread to back-solve for maximum land price. [[Ground-Up Development]] — the deal context in which this metric is most central.

## Sources

ULI, *Real Estate Development: Principles and Process* (5th ed.). CCIM Institute, development feasibility coursework. Institutional REPE development underwriting practice.
