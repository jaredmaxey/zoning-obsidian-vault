---
title: "Discounted Cash Flow (DCF)"
aliases: ["Discounted Cash Flow (DCF)"]
type: framework
tags: [cre/underwriting, cre/frameworks]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Multi-period valuation and return analysis method that discounts projected property cash flows and terminal value to their present value, producing NPV and IRR.
inputs_required:
  - Year-by-year projected NOI and cash flows (from pro forma)
  - Discount rate (risk-adjusted required return)
  - Hold period
  - Exit cap rate (for terminal value)
  - Acquisition price or equity investment (initial outflow)
  - Financing terms (for levered analysis)
outputs:
  - Net Present Value (NPV) — at the discount rate
  - Unlevered and levered Internal Rate of Return (IRR)
  - Equity Multiple
  - Maximum supportable acquisition price (bid price at target IRR)
related:
  - "Direct Capitalization"
  - "Pro Forma Construction Method"
  - "Sensitivity Analysis"
  - "Stress Testing"
  - "Internal Rate of Return (IRR)"
  - "Equity Multiple"
  - "Discount Rate"
  - "Exit Cap Rate"
  - "Weighted Average Cost of Capital (WACC)"
  - "Net Operating Income (NOI)"
  - "Stabilized NOI"
  - "Cash-on-Cash Return"
---

# Discounted Cash Flow (DCF)

## Purpose

The Discounted Cash Flow model is the primary multi-period valuation and return framework for CRE investment analysis. Rather than capitalizing a single stabilized income figure (the [[Direct Capitalization]] approach), the DCF models a full projection of annual cash flows across the expected hold period, plus a terminal value at sale, and discounts all of those cash flows back to a present value using a risk-adjusted discount rate. The result is either an NPV (positive NPV means the asset at the stated price meets the required return) or an IRR (the actual return generated at the stated acquisition price).

The DCF is the preferred method when the income stream is not yet stabilized, is expected to change materially over the hold period, or when the analyst wants to explicitly model lease rollover, capital events, or the time path of returns rather than assuming a perpetual, steady-state income. For institutional equity underwriting, the DCF is the definitive return analysis framework — every investment committee presentation leads with levered IRR and equity multiple derived from the DCF. For lender underwriting, the DCF (unlevered) confirms the asset has sufficient value to support the loan across all periods.

## Inputs Required

- **Annual net operating income projections:** From [[Pro Forma Construction Method]], year 1 through year N of the hold period. Units: dollars.
- **Annual debt service:** Principal and interest on the senior (and any mezzanine) debt, drawn from the financing terms. Units: dollars.
- **Capital expenditures:** Renovation budget, TI and LC reserves, and ongoing CapEx by year. Units: dollars.
- **Terminal value:** Exit cap rate applied to Year N+1 NOI, minus transaction costs (typically 1.0–2.0% of gross proceeds). Units: dollars.
- **Discount rate:** Risk-adjusted required return on equity (for levered analysis) or on the asset (for unlevered analysis). Often referenced as [[Discount Rate]] or compared to [[Weighted Average Cost of Capital (WACC)]]. Units: percentage.
- **Hold period:** Typically 3–10 years for institutional CRE; the most common underwriting hold is 5 years (varies by strategy and market cycle).
- **Initial equity investment:** Acquisition price minus loan proceeds (plus closing costs and initial capex funded at close).

## Method

1. **Build the annual cash flow projection.** The pro forma (see [[Pro Forma Construction Method]]) produces EGI, NOI, and net cash flow for each year of the hold. Label Year 0 as the acquisition date (negative cash flow = equity invested).

2. **Compute annual before-tax levered cash flow (BTCF).** For each hold-period year:
   - Plain text: `BTCF = NOI − Debt Service − CapEx`
   - LaTeX: $$ BTCF_t = NOI_t - ADS_t - CapEx_t $$
   - Where: BTCF_t = before-tax levered cash flow in year t; NOI_t = net operating income; ADS_t = annual debt service; CapEx_t = capital expenditures.

3. **Estimate the terminal value at end of hold.** Apply the exit cap rate to the projected Year N+1 NOI:
   - Plain text: `Terminal Value = NOI(N+1) / Exit Cap Rate`
   - LaTeX: $$ TV = \frac{NOI_{N+1}}{R_{exit}} $$
   Net sale proceeds = TV minus transaction costs minus remaining loan payoff = net equity reversion.

4. **Construct the cash flow stream.** Combine: Year 0: −equity invested. Years 1 through N: BTCF_t. Year N: BTCF_N + net equity reversion.

5. **Compute NPV at the discount rate.** Discount each period's cash flow at the required return rate:
   - Plain text: `NPV = Σ [CF_t / (1 + r)^t]`
   - LaTeX: $$ NPV = \sum_{t=0}^{N} \frac{CF_t}{(1+r)^t} $$
   - Where: CF_t = cash flow in period t; r = discount rate (decimal); t = period (0 = today). Positive NPV indicates the deal meets or exceeds the required return at the stated price.

6. **Compute IRR.** The IRR is the discount rate that sets NPV = 0. Computed using Excel's IRR() function or equivalent. Both unlevered IRR (using NOI and unlevered terminal value, no debt) and levered IRR (using BTCF and equity reversion) should be reported. Unlevered IRR benchmarks the asset's inherent return independent of financing; levered IRR reflects the return to equity.
   - LaTeX: $$ \sum_{t=0}^{N} \frac{CF_t}{(1+IRR)^t} = 0 $$

7. **Compute equity multiple.** Total equity distributions (all period cash flows and reversion, summed undiscounted) divided by total equity invested.
   - Plain text: `Equity Multiple = Total Equity Distributions / Total Equity Invested`
   - LaTeX: $$ EM = \frac{\sum_{t=1}^{N} CF_t^+}{|CF_0|} $$

8. **Back-solve for the maximum bid price.** Set NPV = 0 and solve for the Year 0 equity investment that produces the target IRR. This is the maximum supportable equity price at the required return.

## Outputs

The DCF produces: (1) annual BTCF for each year of the hold; (2) net equity reversion at sale; (3) unlevered and levered IRR; (4) equity multiple; (5) NPV at the required return (positive = buys meeting hurdle); and (6) a maximum supportable bid price at the target return. These outputs feed directly into [[Sensitivity Analysis]] and [[Stress Testing]].

## Example Walkthrough

*All figures below are illustrative and hypothetical — not derived from any real transaction.*

A 5-year hold value-add multifamily acquisition. Year 0 equity: −$8,500,000. Annual BTCF (levered, after debt service and CapEx): Year 1 $220k, Year 2 $315k, Year 3 $410k, Year 4 $490k, Year 5 $555k. Year 5 exit: $1,540,000 stabilized NOI × (1.025 rent growth) / 6.0% exit cap = $26,167,000 gross; minus $393k transaction costs; minus $15,000k loan payoff = $10,774,000 net equity reversion. Total Year 5 cash flow: $555k + $10,774k = $11,329,000. Cash flow stream: −$8,500k, $220k, $315k, $410k, $490k, $11,329k. Levered IRR = approximately 13.8% (illustrative). Equity multiple = ($220k+$315k+$410k+$490k+$11,329k) / $8,500k = 1.50×.

## Limitations

The DCF is highly sensitive to the exit cap rate and the rent growth assumptions embedded in the terminal year NOI — together these two inputs drive the majority of levered IRR in most deals. A disciplined analyst always pairs the DCF with a sensitivity analysis on these two variables per [[Sensitivity Analysis]]. The DCF also assumes cash flows are reinvested at the IRR, which may overstate returns in high-IRR environments — equity multiple is a more stable companion metric. Finally, the DCF is a deterministic model; it does not capture outcome uncertainty without [[Sensitivity Analysis]] or [[Monte Carlo in CRE]] overlays.

## Related Frameworks

[[Direct Capitalization]] — the single-period simplification; the DCF's terminal value IS a direct capitalization of the exit year NOI. [[Pro Forma Construction Method]] — provides the annual cash flows. [[Sensitivity Analysis]] — the required companion for DCF output. See also [[Internal Rate of Return (IRR)]], [[Equity Multiple]], [[Discount Rate]], and [[Exit Cap Rate]].

## Sources

Geltner et al., *Commercial Real Estate Analysis and Investments* (3rd ed.) — Chapters 8–10. CCIM Institute, *Financial Analysis for Commercial Investment Real Estate* (CI 101/102). Appraisal Institute, *The Appraisal of Real Estate* (14th ed.).
