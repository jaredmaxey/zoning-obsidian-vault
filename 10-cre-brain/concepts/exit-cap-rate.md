---
title: "Exit Cap Rate"
type: concept
tags: [cre/concepts]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Exit cap rate is the assumed capitalization rate applied to projected NOI at the end of a hold period to estimate the terminal sale price, and is typically the single largest driver of IRR sensitivity in a DCF model.
domain: concepts
formula: true
related:
  - "Going-In Cap Rate"
  - "Cap Rate"
  - "Net Operating Income (NOI)"
  - "Stabilized NOI"
  - "Internal Rate of Return (IRR)"
  - "Discounted Cash Flow (DCF)"
  - "Equity Multiple"
  - "Sensitivity Analysis"
  - "Exit Cap Rate Derivation"
---

# Exit Cap Rate

## Definition

The exit cap rate (also called the terminal cap rate, reversion cap rate, or going-out cap rate) is the capitalization rate assumed to be prevailing in the market at the end of the projected hold period, applied to the property's projected NOI at that future date to estimate the terminal (reversion) value. It is a critical underwriting assumption in any multi-period DCF model because the terminal value — the projected sale price — typically represents the single largest cash flow in the analysis, often comprising 50–70% of total equity proceeds in a 5–10 year hold. A change in exit cap rate assumption of just 50 basis points can swing levered IRR by 200–400 basis points on a typical deal.

Exit cap rates are necessarily speculative: they require predicting what buyers will pay for the property 5, 7, or 10 years into the future, in a market and capital environment that is unknowable today. Responsible underwriting treats the exit cap rate as a range assumption, sensitivity tests it, and applies a "premium" or "haircut" relative to the going-in cap rate based on the age progression of the asset, expected market conditions, and the risk that the exit environment is less favorable than today. See [[Exit Cap Rate Derivation]] for the methodological framework.

Most institutional underwriting conventions assume the exit cap rate is higher (more conservative) than the going-in cap rate — usually by 25–75 basis points — to reflect that (1) the building will be older at exit; (2) capital markets conditions may be less favorable; and (3) prudent conservatism is appropriate for a highly uncertain assumption. Underwriting that assumes an exit cap rate equal to or below the going-in cap rate requires strong justification (expected significant rent growth, a cap rate compression thesis) and will face skepticism from lenders and sophisticated equity investors.

## Formula

- Plain text: `Terminal Value = Exit-Year NOI / Exit Cap Rate`
- LaTeX: $$ \text{Terminal Value} = \frac{\text{NOI}_{\text{exit year}}}{\text{Exit Cap Rate}} $$

**Where:**
- **NOI_exit year** — the projected stabilized NOI in the year of disposition; typically modeled as the first full year of NOI following the projected sale date (year n+1 convention) to reflect the forward-looking nature of cap rate pricing
- **Exit Cap Rate** — the assumed prevailing market cap rate for comparable stabilized assets at the time of disposition

Net sale proceeds (the equity cash flow): `Net Proceeds = Terminal Value − Selling Costs − Loan Payoff`

## When It's Used

Exit cap rate is the terminal value assumption in every CRE DCF model. In a 5-year hold analysis, the year-5 (or year-6, depending on convention) NOI is divided by the exit cap rate to get the projected gross sale price. Selling costs (typically 1–2% of gross sale price for brokerage and closing) are deducted, the loan balance is repaid, and the net equity proceeds are the terminal cash flow in the IRR calculation.

Equity investors require the exit cap rate assumption to be disclosed and sensitivity-tested. Investment committees for fund managers and real estate allocators focus specifically on exit cap rate sensitivity: "what is the IRR if exit cap rates expand 50 bps? 100 bps?" — because small changes in this assumption dominate the return analysis. See [[Sensitivity Analysis]].

Lenders also assess exit cap rate assumptions when underwriting construction loans and bridge loans, because loan payoff depends on the borrower's ability to refinance or sell at a value that covers the outstanding balance. An overly optimistic exit cap rate assumption may mean the permanent loan or sale proceeds will not fully retire the construction loan.

## Variations & Edge Cases

**Year n vs. year n+1 NOI:** Some underwriters apply the exit cap rate to the current (holding period final year) NOI; others use the following year's projected NOI (the "forward year" convention), reflecting the fact that buyers price to their first full year of ownership. The forward year convention produces a modestly higher terminal value because it applies a growing NOI. Both conventions are used; consistency within a model and disclosure of the convention is important.

**Exit cap rate for value-add vs. core assets:** A value-add asset acquired at a discount to stabilized value may be underwritten with an exit cap rate equal to or close to market stabilized rates — reflecting that the asset will be a fully repositioned, Class B or B+ asset at exit. An aging core asset that will be 10 years older at exit may warrant a larger going-in to exit cap rate step-up.

**Portfolio vs. individual asset exit cap rate:** In portfolio dispositions, large institutional owners may achieve slight discounts to individual asset exit cap rates due to buyer portfolio-level synergies and reduced transaction costs per asset. Individual asset dispositions typically must assume single-asset buyer pricing.

## Common Mistakes

**Assuming the exit cap rate equals the going-in cap rate.** This is the most common aggressive assumption. A property bought at a 5.0% cap rate and underwritten to sell at a 5.0% cap rate in 7 years — with the asset now 7 years older and an uncertain market environment — is a pro forma that should raise red flags.

**Neglecting the NOI growth assumption in conjunction with the exit cap rate.** Even if the exit cap rate is higher, strong NOI growth can more than offset the cap rate expansion. Conversely, if NOI growth is assumed to be high (inflating the terminal year NOI) AND the exit cap rate is assumed to be low (applying a favorable multiple to that high NOI), the double-layered optimism creates fragile underwriting.

**Applying a single-point exit cap rate without sensitivity analysis.** Given the exit cap rate's outsized influence on IRR, presenting underwriting with only one exit cap rate scenario is insufficient for institutional analysis.

## Related Concepts

- [[Going-In Cap Rate]] — the acquisition-day cap rate; exit cap rate is typically set at a spread above going-in
- [[Cap Rate]] — the foundational concept from which exit cap rate is derived
- [[Net Operating Income (NOI)]] — the operating income basis for the terminal value calculation
- [[Stabilized NOI]] — the projected stabilized NOI applied at the exit
- [[Internal Rate of Return (IRR)]] — the total return metric most sensitive to exit cap rate assumptions
- [[Discounted Cash Flow (DCF)]] — the modeling framework that uses exit cap rate as the terminal value input
- [[Sensitivity Analysis]] — the tool used to test exit cap rate sensitivity
- [[Exit Cap Rate Derivation]] — the methodology for arriving at a defensible exit cap rate assumption

## Sources

Exit cap rate methodology is covered in CCIM's CI 101 and CI 102 courses, Geltner et al.'s *Commercial Real Estate Analysis and Investments*, and institutional equity underwriting standards from NCREIF-member firms and fund managers. Market cap rate and exit cap rate trends are published by CBRE, JLL, and NCREIF (varies by market and vintage; current as of 2026-05-24).
