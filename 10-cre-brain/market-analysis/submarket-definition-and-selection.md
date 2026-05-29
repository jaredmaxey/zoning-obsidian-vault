---
title: "Submarket Definition and Selection"
type: framework
tags: [cre/market-analysis]
created: "2026-05-24"
updated: "2026-05-24"
status: draft
ai_summary: Framework for drawing defensible submarket boundaries and selecting the right competitive set for any CRE market study.
inputs_required:
  - Subject property address and parcel data
  - Property type (office, industrial, retail, multifamily, etc.)
  - CoStar or equivalent broker-defined submarket boundaries (shapefile or map)
  - Census tract and ZIP code boundaries (Census/ACS)
  - Major physical barriers (freeways, rivers, rail corridors) from aerial/GIS
  - Leasing and sales activity by geography (CoStar, MSCI/RCA)
  - Drive-time or radius isochrones (ESRI or Google Maps)
outputs:
  - Written submarket definition with boundary rationale
  - Map exhibit with subject, boundaries, and competitive properties
  - Competitive set list (typically 5–15 properties) with key attributes
  - Justification memo or narrative for appraisal or investment memo
related:
  - "Demand Driver Analysis"
  - "Supply Pipeline Analysis"
  - "Comparable Sales (Sales Comps)"
  - "Comparable Rents (Rent Comps)"
  - "Absorption Rate"
  - "Trade Area Analysis (Retail)"
  - "Site Selection Scorecard"
---

# Submarket Definition and Selection

## Purpose

Submarket definition is the foundational step in any CRE market study. Before an analyst can measure vacancy, quantify demand, or benchmark rents, the analyst must establish which geographic area and which set of comparable properties constitute the subject's true competition. A poorly drawn submarket produces misleading vacancy and absorption statistics, inflates or deflates achievable rents, and ultimately distorts underwriting. This framework answers two questions: (1) what boundaries define the competitive arena in which the subject competes for tenants or buyers, and (2) which specific properties constitute the competitive set within that arena?

Analysts reach for this framework at the outset of every acquisition underwrite, development feasibility study, or third-party market study. The output feeds directly into [[Supply Pipeline Analysis]], [[Demand Driver Analysis]], [[Comparable Rents (Rent Comps)]], [[Comparable Sales (Sales Comps)]], and [[Absorption Rate]] analysis. Because lenders, appraisers, and investors will scrutinize submarket selection, the boundaries must be defensible on physical, economic, and behavioral grounds — not merely drawn to produce a favorable vacancy rate.

## Inputs Required

- **Subject property address and parcel data:** Confirms asset type, size, age, and location from county assessor records or CoStar.
- **Broker-defined submarket polygons:** CoStar, CBRE, JLL, and similar sources publish submarket boundaries by property type. These serve as a starting reference but may need refinement for the subject's specific situation.
- **Census tract and ZIP code boundaries:** From Census Bureau TIGER files; useful for demographic overlay and ACS data alignment.
- **Physical barrier layer:** Major freeways, rivers, railroad corridors, and topographic breaks visible in Google Maps satellite view or local MPO GIS layers that naturally segment tenant search patterns.
- **Leasing and sales activity by geography:** CoStar or MSCI/RCA transaction exports showing where comparable deals have actually occurred, revealing the organic competitive zone.
- **Drive-time isochrones:** ESRI Business Analyst or Google Maps Distance Matrix API to define 5-, 10-, and 15-minute drive-time rings from the subject, calibrated by property type (e.g., 3-mile ring for neighborhood retail vs. 20-mile ring for regional distribution).
- **Tenant or buyer search criteria:** Broker interviews or tenant rep feedback on how prospective occupants define their search area.

## Method

1. **Start with the broker-defined submarket.** Pull the CoStar (or equivalent) submarket polygon for the subject's property type and review its boundary logic. Note any areas it includes that are physically or economically disconnected from the subject, and any areas it excludes that clearly compete.

2. **Map physical barriers.** Overlay major freeways, rail lines, rivers, and significant grade changes. These features typically limit tenant cross-shopping and often correspond to genuine competitive discontinuities. A warehouse tenant north of a rail corridor rarely competes with one south of it for the same users.

3. **Generate drive-time or distance rings.** As a cross-check, produce 5-, 10-, and 15-minute drive-time isochrones from the subject (ESRI or equivalent). For property types where locational adjacency matters most (neighborhood retail, medical office, self-storage), the drive-time ring often better captures the competitive set than broker-defined polygons.

4. **Identify comparable transaction clusters.** Pull all leases and sales in the prior 24–36 months for the subject's property type within a generous initial radius. Map the transactions and identify where they cluster. Outliers outside the natural cluster can be excluded from the primary submarket definition.

5. **Draft the submarket boundary.** Combine the broker polygon, physical barriers, drive-time rings, and transaction cluster evidence to draw a custom boundary. The boundary should form a contiguous, coherent geographic area. Document the rationale for any deviation from the standard broker submarket.

6. **Build the competitive inventory.** Within the submarket boundary, identify all properties that compete directly with the subject on property type, size, quality class (Class A/B/C), and vintage. Apply secondary screens for functional characteristics (clear heights for industrial, unit mix for multifamily, bay size for retail). The result is the Competitive Set, typically 5–15 properties for most submarket studies.

7. **Validate with broker interviews.** Confirm the boundary and competitive set with one or two local active brokers who lease the subject's property type. Revise if their market knowledge reveals systematic errors in the data-driven boundary.

8. **Document and map.** Produce a written boundary rationale (2–3 paragraphs) and a map exhibit showing the subject property, the submarket boundary, and the competitive set properties.

## Outputs

The primary output is a **written submarket definition** — a 2–3 paragraph narrative explaining the boundary rationale, the property type and quality tier being studied, and any deviations from standard broker-defined submersives. This is accompanied by a **map exhibit** plotting the subject, boundary, and competitive set. The secondary output is a **competitive set list** — typically a table of 5–15 properties with address, size (SF or units), year built, quality class, current occupancy, and asking rent. These outputs become the foundation for all downstream market analysis steps.

## Example Walkthrough

The following numbers are illustrative and hypothetical, labeled as such throughout.

Suppose the subject is a hypothetical 150,000 SF Class B industrial warehouse built in 2010, located in a mid-size Sun Belt metro. The analyst pulls CoStar's broker-defined "Southeast Industrial" submarket polygon and finds it covers roughly 45 million SF across a very large geographic area bisected by two major freeways and a river. Rather than accept this broad boundary, the analyst notes that the primary freeway interchange serving the subject (hypothetically, an I-XX/Highway YY interchange) forms a natural organizing node. Properties more than roughly 5 miles from that node, or on the opposite side of the river, rarely compete for the same 50,000–200,000 SF users based on CoStar lease activity mapping. The analyst draws a tighter custom submarket of approximately 12 million SF centered on the interchange node, capturing the 18 properties (hypothetically, ranging from 80,000 to 400,000 SF) where leasing activity has been concentrated. The resulting submarket shows a hypothetical current vacancy rate of 6–8% (varies by market and vintage; current as of 2026-05-24) versus 10–12% for the broader broker submarket — a material difference with direct implications for rent assumptions in underwriting.

## Limitations

Submarket definition is inherently judgment-based: two competent analysts may draw slightly different boundaries, and both may be defensible. The framework is most reliable when physical barriers, transaction patterns, and broker-defined boundaries all point in the same direction. It becomes less reliable in sprawling suburban markets with few physical barriers, where competitive behavior can shift over time as the tenant base or infrastructure evolves. For specialty property types (data centers, cold storage, medical office building) where the competitive set is thin or regional rather than local, a single submarket boundary may be less meaningful than a carefully curated competitive set drawn from a broader geography. Analysts should also guard against "boundary shopping" — adjusting the submarket to manufacture a favorable vacancy rate; lenders and appraisers will probe this.

## Related Frameworks

[[Demand Driver Analysis]] quantifies the demand side within whatever submarket boundary this framework establishes. [[Supply Pipeline Analysis]] tracks new deliveries within the same boundary. [[Comparable Rents (Rent Comps)]] and [[Comparable Sales (Sales Comps)]] draw their competitive sets from the output of this framework. For retail properties, [[Trade Area Analysis (Retail)]] provides a parallel demand-side boundary framework. [[Site Selection Scorecard]] uses submarket data as one scoring dimension. The concept of [[Absorption Rate]] is only meaningful relative to a defined submarket inventory.
