---
title: "Rent Roll Analysis"
aliases: ["Rent Roll Analysis"]
type: framework
tags: [cre/underwriting, cre/frameworks]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Systematic review of a property's rent roll to assess in-place income quality, lease structure, rollover risk, and mark-to-market upside or downside.
inputs_required:
  - Current rent roll (tenant name, unit/suite, SF, lease start/end, in-place rent, renewal options)
  - Market rent comparables
  - Lease abstracts or lease documents
  - Operating expense structure (gross, NNN, modified gross)
outputs:
  - Weighted average in-place rent vs. market rent (mark-to-market gap)
  - Lease expiration schedule and rollover exposure
  - Tenant concentration risk assessment
  - Stabilized income estimate
  - Upside/downside rent scenarios
related:
  - "Pro Forma Construction Method"
  - "Expense Normalization"
  - "T-12 and T-3 Analysis"
  - "Assumption Hierarchy: Actual vs. Pro Forma"
  - "Net Operating Income (NOI)"
  - "Effective Gross Income (EGI)"
  - "Vacancy and Collection Loss"
  - "Stabilized NOI"
  - "Comparable Rents (Rent Comps)"
---

# Rent Roll Analysis

## Purpose

Rent roll analysis is the discipline of dissecting the lease-by-lease detail of a property's current income to evaluate income quality, durability, and upside or downside from current market conditions. Every CRE acquisition or refinance underwrites a cash flow stream, not a building — and that stream flows directly from the rent roll. A seemingly strong headline NOI can mask deep rollover risk, below-market anchor leases, or heavy tenant concentration that would unravel it. Conversely, a rent roll where in-place rents are materially below market represents a quantifiable upside catalyst.

An analyst reaches for this framework at the earliest stage of diligence — often before any financial model is built — because rent roll quality shapes every downstream assumption in the [[Pro Forma Construction Method]]. Lenders, equity underwriters, and appraisers each scrutinize the rent roll for different risk vectors: lenders focus on near-term lease expirations within the loan term; equity investors focus on mark-to-market and rollover timing; appraisers focus on contract versus market rent differentials to determine appropriate cap rate selection.

## Inputs Required

- **Rent roll (current):** Tenant or unit ID, leased area (SF or units), lease commencement date, lease expiration date, current annual base rent ($/SF/year or $/unit/month), renewal options, and any rent escalation clauses. Sourced from the property owner or property manager.
- **Lease abstracts or full leases:** Confirm rent, term, options, co-tenancy clauses, termination rights, and expense structure. Sourced from seller disclosure package or direct lease review.
- **Expense reimbursement structure:** NNN, gross, modified gross, base-year stop, or expense cap. Determines how much of OpEx is borne by tenants vs. the landlord, affecting NOI comparability.
- **Market rent comparables:** Current asking and effective rents for comparable space in the submarket. Sourced from [[Comparable Rents (Rent Comps)]], broker surveys, CoStar, and Yardi.
- **Historical vacancy and collections:** Prior T-12 rent receipts vs. rent roll billing. Identifies chronic slow-pay or vacant units not yet reflected on the roll.

## Method

1. **Ingest and clean the rent roll.** Obtain the rent roll in spreadsheet form. Verify unit/suite counts, total rentable square footage (or unit count), and reconcile to the property's offering memorandum or rent schedule. Flag any discrepancies between scheduled rent and collected rent per [[T-12 and T-3 Analysis]].

2. **Compute weighted average in-place rent.** Calculate average in-place rent per SF (commercial) or per unit (multifamily), weighted by leasable area or unit count. This is the baseline against which market rent is benchmarked.
   - Plain text: `WAIR = Σ(rent_i × SF_i) / Σ(SF_i)`
   - LaTeX: $$ WAIR = \frac{\sum_{i} r_i \cdot sf_i}{\sum_{i} sf_i} $$
   - Where: WAIR = weighted average in-place rent; r_i = annual rent per SF for tenant i; sf_i = leased SF for tenant i.

3. **Compute mark-to-market gap.** Compare WAIR to current market rent from comparables. The gap expressed as a percentage indicates the direction and magnitude of rent upside or downside upon lease rollover.
   - Plain text: `MTM gap % = (Market Rent − In-Place Rent) / In-Place Rent`
   - LaTeX: $$ MTM = \frac{r_{market} - r_{inplace}}{r_{inplace}} $$
   - A positive MTM indicates in-place rents are below market (upside); negative indicates above-market leases (rollover downside risk).

4. **Build lease expiration schedule.** Group leases by expiration year and calculate the percentage of total revenue and total SF expiring in each year of the hold period. Identify years with concentrated expirations (cliff risk). For commercial properties, any year with more than 20–30% of revenue rolling creates material re-leasing uncertainty.

5. **Assess tenant concentration risk.** Compute each tenant's share of total base rent revenue. A single tenant exceeding 20–25% of revenue, or a top-3 group exceeding 50%, constitutes meaningful concentration. Evaluate each major tenant's credit quality (public vs. private, industry, lease guarantee structure).

6. **Review lease economics and embedded optionality.** Flag renewal options — are they at fixed rents, fair market value, or CPI? Fixed-rate renewals below current market can impair upside. Termination rights or co-tenancy clauses (common in retail) introduce embedded lease-break risk that must be scenario-planned. Verify any free rent, tenant improvement (TI) obligations, or landlord work remaining under existing leases.

7. **Construct base and stress-case income scenarios.** Model the rent roll forward lease-by-lease. Base case: renewals at current market rent; downtime between leases of 3–9 months (varies by asset class and market); new TI and leasing commissions. Bear case: some tenants do not renew; leases at a discount to market with extended downtime.

## Outputs

The rent roll analysis produces: (1) a weighted average in-place rent and mark-to-market gap summary; (2) a lease expiration schedule showing revenue and SF rolling by year; (3) tenant concentration metrics; (4) identified lease-level risks (options, termination rights, co-tenancy clauses); and (5) a base and stress-case income projection that feeds directly into the [[Pro Forma Construction Method]].

## Example Walkthrough

*All figures below are illustrative and hypothetical — not derived from any real transaction.*

Consider a 50,000 SF suburban office building with 5 tenants. Tenant A (20,000 SF, $20/SF NNN, expires Year 1), Tenant B (15,000 SF, $22/SF NNN, expires Year 3), Tenants C/D/E (15,000 SF combined, $18–21/SF NNN, expires Year 5+). Current market rent: $24/SF NNN. WAIR: ($20×20k + $22×15k + $19.5×15k) / 50k = $20.79/SF. MTM gap: ($24−$20.79)/$20.79 = +15.4% upside. Tenant A (40% of revenue) expiring in Year 1 is the critical risk — if not renewed, $400,000 in annual rent is at risk with 3–6 months downtime and $30/SF in TI and leasing commissions to replace. This single expiration event would cause a year of negative levered cash flow under the base case, a fact that must be priced into acquisition underwriting.

## Limitations

The rent roll is a snapshot as of a single date and can be presented favorably by sellers — always request the most recent 12-month rent receipts to cross-check against the roll. Commercial leases are long and complex; a rent roll summary necessarily simplifies; critical deal points (options, termination rights, landlord obligations) live in the lease documents, not the summary. Multifamily rent rolls are simpler in structure but higher in tenant turnover, requiring different attention to loss-to-lease versus street rent dynamics.

## Related Frameworks

[[Pro Forma Construction Method]] — the rent roll populates the income section of the pro forma. [[T-12 and T-3 Analysis]] — validates actual collections vs. scheduled rents. [[Expense Normalization]] — the companion framework for the expense side. [[Assumption Hierarchy: Actual vs. Pro Forma]] — governs how much weight to put on in-place vs. projected rents. See also [[Net Operating Income (NOI)]], [[Effective Gross Income (EGI)]], [[Stabilized NOI]], and [[Comparable Rents (Rent Comps)]].

## Sources

CCIM Institute, *Lease Analysis and Income Property Valuation* coursework. CoStar and Yardi market data methodologies. Standard institutional due-diligence practice as described in REPE underwriting manuals from major private equity real estate managers.
