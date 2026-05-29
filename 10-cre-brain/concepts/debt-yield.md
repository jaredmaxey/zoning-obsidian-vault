---
title: "Debt Yield"
type: concept
tags: [cre/concepts]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Debt yield is the ratio of a property's NOI to the loan amount, providing a market-rate-independent measure of lender risk that complements DSCR and LTV in loan sizing.
domain: concepts
formula: true
related:
  - "Net Operating Income (NOI)"
  - "Loan-to-Value (LTV)"
  - "Debt Service Coverage Ratio (DSCR)"
  - "Cap Rate"
  - "CMBS"
  - "Senior Debt"
  - "Stabilized NOI"
  - "Permanent Loan"
---

# Debt Yield

## Definition

Debt yield is the ratio of a property's net operating income to the loan balance, expressed as a percentage. It answers the question: "if the lender had to foreclose and sell this property at a cap rate equal to its debt yield, what would they recover relative to the loan balance?" A debt yield of 8.0% means the lender would break even on foreclosure if the market was willing to pay at an 8.0% cap rate. A higher debt yield indicates a more conservatively underwritten loan with a greater margin of safety for the lender.

Debt yield rose to prominence as a loan sizing constraint in the CMBS and life company markets following the 2008–2010 financial crisis, when lenders realized that low interest rate environments allowed DSCR tests to pass at very high LTVs (because low rates produce low debt service, inflating DSCR). A 1.25x DSCR at a 3% interest rate corresponds to a much larger loan than at a 6% interest rate, even on the same property with the same NOI. Debt yield is immune to this distortion: it depends only on NOI and loan balance, with no sensitivity to interest rates.

Debt yield effectively acts as an interest-rate-normalized floor on the cap rate at which a lender can recover their loan. Because it is independent of the financing cost and the specific interest rate environment, institutional lenders use it as a minimum threshold that must be cleared regardless of how favorable DSCR looks in a low-rate environment. See [[CMBS]] for context on how rating agencies incorporate debt yield into securitization analysis.

## Formula

- Plain text: `Debt Yield = NOI / Loan Amount`
- LaTeX: $$ \text{Debt Yield} = \frac{\text{NOI}}{\text{Loan Amount}} $$

**Where:**
- **NOI** — the lender's underwritten net operating income, typically at stabilization using a stressed or conservative NOI estimate (see [[Stabilized NOI]])
- **Loan Amount** — the total committed loan balance at origination

Rearranging to solve for maximum loan: `Max Loan = NOI / Minimum Required Debt Yield`

For example: if a property has $600,000 of underwritten NOI and the lender requires a minimum 9% debt yield, the maximum loan is $600,000 / 0.09 = $6,667,000.

## When It's Used

Debt yield is used primarily by CMBS lenders, life company lenders, and sophisticated institutional bank lenders as a third loan sizing constraint alongside LTV and DSCR. Minimum debt yield requirements in the CMBS market typically range from 7–10%, varying by asset class, loan quality, and market conditions — with higher requirements for riskier asset classes or markets (varies by market and vintage; current as of 2026-05-24).

Rating agencies use debt yield (alongside LTV and DSCR) to assign credit ratings to CMBS bonds: a loan pool with higher aggregate debt yields is viewed as more conservatively underwritten, supporting higher ratings for senior tranches. See [[CMBS]].

For borrowers, debt yield is a soft ceiling on loan size: if the property's NOI is thin relative to the desired loan amount, debt yield may be the binding constraint. Borrowers can push debt yield higher by improving NOI underwriting credibility (stronger rent roll, lower vacancy), but they cannot manufacture debt yield by adjusting financing assumptions the way they might game DSCR in a low-rate environment.

## Variations & Edge Cases

**As-is vs. stabilized debt yield:** Some lenders test debt yield on current in-place NOI (as-is basis) rather than stabilized NOI. For a value-add property with below-market occupancy, this produces a much lower debt yield and a more conservative loan test.

**Debt yield on IO vs. amortizing loans:** Because debt yield has no interest rate component, it is the same regardless of whether the loan is interest-only or amortizing. This is specifically why lenders use it: as a check that DSCR alone (which fluctuates with the interest rate) is not masking an insufficiently covered loan.

**Relationship to cap rate:** If debt yield equals the market cap rate, the loan is sized so that the lender could recover the loan by selling the property at market value — equivalent to a 100% LTV at market cap rates. In practice, lenders require debt yield meaningfully above the market cap rate to provide loss protection.

## Common Mistakes

**Conflating debt yield with cap rate.** Cap rate is NOI divided by property value; debt yield is NOI divided by loan balance. If LTV = 100%, they would be equal. In practice, debt yield is higher than the cap rate by the margin implied by the LTV discount.

**Ignoring debt yield in favor of DSCR alone.** In low-interest-rate environments, a loan can pass DSCR easily while debt yield signals an aggressively sized loan. Reviewing only DSCR missed this warning sign in the pre-2008 period.

**Testing debt yield on inflated NOI.** A lender who accepts borrower pro forma NOI without haircut will produce an artificially high debt yield, defeating the metric's protective purpose. Lenders should underwrite to their own independently derived NOI.

## Related Concepts

- [[Net Operating Income (NOI)]] — the numerator; lender-underwritten NOI quality is critical
- [[Loan-to-Value (LTV)]] — operates simultaneously; together LTV, DSCR, and debt yield form the three-constraint framework
- [[Debt Service Coverage Ratio (DSCR)]] — the income-to-debt-service constraint; debt yield is the interest-rate-independent complement
- [[Cap Rate]] — the market pricing rate; debt yield should exceed cap rate to provide collateral cushion
- [[CMBS]] — the primary institutional context in which debt yield is used as a hard sizing test
- [[Senior Debt]] — the debt instrument subject to debt yield underwriting
- [[Stabilized NOI]] — the income basis used in debt yield calculations

## Sources

Debt yield as a lending metric is discussed in CMBS underwriting guidelines, rating agency methodologies (Moody's, S&P, Fitch), and post-GFC lender reform literature. CBRE and JLL publish periodic lending surveys that include debt yield requirements by lender type (varies by market and vintage; current as of 2026-05-24).
