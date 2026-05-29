---
title: Office — Key Metrics
type: asset-class
tags: [cre, asset/office]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Defines office-specific key performance metrics including net effective rent, TI/LC amortization, WALT, occupancy, load factor, parking ratio, and expense recovery.
asset_class: office
subtypes: []
related:
  - Office
  - Office — Underwriting Norms
  - Office — Risks & Considerations
  - Net Operating Income (NOI)
  - Effective Gross Income (EGI)
  - Vacancy and Collection Loss
  - Operating Expense Ratio
  - Absorption Rate
  - Rent Roll Analysis
  - Discounted Cash Flow (DCF)
  - Price per Square Foot
---

# Office — Key Metrics

Office investment analysis relies on a set of class-specific metrics that go beyond generic CRE measures. Because office cash flows are driven by multi-year leases with embedded concession packages, and because income can diverge significantly from face rent, metrics that capture lease economics in full are essential for accurate underwriting and portfolio monitoring.

---

### Net Effective Rent (NER)

**Definition.** Net effective rent is the true economic rent per square foot per year (or month) after subtracting the amortized cost of tenant improvement allowances and free-rent periods from the nominal face rent. NER allows apples-to-apples comparison of leases with different concession structures and is the single most important rent metric in office leasing.

**Use.** NER is used to compare competing lease proposals, track market rent trends accurately, and underwrite proforma revenue. Face rents in headline market reports can be misleading — a building quoting $50/RSF gross with 12 months free rent and a $100/RSF TI may have a materially lower NER than a competing building at $45/RSF with minimal concessions.

**Formula (plain).** NER = Face Rent − (TI Allowance ÷ Lease Term in Years) − (Free Rent Months ÷ 12 × Face Rent)

**Formula (LaTeX).**
$$\text{NER} = R_{\text{face}} - \frac{\text{TI}}{T} - \frac{M_{\text{free}}}{12} \times R_{\text{face}}$$

Where $R_{\text{face}}$ = annual face rent per RSF, $\text{TI}$ = TI allowance per RSF, $T$ = lease term in years, $M_{\text{free}}$ = free rent months.

*Note: A more precise version discounts TI and amortizes using the landlord's cost of capital, but the above linear approximation is common in practice.*

---

### TI/LC Amortization

**Definition.** Tenant improvement (TI) allowances and leasing commissions (LC) are capital outlays paid at or near lease commencement that must be amortized over the lease term to properly represent their impact on investment returns. TI/LC amortization converts one-time capital costs into an annual per-SF drag on cash flow.

**Use.** Modeled in the [[Discounted Cash Flow (DCF)]] as capital line items in the year paid (affecting levered cash flow and equity returns) and also as an annual amortized charge to compute net effective rent. In a leveraged deal, large TI/LC outlays in early years can create negative or near-zero levered cash flows even when NOI is positive, which must be modeled accurately.

**Formula (plain).** Annual TI/LC Amortization per RSF = (TI + LC per RSF) ÷ Lease Term in Years

**Formula (LaTeX).**
$$\text{Annual TI/LC Amort} = \frac{\text{TI} + \text{LC}}{T}$$

Where costs are expressed per RSF and $T$ is the lease term in years.

---

### Weighted Average Lease Term (WALT)

**Definition.** WALT is the duration-weighted average of remaining lease terms across all tenants in a building, weighted by each tenant's share of total leased square footage (or, alternatively, by base rent).

**Use.** WALT is a primary risk indicator in office underwriting and financing. Short WALT (under 3–4 years) signals imminent rollover, requiring the underwriter to model re-leasing assumptions explicitly within the hold period. Lenders use WALT as a key sizing criterion — permanent loans generally require WALT well in excess of the loan term; bridge loans underwrite the lease-up story. A high WALT provides income visibility; a low WALT can be an opportunity (mark-to-market upside) or a risk (re-tenanting cost and downtime).

**Formula (plain).** WALT = Sum of (Remaining Term × Leased SF for each tenant) ÷ Total Leased SF

**Formula (LaTeX).**
$$\text{WALT} = \frac{\sum_{i=1}^{n} T_i \times SF_i}{\sum_{i=1}^{n} SF_i}$$

Where $T_i$ = remaining lease term in years for tenant $i$, $SF_i$ = leased square footage of tenant $i$.

---

### Occupancy Rate and Availability Rate

**Definition.** Physical occupancy rate is the percentage of rentable square footage currently occupied by a paying tenant. Availability rate (or availability) is the percentage of space currently available for lease — including both vacant space and space being marketed for sublease while still under lease to another tenant.

**Use.** Occupancy and availability are complementary metrics. A building may report 85% physical occupancy but 25% availability if existing tenants are subleasing significant portions of their space. Availability rate is a leading indicator of future vacancy because subleased space that does not find a new user will eventually be surrendered. Institutional investors and lenders watch both metrics; availability rate is more conservative and forward-looking.

**Formula (plain).** 
- Occupancy Rate = Occupied RSF ÷ Total Rentable RSF × 100
- Availability Rate = Available RSF (vacant + sublease) ÷ Total Rentable RSF × 100

---

### Load Factor (Add-On Factor)

**Definition.** The load factor (also called the add-on factor or loss factor) is the ratio of a building's total rentable area to its usable area, expressed as a multiplier. Tenants lease rentable square footage (RSF), which includes their allocated share of common areas (lobbies, corridors, mechanical rooms, restrooms). The usable square footage (USF) is the tenant's actual enclosed space. The load factor equals RSF ÷ USF.

**Use.** Load factor directly affects tenant occupancy cost: a tenant paying $50/RSF on a space with a 1.20 load factor is paying $60/USF for actual usable space, versus a competitor in a building with a 1.10 load factor who pays $55/USF. Lower load factors are a competitive advantage for landlords. Building Owners and Managers Association (BOMA) standards govern how load factors are measured.

**Formula (plain).** Load Factor = Rentable SF ÷ Usable SF

**Formula (LaTeX).**
$$\text{Load Factor} = \frac{\text{RSF}}{\text{USF}}$$

A typical Class A office load factor ranges from 1.10 to 1.25 (10%–25% add-on); varies by market and vintage.

---

### Parking Ratio

**Definition.** Parking ratio is the number of parking spaces available per 1,000 rentable square feet of the building.

**Use.** Parking ratio is a critical competitive variable for suburban office assets, where employees commute by car and buildings without adequate parking lose leasing prospects. CBD buildings rely on transit access and public parking structures, so parking ratio matters less. Standard suburban office requirements typically run 4.0–5.0 spaces per 1,000 RSF, but varies by market and tenant type. Buildings with inadequate parking relative to submarket norms face a competitive disadvantage that is difficult to cure without adjacent land.

**Formula (plain).** Parking Ratio = Total Parking Spaces ÷ (Total RSF ÷ 1,000)

---

### Expense Recovery Ratio

**Definition.** The expense recovery ratio measures the percentage of a building's total operating expenses that are reimbursed by tenants through lease provisions (CAM, tax, insurance reimbursements, or NNN pass-throughs), as opposed to expenses absorbed by the landlord.

**Use.** In a full-service gross building, expense recovery may be 0–20% (landlord absorbs almost all OpEx); in a NNN multi-tenant building, recovery may exceed 80–90%. The expense recovery ratio directly affects NOI sensitivity to expense inflation — a building with high recovery insulates the landlord from rising costs and is generally more valuable to institutional buyers. Underwriters model recovery separately for each expense category based on lease language, not as a blanket assumption.

**Formula (plain).** Expense Recovery Ratio = Tenant Reimbursements ÷ Total Operating Expenses × 100
