---
title: "Refinance Decision Framework"
aliases: ["Refinance Decision Framework"]
type: concept
tags: [cre/operations]
created: "2026-05-24"
updated: "2026-05-24"
status: draft
ai_summary: Structured process for deciding whether and when to refinance an existing loan, sizing the new proceeds, and evaluating the trade-off between cost of capital, hold period extension, and investor distributions.
domain: operations
formula: true
related:
  - "Hold vs. Sell Analysis"
  - "Permanent Loan"
  - "Bridge Loan"
  - "Agency Debt (Fannie/Freddie)"
  - "CMBS"
  - "Debt Service Coverage Ratio (DSCR)"
  - "Debt Yield"
  - "Loan-to-Value (LTV)"
  - "Net Operating Income (NOI)"
  - "Cash-on-Cash Return"
  - "Internal Rate of Return (IRR)"
---

# Refinance Decision Framework

## Definition

The refinance decision framework is the analytical process an asset manager uses to evaluate whether to replace an existing loan with a new loan on the same property, and if so, on what terms and timeline. A refinance can serve several strategic objectives: (1) **rate reduction**—replacing a higher-rate loan with a lower-rate loan to reduce debt service and improve [[Cash-on-Cash Return]]; (2) **proceeds maximization**—extracting equity appreciation as tax-free cash proceeds by sizing the new loan on the property's higher stabilized value; (3) **maturity extension**—extending the loan term to continue the hold period without forcing a sale; or (4) **structure optimization**—moving from a floating-rate bridge loan to fixed-rate permanent financing as the asset stabilizes. In practice, a single refinance often pursues multiple objectives simultaneously.

The central financial question in any refinance is: **how large a loan will the asset support?** Institutional lenders size loans using three constraints applied simultaneously, and the binding (most restrictive) constraint determines maximum proceeds:

- **LTV constraint**: loan ≤ (LTV limit × appraised value)
- **DSCR constraint**: loan ≤ NOI / (min DSCR × debt constant)
- **Debt yield constraint**: loan ≤ NOI / minimum debt yield

The resulting proceeds, net of prepayment penalties, closing costs, and the payoff of the existing loan, determine the equity distribution to investors—the primary economic purpose of most refinances in value-add and opportunistic strategies.

## Formula

**Loan sizing from NOI (DSCR-based):**

Plain text:
`Max Loan (DSCR) = Stabilized NOI / (Minimum DSCR × Annual Debt Constant)`

$$
\text{Max Loan (DSCR)} = \frac{\text{Stabilized NOI}}{\text{Minimum DSCR} \times \text{Debt Constant}}
$$

Where:
- **Stabilized NOI** = underwritten net operating income at stabilization (not in-place NOI if still in lease-up); see [[Stabilized NOI]]
- **Minimum DSCR** = lender's required coverage ratio (typically 1.20x–1.35x for agency and permanent lenders; varies by product and market; current as of 2026-05-24)
- **Debt Constant** = annual debt service per dollar of loan (function of interest rate and amortization term)

**Loan sizing from Debt Yield:**

Plain text:
`Max Loan (Debt Yield) = Stabilized NOI / Minimum Debt Yield`

$$
\text{Max Loan (DY)} = \frac{\text{Stabilized NOI}}{\text{Minimum Debt Yield}}
$$

Where:
- **Minimum Debt Yield** = lender's required NOI/loan ratio (typically 7.0%–10.0%; varies by product, lender, and market; current as of 2026-05-24)

**Net refi proceeds:**

Plain text:
`Net Proceeds = Loan Amount - Existing Loan Payoff - Prepayment Penalty - Closing Costs`

$$
\text{Net Proceeds} = \text{Loan} - \text{Payoff} - \text{Prepayment} - \text{Costs}
$$

## When It's Used

The refinance decision is evaluated formally at three moments. First, **planned milestone refinances** built into the original underwriting—common in value-add deals structured as "bridge-to-perm," where the sponsor takes a short-term bridge loan during renovation and lease-up, then refinances into permanent debt once stabilized, typically returning a portion of equity to investors. Second, **opportunistic rate refinances** when market interest rates decline materially from the rate on existing debt, making a prepayment-and-refinance economically attractive even before the original loan matures. Third, **maturity-driven refinances** when the existing loan approaches its maturity date and the owner elects to extend the hold rather than sell.

The decision to refinance versus sell is analyzed in [[Hold vs. Sell Analysis]]. The refinance path makes sense when the equity IRR from holding—extended by the refi—exceeds the projected IRR from selling now; when the refi generates a meaningful return of capital that improves LP equity multiples; and when the owner believes the asset has further appreciation potential that a sale would forfeit.

## Variations & Edge Cases

Refinance execution differs by loan product. **Agency refinances** (Fannie Mae/Freddie Mac multifamily) are the most competitive in multifamily, offering long-term fixed rates and non-recourse execution, but require stabilized occupancy (typically 90%+ for 90 days) and have maximum LTV limits (currently 75–80% depending on loan type; varies; current as of 2026-05-24). **CMBS** (see [[CMBS]]) offers high proceeds on commercial properties but is inflexible post-closing (no partial prepayments, lockout periods). **Life company permanent loans** offer the best rates for trophy assets but are conservatively sized.

A critical edge case is the **defeasance or yield maintenance** prepayment on existing CMBS or life company loans, which can cost millions of dollars and dramatically reduce net refi proceeds. Owners must model the prepayment penalty explicitly when evaluating whether refinancing makes economic sense. In rising-rate environments, prepayment costs on fixed-rate loans are highest, making refinance less attractive even when appraised values have risen.

## Common Mistakes

The most common refinancing mistake is using in-place NOI rather than stabilized NOI to size loan proceeds, resulting in an overly optimistic proceeds estimate. A property in lease-up will have lower in-place NOI than its stabilized projection; lenders will underwrite to in-place (or a blended trailing/projected figure) and the actual proceeds will be lower than modeled. A second common error is ignoring the lender's debt yield floor—as interest rates decline, the DSCR constraint loosens and suggests more loan proceeds are available, but the debt yield constraint may still bind and cap proceeds below the DSCR-derived amount.

Owners also frequently underestimate closing costs and the timeline for refinancing, which can be 60–120 days from application to funding. If a bridge loan matures before the permanent loan closes, the owner faces a maturity default—a scenario that requires proactive management, typically by securing a short-term extension from the existing lender (which may carry a fee and an extension condition tied to debt paydown or stabilization milestones).

## Related Concepts

- [[Hold vs. Sell Analysis]] — the refinance decision is the primary alternative to disposition
- [[Permanent Loan]] — the typical destination for a bridge-to-perm refinance
- [[Bridge Loan]] — the loan commonly being replaced in a value-add refinance
- [[Agency Debt (Fannie/Freddie)]] — the most common permanent refi product for multifamily
- [[CMBS]] — alternative permanent debt product for commercial properties
- [[Debt Service Coverage Ratio (DSCR)]] — primary loan-sizing constraint
- [[Debt Yield]] — secondary loan-sizing constraint increasingly used by lenders
- [[Loan-to-Value (LTV)]] — third loan-sizing constraint based on appraised value
- [[Net Operating Income (NOI)]] — the NOI input that drives all three sizing constraints

## Sources

- Fannie Mae Multifamily Selling and Servicing Guide: underwriting criteria including DSCR, LTV, and debt yield requirements (fanniemae.com).
- Freddie Mac Multifamily: comparable underwriting standards (freddiemac.com).
- CCIM Institute: *CI 103 User Decision Analysis* — hold/refi/sell decision frameworks.
- Geltner, Miller, Clayton, Eichholtz: *Commercial Real Estate Analysis and Investments* — debt sizing and refinance analysis.
