---
title: "Construction Loan"
type: concept
tags: [cre/financing]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Short-term, draw-based financing that funds ground-up or major renovation construction, repaid from permanent financing or sale proceeds upon project completion.
domain: financing
formula: true
related:
  - "Senior Debt"
  - "Bridge Loan"
  - "Permanent Loan"
  - "Bank Debt"
  - "Private Credit"
  - "Capital Stack Overview"
  - "Recourse vs. Non-Recourse"
  - "Bad-Boy Carve-Outs"
  - "Loan-to-Cost (LTC)"
  - "Loan-to-Value (LTV)"
  - "Ground-Up Development"
  - "Yield on Cost"
  - "Development Feasibility Test"
---

# Construction Loan

## Definition

A construction loan is a short-term, draw-based financing facility used to fund the construction or major rehabilitation of a commercial real estate project. Unlike a standard mortgage, a construction loan is not fully funded at closing; instead, proceeds are disbursed incrementally ("drawn down") as construction milestones are achieved and verified by a third-party inspector or lender's construction management team. The loan is typically interest-only during the construction period, with interest accruing only on amounts actually drawn (not the full commitment), and is repaid in full upon project completion through a take-out: either a permanent loan, agency financing, CMBS securitization, or property sale.

Construction loans represent the highest-risk position among senior debt products because the collateral (the completed project) does not exist at origination. The lender is underwriting the borrower's ability to deliver a completed project on time and on budget, the contractor's creditworthiness and track record, the market's absorption of the completed product, and the feasibility of the permanent take-out at assumed cap rates and rents. This compounded uncertainty is reflected in construction loan pricing — spreads above the floating benchmark are significantly higher than permanent loan spreads, and recourse from the borrowing entity to the sponsor (completion guaranty and repayment guaranty) is standard in most markets (varies by lender, asset class, and market conditions, current as of 2026-05-24).

Sizing of construction loans is governed primarily by LTC — the maximum loan as a percentage of total project cost including land, hard costs, soft costs, and contingency. LTC limits typically range from 60% to 75% of total cost, though some highly pre-leased or pre-sold projects can achieve higher leverage. The gap between the construction loan and total project cost is the equity requirement, funded by the sponsor's co-investment and LP equity capital raised before closing.

## Formula

**Maximum Construction Loan (LTC basis):**

- Plain text: `Max Loan = LTC_max × Total_Project_Cost`
- LaTeX: $$ L_{max} = \text{LTC}_{max} \times C_{total} $$

**Interest Carry During Construction (on average drawn balance):**

- Plain text: `Interest_Carry = Avg_Outstanding × (Benchmark + Spread) × Construction_Period_Years`
- LaTeX: $$ I_{carry} = \bar{L} \times (r_{benchmark} + s) \times t_{construction} $$

**Minimum Equity Contribution:**

- Plain text: `Min_Equity = Total_Project_Cost - Max_Loan`
- LaTeX: $$ E_{min} = C_{total} - L_{max} $$

**Stabilized Yield on Cost (development feasibility check):**

- Plain text: `Yield_on_Cost = Stabilized_NOI / Total_Cost`
- LaTeX: $$ \text{YOC} = \frac{\text{NOI}_{stab}}{C_{total}} $$

Where:
- **LTC_max** = maximum loan-to-cost ratio (typically 60%–75% for ground-up construction; varies by market and vintage)
- **C_total** = total all-in project cost (land + hard costs + soft costs + contingency + carry + financing costs + developer fee)
- **L_bar** = average outstanding loan balance during construction period (often modeled as ~60%–70% of max commitment)
- **r_benchmark + s** = floating benchmark rate plus lender spread (varies significantly by market and vintage, current as of 2026-05-24)
- **t_construction** = construction period in years
- **NOI_stab** = projected stabilized NOI after lease-up

## When It's Used

Construction loans are the standard vehicle for any ground-up development or major adaptive reuse where the property must be substantially rebuilt before it can be occupied and generate income. Every ground-up development — multifamily, industrial, office, retail, or mixed-use — requires construction financing unless the developer is fully self-financing. Because construction loans mature at completion (typically 18–36 months for vertical construction, longer for large mixed-use or phased projects), they require a clear take-out strategy underwritten from day one.

Pre-leasing or pre-sales materially affect construction loan availability and pricing. Industrial or office developments with anchor tenants pre-leased to creditworthy tenants can command better LTC terms because the income stream reduces lease-up risk. Speculative ("spec") development without pre-leasing faces more conservative sizing and higher spreads. Multifamily construction loans are typically speculative (no pre-leases), so lenders rely on market absorption forecasts and comparable property performance to validate the take-out underwriting.

From the equity perspective, the construction period is a period of pure cash outflow — there is no income to service the loan, and interest accrues (usually paid from the interest reserve funded at closing). The developer and its LP investors are "all in" on the development thesis: they need the market to absorb the completed project at underwritten rents and occupancy before the construction loan matures and demands repayment.

## Variations & Edge Cases

"Construction-to-permanent" (C-to-P) loans combine a construction phase and a permanent phase in a single loan, with an automatic conversion at a predefined trigger (substantial completion plus minimum occupancy). These reduce execution risk by locking in permanent financing terms at construction loan origination but may limit flexibility if market conditions improve and better permanent financing becomes available at completion.

"Mini-perm" extensions are short extension periods (often 12–24 months) appended to a construction loan at maturity that allow the borrower additional time to achieve stabilization before permanent take-out, without the cost of fully refinancing. These are common in markets with longer lease-up cycles or where permanent lending markets are temporarily dislocated.

Renovation or "gut rehab" projects that require major structural work can use a construction loan structure even though an existing building is present. The key distinction from a bridge loan is the depth of the construction program and the draw-down mechanics: heavy rehabilitation follows a construction draw schedule, while bridge loans for lighter value-add work typically fund proceeds at closing with a capex holdback.

## Common Mistakes

The most common construction loan error is underestimating total project cost, particularly soft costs, contingency, and carry. Hard construction costs are visible in the GC contract; soft costs (architecture, engineering, permits, legal, accounting, marketing, developer fee) and financing carry (interest during construction, extension fees, and post-construction lease-up carry) are frequently understated, shrinking the effective equity cushion and exposing the lender and equity to cost overruns. Lenders typically require 5%–10% hard cost contingency and 3%–5% soft cost contingency at minimum; sponsors with thin equity cushions who undersize contingency are the first to face completion guaranty calls.

A second error is failing to synchronize the construction draw schedule with the equity funding schedule. Equity is almost always funded first (before the lender will advance), meaning the sponsor must either commit to a large up-front equity infusion or maintain a credible equity call schedule tied to construction milestones. Misalignment between draw timing and equity availability can create funding gaps that trigger construction loan defaults.

## Related Concepts

See [[Senior Debt]] for the broader context of first-lien mortgage financing. [[Bridge Loan]] is the analog for transitional (non-construction) business plans. [[Permanent Loan]] is the standard take-out vehicle post-construction. [[Ground-Up Development]] is the deal type context. [[Yield on Cost]] and [[Development Feasibility Test]] are the primary feasibility metrics used to evaluate whether a construction project's projected stabilized income justifies the development cost. [[Loan-to-Cost (LTC)]] is the primary sizing metric.

## Sources

Construction lending mechanics are covered in detail in Geltner et al., *Commercial Real Estate Analysis and Investments*, 3rd ed., and in the Mortgage Bankers Association's construction lending program materials. The Associated General Contractors of America (AGC) and American Institute of Architects (AIA) publish standard owner-GC contract forms (AIA A101/A102) that form the contractual basis for construction draw mechanics. CREFC guidelines address construction-to-permanent loan structuring norms.
