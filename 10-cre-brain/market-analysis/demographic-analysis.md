---
title: "Demographic Analysis"
aliases: ["Demographic Analysis"]
type: framework
tags: [cre/market-analysis]
created: "2026-05-24"
updated: "2026-05-24"
status: draft
ai_summary: Framework for profiling the population, household, age, income, and education characteristics of a trade area to support demand underwriting for residential and consumer-facing CRE.
inputs_required:
  - Defined trade area or submarket boundary (from Submarket Definition and Selection or Trade Area Analysis (Retail))
  - Census/ACS current population and household estimates (Census Bureau)
  - ESRI Business Analyst or equivalent demographic projections (1-, 3-, 5-year)
  - Age cohort distribution (Census/ACS Table B01001)
  - Household income distribution (Census/ACS Table B19001)
  - Educational attainment (Census/ACS Table B15003)
  - Tenure (owner vs. renter) and housing cost burden (Census/ACS)
  - Migration data (Census/ACS Table B07001, IRS SOI migration data)
outputs:
  - Demographic profile summary (population, households, income, age, education)
  - Growth rate analysis (historical CAGR and forward projection)
  - Renter/owner split and affordability metrics for multifamily
  - Demand cohort identification (target demographic segments for the proposed use)
  - Narrative demographic market context for investment memo
related:
  - "Submarket Definition and Selection"
  - "Demand Driver Analysis"
  - "Employment and Jobs Analysis"
  - "Trade Area Analysis (Retail)"
  - "Psychographic Analysis"
  - "Absorption Modeling"
---

# Demographic Analysis

## Purpose

Demographic analysis profiles the population and household characteristics of a defined market area to establish whether sufficient demand generators — people, households, and income — exist to support a proposed CRE use. It is the foundational data layer beneath [[Demand Driver Analysis]] for consumer-facing property types: multifamily, retail, self-storage, senior housing, and medical office all depend fundamentally on who lives in the trade area, how many of them there are, and whether that number is growing. For multifamily, the analyst is specifically interested in renter-age cohorts (typically 20–34 and 55–74 year olds), household income distribution relative to the proposed rent tier, and in-migration velocity. For retail, demographic analysis quantifies spending power and population density. For office and industrial, demographic data plays a supporting role in labor supply analysis.

Demographic analysis is grounded in public-sector data — primarily the U.S. Census Bureau's American Community Survey (ACS) and its population estimates program — supplemented by commercial enrichment from ESRI Business Analyst, CoStar, or similar platforms that extrapolate Census data to non-Census-year estimates and forward projections. Analysts use this framework early in market study preparation, before layering in [[Psychographic Analysis]] (which adds lifestyle and behavior segmentation) and [[Employment and Jobs Analysis]] (which addresses the jobs side of the demand equation).

## Inputs Required

- **Trade area or submarket boundary:** Defined via [[Submarket Definition and Selection]] or [[Trade Area Analysis (Retail)]]; all demographic queries must be aligned to this geography.
- **Census/ACS current estimates:** ACS 5-year estimates at the census tract, ZIP code, or county level (Census Bureau data.census.gov). Key tables: B01001 (age by sex), B19001 (household income), B15003 (educational attainment), B25003 (tenure), B25070 (gross rent as % of income), B07001 (geographic mobility/migration).
- **ESRI Business Analyst projections:** 1-, 3-, and 5-year demographic forecasts for non-ACS-survey years and forward projections; available through ESRI Business Analyst Online or Tapestry Segmentation.
- **IRS Statistics of Income (SOI) migration data:** Tracks county-to-county migration flows based on tax return address changes; useful for identifying net in-migration trends and origin markets.
- **Local MPO forecasts:** Metropolitan Planning Organization regional transportation plan demographic forecasts for 10–25 year horizons; often the most defensible long-range projection source for local presentations.

## Method

1. **Align the trade area to Census geographies.** Map the defined trade area against census tract boundaries. For radius or drive-time geographies, use ESRI Business Analyst or Census's American FactFinder to apportion tract-level data by the fraction of each tract that falls within the study area.

2. **Pull current population and household counts.** From ACS 5-year estimates, extract total population, total households, average household size, and median age. Note the survey vintage (ACS 5-year estimates lag by 2–3 years) and supplement with ESRI current-year estimates.

3. **Calculate historical population growth rate.** Compare current ACS estimates to the prior decennial Census (2020) to calculate the compound annual population growth rate (CAGR) over the observation period. Compare to the broader MSA CAGR to assess whether the trade area is growing faster or slower than the metro.

4. **Profile age cohorts.** Extract the age distribution (ACS Table B01001). For multifamily underwriting, flag the 20–34 and 55–74 cohorts (high propensity-to-rent groups). For senior housing, focus on 65+ and 75+. For retail, note the working-age population (25–54) as a proxy for peak spending years.

5. **Profile income distribution.** Extract household income distribution (ACS Table B19001). Map income brackets against the proposed product's rent or price point. For multifamily, calculate the percentage of renter households that can afford the proposed rent at a 30% cost-burden threshold (i.e., affordable rent = household income × 30% ÷ 12). For retail, calculate average household expenditures in relevant categories using BLS Consumer Expenditure Survey benchmarks.

6. **Assess renter/owner split and housing affordability.** ACS Table B25003 provides tenure data. Calculate the current renter share of households. ACS Table B25070 reveals what percentage of renters are already cost-burdened (paying >30% of income on housing), which can signal both pent-up demand for more affordable product and a constraint on rent growth potential.

7. **Measure in-migration and net migration.** IRS SOI data or Census mobility tables identify whether the trade area is attracting net in-migrants, from which metros, and at what income levels. Strong net in-migration from higher-cost metros supports above-average rent growth assumptions.

8. **Project forward growth.** Use ESRI 5-year projections and MPO long-range forecasts to project household growth over the investment horizon. Triangulate across sources and note the range as a measure of forecast uncertainty. Convert projected household growth to implied demand for the subject's product type using the appropriate conversion ratio.

9. **Summarize the demographic profile.** Compile a one-page demographic snapshot table and a 2–3 paragraph narrative interpretation connecting the demographic evidence to the specific demand case for the proposed use.

## Outputs

The primary output is a **demographic profile table** covering population, households, age distribution, median household income, educational attainment, renter share, and growth rates — current and projected. This is accompanied by a **growth rate analysis** showing CAGRs and forward projections. For multifamily, an **affordability matrix** shows the income distribution of renter households relative to the proposed rent tier. A **demand cohort identification** names the primary and secondary target demographic segments and quantifies their size in the trade area. The narrative demographic summary is typically a 1–2 page section in a market study or investment memo.

## Example Walkthrough

The following numbers are illustrative and hypothetical, labeled as such throughout.

Suppose the subject is a hypothetical 200-unit Class B multifamily development targeting workforce renters in a suburban Sun Belt location. The analyst pulls ACS 5-year data for a hypothetical 3-mile trade area and finds approximately 45,000 people in 18,000 households, with a median household income of $62,000 and a renter share of 38% (hypothetical; varies by market and vintage; current as of 2026-05-24). The 20–34 cohort represents approximately 22% of the population, or roughly 9,900 people — a healthy renter-age cohort. ESRI projects the trade area will add approximately 1,200 net households over the next 5 years (hypothetical), driven by in-migration from a higher-cost coastal metro. At a proposed rent of $1,400/month, the affordability threshold (30% of income) requires a renter household income of approximately $56,000 — a level exceeded by roughly 55% of current renter households in the trade area (hypothetical). The demographic profile supports a market-rate workforce product with a strong addressable demand pool, subject to the supply pipeline analysis.

## Limitations

ACS data lags by 2–3 years and is based on survey methodology subject to sampling error, particularly for small geographies (tracts with fewer than 1,000 housing units). Commercial demographic projections (ESRI, Claritas) apply modeled extrapolations to the Census base data and can differ materially from each other and from eventual outcomes in fast-growing or rapidly declining markets. The framework does not capture qualitative factors such as neighborhood trajectory (gentrifying vs. declining) that can matter as much as headline demographic statistics. For very small or non-standard trade areas (a single city block, a remote rural site), Census geography alignment challenges can introduce material aggregation error. Demographic analysis is also backward-looking in its data: a market that has just experienced a major employer arrival or departure may not show the shift in any available dataset for 1–3 years.

## Related Frameworks

[[Trade Area Analysis (Retail)]] applies demographic analysis specifically to retail demand quantification. [[Psychographic Analysis]] layers lifestyle and behavior segmentation onto the demographic foundation. [[Employment and Jobs Analysis]] covers the jobs-side of the demand picture. [[Demand Driver Analysis]] synthesizes demographics, employment, and other drivers into a unified demand forecast. [[Submarket Definition and Selection]] establishes the geographic boundary to which all demographic data is aligned.
