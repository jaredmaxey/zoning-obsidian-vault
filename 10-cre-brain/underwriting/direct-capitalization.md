---
title: "Direct Capitalization"
aliases: ["Direct Capitalization"]
type: framework
tags: [cre/underwriting, cre/frameworks]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Single-period valuation method that divides stabilized NOI by a market-derived cap rate to estimate a property's current market value.
inputs_required:
  - Stabilized NOI (annual, normalized)
  - Market cap rate (from comparable sales)
outputs:
  - Estimated property value (direct cap value)
  - Implied going-in cap rate on acquisition price
  - Sensitivity of value to cap rate movement
related:
  - "Discounted Cash Flow (DCF)"
  - "Residual Land Value Method"
  - "Pro Forma Construction Method"
  - "Rent Roll Analysis"
  - "Expense Normalization"
  - "T-12 and T-3 Analysis"
  - "Net Operating Income (NOI)"
  - "Cap Rate"
  - "Going-In Cap Rate"
  - "Exit Cap Rate"
  - "Stabilized NOI"
  - "Comparable Sales (Sales Comps)"
---

# Direct Capitalization

## Purpose

Direct capitalization is the most widely used single-period income approach to CRE valuation. It converts a property's stabilized net operating income into a value estimate by dividing NOI by a market-derived capitalization rate. The method is fast, intuitive, and transparent — which is why it is the primary valuation shorthand in every acquisition screen, broker opinion of value, and lender quick-look. It is the engine behind the [[Cap Rate]] concept in practice.

Analysts reach for direct capitalization as a first-pass valuation in the acquisition screening phase, as a cross-check on the terminal value in a [[Discounted Cash Flow (DCF)]] model, and as the primary method when a property is stabilized and the income stream is relatively predictable. It is also the standard method for appraisal when the income approach dominates — a formal appraisal for a stabilized multifamily or industrial asset will lean heavily on direct capitalization, with the cap rate derived from a careful analysis of comparable sales.

## Inputs Required

- **Stabilized NOI:** Annual net operating income at stabilized occupancy and market rents, normalized for non-recurring items. Sourced from [[Pro Forma Construction Method]], [[Expense Normalization]], and [[T-12 and T-3 Analysis]]. Units: dollars per year.
- **Market capitalization rate:** The prevailing cap rate for comparable stabilized assets in the same submarket, asset class, and quality tier. Sourced from [[Comparable Sales (Sales Comps)]], broker surveys, CoStar/RCA market data. Units: percentage or decimal.

## Method

1. **Determine stabilized NOI.** Stabilized NOI is the property's projected income at market occupancy and rents, with normalized expenses, excluding non-recurring items and transition noise. See [[Stabilized NOI]] for the precise definition. If the property is already stabilized, the T-12 normalized actuals form the base. If the property is in lease-up or value-add, the stabilized NOI is a projection.

2. **Select the appropriate cap rate.** Pull comparable sales from the same submarket, asset class, and quality tier. Adjust for timing, size, quality differences, and market conditions to arrive at a supportable range. For the subject property, position within that range based on its specific attributes: location quality, lease term/credit, physical condition, market outlook. Cap rate ranges vary enormously by asset class, market, and cycle (broadly, institutional-quality assets in primary markets have traded at 3–6% for multifamily and industrial, 5–8% for office and retail, though these ranges shift materially with interest rate cycles; varies by market and vintage as of 2026-05-24). Be explicit about what is included vs. excluded from NOI when stating and applying the cap rate (reserves, management fees, leasing commissions).

3. **Calculate direct cap value.** Divide stabilized NOI by the selected cap rate.
   - Plain text: `Value = NOI / Cap Rate`
   - LaTeX: $$ V = \frac{NOI}{R} $$
   - Where: V = estimated property value (dollars); NOI = net operating income (dollars per year); R = capitalization rate (decimal, e.g., 0.055 for 5.5%).

4. **Compute implied cap rate on the bid price.** If a specific price is being evaluated, compute the going-in cap rate the price implies: Going-In Cap = NOI / Purchase Price. Compare to market cap rates to assess relative value.
   - Plain text: `Going-In Cap = NOI / Purchase Price`
   - LaTeX: $$ R_{going-in} = \frac{NOI}{P} $$

5. **Build a cap rate sensitivity table.** Because value is highly sensitive to cap rate selection, build a one-variable table showing value across a range of cap rates (e.g., the market range ±50 bps). A 50 bps move in cap rate on a 5.5% cap property changes value by approximately 9% — a material difference in a large transaction.

   | Cap Rate | Implied Value |
   |---|---|
   | 4.50% | $31.1M |
   | 5.00% | $28.0M |
   | 5.50% (base) | $25.5M |
   | 6.00% | $23.3M |
   | 6.50% | $21.5M |
   *(Illustrative figures only, based on hypothetical $1.4M NOI)*

## Outputs

Direct capitalization produces: (1) an estimated property value (the direct cap value); (2) the going-in cap rate implied by any target purchase price; (3) a sensitivity table of value vs. cap rate; and (4) a quick sanity check against comparable sales pricing.

## Example Walkthrough

*All figures below are illustrative and hypothetical — not derived from any real transaction.*

A 200-unit stabilized multifamily property has normalized stabilized NOI of $1,540,000 (after management fees, reserves, and all recurring expenses). Market cap rates for comparable stabilized multifamily in the submarket are observed at 5.00–5.50%, with institutional-quality assets trading at the tighter end. Base-case cap rate selected: 5.25%. Direct cap value: $1,540,000 / 0.0525 = $29,333,333. Per-unit: $29,333,333 / 200 = $146,667/unit. The seller is asking $30,500,000 — implying a going-in cap of $1,540,000 / $30,500,000 = 5.05%. The buyer's analysis indicates the seller is pricing the property at the tighter end of the cap range, offering limited spread over the comparable set. At the base-case cap of 5.25%, the bid value is $29.3M — an $1.2M gap vs. the ask.

## Limitations

Direct capitalization is a single-period method — it makes no explicit statement about income growth, hold period, or exit conditions. It implicitly assumes the income stream is stable and perpetual (or growing at a constant rate embedded in the cap rate selection). For properties with near-term income transitions (lease-up, renovations, major rollover), direct capitalization based on stabilized NOI requires explicit acknowledgment of the gap between current and stabilized income, and how long it takes to close that gap. In those cases, [[Discounted Cash Flow (DCF)]] analysis — which models the transition period explicitly — is more appropriate and should be used alongside direct capitalization.

The method is also highly sensitive to NOI definition and cap rate selection. Small adjustments to either produce large value swings. Two analysts with the same comparable sales can reasonably select cap rates that are 25–50 bps apart, producing a 5–10% value difference on a large asset. This is not a defect of the method but a feature: it forces the analyst to be explicit about their assumptions and justify them against the market evidence.

## Related Frameworks

[[Discounted Cash Flow (DCF)]] — the multi-period complement that models income transitions and is more appropriate for non-stabilized assets. [[Residual Land Value Method]] — applies the same capitalization concept to back-solve for land value in a development. [[Pro Forma Construction Method]] — produces the stabilized NOI that direct capitalization inputs. See also [[Cap Rate]], [[Going-In Cap Rate]], [[Exit Cap Rate]], and [[Stabilized NOI]].

## Sources

Appraisal Institute, *The Appraisal of Real Estate* (14th ed.) — Chapter 22, Direct Capitalization. CCIM Institute, *Financial Analysis for Commercial Investment Real Estate* (CI 102). CoStar and Real Capital Analytics market cap rate data methodology.
