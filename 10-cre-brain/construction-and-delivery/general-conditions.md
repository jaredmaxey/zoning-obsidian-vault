---
title: "General Conditions"
aliases: ["General Conditions"]
type: concept
tags: [cre/construction]
created: "2026-05-24"
updated: "2026-05-24"
status: draft
ai_summary: The general contractor's direct project overhead—superintendent, field office, temporary utilities, and site logistics—billed separately from trade work and GC fee.
domain: construction
formula: true
related: ["Hard Costs", "Soft Costs", "GMP vs. Cost-Plus vs. Lump-Sum", "Contingency: Hard vs. Soft", "Construction Schedule and Critical Path", "Pro Forma Construction Method"]
---

# General Conditions

## Definition

General conditions (GC) are the direct project overhead costs a general contractor incurs to manage and operate a construction site—as distinct from the actual trade work (subcontractor scopes) and the GC's profit and overhead fee. Typical general conditions line items include: project superintendent and assistant superintendent salaries, project manager time, field trailer and site office, temporary utilities (power, water, lighting), site fencing and security, temporary sanitation, safety and first-aid programs, construction hoisting and vertical transportation, progress photography, project signage, final cleaning, and dumpster/debris removal. They are the logistical infrastructure that enables construction to happen, but they do not directly create the physical building.

General conditions are time-dependent: they are a function of the project schedule duration, site complexity, and workforce size. A project that runs long—whether due to design changes, weather, supply chain delays, or permitting—incurs more general conditions cost, which is why schedule management has direct cost implications (see [[Construction Schedule and Critical Path]]). This time-sensitivity distinguishes general conditions from trade costs, which are more closely tied to quantity takeoffs.

The term "general conditions" overlaps with "general requirements" (CSI Division 1 in the MasterFormat system)—they are used interchangeably in practice. Some practitioners use "general conditions and general requirements" (GCGR) as a combined line. The GC's overhead and profit (OH&P) or "fee" is a separate percentage added on top of general conditions and is not included in general conditions itself.

## Formula

General conditions are typically expressed as a percentage of total construction cost (subcontractor work + material costs), or as a separate lump sum within the contract. As a benchmark rule of thumb:

- Plain text: `GC Cost = Total Construction Cost × GC%`
- LaTeX: $$ \text{GC Cost} = \text{Total Construction Cost} \times \text{GC\%} $$

Where:
- **Total Construction Cost** = the sum of all subcontracted trade costs and self-performed work, excluding general conditions and fee
- **GC%** = general conditions as a percentage of trade costs, typically in the range of 5–12%, varying by project size, complexity, schedule, and market (varies by market, product type, and vintage; current as of 2026-05-24). Larger, longer, and more complex projects tend to produce lower GC percentages as overhead is spread over a larger base.

Note that the GC's profit and overhead fee is added separately—often 3–8% on top of all costs including general conditions—and should not be conflated with general conditions. The combined "GC markup" (general conditions + fee) commonly runs 8–18% of total trade cost depending on contract type and project size (varies by market, product type, and vintage; current as of 2026-05-24).

## When It's Used

General conditions budgeting is relevant throughout the project delivery process. During early feasibility and underwriting, developers apply general conditions as a rule-of-thumb percentage to the estimated hard cost base when preparing development budgets and pro formas (see [[Pro Forma Construction Method]]). As design advances and a GC is selected, general conditions are detailed and negotiated, particularly in [[GMP vs. Cost-Plus vs. Lump-Sum]] contracts where the general conditions scope is defined with precision.

In cost-plus and GMP contracts, general conditions are typically listed as a reimbursable cost—the owner pays actual general conditions incurred, up to any agreed cap or GMP ceiling. This creates an incentive alignment issue: the GC benefits from a longer schedule because more general conditions are incurred and reimbursed. Owners often address this with schedule incentive provisions and careful auditing of general conditions billings.

In lump-sum contracts, the GC prices general conditions into the fixed price and bears the risk of any overrun—but also keeps any savings. Buyers and lenders reviewing a lump-sum bid should verify that the GC's included general conditions are sufficient for the project scope; an artificially thin general conditions allocation in a bid can signal that the GC plans to recover costs through change orders.

## Variations & Edge Cases

The placement of general conditions in the project budget varies by convention. Some developers include them within [[Hard Costs]] since they are part of the construction contract. Others report them as a separate line between hard costs and [[Soft Costs]]. Lenders and institutional investors often have their own required budget formats that specify where general conditions should appear—always confirm.

On multi-phase or campus developments, general conditions allocation across phases is a negotiated and sometimes contentious topic. If one phase's GC team supports future phases, the cost allocation affects each phase's pro forma and may affect lender advance mechanics. Similarly, on design-build projects (see [[Design-Build vs. Design-Bid-Build]]), the design-builder may blend general conditions into a combined price, obscuring the line item.

Owner's general conditions—the developer's own project management staff, their office, their equipment—are not part of the GC's general conditions. These are developer soft costs (project management overhead) and should be tracked separately to avoid double-counting.

## Common Mistakes

The most common error is conflating general conditions with the GC's fee/profit. These are separate: general conditions are reimbursable project overhead; fee is the GC's compensation for managing the project. Confusing them leads to misunderstanding the true cost of construction and the GC's risk-taking incentives.

A second mistake is not escalating general conditions budgets for schedule slippage in sensitivity analysis. A six-month schedule extension on a mid-size project can add hundreds of thousands to over a million dollars in incremental general conditions—this should be modeled in the contingency and schedule risk analysis.

Failing to audit general conditions billings in cost-plus contracts is a third error. GCs may bill borderline items (home office overhead, corporate staff time, unrelated equipment) as general conditions. Owners should have their construction manager or owner's representative review general conditions billings monthly.

## Related Concepts

[[Hard Costs]] is the broader category in which general conditions may be embedded. [[Soft Costs]] may also include GC-adjacent costs depending on budget convention. [[GMP vs. Cost-Plus vs. Lump-Sum]] explains how general conditions are risk-allocated in different contract types. [[Contingency: Hard vs. Soft]] discusses how reserves are sized against general conditions exposure. [[Construction Schedule and Critical Path]] explains why schedule duration directly drives general conditions cost.

## Sources

- AIA (American Institute of Architects), *AIA Document A201 — General Conditions of the Contract for Construction* — the standard legal framework defining GC responsibilities and reimbursable costs.
- CSI MasterFormat, Division 01 (General Requirements) — the industry-standard cost code structure for general conditions items.
- Urban Land Institute, *Real Estate Development: Principles and Process*, 5th ed. (Washington, DC: ULI, 2015). Cost structure and GC fee benchmarking.
- RSMeans Cost Data (annual editions) — general conditions as a percentage of total cost by project type.
