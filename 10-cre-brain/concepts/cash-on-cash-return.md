---
title: "Cash-on-Cash Return"
type: concept
tags: [cre/concepts]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Cash-on-cash return measures annual pre-tax cash flow after debt service as a percentage of equity invested, capturing the current-period levered income yield on a real estate investment.
domain: concepts
formula: true
related:
  - "Cap Rate"
  - "Net Operating Income (NOI)"
  - "Internal Rate of Return (IRR)"
  - "Equity Multiple"
  - "Debt Service Coverage Ratio (DSCR)"
  - "Effective Gross Income (EGI)"
  - "Waterfall Structures and Promote"
  - "Preferred Return Mechanics"
---

# Cash-on-Cash Return

## Definition

Cash-on-cash return (CoC) is the ratio of a property's annual pre-tax cash flow — after all operating expenses and debt service, but before depreciation, taxes, and principal paydown — to the equity capital invested at acquisition or completion. It answers the immediate income question: "for every dollar of equity I put in, how many cents do I receive in distributable cash each year?" Unlike IRR or equity multiple, it is a single-period metric focused on current yield rather than total return over the hold.

Cash-on-cash is a levered metric: the presence and cost of debt directly affects the outcome. Positive leverage (when the cap rate exceeds the mortgage constant) amplifies cash-on-cash above the unlevered cap rate; negative leverage (when the mortgage constant exceeds the cap rate, as often occurs in high-rate environments) compresses or inverts it. This leverage sensitivity makes cash-on-cash a useful stress-test: if interest rates rise or NOI falls, does the property still generate positive cash flow?

For income-focused investors — private high-net-worth buyers, 1031 exchange buyers, and some institutional core funds with distribution requirements — a minimum cash-on-cash threshold is a hard underwriting criterion. For value-add and development deals where current cash flow is suppressed during renovation or lease-up, cash-on-cash in early years may be low or negative, and total return is better captured by [[Internal Rate of Return (IRR)]] and [[Equity Multiple]].

## Formula

- Plain text: `Cash-on-Cash Return = Annual Pre-Tax Cash Flow / Total Equity Invested`
- LaTeX: $$ \text{CoC} = \frac{\text{Annual Pre-Tax Cash Flow}}{\text{Total Equity Invested}} $$

**Where:**
- **Annual Pre-Tax Cash Flow** — effective gross income minus operating expenses minus annual debt service (principal + interest). Also called "before-tax cash flow" (BTCF). Does not deduct depreciation or income taxes.
- **Total Equity Invested** — the cash equity deployed: down payment, closing costs, capital reserves contributed at closing, and any funded reserves held back from the loan. Excludes the loan principal.

The calculation is typically run year-by-year over the hold period, producing a CoC profile. In early value-add years, CoC may be near zero or negative; in stabilized years it should reflect market-rate levered yield.

## When It's Used

Cash-on-cash return is used at the acquisition stage to evaluate whether an income property generates adequate current distributions to meet investor expectations. Private equity sponsors compare projected year-one CoC against investor preferred return hurdles — a deal that does not cover the preferred return in year one will require cash management or investor communication about the ramp-up period. See [[Preferred Return Mechanics]].

Lenders, while not using CoC directly, are interested in the same underlying cash flow: [[Debt Service Coverage Ratio (DSCR)]] is essentially NOI divided by debt service, and CoC and DSCR move in tandem. A deal with a healthy DSCR will generally produce a positive CoC, though DSCR is on NOI (pre-equity distributions) while CoC is on levered cash flow (post-debt service, pre-tax).

In portfolio management, year-over-year CoC trends reveal whether a stabilized asset's income performance is improving or deteriorating — a declining CoC may signal rising expenses, rent roll erosion, or the onset of deferred maintenance.

## Variations & Edge Cases

**Before-tax vs. after-tax:** Most institutional underwriting uses before-tax cash flow. Some individual investor analysis applies tax benefits (depreciation shelter, interest deduction) to produce an after-tax CoC, which is higher but investor-specific.

**Year-one vs. stabilized:** Quoting year-one CoC on a value-add deal can be misleading if the asset is in renovation or lease-up. Stabilized-year CoC (typically year 2–3 in a value-add model) is more representative of the income yield the investor will receive during the hold.

**Equity basis changes:** If the sponsor refinances and returns equity capital, the denominator changes — the same cash flow is now divided by less equity, so CoC appears to improve. This is mechanically accurate but reflects capital structure change, not operating improvement.

Cash-on-cash return hurdles for stabilized assets vary considerably by asset class, leverage level, and market. As of 2026-05-24, ranges in institutional deals span from near zero (core assets with thin leverage) to mid-single digits for higher-leveraged core-plus acquisitions (varies by market and vintage).

## Common Mistakes

**Confusing CoC with cap rate.** Cap rate is unlevered and pre-financing; CoC is levered and post-debt-service. They are related but measure different things. On an all-cash purchase, CoC equals the cap rate.

**Using NOI as the numerator instead of after-debt-service cash flow.** NOI is the correct numerator for cap rate. Cash-on-cash requires subtracting debt service; using NOI overstates CoC on any leveraged deal.

**Ignoring equity contributed over time.** On development deals with equity contributions staged over the construction period (equity draws), the denominator at any point in time is the cumulative invested equity, not the total committed amount.

**Treating CoC as a total return metric.** A 6% year-one CoC says nothing about appreciation, principal paydown, or terminal value. CoC must be read alongside IRR and equity multiple for a complete picture.

## Related Concepts

- [[Cap Rate]] — the unlevered analog; CoC exceeds cap rate with positive leverage
- [[Net Operating Income (NOI)]] — the pre-financing income that drives cash flow available for debt service and equity distributions
- [[Internal Rate of Return (IRR)]] — the time-weighted total return measure that captures appreciation and terminal value
- [[Equity Multiple]] — the total return scalar that pairs with IRR to fully characterize deal economics
- [[Debt Service Coverage Ratio (DSCR)]] — lender's version of the income-to-debt coverage test
- [[Effective Gross Income (EGI)]] — the top-line revenue from which operating expenses and debt service are deducted
- [[Waterfall Structures and Promote]] — how CoC-based cash flows are allocated between LP and GP
- [[Preferred Return Mechanics]] — the hurdle rate CoC must often clear before promote kicks in

## Sources

Cash-on-cash methodology is covered in CCIM's *CI 101* and Linneman's *Real Estate Finance and Investments*. Specific return hurdles vary by fund mandate, leverage, and market cycle (varies by market and vintage; current as of 2026-05-24).
