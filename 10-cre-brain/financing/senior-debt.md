---
title: "Senior Debt"
type: concept
tags: [cre/financing]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: First-lien mortgage debt secured by a property; holds the highest repayment priority in the capital stack and typically offers the lowest cost of capital.
domain: financing
formula: true
related:
  - "Mezzanine Debt"
  - "Bridge Loan"
  - "Permanent Loan"
  - "Construction Loan"
  - "Recourse vs. Non-Recourse"
  - "Bad-Boy Carve-Outs"
  - "Capital Stack Overview"
  - "Loan-to-Value (LTV)"
  - "Loan-to-Cost (LTC)"
  - "Debt Service Coverage Ratio (DSCR)"
  - "Debt Yield"
  - "Agency Debt (Fannie/Freddie)"
  - "CMBS"
  - "Life Company Debt"
  - "Bank Debt"
  - "Private Credit"
---

# Senior Debt

## Definition

Senior debt is first-lien mortgage financing secured by real property and recorded at the county level. Because it holds the first position in the repayment waterfall, senior lenders are paid in full before any junior creditor or equity partner receives proceeds from operations, refinancing, or sale. This structural priority translates directly into the lowest required yield among all capital sources in a deal — lenders accept a tighter margin precisely because their claim is best-protected. In institutional CRE transactions senior debt typically represents the largest single slice of total capitalization, commonly ranging from roughly 50% to 75% of either stabilized value or total project cost, depending on asset type, business plan, and lender appetite (varies by market and vintage, current as of 2026-05-24).

From a practical standpoint, senior debt sets the floor of the entire capital structure: the amount of leverage available governs how much equity must be raised, what returns are achievable for equity investors, and whether a deal is financeable at all. Lenders size proceeds through multiple overlapping tests — LTV, DSCR, and debt yield — and the most constraining test controls. Sponsors who understand where each constraint is likely to bind can structure a transaction to maximize proceeds while remaining within credit-acceptable parameters.

Senior mortgages are documented with a promissory note, a deed of trust or mortgage instrument, and a loan agreement that contains operating and financial covenants. Upon default the lender may foreclose on the collateral, making the quality, liquidity, and location of the underlying asset central to underwriting. Lenders generally distinguish between recourse loans (where the borrower entity and sometimes its principals bear personal liability) and non-recourse loans (where the lender's sole remedy is the collateral), a distinction covered in [[Recourse vs. Non-Recourse]].

## Formula

Senior debt sizing is governed by three overlapping constraints, each expressing a different view of risk. The binding constraint in any given deal is whichever produces the lowest loan amount.

**LTV sizing (stabilized or as-is value basis):**

- Plain text: `Max Loan = LTV_max × Appraised_Value`
- LaTeX: $$ \text{Max Loan} = \text{LTV}_{max} \times \text{Appraised Value} $$

**DSCR sizing (income coverage basis):**

- Plain text: `Max Loan = NOI / (DSCR_min × Annual_Debt_Service_per_Dollar)`
- LaTeX: $$ \text{Max Loan} = \frac{\text{NOI}}{\text{DSCR}_{min} \times \text{Debt Service Constant}} $$

**Debt Yield sizing (yield-on-loan basis):**

- Plain text: `Max Loan = NOI / Debt_Yield_min`
- LaTeX: $$ \text{Max Loan} = \frac{\text{NOI}}{\text{Debt Yield}_{min}} $$

Where:
- **NOI** = Stabilized Net Operating Income (in dollars per year; typically lender-underwritten, not sponsor-projected)
- **LTV_max** = maximum loan-to-value ratio set by lender policy (often 60–75% for permanent loans, 65–75% for bridge, varies by asset class and lender type)
- **DSCR_min** = minimum debt service coverage ratio (often 1.20x–1.35x for agency/life-co; more flexible for bridge/construction)
- **Debt Service Constant** = annual debt service as a fraction of loan principal (function of rate and amortization)
- **Debt Yield_min** = minimum NOI/loan ratio acceptable to lender (often 7%–10%+ depending on lender and product type, current as of 2026-05-24)

## When It's Used

Senior debt is present in virtually every institutionally structured CRE transaction. For stabilized acquisitions, borrowers seek permanent or agency financing sized to capture maximum leverage while satisfying DSCR and LTV tests. For transitional or value-add deals, borrowers typically use floating-rate bridge loans at higher spreads that allow more flexible sizing and prepayment during the business plan period, then refinance into permanent debt at stabilization. For ground-up development, construction loans fund in draws against cost rather than value, with DSCR tests deferred to stabilization. See [[Construction Loan]], [[Bridge Loan]], and [[Permanent Loan]] for each product in detail.

Lenders, equity investors, and brokers all rely on senior debt capacity as the first constraint in feasibility analysis. If the maximum loan available at acceptable coverage metrics does not pencil against the purchase price or project cost, the deal either requires more equity (diluting returns) or must be repriced. Senior debt capacity is therefore a primary governor of asset pricing throughout the real estate cycle.

## Variations & Edge Cases

Senior debt takes several forms depending on lender type, loan purpose, and capital market execution route. Agency lenders (Fannie Mae, Freddie Mac) focus almost exclusively on multifamily; life insurance companies favor lower-leverage, high-quality stabilized assets; CMBS securitizes pools of fixed-rate loans for capital-market execution; banks and debt funds serve transitional, construction, and specialty deals. Each lender type carries different sizing, covenant, and prepayment norms — see [[Agency Debt (Fannie/Freddie)]], [[Life Company Debt]], [[CMBS]], [[Bank Debt]], and [[Private Credit]].

Some practitioners distinguish "A-note/B-note" structures where the senior loan is bifurcated: the A-note is a first-position senior tranche sold to a third party, and the B-note is a subordinate participation still part of the same mortgage but bearing a higher yield. This should be distinguished from true mezzanine debt, which sits above equity but below the mortgage (see [[Mezzanine Debt]]). Competing definitions exist in the market; always clarify whether "senior debt" includes or excludes a B-note participation when reviewing deal term sheets.

## Common Mistakes

A common error is using sponsor-projected (rather than lender-underwritten) NOI to compute maximum loan proceeds. Lenders normalize income by haircut vacancy, cap management fees, and verify expense loads against market comparables; the underwritten NOI is often 5%–15% below the sponsor's stabilized pro forma, which can materially reduce loan proceeds and increase required equity. Sponsors who discover this gap late in the process face closing risk.

A second recurring mistake is failing to model the binding constraint. Analysts sometimes compute only DSCR or only LTV sizing, miss that debt yield is the binding test (particularly common in high-cap-rate markets or when NOI is thin), and build deal structures around loan amounts the lender will not actually approve. Always run all three tests simultaneously and identify which constraint is most limiting given the specific deal's income and value.

Finally, ignoring prepayment mechanics creates execution problems. Fixed-rate senior loans — especially CMBS and agency — often carry defeasance or yield-maintenance provisions that can represent substantial exit costs at refinance or sale. Floating-rate bridge loans may carry exit fees or minimum interest provisions. These must be modeled explicitly in the hold period analysis.

## Related Concepts

See [[Loan-to-Value (LTV)]], [[Loan-to-Cost (LTC)]], [[Debt Service Coverage Ratio (DSCR)]], and [[Debt Yield]] for the sizing metrics. See [[Capital Stack Overview]] for how senior debt fits into the full financing structure. See [[Recourse vs. Non-Recourse]] and [[Bad-Boy Carve-Outs]] for liability structure. Lender product notes: [[Agency Debt (Fannie/Freddie)]], [[CMBS]], [[Life Company Debt]], [[Bank Debt]], [[Private Credit]].

## Sources

Foundational treatment of senior debt priority and sizing is covered in the CCIM Institute's "Financial Analysis for Commercial Investment Real Estate" (CI 101) curriculum and the Urban Land Institute's *Real Estate Finance Fundamentals*. Debt yield as a primary sizing metric gained prominence post-2008 as lenders sought metrics less susceptible to appraisal manipulation; see discussion in Geltner et al., *Commercial Real Estate Analysis and Investments*, 3rd ed.
