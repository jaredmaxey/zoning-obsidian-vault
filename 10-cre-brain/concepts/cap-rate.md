---
title: "Cap Rate"
type: concept
tags: [cre/concepts]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Capitalization rate expresses a property's annual NOI as a percentage of its value, serving as the primary pricing and return benchmark in CRE.
domain: concepts
formula: true
related:
  - "Net Operating Income (NOI)"
  - "Going-In Cap Rate"
  - "Exit Cap Rate"
  - "Yield on Cost"
  - "Discount Rate"
  - "Direct Capitalization"
  - "Stabilized NOI"
  - "Spread to Treasuries"
---

# Cap Rate

## Definition

The capitalization rate (cap rate) is the ratio of a property's net operating income (NOI) to its market value or acquisition price, expressed as a percentage. It is the single most widely cited metric in commercial real estate pricing, functioning simultaneously as a valuation shorthand, a return proxy, and a market sentiment indicator. When a buyer pays a low cap rate, they are paying a high price relative to current income — implying an expectation of income growth, low risk, or both.

Cap rates compress (fall) when capital floods into real estate or when the risk-adjusted premium investors demand over alternatives (Treasuries, corporate bonds) narrows. They expand (rise) when credit tightens, interest rates rise, or perceived property risk increases. Understanding cap rate movements is therefore inseparable from understanding macro capital markets conditions. As of 2026-05-24, cap rates for institutional-quality assets vary considerably by asset class and submarket — see [[Spread to Treasuries]] for the risk premium context.

Cap rates differ conceptually from cash-on-cash returns and IRRs: the cap rate ignores financing, capital expenditures beyond normal operations, and the time value of money over a hold period. It is a point-in-time, unlevered income yield, not a total-return measure.

## Formula

- Plain text: `Cap Rate = NOI / Property Value`
- LaTeX: $$ \text{Cap Rate} = \frac{\text{NOI}}{\text{Property Value}} $$

**Where:**
- **NOI** — Net Operating Income: annual gross revenue less all operating expenses, before debt service and capital expenditures. Can be trailing (T-12 actuals) or forward (pro forma). See [[Net Operating Income (NOI)]].
- **Property Value** — current market value or acquisition price (gross, before financing costs).

The formula inverts to solve for value: `Value = NOI / Cap Rate`. This inversion is how the [[Direct Capitalization]] valuation method works — divide stabilized NOI by the market cap rate to derive a value indication.

## When It's Used

Cap rates anchor acquisition underwriting: buyers convert a target acquisition price into a cap rate and compare it against market-clearing rates for similar assets. Lenders use the going-in cap rate to assess whether leverage is accretive and whether stabilized cash flow supports debt service. Appraisers use cap rates derived from comparable sales to value income-producing properties under the income approach.

Brokers and sellers use cap rates to price listings and market assets. Institutional equity investors (core and core-plus funds) often set minimum unlevered yield thresholds expressed as cap rates. Development underwriters compare the expected stabilized cap rate (yield on cost) against market acquisition cap rates to assess development spread and feasibility — see [[Yield on Cost]] and [[Development Spread]].

## Variations & Edge Cases

**Going-in vs. exit cap rate:** The going-in cap rate is applied to in-place or near-term stabilized NOI at acquisition. The exit (terminal) cap rate is the assumed rate applied to projected NOI at disposition. See [[Going-In Cap Rate]] and [[Exit Cap Rate]].

**Trailing vs. forward NOI:** Some markets and brokers quote cap rates on trailing twelve-month (T-12) actuals; others quote on year-one pro forma. The distinction can be material on value-add assets where current NOI is suppressed. Always clarify which NOI basis is used.

**Gross vs. net cap rate:** A small minority of markets (some retail leases, some international practice) define cap rates on gross income before expenses. Institutional U.S. practice is always net (NOI-based).

**Stabilized vs. in-place:** For assets with lease-up vacancy, an "in-place" cap rate reflects current partial occupancy; a "stabilized" cap rate assumes normal market occupancy. These can diverge by 100–200 bps on a value-add deal.

Cap rates vary materially by asset class, submarket quality, and vintage. As of 2026-05-24, institutional-quality multifamily in gateway markets, industrial in logistics hubs, and Class A office in trophy locations trade at materially different cap rates — all figures should be treated as ranges (varies by market and vintage).

## Common Mistakes

**Applying cap rates to non-stabilized NOI without disclosure.** Presenting a cap rate on depressed in-place NOI as equivalent to a market cap rate misleads counterparties. Always state the NOI basis.

**Ignoring capital expenditure requirements.** A 6.0% cap rate looks different if the property requires $5M of near-term capex. Cap rate alone is a pre-capex metric; adjust for required investment when comparing assets.

**Confusing cap rate with cash-on-cash return.** Cash-on-cash return reflects levered, after-debt-service cash flow relative to equity invested. Cap rate is unlevered. At low leverage, these can be similar; at high leverage with positive spread, cash-on-cash will significantly exceed cap rate.

**Extrapolating a single comp.** One transaction may reflect a motivated seller, buyer synergies, or unusual financing. Cap rate conclusions should be based on a cluster of comparable sales, not a single data point.

## Related Concepts

- [[Net Operating Income (NOI)]] — the numerator; quality of NOI drives cap rate reliability
- [[Going-In Cap Rate]] — the acquisition-day application
- [[Exit Cap Rate]] — the disposition assumption in a DCF model
- [[Yield on Cost]] — development analog to cap rate
- [[Discount Rate]] — the total-return rate used in DCF; incorporates but differs from the cap rate
- [[Direct Capitalization]] — the valuation method that applies a cap rate to stabilized NOI
- [[Stabilized NOI]] — the NOI basis most commonly used in cap rate calculations
- [[Spread to Treasuries]] — frames cap rates relative to risk-free rates

## Sources

Cap rate methodology is covered in depth in CCIM Institute's *CI 101: Financial Analysis for Commercial Investment Real Estate* and the Appraisal Institute's *The Appraisal of Real Estate* (15th ed.). NCREIF, CBRE, JLL, and CoStar publish periodic cap rate surveys by asset class and market. Market figures should be validated against current broker surveys or appraisal comp sets (varies by market and vintage; current as of 2026-05-24).
