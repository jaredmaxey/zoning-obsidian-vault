---
title: Self-Storage — Key Metrics
type: asset-class
tags: [cre, asset/self-storage]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Defines the key self-storage operating and underwriting metrics — physical vs. economic occupancy, RevPAF, rate per occupied SF, churn, ECRI, breakeven occupancy, and NRSF — with formulas.
asset_class: self-storage
related:
  - Self-Storage
  - Self-Storage — Underwriting Norms
  - Self-Storage — Risks & Considerations
  - Net Operating Income (NOI)
  - Effective Gross Income (EGI)
  - Vacancy and Collection Loss
  - Operating Expense Ratio
  - Stabilized NOI
  - Absorption Rate
  - Pro Forma Construction Method
---

# Self-Storage — Key Metrics

Self-storage uses a distinct operating metric set that reflects the month-to-month lease structure, high unit count, and revenue management–driven business model. Understanding how each metric is defined, calculated, and used in underwriting is essential for evaluating performance and pro forma assumptions.

---

### NRSF (Net Rentable Square Feet)

**Definition.** NRSF is the total square footage of rentable unit interiors across a facility — the sum of all individual unit floor areas. It excludes hallways, elevator shafts, office space, mechanical rooms, and other common areas. NRSF is the denominator for most per-square-foot metrics in self-storage and is the standard basis for facility sizing and pricing.

**Use.** NRSF is used to size facilities (e.g., "a 60,000 NRSF facility"), compare per-foot construction costs and revenues, and calculate revenue-per-available-foot metrics. It is the self-storage equivalent of rentable square footage in office or gross leasable area (GLA) in retail, but strictly refers to the unit interiors only.

**Formula (plain).** NRSF = sum of all individual unit floor areas (length × width per unit).

---

### Physical Occupancy

**Definition.** Physical occupancy is the percentage of a facility's NRSF (or unit count) that is currently occupied by a paying tenant. It is the headline leasing metric and the most commonly cited measure of facility performance.

**Use.** Physical occupancy is used to benchmark performance against market, assess lease-up trajectory for new or transitional assets, and set revenue management responses (when occupancy is high, street rates are raised; when it falls, discounts and promotions are deployed).

**Formula (plain).** Physical Occupancy (%) = Occupied NRSF ÷ Total NRSF × 100.

**Formula (LaTeX).**
$$\text{Physical Occupancy} = \frac{\text{Occupied NRSF}}{\text{Total NRSF}} \times 100$$

**Notes.** Some operators calculate physical occupancy on a unit-count basis rather than square footage basis; the two measures can diverge when a mix of large and small units is involved. Square-footage-based occupancy is preferred for revenue management and underwriting purposes.

---

### Economic Occupancy

**Definition.** Economic occupancy measures actual revenue collected as a percentage of potential gross revenue — i.e., what would be earned if every unit were occupied at the current street rate with no concessions or bad debt.

**Use.** Economic occupancy is a more conservative and more informative underwriting metric than physical occupancy because it captures the revenue impact of concessions (first-month-free promotions, move-in discounts), delinquency, and units rented at below-street rates. A facility at 92% physical occupancy may be at only 84% economic occupancy if it is running heavy concessions or carrying delinquent accounts. The gap between physical and economic occupancy is a key underwriting signal.

**Formula (plain).** Economic Occupancy (%) = Actual Gross Revenue ÷ Potential Gross Revenue (all units at street rate) × 100.

**Formula (LaTeX).**
$$\text{Economic Occupancy} = \frac{\text{Actual Gross Revenue}}{\text{Potential Gross Revenue}} \times 100$$

---

### RevPAF — Revenue per Available Foot

**Definition.** RevPAF (Revenue per Available Foot) is total storage revenue divided by total NRSF. It is analogous to RevPAR in hospitality — it blends both rate and occupancy into a single top-line performance metric.

**Use.** RevPAF is used to compare revenue productivity across facilities of different sizes and unit mixes, track same-store revenue trends, and benchmark against competitive set data. Rising RevPAF can be driven by rate increases (ECRI, street rate growth), occupancy gains, or both.

**Formula (plain).** RevPAF = Total Storage Revenue ÷ Total NRSF.

**Formula (LaTeX).**
$$\text{RevPAF} = \frac{\text{Total Storage Revenue}}{\text{Total NRSF}}$$

---

### Rate per Occupied SF

**Definition.** Rate per occupied SF is the average rent collected per square foot of occupied space — the average in-place rate across all currently rented units. It differs from the street rate (the rate offered to new tenants) and from RevPAF (which includes vacant space in the denominator).

**Use.** Rate per occupied SF tracks in-place rate performance independent of occupancy changes. A rising rate per occupied SF while RevPAF is flat signals occupancy erosion masking rate growth. Comparing rate per occupied SF to street rates reveals the gap that ECRI programs are designed to close (when in-place < street) or the risk of elevated churn (when in-place > street).

**Formula (plain).** Rate per Occupied SF = Total Storage Revenue ÷ Occupied NRSF.

**Formula (LaTeX).**
$$\text{Rate per Occupied SF} = \frac{\text{Total Storage Revenue}}{\text{Occupied NRSF}}$$

---

### Churn / Move-Out Rate

**Definition.** The monthly move-out rate is the percentage of occupied units (or NRSF) that vacate during a given month. It reflects tenant turnover and is the primary demand on leasing and marketing activity to maintain occupancy.

**Use.** Churn is a critical operational metric because it drives the replacement leasing required to hold steady-state occupancy. A facility with 5%–10% monthly move-outs must continuously convert new prospects to avoid occupancy erosion. Elevated churn can result from aggressive ECRI programs, poor customer satisfaction, or competitive pressure from nearby alternatives. Underwriters should track churn trends alongside ECRI activity to assess whether rate increases are being absorbed or are driving excess vacates.

**Formula (plain).** Monthly Churn Rate (%) = Move-Out Units in Month ÷ Total Occupied Units at Month Start × 100.

**Formula (LaTeX).**
$$\text{Monthly Churn} = \frac{\text{Move-Out Units}}{\text{Occupied Units (Start of Period)}} \times 100$$

---

### ECRI (Existing-Customer Rate Increase)

**Definition.** ECRI is the systematic, recurring increase in rent charged to existing tenants — distinct from changes in street rates for new move-ins. Facilitated by the month-to-month lease structure, ECRI programs notify tenants of rent increases (typically 30 days in advance) on a scheduled basis, usually every 3–9 months per tenant.

**Use.** ECRI is the primary driver of same-store NOI growth in self-storage. Because tenants are less price-sensitive than the market suggests (moving costs, time, and hassle create switching friction), operators can increase rents on existing tenants without proportionate move-out responses. The size and frequency of ECRI increases varies by operator, unit type, market conditions, and individual tenant tenure. Underwriting ECRI upside requires estimating the current gap between in-place and street rates and modeling move-out response curves. See [[Self-Storage — Underwriting Norms]] for detail.

**No single formula.** ECRI is a management program, not a calculated metric. The revenue impact is: incremental revenue = (targeted rate increase) × (in-place occupied NRSF) × (1 − projected move-out response rate).

---

### Breakeven Occupancy

**Definition.** Breakeven occupancy is the physical occupancy rate at which a facility's revenue exactly covers its total operating expenses and debt service — i.e., the occupancy below which the investment produces negative cash flow after debt service.

**Use.** Breakeven occupancy is a stress-test metric used in underwriting and lender analysis to assess downside protection. Self-storage's low OpEx ratio means breakeven occupancy is typically lower than for other asset classes — often in the 60%–75% range for stabilized facilities with moderate leverage — providing a meaningful buffer against occupancy declines. Highly leveraged or lease-up deals carry higher breakevens.

**Formula (plain).** Breakeven Occupancy (%) = (Total OpEx + Annual Debt Service) ÷ Potential Gross Revenue at 100% Occupancy × 100.

**Formula (LaTeX).**
$$\text{Breakeven Occupancy} = \frac{\text{Total OpEx} + \text{Annual Debt Service}}{\text{Potential Gross Revenue}} \times 100$$

**Notes.** Potential gross revenue should be calculated at current street rates, not in-place rates, for comparability. The metric is closely related to [[Debt Service Coverage Ratio (DSCR)]] — a facility at breakeven occupancy has a DSCR of 1.0×.
