---
title: "Going-In Cap Rate"
aliases: ["Going-In Cap Rate"]
type: concept
tags: [cre/concepts]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Going-in cap rate is the capitalization rate implied by the acquisition price relative to year-one or stabilized NOI, establishing the entry pricing benchmark and the starting point for hold-period return analysis.
domain: concepts
formula: true
related:
  - "Cap Rate"
  - "Exit Cap Rate"
  - "Net Operating Income (NOI)"
  - "Stabilized NOI"
  - "Yield on Cost"
  - "Direct Capitalization"
  - "Discounted Cash Flow (DCF)"
  - "Spread to Treasuries"
---

# Going-In Cap Rate

## Definition

The going-in cap rate is the capitalization rate implied by the acquisition price divided by the property's NOI at or near the time of acquisition — either year-one pro forma NOI or in-place stabilized NOI, depending on the underwriting convention. It establishes the entry pricing point for the investment: how much income yield the investor is "buying" relative to the price paid. The going-in cap rate is distinguished from the [[Exit Cap Rate]], which is the assumed prevailing cap rate at disposition, and from the overall market cap rate, which is the average rate across all recent comparable transactions.

The going-in cap rate is the first number investors and brokers use to locate an asset on the risk-return spectrum. A low going-in cap rate (say, 4.0–4.5%) signals that the buyer is paying a high price relative to current income — implying high expected rent growth, low perceived risk, a value-add or development thesis, or simply aggressive pricing by a motivated buyer. A high going-in cap rate (say, 7.0–8.0%) implies the opposite: the buyer is receiving more income per dollar invested, which typically reflects higher risk (property condition, market quality, tenant credit, lease term), or a buyer who is acquiring at an opportunistic discount.

Going-in cap rates are the primary language of CRE deal marketing. Brokers "quote" deals in terms of going-in cap rates, and buyers screen acquisitions against their fund's minimum going-in cap rate hurdle. Institutional core funds typically have lower going-in cap rate floors (they accept lower current yields for more stable, lower-risk assets); value-add and opportunistic funds focus more on total return IRR and may underwrite to low going-in cap rates because they expect NOI growth to significantly increase the stabilized cap rate relative to the acquisition price.

## Formula

- Plain text: `Going-In Cap Rate = Year-One NOI / Acquisition Price`
- LaTeX: $$ \text{Going-In Cap Rate} = \frac{\text{Year-One NOI}}{\text{Acquisition Price}} $$

**Where:**
- **Year-One NOI** — projected NOI for the first full year of ownership (forward NOI); some investors use in-place stabilized NOI instead (see Variations)
- **Acquisition Price** — the agreed purchase price; in deals with significant closing costs or immediate capex, some underwriters use total acquisition cost (price + fees + immediate capex) as the denominator

## When It's Used

Going-in cap rate is used in the initial acquisition screening to answer: "is this deal priced at a cap rate that makes sense for our fund's mandate?" Core and core-plus funds compare going-in cap rates against their target yield thresholds; if the going-in cap rate is too low, the deal doesn't clear the investment committee's minimum unlevered yield test.

In financing, going-in cap rate is used by lenders as a signal of deal quality and value cushion. A going-in cap rate well above the relevant Treasury spread signals a conservative purchase price relative to income; a going-in cap rate compressed toward (or below) the lender's required debt yield signals aggressive pricing that leaves little room for NOI decline.

Going-in cap rate also sets up the development spread analysis for new construction: if developers are building at a 150 bps spread over stabilized market going-in cap rates, and the market going-in cap rate tightens (buyers pay more per dollar of NOI), the spread narrows and development incentive weakens. See [[Yield on Cost]] and [[Development Spread]].

## Variations & Edge Cases

**In-place vs. forward NOI basis:** Some practitioners use trailing 12-month actual NOI (T-12) in the denominator; others use year-one forward pro forma NOI. For fully stabilized assets with little change, these are nearly identical. For assets with significant lease-up, rent escalations kicking in at year one, or near-term lease expirations, the choice of NOI basis materially affects the stated cap rate. Always clarify which basis is used.

**Stabilized vs. in-place cap rate for value-add:** On a value-add acquisition at 75% occupancy, the going-in cap rate on current (in-place) NOI will be lower than the "stabilized going-in cap rate" that the buyer is underwriting toward. Buyers typically present both: "we are buying at a 4.5% in-place cap rate, and expect a 6.5% stabilized cap rate after repositioning."

**Gross vs. net going-in cap rate:** Rare, but some market participants quote going-in cap rates on gross scheduled income (before expenses). This is non-standard in the U.S. and generally not used in institutional analysis.

Going-in cap rates by asset class and market vary significantly. As of 2026-05-24, institutional quality assets trade across a wide range based on asset class, location, and capital markets conditions (varies by market and vintage).

## Common Mistakes

**Accepting the broker's stated going-in cap rate without verifying the NOI.** Brokers sometimes present the most favorable NOI (forward pro forma, normalized for below-market leases, inflated other income) to produce the lowest possible cap rate for comparison purposes. Buyers must independently underwrite NOI.

**Comparing going-in cap rates across different NOI definitions.** A deal quoted at a 5.5% cap rate on T-12 NOI and another at 5.5% on forward pro forma NOI are not equivalent — the forward NOI deal is effectively priced lower (you're paying more for future income, not current income).

**Ignoring the relationship to interest rates.** Going-in cap rates are anchored to prevailing interest rates via the Treasury spread; a cap rate that was conservative in a low-rate environment may be thin in a rising-rate environment. Always evaluate going-in cap rate relative to current debt cost and spread. See [[Spread to Treasuries]].

## Related Concepts

- [[Cap Rate]] — the foundational concept; going-in cap rate is the acquisition-day application
- [[Exit Cap Rate]] — the assumed cap rate at disposition; paired with going-in cap rate to define the investment thesis
- [[Net Operating Income (NOI)]] — the numerator in the going-in cap rate formula
- [[Stabilized NOI]] — the normalized income basis used to compute the stabilized going-in cap rate
- [[Yield on Cost]] — the development analog; stabilized YOC compared to the market going-in cap rate defines development spread
- [[Direct Capitalization]] — the valuation method that inverts the going-in cap rate to produce a value estimate
- [[Spread to Treasuries]] — the risk premium embedded in going-in cap rates relative to risk-free rates

## Sources

Going-in cap rate methodology is addressed in CCIM's income property analysis curriculum, Geltner et al.'s *Commercial Real Estate Analysis and Investments*, and broker research from CBRE, JLL, and CoStar. Market cap rate surveys are published quarterly by major CRE research firms. Specific cap rates vary by asset class, submarket, and market cycle (varies by market and vintage; current as of 2026-05-24).
