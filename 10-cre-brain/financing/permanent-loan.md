---
title: "Permanent Loan"
aliases: ["Permanent Loan"]
type: concept
tags: [cre/financing]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Long-term, typically fixed-rate first-lien mortgage placed on stabilized income-producing property after construction or business plan execution is complete.
domain: financing
formula: true
related:
  - "Senior Debt"
  - "Bridge Loan"
  - "Construction Loan"
  - "Agency Debt (Fannie/Freddie)"
  - "CMBS"
  - "Life Company Debt"
  - "Recourse vs. Non-Recourse"
  - "Bad-Boy Carve-Outs"
  - "Debt Service Coverage Ratio (DSCR)"
  - "Loan-to-Value (LTV)"
  - "Debt Yield"
  - "Refinance Decision Framework"
  - "Cap Rate"
  - "Net Operating Income (NOI)"
---

# Permanent Loan

## Definition

A permanent loan is a long-term, typically fixed-rate first-lien mortgage placed on a stabilized, income-producing commercial property. It is the "take-out" financing that replaces a bridge loan, construction loan, or other transitional financing once a property has achieved the occupancy, income, and condition levels necessary to satisfy underwriting tests. Permanent loans typically have initial terms of 5–10 years (sometimes 15–30 years for certain agency products), are amortized over 20–30 years (or structured as interest-only for higher-credit or lower-leverage deals), and provide long-term, predictable financing at the lowest cost of any debt product.

The defining characteristic of a permanent loan is that the collateral is the stabilized income stream of the property — the lender is confident that occupancy, rents, and operating expenses have normalized to a level sufficient to support debt service through market cycles, not merely during a favorable point in a business plan. This requirement means permanent loans are categorically unavailable for properties in lease-up, repositioning, or heavy renovation programs; those require bridge or construction financing until stabilization is achieved.

Permanent loans are originated by four primary institutional lender types, each with distinct product characteristics: agency lenders (Fannie Mae, Freddie Mac) for multifamily; life insurance companies for large, high-quality stabilized assets across property types; CMBS conduit lenders for fixed-rate securitized execution across property types; and banks for portfolio-held balance-sheet loans, often with floating rates and greater structural flexibility. See [[Agency Debt (Fannie/Freddie)]], [[Life Company Debt]], [[CMBS]], and [[Bank Debt]] for detailed product notes.

## Formula

Permanent loan sizing uses the same three-constraint methodology as senior debt generally. For a stabilized asset, the operative inputs are in-place or lender-underwritten NOI and appraised value:

**DSCR-Based Maximum Loan:**

- Plain text: `Max Loan = (NOI / DSCR_min) / Debt_Constant`
- LaTeX: $$ L_{max} = \frac{\text{NOI} / \text{DSCR}_{min}}{k} $$

**LTV-Based Maximum Loan:**

- Plain text: `Max Loan = LTV_max × Appraised_Value`
- LaTeX: $$ L_{max} = \text{LTV}_{max} \times V $$

**Debt Yield Test:**

- Plain text: `Debt Yield = NOI / Loan_Amount ≥ Debt_Yield_minimum`
- LaTeX: $$ DY = \frac{\text{NOI}}{L} \geq DY_{min} $$

**Annual Debt Service (fixed-rate, amortizing):**

- Plain text: `Annual DS = Loan × Mortgage_Constant`
- LaTeX: $$ DS = L \times k $$
$$k = \frac{r(1+r)^n}{(1+r)^n - 1} \times 12 \text{ (annualized from monthly)}$$

Where:
- **NOI** = lender-underwritten stabilized Net Operating Income (not sponsor's pro forma; lenders typically haircut vacancy, normalize expenses)
- **DSCR_min** = minimum debt service coverage ratio (commonly 1.20x–1.35x for agency/life-co; varies by product)
- **k** = mortgage constant (annual debt service per dollar of loan; function of rate and amortization term)
- **LTV_max** = maximum LTV (commonly 60%–75% for permanent loans; varies by lender type and asset class)
- **V** = appraised stabilized value
- **DY_min** = minimum debt yield floor (often 7%–10%+ depending on lender and product; varies by market and vintage, current as of 2026-05-24)
- **r** = annual interest rate; **n** = amortization periods (months)

## When It's Used

Permanent loans are the end state of most CRE financing strategies. At the end of a value-add hold period, the sponsor either sells the property (realizing equity proceeds) or refinances the bridge loan into a permanent loan, extracting equity while maintaining ownership. At the completion of ground-up development, the developer either sells or refinances the construction loan into a permanent loan. Core investors may acquire a property with permanent financing in place at purchase, rolling existing debt or securing new long-term financing to minimize refinancing risk and maximize income predictability.

From a hold period modeling standpoint, permanent financing has two critical effects: it determines how much equity can be returned to investors via refinancing (a cash-out refi is a key equity return event in many value-add strategies), and it establishes the annual debt service that determines going-forward cash-on-cash returns. Fixed-rate permanent loans also create interest-rate exposure on the exit side — if market cap rates compress relative to the permanent loan rate, the loan balance relative to value may increase at maturity, creating refinancing risk if the market has repriced.

## Variations & Edge Cases

"Interest-only" (IO) permanent loans — where no principal amortization occurs during the loan term, with the full balance due at maturity — are periodically available from agency and CMBS lenders for lower-LTV, higher-quality deals. IO loans produce higher in-period cash flows (no principal paydown) but create "bullet maturity" refinancing risk and result in a higher outstanding balance at sale or refinance than a fully amortizing loan. IO periods within otherwise amortizing loans (a specified IO period followed by amortization) are a common middle ground.

"Floating-rate permanent" loans — balance-sheet loans from banks or debt funds at floating rates but with 5–7 year terms — blur the line between bridge and permanent. They are used when borrowers expect to sell or refinance before a fixed-rate term would make sense, or when the interest rate environment makes floating-rate exposure desirable (e.g., in declining-rate environments). See [[Bank Debt]] for detail.

Prepayment protection is a defining feature of permanent loans that affects exit strategy. Agency loans typically use yield maintenance or defeasance (substituting Treasury securities for the real estate collateral, allowing the lender to continue receiving the contracted yield). CMBS loans use defeasance or step-down prepayment penalties. Life company loans typically use yield maintenance. Understanding the prepayment obligation at any given point in the hold is essential for accurate IRR modeling.

## Common Mistakes

Underestimating the cost and complexity of permanent loan prepayment is a systemic error in early-stage deal modeling. Sponsors building a 5-year hold period model that assumes a 10-year fixed-rate loan can be paid off early without cost will overestimate net sale proceeds. Defeasance on a 10-year agency loan during years 2–8 can cost millions of dollars on a large loan, dramatically affecting IRR.

A second common mistake is using the sponsor's pro forma NOI (rather than the lender's underwritten NOI) to pre-screen permanent loan capacity. Lenders normalize income at their own underwriting standards — often using in-place leases rather than projected rents, capping vacancy at market norms rather than sponsor-projected lows, and adding back management fees below market. The gap between sponsor NOI and lender underwritten NOI can be 10%–20%, with a direct impact on loan proceeds.

## Related Concepts

See [[Senior Debt]] for the broader conceptual framework. [[Bridge Loan]] and [[Construction Loan]] are the preceding transitional products permanent loans refinance. [[Agency Debt (Fannie/Freddie)]], [[CMBS]], [[Life Company Debt]], and [[Bank Debt]] cover the specific lender types originating permanent loans. [[Debt Service Coverage Ratio (DSCR)]], [[Loan-to-Value (LTV)]], and [[Debt Yield]] are the sizing metrics. [[Refinance Decision Framework]] in operations covers the decision to refinance vs. sell. [[Cap Rate]] and [[Net Operating Income (NOI)]] are the core income and value metrics that determine permanent loan proceeds.

## Sources

Permanent loan structuring is covered in Geltner et al., *Commercial Real Estate Analysis and Investments*, 3rd ed. Agency loan product guides are published by Fannie Mae DUS and Freddie Mac Optigo programs. CREFC publishes market surveys on permanent loan pricing and terms across lender types. Defeasance mechanics are addressed in CMBS trust and pooling agreements and in practitioner guides from the Commercial Real Estate Finance Council.
