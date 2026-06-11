---
title: Industrial — Key Metrics
aliases: ["Industrial — Key Metrics"]
type: asset-class
tags: [cre, asset/industrial]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Defines key industrial real estate metrics — clear height, dock-door ratio, truck court depth, parking, NNN rent, cubic utilization, and power capacity — with formulas and underwriting context.
asset_class: industrial
subtypes: []
related:
  - Industrial
  - Industrial — Underwriting Norms
  - Industrial — Subtypes
  - Bulk Warehouse
  - Last-Mile Logistics
  - Light Industrial
  - Cold Storage
  - Manufacturing
  - Net Operating Income (NOI)
  - Price per Square Foot
  - Comparable Rents (Rent Comps)
  - Replacement Cost
  - Yield on Cost
  - Development Feasibility Test
---

# Industrial — Key Metrics

Industrial real estate is evaluated on a set of physical and financial metrics that differ substantially from other asset classes. Physical metrics directly determine a building's functional competitiveness — a property that falls short on clear height or truck court depth may trade at a discount or face limited re-leasing demand even in a strong market. Financial metrics (primarily $/SF NNN rent and cap rate derivatives) must be interpreted through the lens of the physical profile. This note defines each key metric, explains its use in underwriting and due diligence, and provides formulas where applicable.

### Clear Height

**Definition:** The usable interior ceiling height of a warehouse or distribution facility, measured in feet from the finished floor to the lowest overhead obstruction — typically the bottom chord of the roof structure, a sprinkler main, or a lighting fixture. Clear height is distinct from eave height (the height at the building's perimeter wall), which is often several feet higher. Specifications should always be confirmed from the architectural drawings or an independent measurement, not the marketing materials.

**Use:** Clear height determines how high tenant racking systems can be stacked, directly setting the usable cubic volume available per square foot of floor area. A building with 40 ft clear can support pallet racking to heights that a 24 ft clear building cannot, meaning the same footprint can handle significantly more inventory throughput. Modern bulk distribution tenants commonly require 36–40 ft clear minimum; last-mile infill and light industrial tenants often operate efficiently with 24–32 ft clear; cold storage and high-bay automated facilities may spec 50+ ft clear.

**Formula (cubic capacity):**

Plain: Usable Cubic Feet = Floor Area (SF) × Effective Stacking Height (ft)  
Where Effective Stacking Height ≈ Clear Height − Racking Clearance (typically 1–2 ft below obstruction)

$$\text{Usable Cubic Feet} = \text{Floor Area (SF)} \times (\text{Clear Height (ft)} - \text{Racking Clearance (ft)})$$

Older product (18–26 ft clear) may be functionally obsolete for modern logistics tenants and must be underwritten with a re-leasing discount or heavy TI investment to install mezzanines.

### Dock-Door Ratio

**Definition:** The number of dock-high loading doors per square foot of warehouse building area, expressed as doors per total SF (or its inverse: SF per dock door). A dock door is a raised loading position that aligns with the bed of a tractor-trailer, enabling forklift transfer of palletized goods without ramps.

**Use:** Dock-door ratio is a primary determinant of tenant throughput capacity. A building with insufficient dock doors relative to its size creates a loading bottleneck — regardless of clear height or floor area, tenants cannot move goods fast enough to meet operational needs. Modern bulk distribution typically targets 1 dock door per 8,000–12,000 SF; cross-dock facilities (receiving on one side, shipping on the other) have higher ratios; cold storage typically has fewer doors (each opening is a thermal break) but designs them for high efficiency.

**Formula:**

Plain: Dock-Door Ratio = Number of Dock Doors ÷ Building Area (SF)  
(Alternatively expressed as SF per Dock Door = Building Area ÷ Number of Dock Doors)

$$\text{Dock-Door Ratio} = \frac{\text{Number of Dock Doors}}{\text{Building Area (SF)}}$$

$$\text{SF per Dock Door} = \frac{\text{Building Area (SF)}}{\text{Number of Dock Doors}}$$

Underwriters should compare the property's dock-door ratio to the submarket standard and the prospective tenant's stated requirements. A deficient ratio may require capital investment to cut additional doors, subject to building structure and truck-court constraints.

### Truck Court Depth

**Definition:** The horizontal distance, in feet, between the dock face of a building and the opposite boundary (a building face, fence, property line, or trailer-parking stall). Truck court depth determines whether a standard tractor-trailer (typically 53 ft long) can maneuver into and back up to a dock position without obstruction.

**Use:** Insufficient truck court depth forces drivers to perform multi-point turns to access dock positions, slowing throughput and increasing accident risk. It can also prevent access for longer or combination vehicles. The industry standard for a fully functional dock-to-truck-court layout is 185–210 ft (dock face to opposite face/fence), with 185 ft considered a workable minimum for a standard 53-ft trailer and 210 ft providing more comfortable maneuvering plus a row of spotted-trailer parking. Shallower courts (120–160 ft) are common in older infill product and constrain operations.

**No universal formula:** Truck court depth is a direct measurement. Underwriters should flag any truck court depth below 185 ft as a functional deficiency that requires tenant-specific confirmation and potential TI or site-improvement cost.

### Trailer and Auto Parking

**Definition:** The total number of parking stalls on-site, differentiated by type:
- **Trailer stalls** (also called "spotted trailer parking"): positions where loaded or empty trailers can be staged awaiting dock loading/unloading. Each position accommodates one 53-ft trailer.
- **Auto stalls**: conventional employee and visitor parking.

**Use:** Trailer parking is critical for distribution tenants with high inbound/outbound shipment frequency — insufficient trailer stalls forces tenants to keep trucks running or miss delivery windows. Auto parking ratios are lower for pure-warehouse use (0.5–1.0 stall per 1,000 SF is typical for bulk logistics) but rise substantially for light industrial and flex tenants with higher employee-per-SF density. Zoning codes and entitlement approvals may limit total parking (impervious surface, traffic mitigation) even where the tenant demands more.

**Formula:**

Plain: Auto Parking Ratio = Total Auto Stalls ÷ Building Area (per 1,000 SF)

$$\text{Auto Parking Ratio} = \frac{\text{Auto Stalls}}{\text{Building Area (SF)} / 1{,}000}$$

Underwriters should confirm that trailer parking is legally permitted under the zoning entitlements (an increasingly contested issue in municipalities pursuing IOS restrictions).

### $/SF NNN Rent

**Definition:** Annualized base rent per square foot of leased area, quoted on a net basis (tenant pays operating expenses separately). The standard financial metric for quoting and comparing industrial leases in the US market.

**Use:** $/SF NNN rent is the primary rent metric used in [[Comparable Rents (Rent Comps)]] analysis, lease negotiation, and underwriting pro formas. It must be interpreted in context of the net lease structure — a "gross" or "modified gross" rent quoted for a comparable space should be adjusted to a NNN-equivalent basis by subtracting estimated operating expenses for an apples-to-apples comparison. Rents also vary materially by clear height, dock count, location, and lease term.

**Formula:**

Plain: Effective Gross Income (base rent) = $/SF NNN × Total Leased Area (SF)

$$\text{Base Rent Income} = \left(\frac{\$}{\text{SF}} \cdot \text{NNN}\right) \times \text{Leased Area (SF)}$$

Annual rent bumps are then applied to each year's base rent according to the lease escalation structure.

### Cubic Utilization

**Definition:** A measure of how efficiently a warehouse tenant uses the three-dimensional volume of the building, expressed as the ratio of occupied cubic volume (actual pallet positions × pallet height) to total available cubic volume (floor area × clear height).

**Use:** Cubic utilization is primarily a tenant operations metric (how efficiently is the building being used?) but informs landlord underwriting of renewal probability and lease-up assumptions. A tenant operating at 95%+ cubic utilization is likely to renew (or need more space); a tenant at 40% utilization may be over-leased relative to their actual needs and at risk of downsizing at renewal. Sophisticated industrial analysts track cubic utilization trends across their portfolio to anticipate rollover risk.

**Formula:**

Plain: Cubic Utilization = Occupied Cubic Volume ÷ Available Cubic Volume × 100%

$$\text{Cubic Utilization (\%)} = \frac{\text{Occupied Cubic Volume (ft}^3\text{)}}{\text{Floor Area (SF)} \times \text{Clear Height (ft)}} \times 100$$

### Power Capacity

**Definition:** The total electrical power available to a building, typically expressed in amps (at a stated voltage) and kilowatts (kW) or megawatts (MW). Also relevant are the voltage (208V/240V/480V), service type (single-phase vs. three-phase), and whether power is delivered at the building service entrance or distributed to tenant sub-panels.

**Use:** Power capacity is largely irrelevant for standard ambient-temperature warehouse and distribution uses, but becomes a critical underwriting variable for cold storage (refrigeration compressors draw substantial continuous load), advanced manufacturing (heavy machinery, welding, EV battery production), data-adjacent industrial, and cannabis cultivation. Insufficient power for a prospective tenant's intended use is a hard constraint that may require expensive utility upgrades (new transformers, substation upgrades) with long lead times and uncertain costs.

For cold storage, a general rule of thumb is 400–800 kW per 100,000 SF of refrigerated space, though actual requirements depend on temperature specification, building envelope efficiency, and equipment vintage. For advanced manufacturing, requirements are highly process-specific and should be obtained directly from the tenant's engineering team.

Underwriters acquiring cold storage or manufacturing assets should confirm available power, confirm utility upgrade costs if expansion is contemplated, and consider power cost as a major operating line item for cold-storage tenants (energy costs are often the single largest operating expense in a refrigerated warehouse).
