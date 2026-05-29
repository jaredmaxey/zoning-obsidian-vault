---
title: "Operating Expense Ratio"
type: concept
tags: [cre/concepts]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Operating expense ratio is the percentage of effective gross income consumed by operating expenses, serving as a benchmark for expense efficiency and a key underwriting check on pro forma credibility.
domain: concepts
formula: true
related:
  - "Net Operating Income (NOI)"
  - "Effective Gross Income (EGI)"
  - "Vacancy and Collection Loss"
  - "Reserves for Replacement"
  - "Pro Forma Construction Method"
  - "Expense Normalization"
  - "T-12 and T-3 Analysis"
  - "Stabilized NOI"
---

# Operating Expense Ratio

## Definition

The operating expense ratio (OER) is the percentage of a property's effective gross income consumed by operating expenses (excluding debt service and capital expenditures). It is a fundamental efficiency benchmark: a low OER means the property converts a large share of its gross income into NOI; a high OER means operating costs are consuming a large portion of revenue. The OER provides a quick sanity check on underwriting — if a pro forma presents an unusually low OER relative to market norms, it is a red flag that expenses may be understated or excluded.

OER varies significantly by asset class, lease structure, age of property, and management intensity. Apartment buildings tend to have OERs in the 35–55% range depending on vintage and whether utilities are included in rent; NNN retail properties with tenants paying all operating expenses may have OERs as low as 10–20% at the landlord level; gross-leased office buildings can have OERs of 40–60%. Self-storage tends toward lower OERs due to minimal tenant services; hotels and hospitality have the highest OERs in CRE, often 60–80%, because they are operationally intensive businesses.

Understanding OER in the context of lease structure is critical. In a triple-net (NNN) lease, tenants pay property taxes, insurance, and maintenance directly — so the landlord's OER is very low because most expenses never appear in the landlord's income statement. In a gross lease, the landlord pays all expenses and the OER is much higher. Comparing OERs across different lease structures without adjustment is meaningless.

## Formula

- Plain text: `OER = Operating Expenses / Effective Gross Income`
- LaTeX: $$ \text{OER} = \frac{\text{Operating Expenses}}{\text{EGI}} $$

**Where:**
- **Operating Expenses** — all expenses required to operate the property: property taxes, insurance, management fees, maintenance and repairs, utilities (where landlord-pays), landscaping, janitorial, administrative, and other recurring operating costs. Excludes debt service, depreciation, income taxes, and capital expenditures. The treatment of [[Reserves for Replacement]] varies — including reserves in operating expenses produces a higher OER.
- **EGI (Effective Gross Income)** — gross potential rent less vacancy and collection loss plus other income; see [[Effective Gross Income (EGI)]].

Equivalently: `OER = 1 − (NOI / EGI)`, since NOI = EGI − Operating Expenses.

## When It's Used

OER is used primarily as a due diligence screening and benchmarking tool. When a buyer reviews a seller's offering memorandum, one of the first checks is whether the presented OER is plausible for the asset class and market. Sellers and their brokers sometimes present "proforma" expense ratios that exclude management fees (for self-managed properties), understate insurance, or omit certain maintenance categories — all of which inflate NOI and the implied value. A buyer who benchmarks the presented OER against market norms and BOMA operating expense surveys quickly identifies these manipulations. See [[Expense Normalization]].

Lenders use OER benchmarks to stress-test borrower pro formas. Many institutional lenders apply a minimum OER (expense floor) to ensure they are not lending on a sandbagged expense assumption. For example, an agency lender may require a minimum 35% OER for a multifamily property regardless of what the borrower projects — effectively setting a floor on underwritten expenses.

In asset management, tracking actual OER against budget and against peer properties is a standard performance monitoring tool. A rising OER (expenses growing faster than income) signals deteriorating operational efficiency — possibly due to deferred maintenance catching up, aging systems, or management inefficiency.

## Variations & Edge Cases

**Including vs. excluding reserves:** Some OER calculations include reserves for replacement as an operating expense; others treat reserves as below-the-line. The convention affects comparability. Institutional analysis often excludes reserves from the OER calculation (showing them separately) but then deducts them from cash flow before distributing to equity.

**Gross vs. net lease OER:** As described above, OER is deeply sensitive to lease structure. A 15% OER for a NNN retail strip is not "better" than a 40% OER for a gross-leased apartment complex — they reflect fundamentally different landlord-expense responsibility structures.

**Management fee inclusion:** Owner-occupied or self-managed properties must have a market-rate management fee (typically 3–6% of EGI depending on asset class and size) imputed as an operating expense. Failing to include it produces an unreliably low OER and overstated NOI.

OER benchmarks by asset class vary (current as of 2026-05-24). Multifamily: roughly 35–55% depending on vintage and utility structure. NNN retail: 10–25% landlord OER. Gross office: 40–60%. Hospitality: 60–80% (varies by market and vintage).

## Common Mistakes

**Accepting OER from the seller's offering memorandum without normalization.** Marketing materials present best-case financials. Always normalize expenses — add management fees, estimate realistic maintenance, verify tax assessments, stress insurance — before relying on the OER.

**Comparing OERs across lease structures.** A NNN property with a 15% OER looks "more efficient" than a gross-leased property with a 45% OER, but the comparison is not valid. The tenant is paying the expenses in the NNN case; they're just not appearing in the landlord's OER.

**Forgetting that OER is a percentage of EGI, not GPR.** If vacancy is high, EGI is low, and a fixed level of expenses represents a higher OER percentage. A distressed asset with 70% occupancy will show a higher OER than the same asset at 95% occupancy even with identical expense dollars.

## Related Concepts

- [[Net Operating Income (NOI)]] — the complement: NOI = EGI × (1 − OER)
- [[Effective Gross Income (EGI)]] — the denominator; revenue efficiency is measured relative to collected income
- [[Vacancy and Collection Loss]] — reduces EGI and thereby amplifies the OER if expenses are fixed
- [[Reserves for Replacement]] — treatment of reserves affects OER calculation
- [[Expense Normalization]] — the underwriting process of adjusting expenses to market norms
- [[T-12 and T-3 Analysis]] — the historical data used to assess actual vs. underwritten OER
- [[Stabilized NOI]] — produced by applying a normalized OER to stabilized EGI

## Sources

OER benchmarks are published by BOMA (Building Owners and Managers Association) operating experience reports, IREM (Institute of Real Estate Management) income/expense reports by property type, and NCREIF. Lender-specific OER floors are published in agency guidelines. All benchmarks vary by asset class, vintage, and market conditions (varies by market and vintage; current as of 2026-05-24).
