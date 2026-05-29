---
title: "Rent Roll Maintenance"
type: concept
tags: [cre/operations]
created: "2026-05-24"
updated: "2026-05-24"
status: draft
ai_summary: Live, unit-by-unit occupancy and rent record that is the primary data source for underwriting, lender reporting, and disposition due diligence on any income-producing property.
domain: operations
formula: false
related:
  - "Lease Administration"
  - "Property Management Fundamentals"
  - "Rent Roll Analysis"
  - "Effective Gross Income (EGI)"
  - "Vacancy and Collection Loss"
  - "Net Operating Income (NOI)"
  - "Stabilized NOI"
  - "Asset Management vs. Property Management"
---

# Rent Roll Maintenance

## Definition

A rent roll is a tabular record of every leasable unit or suite in a property, showing for each: the tenant name (or "vacant"), lease start and expiration dates, contracted monthly and annual rent, any concessions in effect (free-rent periods, rent abatements), lease type (gross, modified gross, NNN), and often square footage and rent per square foot. Rent roll maintenance is the ongoing discipline of keeping this dataset current and accurate—updated with every new lease, renewal, amendment, move-out, and rate change—so it reflects actual in-place economic conditions at any given moment. The rent roll is the foundational data set from which [[Net Operating Income (NOI)]] projections, [[Effective Gross Income (EGI)]] calculations, and [[Vacancy and Collection Loss]] estimates are derived.

The rent roll is not a static document prepared only for due diligence; it is a living operational record. Property management software (Yardi, MRI, RealPage, Appfolio, etc.) maintains the rent roll as a database, enabling real-time queries: current occupancy, upcoming expirations within 90 days, delinquency by tenant, and average in-place rent versus market rent. When a property management firm takes over a new asset, reconciling the physical lease files against the rent roll is one of the first operational tasks, because discrepancies—side letters, informal rent concessions, undocumented tenants—are common and consequential.

The rent roll's accuracy directly affects valuation. Buyers and lenders use it to underwrite purchase price and loan proceeds. An inflated or stale rent roll that overstates occupancy or scheduled rents will produce an inflated NOI and, at any given cap rate, an inflated indicated value. This is why sophisticated buyers require both a current rent roll and a trailing-12-month income statement, then cross-check the two: if scheduled rent on the roll exceeds actual collected rent on the statement, the delta represents collection loss, concessions, or reporting error—all of which must be explained and adjusted.

## When It's Used

Rent roll maintenance is a continuous property-management function but surfaces prominently at five points. (1) **Monthly close**: the PM produces a month-end rent roll alongside the operating statement; together they form the basis of investor and lender reporting. (2) **Underwriting at acquisition**: buyers request a current rent roll (typically dated within 30–60 days of closing) to underwrite the deal; see [[Rent Roll Analysis]]. (3) **Loan origination and refinance**: lenders require a certified rent roll as part of the loan application package; agency lenders (Fannie, Freddie) have specific form requirements. (4) **Annual budget preparation**: the asset manager uses the rent roll to project the coming year's scheduled rent, identify expiration risk, and set renewal and re-leasing targets. (5) **Disposition**: the offering memorandum (OM) package prepared by the broker is built on the rent roll, and buyer due diligence will scrutinize it against executed leases.

## Variations & Edge Cases

Rent roll format and depth vary by asset class. A **multifamily** rent roll typically shows unit number, unit type, square footage, current resident, lease start/end, market rent, scheduled rent, actual collected rent, and concessions. A **commercial** (office/retail/industrial) rent roll adds lease type, TI allowance balance, renewal options, and rent escalation schedule—effectively overlapping with the lease abstract produced by [[Lease Administration]]. For **mixed-use** properties, a single rent roll must track both residential and commercial tenancies, often in different sub-schedules.

A critical nuance is the distinction between **scheduled rent** (what the lease says) and **collected rent** (what actually hits the bank). Lenders and buyers using scheduled rent from the roll without adjusting for chronic delinquency or concession burn-off are overestimating EGI. Properties with significant lease-up concessions (e.g., 2 months free on a 12-month lease) may show full scheduled rent on the roll but zero cash in certain months—this must be footnoted in the roll and modeled correctly in [[Stabilized NOI]] projections.

## Common Mistakes

The most common error is maintaining the rent roll as a static spreadsheet rather than a system-of-record, leading to version-control problems where different stakeholders are working from different vintages of the document. Critical decisions (refinance sizing, disposition pricing, board reporting) should always reference the system-of-record rent roll extracted from the PM software, not a manually maintained spreadsheet.

A second frequent error is failing to mark units under concession clearly, so the roll shows "occupied" and "full rent" for units that are actually in a free-rent period. This inflates apparent occupancy and EGI. Buyers who catch this in due diligence will discount the price; buyers who miss it will face a NOI shortfall after close. Owners should also maintain a separate delinquency aging report in parallel with the rent roll, since a tenant can appear "current" on the roll but be 60 days past due on actual payments.

## Related Concepts

- [[Lease Administration]] — the lease-document tracking function that feeds the rent roll with critical-date and economic-term data
- [[Property Management Fundamentals]] — the broader PM function responsible for maintaining the roll
- [[Rent Roll Analysis]] — the buyer/lender analysis performed on the rent roll during underwriting
- [[Effective Gross Income (EGI)]] — calculated from rent roll data adjusted for vacancy and credit loss
- [[Vacancy and Collection Loss]] — the deduction from scheduled rent reflected in EGI
- [[Net Operating Income (NOI)]] — derived from EGI less operating expenses
- [[Stabilized NOI]] — forward projection that relies on an accurate rent roll as its starting point

## Sources

- IREM: *Principles of Real Estate Management* — operational reporting standards including rent roll best practices.
- Fannie Mae/Freddie Mac: Multifamily underwriting guidelines specifying certified rent roll requirements for agency loans.
- CCIM Institute: *CI 101 Financial Analysis for Commercial Investment Real Estate* — rent roll analysis in underwriting context.
- Yardi Systems: rent roll reporting documentation (yardi.com).
