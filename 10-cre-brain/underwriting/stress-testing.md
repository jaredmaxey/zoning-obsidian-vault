---
title: "Stress Testing"
type: framework
tags: [cre/underwriting, cre/frameworks]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Application of defined adverse scenarios to a CRE pro forma to test whether a deal survives downturns in income, occupancy, or capital markets without breaching covenants or losing capital.
inputs_required:
  - Base-case pro forma
  - Defined stress scenarios (e.g., GFC-level rent decline, COVID occupancy shock)
  - Loan covenants and DSCR triggers
  - Equity loss threshold
outputs:
  - Cash flow and DSCR under each stress scenario
  - Debt covenant compliance status under stress
  - Maximum tolerable income decline before loan default or equity loss
  - Equity cushion and loss severity under bear scenarios
related:
  - "Sensitivity Analysis"
  - "Monte Carlo in CRE"
  - "Pro Forma Construction Method"
  - "Assumption Hierarchy: Actual vs. Pro Forma"
  - "Debt Service Coverage Ratio (DSCR)"
  - "Loan-to-Value (LTV)"
  - "Loan-to-Cost (LTC)"
  - "Internal Rate of Return (IRR)"
  - "Exit Cap Rate"
  - "Discount Rate"
---

# Stress Testing

## Purpose

Stress testing applies defined adverse scenarios — rather than just ranging individual variables — to a CRE underwriting model to evaluate whether the investment structure survives material negative outcomes. The distinction from [[Sensitivity Analysis]] is intent: sensitivity analysis maps the return surface across a continuous range of inputs; stress testing applies specific, plausible downside scenarios to answer a binary question — does the deal survive, and if not, what is the loss?

The scenarios used in stress testing are typically calibrated to historical market dislocations: the 2008–2009 GFC (peak-to-trough commercial real estate value declines of 30–45% in many submarkets), the 2020 COVID shock (hotel occupancy dropped to single digits in many markets; retail collected a fraction of rents), regional downturns tied to major employer exits, or rising interest rate environments that impair exit values. Lenders apply stress tests to ensure debt remains serviceable under adverse conditions; equity sponsors apply stress tests to evaluate the probability of equity impairment and to size the equity cushion appropriately.

## Inputs Required

- **Base-case pro forma with explicit debt terms:** Loan amount, interest rate (fixed or floating), amortization, DSCR covenant, LTV covenant, and maturity date. See [[Pro Forma Construction Method]].
- **Defined stress scenarios:** Each scenario should specify the income shock (% decline in revenue or NOI), the duration of the shock, and any recovery trajectory. Examples: 20% NOI decline sustained for 2 years; NOI drops 30% in Year 1, recovers at 5%/year; occupancy falls to 70% for 18 months.
- **Capital markets stress assumptions:** Higher exit cap rates, higher refinancing rates, or a frozen transaction market during the stress period.
- **Loan covenant thresholds:** DSCR trigger for a cash trap or technical default; LTV triggers for additional equity cure requirements.

## Method

1. **Define 2–4 named stress scenarios.** At minimum: a "moderate stress" scenario and a "severe stress" scenario. Examples: (a) Moderate — NOI declines 15% from base in Year 1 and recovers over 3 years; exit cap expands 75 bps from base. (b) Severe — NOI declines 30% and does not recover to base until Year 4; exit cap expands 150 bps; refinancing at loan maturity requires a capital cure. Each scenario should be anchored to a historical analogue or lender downside requirement.

2. **Apply income shock to the pro forma.** Override the base-case revenue growth and vacancy assumptions with the stress scenario inputs for each period. For debt-focused stress tests, use a flat or declining NOI path that persists for the scenario's defined duration.

3. **Calculate DSCR under stress.** Compute NOI divided by annual debt service for each year of the hold.
   - Plain text: `DSCR = NOI / Annual Debt Service`
   - LaTeX: $$ DSCR = \frac{NOI}{ADS} $$
   - Where: DSCR = debt service coverage ratio; NOI = net operating income; ADS = annual debt service (principal + interest). Flag any year where DSCR drops below the loan covenant threshold (typically 1.20–1.25× for stabilized assets; varies by lender and loan type as of 2026-05-24).

4. **Calculate implied value and LTV under stress.** Apply the stress scenario exit cap rate to the depressed NOI to compute a stressed property value. Compare to the outstanding loan balance to determine LTV under stress. Flag any year where stressed LTV exceeds the loan covenant (typically 70–80%; varies by lender and asset class as of 2026-05-24).
   - Plain text: `Stressed LTV = Loan Balance / (Stressed NOI / Stress Exit Cap)`
   - LaTeX: $$ LTV_{stress} = \frac{Loan\:Balance}{NOI_{stress} / Cap_{exit,stress}} $$

5. **Assess equity outcome under stress.** Model the equity cash flows (distributions received pre-stress, distributions during the stress period, and net sale proceeds at the stressed exit value) to compute the equity IRR and equity multiple under each stress scenario. The key question: does the equity lose money (equity multiple < 1.0×), and if so, what is the severity?

6. **Evaluate capital cure requirements.** If the stress scenario triggers a DSCR or LTV covenant breach, model whether the sponsor would inject additional equity (a "cure") to avoid default. Determine the amount of cure required and whether it is feasible given the fund's reserves and LP agreement.

7. **Document results in a stress testing summary.** Present base case and each stress scenario in a side-by-side comparison showing: NOI by year, DSCR by year, LTV at exit, equity multiple, levered IRR, and covenant status.

## Outputs

The stress test produces: (1) NOI and DSCR by year under each stress scenario with covenant status; (2) stressed exit LTV and equity loss severity; (3) equity multiple and IRR under stress; (4) capital cure requirement (if any); and (5) a clear go/no-go assessment of whether the deal structure is defensible under the named scenarios.

## Example Walkthrough

*All figures below are illustrative and hypothetical — not derived from any real transaction.*

A stabilized multifamily property has base-case NOI of $1,400,000 with annual debt service of $980,000 (base DSCR 1.43×). Loan covenant: DSCR must remain above 1.15× or cash is trapped. Moderate stress scenario: NOI falls 20% to $1,120,000. DSCR: $1,120,000 / $980,000 = 1.14× — just below the 1.15× cash trap threshold, triggering covenant. Severe stress scenario: NOI falls 30% to $980,000. DSCR: 1.00× — debt service is exactly covered but there is no cash flow to equity. At a 6.5% exit cap (vs. 5.5% base), stressed value = $980,000 / 0.065 = $15,077,000 vs. a $12,000,000 loan balance, leaving $3,077,000 in equity value — a significant reduction from the base-case $10M+ equity value but technically no principal loss. These results suggest the deal is structurally sound under moderate stress but will cash-trap and produce below-hurdle equity returns under a severe, sustained income decline.

## Limitations

Stress tests depend on the analyst's scenario design — poorly chosen scenarios that are too mild produce false comfort; overly apocalyptic scenarios make every deal look fatally flawed. The scenarios must be calibrated to realistic adverse outcomes grounded in historical data for the specific asset class and market. Stress testing also does not assign probabilities to outcomes; for probabilistic risk analysis see [[Monte Carlo in CRE]]. Finally, stress tests are static — they don't model the dynamic management responses a skilled operator would make (rent concessions, cost cuts, asset sales) that could partially offset the shock.

## Related Frameworks

[[Sensitivity Analysis]] — the complementary framework that maps return across a continuous range of inputs; stress testing applies specific named scenarios. [[Monte Carlo in CRE]] — probabilistic extension. [[Pro Forma Construction Method]] — the base-case that stress scenarios are applied to. See also [[Debt Service Coverage Ratio (DSCR)]] and [[Loan-to-Value (LTV)]] for the covenant mechanics.

## Sources

CCIM Institute, *Financial Analysis for Commercial Investment Real Estate*. Federal Reserve and OCC guidance on commercial real estate loan stress testing for regulated lenders. REPE institutional underwriting practice.
