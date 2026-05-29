---
title: Land — Key Metrics
type: asset-class
tags: [cre, asset/land]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Defines the eight core land metrics — residual land value, $/acre, $/buildable SF, $/door, finished-lot ratio, land basis %, entitlement premium, and carry cost — with formulas.
asset_class: land
subtypes: []
related:
  - Land
  - Land — Underwriting Norms
  - Land — Subtypes
  - Residual Land Value Method
  - Residual Land Value Feasibility
  - Highest and Best Use Analysis
  - Development Feasibility Test
  - Internal Rate of Return (IRR)
  - Equity Multiple
  - Discount Rate
  - Hard Costs
  - Soft Costs
  - Comparable Sales (Sales Comps)
  - Ground-Up Development
  - Entitlement Play
  - Land Banking
---

# Land — Key Metrics

Land underwriting produces no NOI and no cap rate. Instead, practitioners rely on a set of forward-looking metrics that convert projected development outcomes into a supportable land price. The eight metrics below are the standard vocabulary for land analysis.

---

### Residual Land Value (RLV)

**Definition.** Residual land value is the maximum price a rational developer can pay for land and still achieve the required return on the development. It is computed by starting with projected completed-project value and working backwards, subtracting all costs and required profit until a supportable land price remains.

**Use.** RLV is the primary underwriting output for land — it answers the question "What is this land worth given my development assumptions?" It is also used as a bid benchmark and a feasibility screen: if the market-clearing land price exceeds RLV, the project is not feasible at that land cost.

**Formula (plain).**
```
RLV = Projected Completed Value − Total Development Costs − Required Developer Profit
```

Where:
- Projected Completed Value = stabilized asset value or net sellout proceeds
- Total Development Costs = Hard Costs + Soft Costs + Financing/Carry Costs + Sales/Marketing Costs (excluding land)
- Required Developer Profit = typically 10%–20%+ of total project cost (TPC), reflecting the developer's risk premium

**Formula (LaTeX).**

$$\text{RLV} = V_{\text{completed}} - C_{\text{dev}} - P_{\text{developer}}$$

where $V_{\text{completed}}$ is stabilized or net-sellout value, $C_{\text{dev}}$ is all development costs excluding land, and $P_{\text{developer}}$ is required developer profit.

**Notes.** RLV is highly sensitive to each input. A 10% change in $V_{\text{completed}}$ or $C_{\text{dev}}$ can swing RLV by 30–50%+ because the residual absorbs the full impact of each swing. See [[Residual Land Value Method]] and [[Residual Land Value Feasibility]] for extended treatment.

---

### Price per Acre

**Definition.** The purchase price of a land parcel expressed as a dollar amount per acre of total site area.

**Use.** Price per acre is the most commonly cited headline metric for raw and agricultural land transactions. It is useful for broad comparisons across parcels of similar type and location, but becomes less meaningful as density, entitlement status, and infrastructure vary — in those cases, $/buildable unit or $/buildable SF are more precise.

**Formula (plain).**
```
Price per Acre = Total Purchase Price ÷ Total Acres
```

**Formula (LaTeX).**

$$\text{Price per Acre} = \frac{P_{\text{total}}}{\text{Acres}}$$

**Notes.** One acre = 43,560 square feet. Ranges vary from under $10,000/acre for remote agricultural land to $500,000+/acre for entitled suburban land and $1M+/acre for urban infill parcels, depending on location, use, and entitlement status. Always verify the acreage figure (gross vs. net developable) when comparing comps.

---

### Price per Buildable Square Foot

**Definition.** Purchase price divided by the total buildable square footage that can be developed on the site given existing or proposed zoning and FAR assumptions.

**Use.** Used primarily for commercial, office, retail, and mixed-use land analysis. Normalizes land cost across parcels with different FAR allowances, enabling apples-to-apples comparison between sites that have different densities. A parcel allowing 0.5 FAR and one allowing 2.0 FAR will have very different $/acre prices but may have similar $/buildable SF if the market prices density appropriately.

**Formula (plain).**
```
Price per Buildable SF = Total Purchase Price ÷ Total Buildable Square Feet
Total Buildable SF = Net Developable Area (SF) × Allowable FAR
```

**Formula (LaTeX).**

$$\text{Price/BSF} = \frac{P_{\text{total}}}{\text{Net Developable Area} \times \text{FAR}}$$

**Notes.** FAR assumption is critical — changes in the assumed use or density directly change the denominator and therefore the metric. Underwriters should test multiple FAR scenarios. Urban infill typically ranges from $20–$100+/buildable SF; suburban commercial from $5–$30/BSF; industrial land from $3–$15/BSF. Varies significantly by market.

---

### Price per Door / Buildable Unit

**Definition.** Purchase price divided by the number of residential units (apartments, townhomes, single-family lots) that can be developed on the site.

**Use.** The primary land pricing metric for residential development — both multifamily and for-sale single-family. It normalizes land cost to the unit of revenue (a home or apartment), enabling direct comparison to revenue per unit and finished-lot comps. Homebuilders and multifamily developers use this metric to set land bid limits.

**Formula (plain).**
```
Price per Door = Total Purchase Price ÷ Allowable / Planned Units
```

**Formula (LaTeX).**

$$\text{Price per Door} = \frac{P_{\text{total}}}{\text{Units}_{\text{planned}}}$$

**Notes.** The unit count assumption (density) is the key variable — changing density from 15 du/ac to 25 du/ac materially changes the per-door metric on the same parcel. Ranges: finished lots in entry-level residential submarkets $30,000–$80,000/door; multifamily urban infill $40,000–$150,000+/door; raw land $10,000–$50,000/door. Varies significantly by market and product type.

---

### Finished-Lot Ratio

**Definition.** The finished (improved, pad-ready) lot price expressed as a percentage of the projected new home sale price for that lot.

**Use.** A homebuilder rule-of-thumb benchmark. Builders track the ratio to ensure land cost remains within a range that permits profitable construction and a market-clearing home price. If the finished-lot ratio rises above sustainable thresholds, the builder either cannot pencil the project or must reduce margin.

**Formula (plain).**
```
Finished-Lot Ratio = Finished Lot Price ÷ Projected New Home Price
```

**Formula (LaTeX).**

$$\text{Finished-Lot Ratio} = \frac{P_{\text{lot}}}{P_{\text{home}}}$$

**Notes.** Typical range is 15%–30%, with coastal and high-cost markets at the upper end and commodity Sunbelt markets at the lower end. When the ratio exceeds 30%, the land basis is structurally impeding feasibility unless home prices rise or construction costs fall. This metric is closely watched during land boom phases as a feasibility warning signal.

---

### Land Basis as % of Total Development Cost

**Definition.** The land acquisition cost expressed as a percentage of the total project capitalization (land + hard costs + soft costs + financing + contingency).

**Use.** Tracks how much of the total development investment is consumed by land. A higher land percentage implies less cushion in the pro forma — cost overruns in construction hit project economics harder when land is a larger share of TDC. Also used to benchmark land cost against comparable projects and to calibrate lender appetite (lenders typically want to see land as a reasonable share of TDC for construction loan sizing).

**Formula (plain).**
```
Land % of TDC = Land Cost ÷ (Land Cost + All Other Development Costs)
```

**Formula (LaTeX).**

$$\text{Land \%} = \frac{C_{\text{land}}}{C_{\text{land}} + C_{\text{dev}}}$$

**Notes.** Typical range 10%–25%. In supply-constrained urban markets, land can reach 30–35%+ of TDC for high-density projects. In greenfield markets with low land cost, land may represent 8–12% of TDC. Both extremes warrant scrutiny: a very low land percentage may indicate underwriting the land too cheaply; a very high percentage leaves little buffer for construction cost inflation.

---

### Entitlement Premium

**Definition.** The increment of value created by successfully obtaining a discretionary entitlement (zone change, general plan amendment, major use permit, etc.) over the pre-entitlement raw-land value.

**Use.** Quantifies the return earned by the entity that undertook and funded the entitlement process. Used to assess whether the entitlement risk was adequately compensated and to benchmark land transactions at different points on the entitlement spectrum. Also informs the structure of JV splits between capital partners and entitlement-expertise operators.

**Formula (plain).**
```
Entitlement Premium ($) = Post-Entitlement Land Value − Pre-Entitlement (Raw) Land Value
Entitlement Premium (%) = (Post-Entitlement Value − Pre-Entitlement Value) ÷ Pre-Entitlement Value
```

**Formula (LaTeX).**

$$\text{Entitlement Premium} = V_{\text{entitled}} - V_{\text{raw}}$$

$$\text{Entitlement Premium \%} = \frac{V_{\text{entitled}} - V_{\text{raw}}}{V_{\text{raw}}}$$

**Notes.** Typical entitlement premiums range from 20%–100%+ of raw land value, reflecting the probability of success, duration, capital consumed, and the increase in development potential unlocked. In high-barrier markets (coastal California, Oregon, select mountain West markets), entitlement premiums can be multiples of the raw value. See [[Entitlement Play]] for deal-type framing.

---

### Holding / Carry Cost

**Definition.** The annual cost of holding a land parcel without generating any offsetting income, including property taxes, interest on acquisition debt, insurance, legal and entitlement professional fees, and opportunity cost on equity.

**Use.** Carry cost accretes against the land basis every month that the parcel is held without generating income or advancing through value-creation milestones. It is the "clock" that runs against the land investor — the longer the hold, the higher the required exit price just to recover basis plus carry. Underwriters model carry explicitly in the land pro forma to ensure the hold period and return assumption are consistent.

**Formula (plain).**
```
Annual Carry Cost ($) = Property Taxes + Debt Service (Interest Only) + Insurance + Other Holding Costs
Carry as % of Basis = Annual Carry Cost ($) ÷ Total Land Acquisition Basis
```

**Formula (LaTeX).**

$$\text{Annual Carry} = T_{\text{tax}} + I_{\text{debt}} + I_{\text{ins}} + C_{\text{other}}$$

$$\text{Carry \%} = \frac{\text{Annual Carry}}{C_{\text{land}}}$$

**Notes.** A land parcel carrying 50% leverage at a 9% interest rate and 1.5% property tax rate incurs approximately 6%+ annual carry as a percentage of the total land basis (3% taxes on total value + ~4.5% interest on 50% of value). Over a 4-year entitlement hold, this compounds meaningfully. Option structures and seller financing at below-market rates are the primary tools for managing carry. See [[Land Banking vs. Active Pursuit]] and [[Land — Underwriting Norms]] for carry management strategies.
