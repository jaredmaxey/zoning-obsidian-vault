---
title: "Debt Service Coverage Ratio (DSCR)"
aliases: ["Debt Service Coverage Ratio (DSCR)"]
type: concept
tags: [cre/concepts]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: DSCR measures a property's NOI relative to its annual debt service, serving as the primary lender underwriting test for loan sizing and ongoing covenant compliance in CRE debt.
domain: concepts
formula: true
related:
  - "Net Operating Income (NOI)"
  - "Loan-to-Value (LTV)"
  - "Debt Yield"
  - "Loan-to-Cost (LTC)"
  - "Senior Debt"
  - "Permanent Loan"
  - "Agency Debt (Fannie/Freddie)"
  - "CMBS"
  - "Cap Rate"
  - "Stabilized NOI"
  - "Stress Testing"
---

# Debt Service Coverage Ratio (DSCR)

## Definition

The debt service coverage ratio (DSCR) measures how many times a property's net operating income (NOI) covers its annual debt service (principal and interest payments). A DSCR of 1.25x means the property generates $1.25 of NOI for every $1.00 of required debt service, providing a 25-cent buffer. It is the primary income-based underwriting test for all forms of permanent CRE lending: a loan cannot be sized above the amount whose debt service the property's NOI can comfortably service at the lender's required coverage ratio.

Lenders use DSCR to protect against downside scenarios: if NOI falls due to increased vacancy, expense growth, or rent decline, the DSCR cushion determines whether the loan remains serviceable. DSCR is tested at underwriting using either the lender's stress-tested NOI (often below the borrower's pro forma) and often at a higher stressed interest rate, not the actual loan rate, to ensure the loan can survive a rate shock or refinancing into a higher-rate environment. See [[Stress Testing]].

DSCR operates as a simultaneous constraint with [[Loan-to-Value (LTV)]] in determining the maximum loan amount: lenders compute the loan supportable by each constraint and then apply the binding (lower) constraint. In a low-cap-rate environment, DSCR often becomes the binding constraint because high asset prices produce low NOI relative to loan proceeds.

## Formula

- Plain text: `DSCR = NOI / Annual Debt Service`
- LaTeX: $$ \text{DSCR} = \frac{\text{NOI}}{\text{Annual Debt Service}} $$

**Where:**
- **NOI** — net operating income (see [[Net Operating Income (NOI)]]); lenders typically underwrite to a conservative or stressed NOI, not the borrower's optimistic pro forma
- **Annual Debt Service** — total principal and interest payments due on the loan in a 12-month period; on an interest-only loan, this equals interest only; on an amortizing loan, it includes scheduled amortization

Rearranging to solve for maximum loan amount:
- Plain text: `Max Loan = NOI / (Required DSCR × Debt Constant)`
- LaTeX: $$ \text{Max Loan} = \frac{\text{NOI}}{\text{Required DSCR} \times \text{Debt Constant}} $$

Where **Debt Constant** = annual debt service per dollar of loan principal (a function of interest rate and amortization schedule).

## When It's Used

DSCR is the first thing a lender calculates when sizing a permanent loan. Minimum DSCR requirements vary by lender type, loan program, and asset class. As of 2026-05-24, institutional permanent lenders (life companies, agency lenders, CMBS) commonly require minimum DSCRs in the range of 1.20x to 1.35x, with agency lenders (Fannie/Freddie) for multifamily sometimes requiring 1.25x at their underwritten NOI (which may differ from the borrower's NOI), and CMBS lenders underwriting to stressed rates (varies by market and vintage). See [[Agency Debt (Fannie/Freddie)]] and [[CMBS]].

In loan covenants, DSCR is often an ongoing maintenance test: if the property's actual DSCR falls below a trigger (say, 1.15x), the lender may require cash management, reserve funding, or in some structures, a cash trap that redirects distributable cash flow to a reserve account. This covenant monitoring is central to [[Senior Debt]] administration.

Borrowers test DSCR at acquisition to confirm the property can service their target loan amount. If the DSCR-constrained loan amount is lower than what LTV would allow, the deal is "NOI constrained" and the borrower must either accept more equity, improve the NOI assumption (risking underwriting credibility), or accept less leverage.

## Variations & Edge Cases

**Global DSCR:** Some lenders, particularly for recourse loans or smaller balance loans, underwrite a "global DSCR" that includes the borrower's other income and obligations, not just the subject property. This is more common for community bank loans and less common for CMBS or agency debt.

**Interest-only periods:** During an interest-only (IO) loan period, debt service is lower and DSCR appears higher, providing more room. When the IO period expires and amortization begins, the debt service jumps and the DSCR "steps down." Lenders underwriting an IO loan often test DSCR at the fully amortizing payment to ensure the loan can sustain amortization when it kicks in.

**DSCR on construction loans:** Construction loans are typically interest-only during the construction period, with DSCR underwriting focused on the takeout (permanent) loan scenario. The construction loan DSCR test is performed at projected stabilization, not during construction.

**Stressed vs. actual NOI:** Lenders frequently haircut the borrower's NOI (increase vacancy, increase expenses, stress rents) before applying the DSCR test. The specific stress methodology varies by lender and program.

## Common Mistakes

**Using borrower pro forma NOI without adjustment.** Borrowers optimistically project NOI; lenders should independently underwrite NOI using market vacancy, normalized expenses, and appropriate growth assumptions. Accepting borrower NOI at face value leads to mispriced loans.

**Ignoring interest-only expiration.** A loan that DSCRs at 1.30x on an IO basis may fall to 1.05x when amortization begins. Always test DSCR at the fully amortizing debt constant.

**Conflating DSCR with cash flow to equity.** DSCR tests NOI against debt service; it does not reflect equity distributions. Even a strong DSCR may leave little distributable cash after capex, reserves, and operating shortfalls.

## Related Concepts

- [[Net Operating Income (NOI)]] — the numerator; DSCR quality rises and falls with NOI reliability
- [[Loan-to-Value (LTV)]] — the simultaneous loan sizing constraint; DSCR and LTV together determine maximum loan amount
- [[Debt Yield]] — a third loan sizing metric gaining favor with lenders, complementary to DSCR
- [[Senior Debt]] — the loan type most commonly sized and governed by DSCR
- [[Permanent Loan]] — the long-term stabilized loan where DSCR is the primary sizing test
- [[Agency Debt (Fannie/Freddie)]] — multifamily program with specific DSCR requirements
- [[CMBS]] — securitized debt with DSCR tests at origination and as a trigger
- [[Stabilized NOI]] — the NOI basis lenders use for permanent loan sizing
- [[Stress Testing]] — the methodology for testing DSCR under adverse scenarios

## Sources

DSCR methodology is standard across institutional CRE lending and is addressed in Geltner et al.'s *Commercial Real Estate Analysis and Investments*, CCIM lending curriculum, and Fannie Mae/Freddie Mac multifamily underwriting guidelines. Specific DSCR requirements vary by program and market cycle (varies by market and vintage; current as of 2026-05-24).
