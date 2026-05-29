---
title: "Loan-to-Value (LTV)"
type: concept
tags: [cre/concepts]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: LTV is the ratio of the loan amount to the appraised property value, serving as the primary collateral-based constraint on CRE loan sizing and a key risk indicator for lenders.
domain: concepts
formula: true
related:
  - "Loan-to-Cost (LTC)"
  - "Debt Service Coverage Ratio (DSCR)"
  - "Debt Yield"
  - "Cap Rate"
  - "Senior Debt"
  - "CMBS"
  - "Agency Debt (Fannie/Freddie)"
  - "Bridge Loan"
  - "Mezzanine Debt"
  - "Capital Stack Overview"
  - "Recourse vs. Non-Recourse"
---

# Loan-to-Value (LTV)

## Definition

Loan-to-value (LTV) is the ratio of the outstanding loan principal to the appraised or assessed market value of the collateral property, expressed as a percentage. It is the fundamental collateral-based constraint on CRE lending: a lender who caps LTV at 65% will not lend more than $65 for every $100 of appraised value, regardless of how strong the cash flow looks. LTV protects the lender's position by ensuring the loan balance sits well below the property's estimated liquidation value — so that if the borrower defaults, the lender can recover the full loan through foreclosure.

LTV is determined at origination using an independent appraisal (for regulated lenders) or an internal valuation for some private credit lenders. The key input is the appraised value, which uses the [[Cap Rate]] to capitalize stabilized NOI — meaning that LTV is downstream of cap rates: when cap rates compress (values rise), the same NOI supports higher loan amounts. When cap rates expand (values fall), LTVs rise on existing loans, sometimes breaching covenant triggers or creating difficulties at refinancing.

LTV must be analyzed alongside [[Debt Service Coverage Ratio (DSCR)]] and [[Debt Yield]] because all three constrain loan sizing simultaneously. In many market environments, DSCR is the binding constraint on high-quality, cash-flowing assets; on newly constructed or recently repositioned properties with compressed cap rates, LTV may become binding. The maximum loan amount is the lower of the LTV-constrained amount and the DSCR-constrained amount.

## Formula

- Plain text: `LTV = Loan Amount / Appraised Value`
- LaTeX: $$ \text{LTV} = \frac{\text{Loan Amount}}{\text{Appraised Value}} $$

**Where:**
- **Loan Amount** — the outstanding principal balance of the loan at origination (or at any measurement date for ongoing compliance)
- **Appraised Value** — the market value conclusion from an independent MAI appraisal (for bank, agency, and CMBS loans) or an internal valuation (for some private credit lenders); may be "as-is" or "as-stabilized" depending on the loan type

Rearranging: `Max Loan = Appraised Value × Maximum LTV`

## When It's Used

LTV is tested at origination for every institutional CRE loan. Lenders set maximum LTV by loan program, asset class, and market conditions. As of 2026-05-24, typical LTV ranges for stabilized assets vary: agency multifamily programs may allow up to 75–80% LTV, life company loans are often in the 55–65% range, CMBS conduit loans often cap at 65–75%, and bank CRE loans vary widely (varies by market and vintage). Bridge loans and construction loans may use LTC instead of LTV during the construction or repositioning period — see [[Loan-to-Cost (LTC)]].

In ongoing loan monitoring, lenders track LTV as part of covenant compliance. If values decline materially (e.g., a market correction or a property suffering occupancy loss), the loan may breach a "maximum LTV" maintenance covenant, triggering cure requirements or accelerated cash sweeps. CMBS special servicers focus on LTV when assets are in special servicing, as it determines whether a discounted payoff is viable for the lender.

For borrowers, LTV determines equity requirement: a 65% LTV loan on a $10M acquisition requires $3.5M of equity. Borrowers who want more leverage may use mezzanine debt or preferred equity to fill the gap between the senior loan and their desired total leverage — pushing the blended LTV higher while keeping the senior loan within the lender's constraint. See [[Mezzanine Debt]] and [[Capital Stack Overview]].

## Variations & Edge Cases

**As-is vs. as-stabilized LTV:** For value-add or development loans, lenders may underwrite to an "as-stabilized" value (the projected value at stabilization, which is higher), allowing a larger initial loan. The risk is that the as-stabilized value never materializes. Most regulated lenders require as-is LTV to be within policy limits even if as-stabilized LTV is the primary sizing basis.

**Combined LTV (CLTV):** When mezzanine debt or preferred equity sits above the senior loan, the total indebtedness as a percentage of value is the combined LTV (CLTV). Senior lenders typically intercreditor agreements that cap CLTV at a specified level.

**Mark-to-market LTV:** On maturing loans or in stress scenarios, lenders revalue the collateral at current market cap rates. In a cap rate expansion cycle, properties may have experienced significant value decline, bringing the mark-to-market LTV above the original underwritten LTV. This is the mechanism by which a real estate cycle downturn creates distressed loan refinancing challenges.

## Common Mistakes

**Relying solely on LTV without testing DSCR.** A property can be at 60% LTV and still not cover its debt service if NOI is thin relative to the loan amount. LTV protects against collateral risk but not income coverage risk.

**Using purchase price instead of appraised value.** The loan is sized against appraised value, not the agreed purchase price. When a borrower pays above-appraised value, the effective LTV is higher than the nominal calculation suggests.

**Ignoring LTV drift over the hold.** As a loan amortizes (or doesn't, on IO loans), LTV changes relative to value. On IO loans with stagnant NOI, LTV may not decrease and can increase if values soften, creating refinancing difficulty at maturity.

## Related Concepts

- [[Loan-to-Cost (LTC)]] — the analog for development and construction loans, substituting total project cost for appraised value
- [[Debt Service Coverage Ratio (DSCR)]] — the income-based loan sizing constraint that operates simultaneously with LTV
- [[Debt Yield]] — a third sizing metric that lenders use alongside LTV and DSCR
- [[Senior Debt]] — the primary loan type to which LTV constraints apply
- [[CMBS]] — securitized debt with LTV as a key origination and rating test
- [[Agency Debt (Fannie/Freddie)]] — multifamily programs with specific LTV limits by loan type
- [[Bridge Loan]] — shorter-term loan where LTV may be measured as-is vs. as-stabilized
- [[Mezzanine Debt]] — a layer of additional leverage that pushes combined LTV above senior LTV limits
- [[Capital Stack Overview]] — the framework for understanding how LTV fits within total deal leverage

## Sources

LTV standards are set by individual lender programs, banking regulators (OCC, FDIC real estate lending guidelines), and the GSEs (Fannie Mae/Freddie Mac seller-servicer guides). CMBS LTV standards are published by rating agencies (Moody's, S&P, Fitch). Specific LTV limits vary by program, asset class, and market cycle (varies by market and vintage; current as of 2026-05-24).
