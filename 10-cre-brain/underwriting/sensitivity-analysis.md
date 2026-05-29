---
title: "Sensitivity Analysis"
type: framework
tags: [cre/underwriting, cre/frameworks]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Framework for systematically varying key underwriting assumptions to quantify how changes in inputs affect deal returns and identify which variables most drive outcomes.
inputs_required:
  - Base-case pro forma with all key assumptions
  - Defined range of variation for each assumption tested
  - Target return metrics (IRR, equity multiple, DSCR, yield-on-cost)
outputs:
  - Two-variable sensitivity tables (e.g., rent growth vs. exit cap rate)
  - Tornado chart or ranked list of assumption impact on returns
  - IRR, equity multiple, and cash-on-cash across scenarios
  - Identification of break-even levels for critical assumptions
related:
  - "Pro Forma Construction Method"
  - "Stress Testing"
  - "Monte Carlo in CRE"
  - "Assumption Hierarchy: Actual vs. Pro Forma"
  - "Internal Rate of Return (IRR)"
  - "Equity Multiple"
  - "Cash-on-Cash Return"
  - "Exit Cap Rate"
  - "Discount Rate"
---

# Sensitivity Analysis

## Purpose

Sensitivity analysis is the systematic practice of varying one or more key underwriting assumptions while holding others constant in order to map the relationship between inputs and outputs. In CRE underwriting, it answers the question: "How much does my IRR move if rent growth comes in at 1% instead of 3%? If my exit cap expands 50 basis points? If I lease up 12 months later than projected?" These are the questions that determine whether a deal is robust across a realistic range of outcomes or fragile to a single optimistic assumption.

No base-case pro forma, no matter how carefully built, is a point forecast of the future. Sensitivity analysis converts the single-point base case into a multi-dimensional map of the return distribution, revealing which assumptions carry the most leverage and where the deal's critical vulnerabilities lie. Institutional investment committees, lenders, and sophisticated equity partners will not approve a deal without seeing sensitivity tables — they are a standard deliverable in any underwriting package.

## Inputs Required

- **Fully built base-case pro forma:** See [[Pro Forma Construction Method]]. All key assumptions must be explicitly identified: rent growth rate, vacancy, exit cap rate, hold period, construction cost (for development), lease-up timing, and debt terms.
- **Defined variable ranges:** For each input tested, a low/mid/high or a range with defined increment (e.g., exit cap ±25 bps, ±50 bps, ±75 bps). Ranges should be market-calibrated, not arbitrary — use historical cap rate volatility and rent growth distributions where available.
- **Target return metrics:** IRR, equity multiple, [[Cash-on-Cash Return]], and [[Debt Service Coverage Ratio (DSCR)]] at minimum. Some analyses also test loan sizing (maximum leverage at target DSCR).

## Method

1. **Identify the top 3–5 value-driving assumptions.** Common candidates for CRE: exit cap rate, hold-period rent growth rate, lease-up timing (development/value-add), stabilized NOI (going-in cap), and interest rate / refinance assumptions. Not every variable deserves a sensitivity table; focus on the ones with the greatest impact and the greatest uncertainty.

2. **Build one-variable sensitivity tables.** For each identified assumption, hold all other variables at base-case values and compute the return metric (typically IRR and equity multiple) across the defined range. This isolates the marginal impact of each variable.

   Example structure (exit cap rate sensitivity):

   | Exit Cap Rate | Levered IRR | Equity Multiple |
   |---|---|---|
   | 4.50% | 18.2% | 2.1× |
   | 5.00% (base) | 14.5% | 1.85× |
   | 5.50% | 10.8% | 1.62× |
   | 6.00% | 7.2% | 1.41× |

3. **Build two-variable sensitivity tables (data tables).** The most common format pairs the two highest-impact variables — typically exit cap rate on one axis and rent growth (or stabilized NOI) on the other — and fills the table with IRR or equity multiple values for each combination. This is the standard deal-committee output for communicating return risk.

   - Rows: exit cap rate (e.g., 4.50%, 5.00%, 5.50%, 6.00%, 6.50%)
   - Columns: annual rent growth (e.g., 1.0%, 1.5%, 2.0%, 2.5%, 3.0%)
   - Cell values: levered IRR

4. **Rank variables by return impact (tornado analysis).** For each variable, compute the absolute change in IRR over its full modeled range. Rank variables from highest to lowest impact. The resulting ranked list (often visualized as a horizontal bar chart, the "tornado") identifies which assumptions deserve the most diligence and the most conservative treatment.

5. **Identify break-even values.** Determine the value of each key input at which the deal exactly hits the minimum acceptable return hurdle (e.g., 12% IRR). This break-even analysis tells the decision-maker how much deterioration the deal can absorb before it fails to meet objectives. If the exit cap break-even is at 7.0% and current market caps are 5.0%, the deal has significant margin — if the break-even is 5.1%, the deal is fragile.

6. **Document assumptions and ranges in the underwriting package.** Sensitivity outputs without documented rationale for the variable ranges are incomplete. Each range should reference a market data source, historical cap rate volatility, or lender guideline that justifies why the range is reasonable.

## Outputs

The sensitivity analysis produces: (1) one-variable sensitivity tables for each key assumption; (2) two-variable sensitivity tables for the critical pairings; (3) a ranked list or tornado chart of variable impact on returns; and (4) break-even values for each critical assumption vs. the target return hurdle. These outputs are presented alongside the base-case pro forma in the investment committee memo or lender package.

## Example Walkthrough

*All figures below are illustrative and hypothetical — not derived from any real transaction.*

A value-add multifamily acquisition has a base-case levered IRR of 15.5% assuming 2.5% annual rent growth and a 5.75% exit cap. The sensitivity team tests exit cap (5.00%–7.00% in 25 bps steps) against rent growth (1.0%–4.0% in 50 bps steps). In the base case, the IRR is 15.5%. If rent growth falls to 1.5% and the exit cap expands to 6.50%, the IRR falls to 9.8% — below the fund's 12% return hurdle. The break-even exit cap at base-case rent growth is 6.85%, providing roughly 110 bps of cap rate expansion before the deal misses hurdle. This analysis drives the underwriter to focus additional diligence on submarket rent growth fundamentals, since rent growth drives more than 60% of IRR sensitivity according to the tornado chart.

## Limitations

Sensitivity analysis is parametric — it tests defined ranges around a base case but does not estimate the probability of each scenario materializing. A 7% exit cap may be in the sensitivity range but the analyst cannot say whether it has a 10% or 40% probability of occurring. For probabilistic output, see [[Monte Carlo in CRE]]. Sensitivity analysis also tests variables one at a time (or in pairs) and does not naturally capture correlated risk — rising cap rates and declining rent growth often occur together in downturns, and the two-variable table only partially captures this covariance. [[Stress Testing]] complements sensitivity analysis by applying deliberately adverse combinations. Finally, sensitivity analysis is only as good as the base-case model — structural errors in the pro forma propagate into every sensitivity output.

## Related Frameworks

[[Stress Testing]] — applies specific adverse-scenario combinations rather than range-testing individual variables; the two are complementary. [[Monte Carlo in CRE]] — probabilistic extension of sensitivity analysis using probability distributions. [[Pro Forma Construction Method]] — the base-case model that sensitivity analysis interrogates. [[Assumption Hierarchy: Actual vs. Pro Forma]] — governs how conservatively to set base-case assumptions before sensitizing.

## Sources

CCIM Institute, *Financial Analysis for Commercial Investment Real Estate* (CI 102). Real estate private equity deal-committee presentation standards. Standard modeling practice in institutional CRE underwriting.
