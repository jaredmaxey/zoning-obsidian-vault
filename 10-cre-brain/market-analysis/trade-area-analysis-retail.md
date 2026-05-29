---
title: "Trade Area Analysis (Retail)"
type: framework
tags: [cre/market-analysis]
created: "2026-05-24"
updated: "2026-05-24"
status: draft
ai_summary: Framework for defining the geographic zone from which a retail property draws customers, quantifying spending potential, and measuring retail demand against existing supply to identify gaps or surplus.
inputs_required:
  - Subject property address and proposed retail use or tenant mix
  - Drive-time isochrones (ESRI Business Analyst, Google Maps Distance Matrix API)
  - Trade area population and household income (Census/ACS, ESRI)
  - Retail expenditure potential by category (ESRI Retail Marketplace, BLS Consumer Expenditure Survey)
  - Competitive retail supply inventory (CoStar, ESRI, field survey)
  - Traffic counts on primary access roads (state DOT, MPO)
  - Consumer spending leakage and inflow data (ESRI Retail Marketplace)
outputs:
  - Defined primary, secondary, and tertiary trade area boundaries
  - Total trade area retail demand potential ($ by category)
  - Supply-demand gap or surplus analysis (retail leakage/inflow report)
  - Capture rate estimate for subject property
  - Narrative retail market context for investment memo or feasibility study
related:
  - "Submarket Definition and Selection"
  - "Demographic Analysis"
  - "Psychographic Analysis"
  - "Traffic Counts and Visibility"
  - "Demand Driver Analysis"
  - "Employment and Jobs Analysis"
  - "Site Selection Scorecard"
  - "Highest and Best Use Analysis"
---

# Trade Area Analysis (Retail)

## Purpose

Trade area analysis defines the geographic zone from which a retail property realistically draws its customers, quantifies the spending power of those customers by retail category, and measures that potential demand against the existing and planned supply of competitive retail space to identify whether the trade area is underserved (retail gap), in balance, or overserved (retail surplus). It is the foundational demand framework for evaluating any retail property — from a neighborhood strip center to a regional power center — and is a required component of retail development feasibility, retail acquisition underwriting, and retail anchor lease negotiations.

The framework recognizes that different retail categories have different trade area radii: convenience goods (grocery, pharmacy, QSR) draw from a tight primary zone of 1–3 miles or 3–5 minutes drive time; community goods (home improvement, sporting goods, apparel) draw from a secondary zone of 5–10 miles or 10–20 minutes drive time; destination or regional goods (furniture, specialty, entertainment) draw from a tertiary zone of 10–20+ miles. Defining the correct trade area for the contemplated retail use is the first and most critical step, because all downstream analysis is only as good as the geography it is applied to. Trade area analysis works in conjunction with [[Demographic Analysis]] (who lives in the trade area) and [[Psychographic Analysis]] (how they shop and what they value) to build a complete retail demand picture.

## Inputs Required

- **Subject property address and retail use/tenant mix:** Determines the appropriate trade area radius (convenience vs. community vs. regional), the retail categories for expenditure analysis, and the target sales-per-SF performance benchmark.
- **Drive-time isochrones:** 3-, 5-, 10-, and 15-minute drive-time rings generated from ESRI Business Analyst Online or the Google Maps Distance Matrix API, reflecting actual road network travel times rather than straight-line distance.
- **Trade area demographic data:** Census/ACS or ESRI current-year estimates for population, households, and median household income within each drive-time ring.
- **Retail expenditure potential:** ESRI Retail Marketplace (powered by Dun & Bradstreet and ACS income data) or BLS Consumer Expenditure Survey national averages by income quintile, translated to per-household annual expenditures by NAICS retail category.
- **Competitive retail supply inventory:** CoStar square footage by retail category within the trade area; ESRI Retail Marketplace supply data; field survey to confirm current tenanting, occupancy, and any recently closed anchors not reflected in databases.
- **Traffic counts:** AADT from state DOT for primary access roads, used to assess site accessibility and calibrate capture rate assumptions.
- **ESRI Retail Marketplace leakage/inflow data:** Retail Marketplace calculates retail gap or surplus by comparing estimated retail demand (supply potential) to estimated retail sales (demand potential) at the ZIP code or tract level — a direct measure of whether a category is underserved in the trade area.

## Method

1. **Define trade area rings.** Generate 3-, 5-, 10-, and 15-minute drive-time isochrones from the subject site. Designate primary (innermost ring, where the bulk of customers are expected to come from), secondary, and tertiary zones based on the retail category. For a neighborhood grocery-anchored center, the primary trade area is typically the 3–5 minute ring; for a power center with home improvement and sporting goods, the primary zone is typically 10–15 minutes.

2. **Pull trade area demographics.** From ESRI or Census/ACS, extract for each ring: total population, total households, median household income, and 5-year household growth projection.

3. **Calculate total retail expenditure potential.** Multiply households in the primary (and secondary) trade area by the per-household annual expenditure estimate for each relevant retail category. ESRI Retail Marketplace provides this as a single output (Supply and Demand potential by NAICS category); alternatively, use BLS Consumer Expenditure Survey expenditures per household scaled by local income adjustments.

4. **Inventory competitive supply.** From CoStar and field verification, catalog all competitive retail SF within the trade area by category and center type. Note anchor tenants, occupancy, age, and any significant near-term openings or closings. Calculate total competitive retail SF per household in the trade area and compare to national benchmarks (varies by market; U.S. average retail SF per capita has been approximately 20–25 SF/person in recent years; varies by market and vintage; current as of 2026-05-24).

5. **Calculate retail gap or surplus.** Using ESRI Retail Marketplace or a manual calculation: Retail Gap = Retail Demand Potential − Retail Sales (estimated from supply × average sales/SF benchmark for each category). A positive gap indicates unmet demand (leakage to competing centers); a negative gap indicates surplus supply or category saturation.

6. **Estimate capture rate for the subject.** The subject's capture rate is its realistic share of the total retail gap (or total trade area demand for its category). Capture rate depends on the subject's location within the trade area, traffic exposure, anchor tenancy, format, and competitive positioning. For a new or repositioned center, use industry benchmarks or comparisons to similar centers' known performance. A realistic primary trade area capture rate for a neighborhood center ranges from 15–35% of total grocery expenditure potential, for example (varies by competition and market vintage; current as of 2026-05-24).

7. **Translate capture rate to supportable sales volume.** Capture Rate × Trade Area Expenditure Potential = Supportable Annual Sales for the subject (in $). Divide by the subject's GLA to get implied sales per SF. Compare to the relevant tenant or category's typical sales threshold (national QSR or grocery chains publish minimum threshold criteria confidentially; analyst estimates based on comparable performance data).

8. **Assess retail leakage and import potential.** Identify categories where the trade area is severely underserved (high leakage to other markets). These represent the strongest pipeline for new retail recruitment. Identify categories where the trade area is saturated — avoid proposing new supply in those categories.

9. **Write the trade area narrative.** Summarize the trade area demographics, retail supply picture, gap/surplus by category, and the subject's supportable sales conclusion in 2–3 paragraphs.

## Outputs

The primary outputs are a **defined primary, secondary, and tertiary trade area** (map with drive-time rings), a **retail expenditure potential table** (demand potential by NAICS category in $), and a **retail gap/surplus analysis** showing which categories are under- or over-served. A **capture rate estimate** translates to a **supportable sales volume** and implied sales-per-SF for the subject. The narrative retail market context section (2–3 paragraphs) is a required component of any retail market study or investment memo.

## Example Walkthrough

The following numbers are illustrative and hypothetical, labeled as such throughout.

Suppose the subject is a hypothetical 45,000 SF neighborhood retail center anchored by a grocery concept, located in a growing suburban Sun Belt community. The analyst generates 5- and 10-minute drive-time isochrones. The 5-minute primary trade area contains approximately 18,000 households (hypothetical) with a median household income of $72,000. Hypothetical ESRI Retail Marketplace data shows total grocery expenditure potential of approximately $54 million annually in the primary zone ($3,000/household × 18,000 HH; all figures illustrative). Competitive supply within the primary trade area consists of one existing grocery-anchored center with 60,000 SF currently leased to an aging national chain that recently announced a potential closure (hypothetical). The ESRI leakage analysis shows the primary zone currently leaking an estimated $22 million in grocery spending to centers outside the trade area (hypothetical). The analyst estimates the subject can capture 40–50% of current leakage plus natural demand growth, supporting a hypothetical grocery anchor at $400–$450/SF in sales — within the anchor's minimum threshold criteria. The retail gap supports the project's feasibility.

## Limitations

ESRI Retail Marketplace expenditure estimates are modeled outputs derived from ACS income data and BLS expenditure surveys; they are not direct measurements of actual spending and can be materially wrong in markets with atypical income distribution, ethnic spending patterns, or high non-resident tourism spending. The retail gap analysis does not account for new competitive supply in the pipeline — a retail gap can disappear if a competing center delivers before the subject opens. Capture rate estimation requires significant judgment and is where analyses most frequently diverge. Drive-time isochrones reflect average network conditions and may not capture peak-hour access limitations (congested roads, school zones) that materially affect actual trading area shape. For large-format or destination retail, the relevant competition may be 20–30+ miles away, making a tight local trade area analysis insufficient.

## Related Frameworks

[[Demographic Analysis]] provides the population and income data that underpins trade area expenditure potential. [[Psychographic Analysis]] segments the trade area population by lifestyle and spending behavior, helping identify the most relevant retail categories. [[Traffic Counts and Visibility]] evaluates site accessibility, which affects trade area shape and capture rate. [[Submarket Definition and Selection]] is the equivalent boundary-setting framework for non-retail property types. [[Site Selection Scorecard]] integrates trade area analysis scores with other site criteria. [[Highest and Best Use Analysis]] draws on trade area analysis to evaluate whether retail is the highest and best use for a given site.
