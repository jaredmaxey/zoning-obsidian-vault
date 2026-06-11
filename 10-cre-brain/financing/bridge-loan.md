---
title: "Bridge Loan"
aliases: ["Bridge Loan"]
type: concept
tags: [cre/financing]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Short-term, floating-rate senior debt used to finance transitional or value-add properties until they stabilize and qualify for permanent financing.
domain: financing
formula: true
related:
  - "Senior Debt"
  - "Permanent Loan"
  - "Construction Loan"
  - "Bank Debt"
  - "Private Credit"
  - "Capital Stack Overview"
  - "Recourse vs. Non-Recourse"
  - "Bad-Boy Carve-Outs"
  - "Loan-to-Value (LTV)"
  - "Loan-to-Cost (LTC)"
  - "Debt Yield"
  - "Debt Service Coverage Ratio (DSCR)"
  - "Value-Add Acquisition"
  - "Refinance Decision Framework"
---

# Bridge Loan

## Definition

A bridge loan is a short-term, typically floating-rate, senior debt instrument used to finance a commercial real estate asset during a transitional period — before the asset's income, occupancy, or condition qualifies for permanent financing. The "bridge" metaphor is apt: the loan bridges from acquisition or early-stage execution to stabilization, at which point the borrower refinances into a longer-term permanent or agency loan. Bridge loans typically carry initial terms of 2–3 years with one or more one-year extension options (often subject to meeting performance tests), and are priced at floating rates indexed to SOFR or another benchmark, plus a spread that reflects the transitional risk (varies by market and vintage, current as of 2026-05-24).

Bridge loans are the workhorse financing vehicle for value-add acquisitions, lease-up plays, significant renovation programs, and repositioning transactions. Because the underlying asset does not yet generate the income needed to satisfy the DSCR tests required by agency or life company lenders, permanent financing is unavailable at acquisition. Bridge lenders — primarily debt funds, banks, and some life company credit arms — underwrite to stabilized or "as-stabilized" values and income, accepting the transitional risk in exchange for a higher spread and sometimes a participation in upside.

Sizing on bridge loans is typically governed by LTC (during the business plan period) or as-stabilized LTV, and debt yield tests are applied on a forward basis (stabilized NOI / loan amount). Many bridge lenders also impose an interest reserve at closing — a portion of the loan funded into an escrow to cover interest payments during the period when the property is generating below-market income, reducing the risk that the borrower cannot service the loan mid-business-plan. The interest reserve is particularly common on construction and heavy-renovation bridge loans.

## Formula

Bridge loan proceeds sizing (as-stabilized LTV basis and LTC basis):

**As-Stabilized LTV Sizing:**

- Plain text: `Max Loan = As-Stabilized_LTV × As-Stabilized_Value`
- LaTeX: $$ L_{max} = \text{LTV}_{stab} \times V_{stab} $$

**LTC Sizing:**

- Plain text: `Max Loan = LTC_max × Total_Project_Cost`
- LaTeX: $$ L_{max} = \text{LTC}_{max} \times C_{total} $$

**Interest Reserve:**

- Plain text: `Interest_Reserve = Loan_Amount × Floating_Rate × Reserve_Period_Years`
- LaTeX: $$ IR = L \times r_{float} \times t_{reserve} $$

Where:
- **LTV_stab** = as-stabilized LTV, typically 65%–75% for bridge (varies by asset class and lender; varies by market and vintage)
- **V_stab** = as-stabilized value (lender's underwritten stabilized NOI capitalized at market cap rate)
- **LTC_max** = maximum loan-to-cost ratio (often 70%–80% for bridge on value-add; varies by market and vintage)
- **C_total** = total project cost including acquisition, renovation/construction, carry, and closing costs
- **r_float** = floating interest rate (SOFR + spread; varies significantly by market and vintage, current as of 2026-05-24)
- **t_reserve** = anticipated interest reserve period in years (often 6–18 months)

## When It's Used

Bridge loans are the standard financing vehicle for value-add acquisitions across all major CRE asset classes. An investor purchasing a 75%-occupied multifamily property with plan to renovate units and push rents would use a bridge loan because the current NOI does not support permanent-loan DSCR or debt yield tests at any meaningful leverage level. The business plan is to execute the renovation, achieve stabilized occupancy and rents, and then refinance into agency debt or a CMBS permanent loan.

Bridge financing is also common in core-plus transactions where a short hold or near-term lease rollover creates temporary income uncertainty, in office or retail recapitalizations where some tenants are dark, and in sale-leaseback transactions where DSCR tests are in flux during early lease-up. In construction contexts, the final year of a construction loan often converts to a bridge loan (sometimes called a "construction-to-perm" or "mini-perm") to provide time for the project to lease up before permanent financing is sought.

From the lender's perspective, bridge loans are higher-risk than permanent loans and are priced accordingly. Lenders typically take recourse against the sponsor entity (with individual guaranty carve-outs for bad-boy acts; see [[Bad-Boy Carve-Outs]]) or structure the loan as non-recourse but price the spread wider. Bridge loans may also include origination fees (1%–2% of loan amount is common) and exit fees, creating a blended yield that is meaningfully higher than the stated interest rate.

## Variations & Edge Cases

"Heavy bridge" or "construction bridge" refers to loans funding major capital expenditures or substantial renovation programs, often with a draw structure similar to a construction loan. "Light bridge" or "transitional bridge" funds primarily the acquisition with a small capex holdback, suitable for properties requiring only moderate rehabilitation. The distinction affects lender due diligence depth, reserve structure, and pricing.

Some deals use a "stretch senior" bridge loan — a bridge lender willing to go to 75%–80% LTC at a higher spread, effectively eliminating the need for mezzanine debt. Others use a bridge loan in combination with mezzanine or preferred equity to achieve higher total leverage. The choice depends on deal economics, lender relationships, and the relative cost of additional leverage. See [[Senior Debt]] and [[Mezzanine Debt]] for the surrounding context.

## Common Mistakes

The most common bridge loan mistake is underestimating the all-in cost of capital. The stated floating rate is only part of the cost — origination fees, exit fees, extension fees, interest reserves funded at closing (which reduce net proceeds and increase effective cost), and the optionality value of extension tests must all be incorporated into the effective financing cost. A bridge loan at SOFR + 250 bps with a 1.5% origination fee and a 0.5% exit fee can carry an effective yield meaningfully above the headline spread over a typical 2–3 year hold.

A second recurring mistake is failing to model the refinance risk at the end of the bridge period. Bridge loans are underwritten to a take-out scenario (refinancing into permanent financing at stabilization), and if the business plan lags — slower lease-up, higher vacancy, softer rents, or rising cap rates — the borrower may not qualify for the assumed permanent loan at the assumed loan amount. Failing to stress-test the take-out scenario and model the equity impact of a shortfall is a critical gap in bridge loan underwriting.

## Related Concepts

See [[Senior Debt]] for the structural position bridge loans occupy. [[Permanent Loan]] is the take-out financing target after stabilization. [[Construction Loan]] is the analogous transitional product for ground-up development. [[Bank Debt]] and [[Private Credit]] are the primary providers of institutional bridge financing. [[Refinance Decision Framework]] in operations covers the take-out timing decision. [[Loan-to-Cost (LTC)]] and [[Loan-to-Value (LTV)]] are the primary sizing metrics.

## Sources

Bridge loan structuring and pricing conventions are discussed in the Mortgage Bankers Association's *Commercial/Multifamily Finance* resources and in practitioner materials from CREFC. The shift from LIBOR to SOFR as the floating-rate benchmark (complete by mid-2023) affected all floating-rate bridge loan structures; see ARRC (Alternative Reference Rates Committee) guidance for transition mechanics. Geltner et al., *Commercial Real Estate Analysis and Investments*, 3rd ed., provides context on transitional financing within the deal lifecycle.
