---
title: "Discount Rate"
type: concept
tags: [cre/concepts]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: The discount rate is the required rate of return used to present-value future cash flows in a DCF model, reflecting the cost of capital and risk premium for a specific investment.
domain: concepts
formula: true
related:
  - "Internal Rate of Return (IRR)"
  - "Cap Rate"
  - "Weighted Average Cost of Capital (WACC)"
  - "Discounted Cash Flow (DCF)"
  - "Spread to Treasuries"
  - "Net Operating Income (NOI)"
  - "Exit Cap Rate"
  - "Sensitivity Analysis"
---

# Discount Rate

## Definition

The discount rate in CRE is the rate used to convert future cash flows — periodic NOI distributions and the terminal sale proceeds — into their equivalent present values. It represents the investor's required rate of return on the investment, incorporating the time value of money, the opportunity cost of capital, and a risk premium appropriate for the specific asset's risk profile. When you apply the discount rate to a series of future cash flows in a discounted cash flow (DCF) model, the resulting sum is the present value of the investment — if the present value exceeds the acquisition price, the investment provides a return above the required rate.

The discount rate is the "denominator" of value creation: a higher discount rate produces a lower present value for the same cash flow stream. In practical terms, institutional real estate discount rates reflect a risk-free base rate (typically the 10-year Treasury yield) plus a risk premium that incorporates illiquidity, leverage, asset quality, market conditions, and the management complexity of the investment. Changes in Treasury yields therefore directly affect real estate discount rates and values, all else equal — though the magnitude and timing of transmission to real asset prices depends on capital markets dynamics.

The discount rate is closely related to, but not identical to, the cap rate. In theory, the discount rate equals the cap rate plus the expected long-run NOI growth rate (Gordon Growth Model analog). In a zero-growth environment, cap rate and discount rate would converge; in markets with expected growth, the cap rate is lower than the discount rate by the expected growth premium investors are implicitly paying for. This relationship is formalized in the DCF framework where the yield (cap rate) is the first-year income return and the total return (discount rate) includes appreciation. See [[Discounted Cash Flow (DCF)]].

## Formula

**Relationship between Discount Rate, Cap Rate, and Growth:**
- Plain text: `Discount Rate ≈ Cap Rate + Long-Run NOI Growth Rate`
- LaTeX: $$ r \approx \text{Cap Rate} + g $$

**Net Present Value (discount rate as the required return):**
- Plain text: `NPV = Sum of [CF_t / (1 + r)^t] − Initial Investment`
- LaTeX:
$$
\text{NPV} = \sum_{t=1}^{n} \frac{CF_t}{(1+r)^t} - C_0
$$

**Where:**
- **r** — the discount rate (required rate of return)
- **CF_t** — cash flow in period t (operating cash flows plus terminal value in year n)
- **n** — number of periods in the hold
- **C_0** — initial investment (acquisition price + transaction costs)
- **g** — expected long-run NOI growth rate

If NPV > 0, the investment earns more than the required return (r); if NPV < 0, it earns less. When NPV = 0, r equals the IRR.

## When It's Used

Discount rates are used explicitly in DCF models to compute NPV and implicitly in cap rate pricing because investors' required returns are embedded in the market-clearing cap rates they accept. In formal DCF underwriting, the analyst inputs their required return (the discount rate) and solves for NPV to determine whether the acquisition price is justified given their return requirement. More commonly in CRE, the analyst inputs all cash flows and solves for IRR — which is the implicit discount rate at which NPV equals zero.

Appraisers use discount rates explicitly in DCF valuations under the income approach: they derive a market discount rate from comparable sales data and investor surveys, apply it to the projected cash flows, and sum the present values to estimate market value. The Appraisal Institute publishes periodic investor surveys tracking discount rates by property type and investor category.

For development feasibility, the discount rate used to evaluate a development project should reflect the higher risk of development (construction execution, lease-up uncertainty) relative to a stabilized acquisition. Development discount rates are typically set 200–400 basis points above stabilized acquisition discount rates to reflect this incremental risk.

## Variations & Edge Cases

**Levered vs. unlevered discount rate:** Like IRR, the discount rate can be applied on a levered basis (to equity cash flows only) or an unlevered basis (to property-level cash flows treating the project as all-cash). The levered discount rate equals the equity cost of capital; the unlevered rate is a blended measure closer to WACC. See [[Weighted Average Cost of Capital (WACC)]].

**Nominal vs. real discount rate:** Most CRE underwriting uses nominal discount rates (not adjusted for inflation), applied to nominal (non-inflation-adjusted) cash flows. This is consistent as long as both the discount rate and cash flows use the same inflation convention.

**Discount rate vs. required return vs. hurdle rate:** These terms are used interchangeably in some contexts. Formally: the discount rate is the rate applied in present value calculations; the required return is the investor's minimum acceptable return; the hurdle rate in a waterfall structure is the preferred return threshold. In practice, they are often set to the same value in underwriting.

Institutional discount rates for stabilized CRE assets range from approximately 6–10%+ depending on asset class, quality, leverage, and market conditions (unlevered); levered equity discount rates are higher. All figures are sensitive to interest rate environment (varies by market and vintage; current as of 2026-05-24).

## Common Mistakes

**Circular reasoning: using IRR to set the discount rate.** The discount rate should be set exogenously based on required returns and market risk premiums, not derived from the IRR of the deal being evaluated. Using the IRR of the target deal as its own discount rate produces a circular and uninformative NPV of zero.

**Using the same discount rate for all risk profiles.** A stabilized core asset and a ground-up development project in the same market have very different risk profiles. Applying the same discount rate to both conflates fundamentally different investments.

**Ignoring the interest rate environment.** Discount rates are anchored to risk-free rates. A discount rate that was appropriate in a 2% Treasury environment may be below market in a 5% Treasury environment, producing a present value that overstates true market value.

## Related Concepts

- [[Internal Rate of Return (IRR)]] — the break-even discount rate (rate at which NPV = 0); the primary output of CRE DCF analysis
- [[Cap Rate]] — the income yield component of the discount rate; discount rate = cap rate + expected growth
- [[Weighted Average Cost of Capital (WACC)]] — the blended cost of capital used as a project-level discount rate
- [[Discounted Cash Flow (DCF)]] — the analytical framework that uses the discount rate as its core input
- [[Spread to Treasuries]] — the risk premium component of the discount rate above the risk-free rate
- [[Sensitivity Analysis]] — used to test how NPV and IRR vary with discount rate assumptions

## Sources

Discount rate methodology is covered in Geltner et al.'s *Commercial Real Estate Analysis and Investments*, Brealey/Myers/Allen's corporate finance texts, and CCIM's advanced valuation curriculum. Investor survey discount rates are published by the Appraisal Institute and PwC Real Estate Investor Survey. All rates are market- and cycle-dependent (varies by market and vintage; current as of 2026-05-24).
