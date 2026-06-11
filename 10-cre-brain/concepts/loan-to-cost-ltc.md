---
title: "Loan-to-Cost (LTC)"
aliases: ["Loan-to-Cost (LTC)"]
type: concept
tags: [cre/concepts]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: LTC is the ratio of a loan amount to total project cost, serving as the primary collateral-based loan sizing constraint for construction and development financing where an appraised value does not yet exist.
domain: concepts
formula: true
related:
  - "Loan-to-Value (LTV)"
  - "Debt Service Coverage Ratio (DSCR)"
  - "Debt Yield"
  - "Construction Loan"
  - "Bridge Loan"
  - "Hard Costs"
  - "Soft Costs"
  - "Yield on Cost"
  - "Capital Stack Overview"
  - "Development Feasibility Test"
---

# Loan-to-Cost (LTC)

## Definition

Loan-to-cost (LTC) is the ratio of the loan amount to the total all-in project cost, expressed as a percentage. It is the primary loan sizing metric for construction loans, development financing, and bridge loans on properties undergoing significant renovation — situations where an "as-stabilized" appraised value exists but is speculative, and an "as-is" appraised value of the partially completed or to-be-built property is not meaningful. LTC anchors the loan to the hard cost of producing the asset rather than to a market value estimate.

LTC protects the lender by ensuring the borrower has meaningful equity "skin in the game." A lender capping LTC at 65% requires the borrower to fund at least 35 cents of every dollar of project cost from equity. If the project fails or costs overrun, the equity cushion is the first loss — the lender's loan is protected by the borrower's equity contribution. This alignment of incentives is the fundamental rationale for LTC as a lending constraint on development projects.

LTC and [[Loan-to-Value (LTV)]] are related but distinct: LTC uses the actual (or projected) cost of creating the asset; LTV uses the market value conclusion from an appraisal. On development projects, an "as-stabilized" appraisal value often exceeds total project cost (that gap is the developer's profit/value creation), so a 65% LTC may correspond to a lower LTV on the as-stabilized basis — meaning the loan is conservative on both dimensions when the project is well underwritten.

## Formula

- Plain text: `LTC = Loan Amount / Total Project Cost`
- LaTeX: $$ \text{LTC} = \frac{\text{Loan Amount}}{\text{Total Project Cost}} $$

**Where:**
- **Loan Amount** — the full committed construction loan facility or the disbursed principal balance; lenders typically commit the full facility upfront and fund in draws as construction progresses
- **Total Project Cost** — all costs required to complete the project and reach stabilization: land acquisition cost, hard construction costs, soft costs (architecture, engineering, permits, legal, financing fees), contingency (hard and soft), construction period interest carry, developer fee, and pre-leasing costs. See [[Hard Costs]] and [[Soft Costs]].

Maximum loan size: `Max Loan = Total Project Cost × Maximum LTC`

## When It's Used

Construction lenders use LTC as the primary underwriting constraint at loan commitment. Typical institutional construction loan LTC limits range from 55–70% of total project cost depending on asset class, market, lender type, and deal quality, with the equity requirement implying 30–45% equity (varies by market and vintage; current as of 2026-05-24). Larger, more complex projects with higher execution risk tend to command lower LTC limits; straightforward multifamily or industrial projects in strong markets may achieve higher LTC from bank lenders.

During the construction period, lenders fund in monthly or milestone-based draws as verified by an independent construction inspector. The LTC ratio at any given draw date reflects the amount funded relative to total budget, and lenders confirm that actual costs match the schedule before releasing each draw. Cost overruns that push total project cost higher reduce the effective LTC below the committed facility — the lender does not automatically fund overruns above the original budget, so the borrower must fund overruns from equity.

Bridge lenders also use LTC for value-add acquisitions: total project cost includes the purchase price plus the renovation budget, and the lender sizes the loan as a percentage of that combined cost. For example, a $10M acquisition with $3M of planned renovations = $13M total project cost; a 70% LTC bridge loan = $9.1M.

## Variations & Edge Cases

**LTC vs. LTV on construction loans:** Many construction lenders underwrite both LTC and as-stabilized LTV and apply the more conservative (lower) constraint. A well-underwritten development project should satisfy both tests: LTC caps leverage relative to cost, and as-stabilized LTV caps leverage relative to the finished asset value.

**Cost basis definition differences:** Some lenders include developer fee in total project cost; others exclude it. Some include all soft costs; others use a narrower "hard cost + direct soft cost" definition. Always confirm what is included in the denominator before quoting LTC.

**Interest reserve as a cost component:** Construction loan interest carry during the construction and stabilization period is typically funded by an interest reserve included in the total project cost and loan budget. Including interest reserve in the cost basis means LTC reflects the fully loaded cost to get to stabilization, which is the appropriate measure.

## Common Mistakes

**Using hard costs only as the denominator.** A developer who quotes LTC using only hard costs, excluding soft costs, contingency, and carry, presents an artificially low (more favorable) LTC. Institutional lenders use all-in project cost consistently.

**Ignoring cost overrun risk.** LTC is computed on the underwritten budget. If construction costs overrun (materials inflation, design changes, labor shortages), the actual LTC will be lower than underwritten because the borrower must fund the excess from equity. Budget contingency is the risk management buffer against this.

**Conflating LTC with equity requirement.** LTC tells you the percentage of cost funded by the loan; the equity requirement is 100% minus LTC. On a $20M project at 65% LTC, the $7M equity requirement may come from one source or a combination of common equity, mezzanine, and preferred equity — LTC does not tell you the equity capital stack composition.

## Related Concepts

- [[Loan-to-Value (LTV)]] — the stabilized-asset analog; together with LTC, defines the dual constraint framework for construction lending
- [[Construction Loan]] — the primary loan type to which LTC applies
- [[Bridge Loan]] — value-add acquisition financing where LTC covers purchase plus renovation
- [[Hard Costs]] — the largest component of total project cost in the LTC denominator
- [[Soft Costs]] — the second major cost component; often underestimated in early-stage budgets
- [[Yield on Cost]] — the feasibility metric that measures NOI relative to total project cost; shares the same cost denominator as LTC
- [[Capital Stack Overview]] — the framework for understanding LTC within the full equity/debt stack
- [[Development Feasibility Test]] — the broader test of which LTC is one component

## Sources

LTC standards are set by individual construction lender programs, OCC guidelines on commercial real estate lending, and industry practice. CBRE, JLL, and other capital markets advisors publish periodic construction lending surveys with LTC ranges by market and asset class (varies by market and vintage; current as of 2026-05-24).
