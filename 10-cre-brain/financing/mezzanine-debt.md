---
title: "Mezzanine Debt"
aliases: ["Mezzanine Debt"]
type: concept
tags: [cre/financing]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Subordinate debt positioned between senior mortgage and equity; secured by a pledge of the borrowing entity's ownership interests rather than a direct property lien.
domain: financing
formula: true
related:
  - "Senior Debt"
  - "Preferred Equity"
  - "Capital Stack Overview"
  - "Waterfall Structures and Promote"
  - "Loan-to-Value (LTV)"
  - "Loan-to-Cost (LTC)"
  - "Debt Service Coverage Ratio (DSCR)"
  - "Internal Rate of Return (IRR)"
  - "Recourse vs. Non-Recourse"
  - "Private Credit"
---

# Mezzanine Debt

## Definition

Mezzanine debt is subordinate financing that occupies the layer of the capital stack between the senior mortgage and the equity. Unlike senior debt, which is secured by a first-lien on the real property itself, mezzanine debt is typically secured by a pledge of the ownership interests (membership interests or partnership interests) in the entity that directly owns the property. This structural distinction has profound legal consequences: upon a mezzanine default, the lender's remedy is a UCC foreclosure on the pledged equity interests — a process that can be completed far more quickly than a real property mortgage foreclosure, often in 30–60 days depending on jurisdiction and deal structure (varies by state law and intercreditor agreement, current as of 2026-05-24).

Because mezzanine debt is subordinate to senior debt in the repayment waterfall, mezzanine lenders bear substantially more risk than senior lenders. To compensate, mezzanine debt carries significantly higher interest rates — commonly ranging from the mid-single digits above the risk-free rate to well into the teens for highly leveraged or transitional deals — and the yield expectation rises with combined (senior + mezzanine) loan-to-value. Mezzanine is most common in value-add, ground-up development, and other transitional transactions where sponsors seek to reduce equity contributions while managing dilution to IRR.

The relationship between the senior lender and the mezzanine lender is governed by an intercreditor agreement (ICA), which establishes the rights of each party upon default, cure rights, standstill provisions, and the conditions under which the mezzanine lender may purchase the senior loan ("buy-out" right). Senior lenders have become increasingly sophisticated in limiting mezzanine lenders' remedies; the specific ICA terms are as important as the economics in evaluating a mezzanine position.

## Formula

Mezzanine debt is sized in the context of the total leverage stack, most commonly by reference to combined loan-to-cost or loan-to-value, with the mezzanine piece filling the gap between senior capacity and sponsor equity:

**Mezzanine Loan Amount:**

- Plain text: `Mezz Loan = (Total_LTC_target × Total_Cost) - Senior_Loan`
- LaTeX: $$ \text{Mezz Loan} = (\text{LTC}_{total} \times \text{Total Cost}) - \text{Senior Loan} $$

**All-In Blended Cost of Debt:**

- Plain text: `Blended_Rate = (Senior_Loan × Senior_Rate + Mezz_Loan × Mezz_Rate) / (Senior_Loan + Mezz_Loan)`
- LaTeX: $$ r_{blended} = \frac{L_s \cdot r_s + L_m \cdot r_m}{L_s + L_m} $$

Where:
- **LTC_total** = target combined loan-to-cost (e.g., 80%–85% of total project cost; varies by market and vintage)
- **Total Cost** = all-in project cost including land, hard costs, soft costs, and carry
- **Senior Loan** = proceeds from the first-lien senior lender
- **L_s, L_m** = senior and mezzanine loan balances
- **r_s, r_m** = senior and mezzanine interest rates (annualized)
- **r_blended** = weighted average cost of the combined debt stack

## When It's Used

Mezzanine debt is most actively deployed in three contexts. First, value-add acquisitions where the transitional business plan and elevated risk pricing make senior-only leverage insufficient to achieve target equity returns — mezzanine fills the gap between the senior loan and the 15%–25% equity requirement sponsors prefer to maintain. Second, ground-up development where the combined construction loan plus mezzanine can approach 80%–90% of total cost on highly underwritten projects, though lenders have tightened significantly post-cycle (varies by market and vintage, current as of 2026-05-24). Third, recapitalizations where a sponsor needs to extract equity or reliquify a portfolio without triggering a full refinance of seasoned senior debt.

Mezzanine is particularly prominent in large-scale transactions where institutional sponsors are managing portfolio leverage targets and need gap financing to hit acquisition pricing. Debt funds, family offices, and insurance company credit arms are common mezzanine providers at the institutional level; some banks also offer mezzanine through their specialty finance desks.

## Variations & Edge Cases

There is a genuine definitional debate in the market between "true mezzanine" (entity-secured via UCC pledge) and "hard mezzanine" (a second mortgage lien on the property itself, subject to the same foreclosure timeline as the senior). Some practitioners use the terms interchangeably; others distinguish them sharply. The distinction matters because a second mortgage requires the senior lender's explicit consent via a subordination, non-disturbance, and attornment agreement (SNDA) and is far harder to enforce quickly. Always confirm the security instrument when evaluating any structure described as "mezzanine."

Mezzanine debt and [[Preferred Equity]] are frequently confused because both are subordinate to senior debt and both carry preferential cash flow rights. The key distinction: mezzanine is debt (creates a repayment obligation, accrues interest, triggers default) while preferred equity is an equity investment (no maturity, returns governed by the operating agreement, harder to enforce). Some lenders will not permit mezzanine behind their loan while allowing preferred equity. The intercreditor or recognition agreement terms differ accordingly.

## Common Mistakes

The most dangerous error in mezzanine underwriting is underestimating the intercreditor risk. Sponsors sometimes sign ICAs that give the senior lender broad rights to reject mezzanine lenders' attempts to cure defaults, or that restrict the mezzanine lender's UCC foreclosure timeline in ways that eliminate the primary enforcement advantage of the product. Reviewing the ICA is as important as reviewing the mezzanine loan agreement.

Analysts also frequently fail to fully model the debt service waterfall under stress. If senior debt is interest-only and mezzanine is also interest-only, the combined cash-on-cash debt service burden must be stress-tested against the asset's income at various points in the hold period. Properties operating below stabilized occupancy may not generate enough NOI to service both senior and mezzanine debt, creating a negative leverage drag that erodes equity returns faster than the model assumes.

## Related Concepts

See [[Senior Debt]] for the first-lien layer mezzanine sits behind. See [[Preferred Equity]] for the next layer up and the distinction between debt and equity instruments. [[Capital Stack Overview]] provides the full layering context. [[Waterfall Structures and Promote]] explains how cash flows are distributed after debt service. [[Private Credit]] covers debt fund providers that are active in mezzanine. [[Internal Rate of Return (IRR)]] is the primary metric equity sponsors use to evaluate whether added mezzanine leverage enhances or destroys equity returns.

## Sources

Mezzanine debt structure and ICA mechanics are extensively covered in Steven Balkin, *Mezzanine Finance: A Legal and Practical Guide* (Aspatore Books) and in real estate finance practitioner references from the American College of Real Estate Lawyers (ACREL). CCIM Institute CI 101 covers the capital stack hierarchy. Post-2008 tightening of intercreditor terms is documented in industry commentary from the Urban Land Institute and CRE Finance Council (CREFC) publications.
