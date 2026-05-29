---
title: Multifamily — Key Metrics
type: asset-class
tags: [cre, asset/multifamily]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Defines and explains class-specific multifamily performance metrics including effective rent, loss-to-lease, economic vs. physical occupancy, RevPAU, expense ratio, concessions, and retention.
asset_class: multifamily
subtypes: []
related:
  - Multifamily
  - Multifamily — Underwriting Norms
  - Net Operating Income (NOI)
  - Effective Gross Income (EGI)
  - Vacancy and Collection Loss
  - Operating Expense Ratio
  - Price per Unit
  - Gross Rent Multiplier (GRM)
  - Rent Roll Analysis
  - T-12 and T-3 Analysis
  - Stabilized NOI
---

# Multifamily — Key Metrics

## Overview

Multifamily performance metrics track two distinct dimensions: revenue efficiency (how much rent the property actually collects relative to its potential) and operating efficiency (how much of that revenue becomes NOI). Unlike commercial leases where a small number of tenants dominate the rent roll, multifamily derives income from a large number of short-term residential leases, making statistical aggregation — averages per unit, percentages of potential — the standard analytical language. The metrics below are used by institutional operators, acquisition teams, lenders, and asset managers when underwriting, benchmarking, and monitoring multifamily investments.

---

### Effective Rent Per Unit

**Definition:** The average monthly rent actually charged across occupied units, net of concessions granted (free rent, move-in discounts). Also called "net effective rent" when specified to reflect concession adjustments, versus "asking rent" (the advertised rate before concessions).

**How used:** The primary revenue benchmark for comparing a property against its competitive set (rent comps), tracking performance over time, and projecting pro forma revenue. Effective rent per unit is the building block for total potential gross income.

**Formula:**

Plain text: `Effective Rent Per Unit = (Total Monthly Rent Collected — Concession Value) / Occupied Units`

LaTeX: $\text{Effective Rent/Unit} = \frac{\sum(\text{Monthly Rent Charged}) - \sum(\text{Concessions Applied})}{\text{Occupied Units}}$

A property with 200 occupied units, $180,000/month in gross rents charged, and $6,000/month in concessions has an effective rent of $870/unit/month.

---

### Loss-to-Lease (LTL)

**Definition:** The aggregate dollar gap between in-place (contracted) rents on existing leases and current market rents for the same unit types. Loss-to-lease represents "trapped" upside: rent growth that has already occurred in the market but has not yet been captured because existing tenants signed leases at lower rates.

**How used:** The primary value-add underwriting lever in acquisition analysis. A property with 10–20% loss-to-lease has significant embedded NOI growth that can be realized through lease renewals (at higher market rents) and turnover (re-leasing vacated units at current market rates) without any capital expenditure. Loss-to-lease is typically quantified in the rent roll by comparing each unit's in-place rent to the underwriter's estimate of current market rent for that unit type.

**Formula:**

Plain text: `Loss-to-Lease % = (Market Rent — In-Place Rent) / Market Rent × 100`

LaTeX: $\text{LTL\%} = \frac{\text{Market Rent} - \text{In-Place Rent}}{\text{Market Rent}} \times 100$

A property where the average market rent is $1,500/unit and the average in-place rent is $1,350/unit has a loss-to-lease of 10%.

---

### Physical Occupancy

**Definition:** The percentage of leasable units that are occupied by tenants on a given date or over a measurement period.

**How used:** The most commonly cited headline occupancy metric. Physical occupancy measures whether units are filled, but does not account for the revenue quality of those occupancies (concessions, delinquency). A property can have 96% physical occupancy but only 90% economic occupancy if significant concessions are being offered.

**Formula:**

Plain text: `Physical Occupancy = Occupied Units / Total Leasable Units × 100`

LaTeX: $\text{Physical Occupancy\%} = \frac{\text{Occupied Units}}{\text{Total Leasable Units}} \times 100$

---

### Economic Occupancy

**Definition:** The ratio of actual collected revenue to potential gross revenue at full occupancy with no concessions or bad debt. Economic occupancy is always lower than physical occupancy because it captures all revenue leakage: concessions, free rent, delinquency, bad debt, and non-revenue units (model units, employee units).

**How used:** The more accurate revenue efficiency metric for underwriting and lender analysis. Lenders and institutional buyers often focus on economic occupancy and [[Effective Gross Income (EGI)]] rather than physical occupancy when assessing revenue stability.

**Formula:**

Plain text: `Economic Occupancy = Actual Collected Revenue / (Gross Potential Rent at 100% Occupancy, No Concessions) × 100`

LaTeX: $\text{Economic Occupancy\%} = \frac{\text{Actual Collected Revenue}}{\text{Gross Potential Rent (100\%, No Concessions)}} \times 100$

The gap between physical occupancy (e.g., 95%) and economic occupancy (e.g., 88%) is driven by concessions (−3%), bad debt (−2%), and non-revenue units (−2%).

---

### Revenue Per Available Unit (RevPAU)

**Definition:** Total annualized revenue (rent plus ancillary income) divided by total unit count (occupied and vacant). RevPAU combines occupancy and rent level into a single metric, enabling apples-to-apples comparison across properties with different occupancy rates.

**How used:** A holistic benchmarking metric analogous to RevPAR in hospitality. Useful for tracking performance trends, setting revenue targets, and comparing a property against its competitive set. An operator who raises rents but loses occupancy may see RevPAU flat or declining — the metric reveals the net revenue impact.

**Formula:**

Plain text: `RevPAU = Total Annual Revenue / Total Units`

LaTeX: $\text{RevPAU} = \frac{\text{Total Annual Revenue}}{\text{Total Units}}$

---

### Operating Expense Ratio (OER)

**Definition:** Total operating expenses (excluding debt service, depreciation, and replacement reserves unless specifically included) divided by effective gross income. Measures the proportion of revenue consumed by operations.

**How used:** A key efficiency metric for comparing operators, submarkets, and vintages. Garden suburban communities typically achieve lower OERs (35–42%) than urban high-rise (45–52%) due to the absence of elevator systems, doorman services, and structured parking. Rising OERs signal cost pressure that is compressing NOI margins without a corresponding revenue offset.

**Formula:**

Plain text: `OER = Total Operating Expenses / Effective Gross Income × 100`

LaTeX: $\text{OER\%} = \frac{\text{Total Operating Expenses}}{\text{EGI}} \times 100$

See [[Operating Expense Ratio]] for the general concept note.

---

### Concessions

**Definition:** Discounts given to attract or retain tenants: free rent periods, reduced move-in rent, gift cards, or waived fees. Concessions reduce net effective rent below asking rent and must be amortized over the lease term for accurate revenue accounting.

**How used:** Concession levels are a barometer of submarket supply/demand balance. Rising concessions signal landlord competition for tenants (excess supply, declining demand); contracting concessions signal tightening market conditions. Institutional underwriting models concessions as a percentage of potential gross revenue — typically 1–3% in balanced markets, 3–6%+ in oversupplied conditions. Concessions burning off as the market tightens is a common value-add revenue growth assumption.

**Formula (annualized concession as % of potential revenue):**

Plain text: `Concession Rate = Total Concession Value / Gross Potential Rent × 100`

LaTeX: $\text{Concession Rate\%} = \frac{\text{Total Concession Value}}{\text{Gross Potential Rent}} \times 100$

---

### Renewal and Retention Rate

**Definition:** The percentage of expiring leases renewed by existing tenants during a measurement period (typically monthly or trailing 12 months). The inverse — turnover or non-renewal rate — measures what percentage of tenants vacate at lease expiration.

**How used:** Retention rate directly drives operating cost efficiency: each unit turn requires make-ready costs (cleaning, repairs, painting), potential downtime before re-leasing, and leasing costs (advertising, agent fees). Higher retention rates reduce OpEx and minimize revenue gaps between tenancies. Institutional operators track renewal rates by unit type, floor, building, and lease expiration cohort. Strong retention (65–80%) in stabilized communities indicates tenant satisfaction and pricing discipline; aggressive rent increases often produce short-term revenue gains but depress renewal rates and raise OpEx.

**Formula:**

Plain text: `Retention Rate = Leases Renewed / Leases Expiring × 100`

LaTeX: $\text{Retention Rate\%} = \frac{\text{Leases Renewed}}{\text{Leases Expiring}} \times 100$

---

### Bad Debt and Delinquency Rate

**Definition:** Bad debt is the portion of billed rent that is ultimately uncollected (written off after eviction or vacancy); delinquency rate measures the percentage of residents more than a specified number of days past due on rent. Both are components of economic vacancy.

**How used:** Bad debt is typically underwritten at 0.5–2.0% of potential gross revenue in stabilized markets; it spikes during economic downturns, eviction moratorium periods, and in properties with weak tenant screening. Monitoring delinquency as a leading indicator allows operators to accelerate collections activity and adjust underwriting assumptions. Lenders closely scrutinize bad debt history when assessing credit quality of the rent roll.

**Formula:**

Plain text: `Bad Debt Rate = Annual Bad Debt Write-Off / Gross Potential Rent × 100`

LaTeX: $\text{Bad Debt Rate\%} = \frac{\text{Annual Bad Debt Write-Off}}{\text{Gross Potential Rent}} \times 100$

---

### Ancillary Income

**Definition:** Revenue sources beyond base rent, including pet fees, parking fees, storage fees, late charges, laundry income, vending income, package/locker fees, short-term rental premiums, and RUBS (ratio utility billing system) income.

**How used:** Ancillary income is a growing share of multifamily revenue — well-managed Class A communities in competitive markets can derive 8–15%+ of total revenue from non-rent sources. Institutional underwriting treats ancillary income as a separate line above EGI and models it conservatively, often at trailing actuals or modest growth. Value-add programs that add parking management, pet-friendly policies, and amenity-driven fees are a common ancillary revenue enhancement strategy.
