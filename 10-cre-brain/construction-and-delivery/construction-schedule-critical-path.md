---
title: "Construction Schedule and Critical Path"
aliases: ["Construction Schedule and Critical Path"]
type: concept
tags: [cre/construction]
created: "2026-05-24"
updated: "2026-05-24"
status: draft
ai_summary: The timeline governing a construction project and the sequence of interdependent activities whose combined duration determines the earliest possible completion date.
domain: construction
formula: false
related: ["Hard Costs", "Soft Costs", "General Conditions", "Contingency: Hard vs. Soft", "GMP vs. Cost-Plus vs. Lump-Sum", "Design-Build vs. Design-Bid-Build", "Certificate of Occupancy (CO)", "Punchlist and Final Completion", "Construction Loan", "Ground-Up Development", "Development Feasibility Test"]
---

# Construction Schedule and Critical Path

## Definition

The construction schedule is the project's master timeline: an organized sequence of activities, durations, dependencies, and milestones that defines how the project will proceed from mobilization to substantial completion. The **critical path** is the longest chain of dependent activities through the schedule—the sequence that, if any activity slips, directly delays the project completion date. Activities not on the critical path have "float" (slack)—they can slip within limits without affecting the end date.

Critical Path Method (CPM) scheduling is the industry-standard technique for construction schedules. CPM uses a network diagram (activity-on-node or activity-on-arrow) to map all activities and their dependencies, calculates forward and backward passes to identify the critical path and float values for every activity, and produces the baseline schedule. CPM schedules are submitted to the owner and lender as a contract requirement and updated monthly (or more frequently on complex projects) to show actual vs. planned progress.

Construction schedules have major phases that must be tracked: pre-construction (design completion, permitting, GMP), sitework and foundations, structural framing/vertical construction, rough MEP (mechanical, electrical, plumbing) rough-in, building envelope, interior finishes, final MEP, inspections, and [[Certificate of Occupancy (CO)]]. Each phase depends on prior phases, and some phases have long-lead elements—structural steel, curtain wall, elevators, major mechanical equipment—that must be procured far in advance of installation because manufacturing lead times can be 16–40 weeks or longer.

## When It's Used

Schedule management is relevant throughout the entire development process, beginning at feasibility. At the pro forma stage, the developer estimates total construction duration (typically 18–36 months for mid-size multifamily or mixed-use; 12–24 months for industrial; longer for complex mixed-use or high-rise) and models interest carry based on that duration—see [[Soft Costs]] and [[Construction Loan]]. Errors in the schedule assumption directly affect the carry cost and, therefore, the [[Development Feasibility Test]] outcome.

During the construction loan process, the schedule is a key underwriting input. Lenders model construction draws against the CPM schedule to size the construction loan facility and interest reserve. They also impose schedule milestones as loan conditions: failure to achieve a milestone (e.g., framing complete by date X) may trigger a notice of default or extension fee. Lender CPM schedule reviews by a third-party inspector are standard practice.

During construction, the CPM schedule is the owner's primary cost control tool as well as a scheduling tool. Because [[General Conditions]] are time-dependent, every month of schedule slippage incurs incremental general conditions cost. If the critical path slips, the developer must decide whether to accelerate (crash) the schedule by adding resources—at cost—or absorb the delay. Acceleration analysis compares the cost of crashing activities to the cost of extended carry, and the optimal choice depends on current interest rates and market conditions.

## Variations & Edge Cases

Fast-tracking is the practice of overlapping design and construction phases—beginning construction on completed portions of the design (foundations, site work) while later portions are still being designed. Fast-tracking compresses the total project schedule but increases the risk of rework and change orders if the later design phases require changes to already-constructed work. It is common in [[Design-Build vs. Design-Bid-Build]] design-build delivery.

Phased delivery separates a large project into discrete phases that are designed, permitted, and constructed sequentially. This allows early phases to be complete and generating revenue while later phases are under construction—useful on large mixed-use or campus developments. Each phase has its own critical path and [[Certificate of Occupancy (CO)]], which must be coordinated with the overall project financing.

Long-lead procurement management is a critical path discipline. Structural steel, precast concrete, curtain wall systems, elevators, and major mechanical and electrical equipment all have long manufacturing or fabrication lead times. A project that delays procuring these items—waiting for GMP execution before placing orders—can add months to the critical path with no corresponding reduction in any other activity. Experienced developers place purchase orders for long-lead items as early as the structural system is selected, sometimes under early work packages before the full GMP.

## Common Mistakes

The most common schedule error in development underwriting is using best-case schedule assumptions with no slack. A complex urban project underwritten at 18 months that actually takes 24 months has added 6 months of general conditions and carry—often $2–5 million or more for a mid-size project. Schedule contingency (adding buffer to the baseline CPM, or modeling a delay scenario in the pro forma) is essential but often omitted.

Failing to understand the critical path leads to misdirected attention during construction. Owners and developers who focus on non-critical activities (rushing a particular subcontractor who is not on the critical path) while ignoring actual critical path risks are wasting attention and money. CPM schedule reviews should always identify and track the top 3–5 activities with the least float and the most schedule risk.

Ignoring long-lead procurement is a systemic error, particularly for developers entering projects after periods of supply chain disruption. A curtain wall system or specialty HVAC equipment that was six weeks from order to delivery in 2018 may require 52 weeks in a constrained market. Updated lead time surveys from the GC should be obtained at GMP and updated quarterly.

## Related Concepts

[[General Conditions]] are directly driven by schedule duration—every month of delay costs money in GC overhead. [[Contingency: Hard vs. Soft]] includes reserves for schedule-driven cost overruns. [[Certificate of Occupancy (CO)]] is the schedule endpoint that triggers lease-up and revenue. [[GMP vs. Cost-Plus vs. Lump-Sum]] and [[Design-Build vs. Design-Bid-Build]] both affect schedule strategy. [[Construction Loan]] terms impose schedule milestones and interest carry models the schedule duration. [[Punchlist and Final Completion]] is the close-out sequence that follows substantial completion.

## Sources

- Project Management Institute (PMI), *A Guide to the Project Management Body of Knowledge (PMBOK Guide)* — CPM scheduling methodology.
- Construction Management Association of America (CMAA), *CM Standards of Practice*.
- AIA (American Institute of Architects), AIA Document G714 — Construction Change Authorization and Schedule management provisions.
- Urban Land Institute, *Real Estate Development: Principles and Process*, 5th ed. (Washington, DC: ULI, 2015). Schedule management in development.
