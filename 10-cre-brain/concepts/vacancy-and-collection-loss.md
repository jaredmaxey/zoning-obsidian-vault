---
title: "Vacancy and Collection Loss"
type: concept
tags: [cre/concepts]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Vacancy and collection loss is the revenue reduction applied to gross potential rent to account for unleased space and uncollected receivables, forming a critical underwriting assumption in every CRE pro forma.
domain: concepts
formula: true
related:
  - "Net Operating Income (NOI)"
  - "Effective Gross Income (EGI)"
  - "Stabilized NOI"
  - "Pro Forma Construction Method"
  - "Absorption Rate"
  - "T-12 and T-3 Analysis"
  - "Expense Normalization"
  - "Rent Roll Analysis"
---

# Vacancy and Collection Loss

## Definition

Vacancy and collection loss is the aggregate reduction to gross potential rent (GPR) that accounts for: (1) physical vacancy — space that is unleased and generating no rent; and (2) credit loss (collection loss) — rent that is owed by tenants but not collected due to delinquency, default, or disputed billing. Together, these items convert gross potential rent (100% occupancy at market rents) to the actual, collectible revenue base. In most institutional pro formas, vacancy and collection loss are combined into a single line-item deduction applied as a percentage of GPR.

Vacancy is the more predictable and better-benchmarked component: market vacancy rates are tracked by CoStar, CBRE, JLL, and other data providers at the submarket level by asset class. Institutional underwriters set their vacancy assumption to reflect the realistic long-term stabilized vacancy rate for the specific submarket and asset type, not the current best-case occupancy. For a new development, additional "absorption vacancy" — the time needed to initially lease up from zero occupancy — is separate from stabilized long-run vacancy and is modeled during the construction/lease-up phase.

Collection loss is asset-class specific and tenant-quality dependent. For institutional-quality multifamily with strong credit screening, collection loss may be a fraction of 1% of GPR under normal conditions. For affordable housing or working-class apartment communities, collection loss can be 2–4% or more. For retail with small local tenants in a stressed economic environment, collection loss can spike significantly. Lenders and appraisers set collection loss assumptions based on the tenant credit profile and historical data for comparable properties.

## Formula

- Plain text: `Vacancy & Collection Loss = GPR × (Vacancy Rate + Collection Loss Rate)`
- LaTeX: $$ \text{V\&CL} = \text{GPR} \times (v + c) $$

**Where:**
- **GPR** — Gross Potential Rent: total scheduled income at 100% occupancy and current market/contract rents
- **v** — Vacancy rate: the percentage of units/space expected to be unleased in a stabilized operating year
- **c** — Collection loss rate: the percentage of GPR expected to be uncollected from lease defaults, delinquencies, or write-offs

EGI = GPR − Vacancy & Collection Loss (simplified). In practice, other income is added before or after; see [[Effective Gross Income (EGI)]].

## When It's Used

Vacancy and collection loss assumptions are the most scrutinized underwriting assumption in lender and equity review, because small changes compound significantly into NOI and value. A property with $1,000,000 of GPR: at 5% vacancy + 1% collection loss, the deduction is $60,000, leaving $940,000 EGI. At 8% vacancy + 2% collection loss, the deduction is $100,000, leaving $900,000 EGI — a $40,000 NOI difference that at a 5.5% cap rate is worth $727,000 in value. Lenders typically apply their own submarket vacancy floor (minimum vacancy assumption) regardless of the borrower's claim of current full occupancy.

Appraisers select vacancy and collection loss assumptions in the income approach based on comparable property operating histories and submarket data. For a recently stabilized asset, historical vacancy trends are critical context; for a new construction project, lease-up assumptions drive the absorption period cash flow model. See [[Absorption Rate]].

For value-add acquisitions, the underwriting explicitly models the path from current elevated vacancy (often 70–85% occupancy) to stabilized market vacancy (90–95%). This "lease-up" modeling requires assumptions about monthly absorption, concessions offered, and timing — all of which feed into the pro forma vacancy and collection loss line.

## Variations & Edge Cases

**Economic vacancy vs. physical vacancy:** Physical vacancy is the share of space that is unleased. Economic vacancy also includes leased space at below-market rates (above-market-rent leases have negative economic vacancy), concessions (free rent periods), and the present-value cost of lease-up periods. Institutional pro formas typically model physical vacancy but may include a separate concession line.

**Asset class differences:** Vacancy benchmarks vary enormously by asset class. Industrial has historically run at very low vacancy in supply-constrained markets; central business district office in post-pandemic markets has seen elevated structural vacancy. As of 2026-05-24, vacancy rates across asset classes vary significantly by market, with some office submarkets running double-digit vacancy while top industrial submarkets remain near historic lows (varies by market and vintage).

**NNN vs. gross leases:** In a triple-net lease, vacancy loss falls entirely on the landlord (lost base rent), while in a gross lease, the landlord also avoids paying tenant-reimbursable expenses on vacant space, partially offsetting the vacancy impact.

## Common Mistakes

**Using current occupancy instead of stabilized vacancy.** A property currently at 97% occupancy does not warrant a 3% vacancy assumption in perpetuity. Market stabilized vacancy reflects the long-run average for the submarket — which may be higher if the current occupancy reflects temporary conditions or a favorable lease.

**Separating vacancy from collection loss and then underestimating both.** Some sponsors break out vacancy and collection loss but apply unrealistically low assumptions to each. The combined V&CL rate should be benchmarked against comparable property operating histories and lender underwriting standards.

**Applying national averages.** Vacancy rates are intensely local. Using a national average multifamily vacancy rate for a deal in a specific submarket with different supply/demand dynamics produces an unreliable underwriting.

## Related Concepts

- [[Net Operating Income (NOI)]] — vacancy and collection loss is the primary deduction between GPR and EGI, directly impacting NOI
- [[Effective Gross Income (EGI)]] — the resulting income base after applying vacancy and collection loss
- [[Stabilized NOI]] — the NOI projection based on a normalized stabilized vacancy assumption
- [[Absorption Rate]] — the rate at which vacant space is absorbed by new leasing activity
- [[Pro Forma Construction Method]] — the line-by-line methodology in which vacancy and collection loss is a primary input
- [[Rent Roll Analysis]] — the current-leases analysis that informs in-place vs. market vacancy
- [[T-12 and T-3 Analysis]] — historical operating data used to calibrate realistic vacancy and collection loss assumptions

## Sources

Vacancy data by asset class and submarket is published by CoStar, CBRE, JLL, Cushman & Wakefield, and Yardi Matrix. Collection loss benchmarks are derived from property operating statements and lender guidelines. Appraisal Institute guidelines address vacancy and collection loss in income property appraisal. All figures vary by market, vintage, and economic conditions (varies by market and vintage; current as of 2026-05-24).
