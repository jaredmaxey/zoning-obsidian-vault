---
title: "Employment and Jobs Analysis"
aliases: ["Employment and Jobs Analysis"]
type: framework
tags: [cre/market-analysis]
created: "2026-05-24"
updated: "2026-05-24"
status: draft
ai_summary: Framework for analyzing local employment base, sector composition, growth trends, and labor supply to underpin demand projections for office, industrial, and other employment-driven CRE.
inputs_required:
  - BLS Quarterly Census of Employment and Wages (QCEW) by county and NAICS sector
  - BLS Current Employment Statistics (CES) for MSA-level monthly payroll data
  - BLS location quotient data for sector concentration analysis
  - MSA-level unemployment rate trends (BLS Local Area Unemployment Statistics, LAUS)
  - Major employer list and headcount (business license records, local EDC, CoStar)
  - Labor shed analysis (commute data from Census LEHD or ACS B08301)
  - Forward employment projections (BLS state occupational projections, Moody's Analytics, Woods & Poole)
outputs:
  - Employment base profile by sector (jobs count, share, growth rate)
  - Location quotient analysis (sector concentration vs. national benchmark)
  - Major employer dependency assessment
  - Implied space demand calculation (SF per job by sector)
  - Employment-demand narrative for investment memo
related:
  - "Demand Driver Analysis"
  - "Demographic Analysis"
  - "Submarket Definition and Selection"
  - "Supply Pipeline Analysis"
  - "Trade Area Analysis (Retail)"
  - "Four-Quadrant Model"
---

# Employment and Jobs Analysis

## Purpose

Employment and jobs analysis examines the structure, composition, and trajectory of the local labor market to establish how much and what type of CRE demand the economy is generating. Employment is the single most important demand driver for office and industrial space, a significant driver for retail expenditure, and an important context variable for multifamily (in-migration typically follows job growth). The framework goes beyond headline job counts: it profiles sector mix, concentrations, and vulnerabilities to identify whether a market's employment base is diversified and growing or concentrated in volatile sectors that pose demand risk.

Analysts use this framework when the demand case for an acquisition or development hinges on job growth — which is most of the time for commercial (non-residential) underwriting. The output feeds directly into [[Demand Driver Analysis]] and is a critical input to any [[Four-Quadrant Model]] analysis of market rent equilibrium. For retail and multifamily analysis, employment data provides the income and population growth context that supports spending power and household formation assumptions. Employment analysis also informs labor supply (key for manufacturing, distribution, and call-center industrial tenants) and commute shed analysis (key for suburban office positioning).

## Inputs Required

- **BLS QCEW:** Quarterly Census of Employment and Wages; county-level employment by NAICS supersector; the most complete and reliable local employment dataset in the U.S. Available at bls.gov/cew. Lags by roughly 6 months.
- **BLS CES:** Current Employment Statistics; MSA-level monthly payroll data with a shorter lag. Good for identifying recent trend inflections.
- **BLS LAUS:** Local Area Unemployment Statistics; monthly unemployment rate by county and MSA for cyclical context.
- **Location quotient data:** Available from BLS or ESRI; measures whether the local economy is over- or under-represented in a sector relative to the national economy.
- **Major employer list:** Local Economic Development Corporation (EDC) publications, CoStar tenant-in-common records, business license data, or news research for the top 10–20 employers by headcount.
- **Census LEHD (LODES):** Longitudinal Employer-Household Dynamics data; block-level jobs count and worker flow data; useful for mapping where jobs are located within the submarket.
- **Forward projections:** BLS state-level 10-year occupational employment projections; Moody's Analytics MSA employment forecast; Woods & Poole long-range county employment model.

## Method

1. **Pull total employment and growth trend.** From BLS QCEW at the county level (or MSA for broader context), extract total covered employment for the past 10 years. Calculate the 5-year and 10-year employment CAGR. Compare to U.S. national employment CAGR for the same period to assess relative performance.

2. **Profile sector composition.** Extract employment by NAICS supersector (e.g., Natural Resources and Mining; Construction; Manufacturing; Trade, Transportation, and Utilities; Information; Financial Activities; Professional and Business Services; Education and Health Services; Leisure and Hospitality; Other Services; Government). Express as both absolute jobs count and percentage share of total employment.

3. **Calculate location quotients (LQs).** For each supersector: LQ = (Local sector employment share) ÷ (National sector employment share). An LQ > 1.2 indicates a sector concentration (the local economy exports that sector's output); an LQ < 0.8 indicates an under-representation. High LQs identify the sectors that define the local economy and drive in-migration and wage income.

4. **Assess major employer concentration and diversity.** Identify the top 10 employers by headcount (EDC data, news research). Calculate the share of total county employment represented by the top 5 and top 10 employers. High concentration (top 5 employers > 15–20% of total employment; varies by market and vintage; current as of 2026-05-24) signals single-employer risk. Cross-reference employer industry with sector LQs.

5. **Map the labor shed.** Using Census LEHD or ACS commute data (Table B08301), identify the geographic extent of the labor shed — where workers commute from to reach the submarket's major employment nodes. A large labor shed (30+ minute average commute) affects suburban office positioning and industrial labor availability.

6. **Identify cyclical vs. structural components.** Distinguish between job losses/gains that are cyclical (recession-related, likely to reverse) and structural (industry contraction, automation, remote work, trade policy). Structural losses warrant a permanent downward adjustment to space demand; cyclical losses do not.

7. **Project forward employment growth.** Gather forward projections from BLS state occupational projections, Moody's Analytics, or Woods & Poole. Construct a low/base/high range. Convert projected employment growth in the target sectors to implied annual space demand using sector-specific space-per-job benchmarks (varies by sector and market; validate against local historical CoStar absorption per job added).

8. **Write the employment narrative.** Summarize the employment profile in 2–3 paragraphs: market size, sector mix, key concentrations, growth trajectory, and the 2–3 largest demand risks (employer consolidation, remote work, sector displacement). State the base-case employment growth assumption and its implied annual space demand.

## Outputs

The primary output is an **employment base profile** — a table showing employment by sector with absolute job counts, sector shares, location quotients, and 5-year growth rates. Supporting this is a **major employer dependency assessment** (top-10 employer list with headcount and sector). The **implied space demand calculation** translates projected job growth into annual SF demand by sector. The **employment narrative** (2–3 paragraphs) contextualizes the data and states the demand projection assumption, feeding [[Demand Driver Analysis]].

## Example Walkthrough

The following numbers are illustrative and hypothetical, labeled as such throughout.

Suppose the subject is a hypothetical 80,000 SF Class B flex/office building in a mid-size metro. The analyst pulls BLS QCEW for the county and finds approximately 180,000 covered jobs (hypothetical), with a 5-year employment CAGR of approximately 2.1% — above the hypothetical national average of 1.3%. Professional and Business Services (PBS) accounts for 16% of total employment (hypothetical LQ of 1.15), suggesting a modest above-average concentration. The top 5 employers represent approximately 8% of total employment — a relatively diversified base. A Moody's Analytics forecast projects the county to add approximately 3,500 PBS jobs per year over the next 5 years (hypothetical). Applying a hypothetical PBS space-per-job benchmark of 175 SF/employee (varies by market and vintage; current as of 2026-05-24), the model implies approximately 612,500 SF of annual gross office demand — consistent with historical CoStar net absorption of 500,000–700,000 SF/year in the submarket. The analysis supports the subject's lease-up assumption.

## Limitations

BLS QCEW data lags by 5–6 months and covers only employees on covered payrolls — it under-counts self-employed, gig workers, and contractor-heavy industries. Location quotients reflect current conditions; emerging industries may not yet appear as concentrated even if they are the fastest-growing employers in the market. The space-per-job benchmark is a simplifying assumption that varies widely by industry, corporate culture, and remote work policy; the same job gain in a tech company vs. a back-office financial firm may imply very different space demand. Employment projections are unreliable beyond 3–5 years and particularly vulnerable to macro shocks, policy changes, and technological disruption. For markets heavily dependent on a single major employer or federal government payrolls, headline job growth may mask underlying diversification risk.

## Related Frameworks

[[Demand Driver Analysis]] incorporates employment analysis as its primary input for commercial property types. [[Demographic Analysis]] covers the population and income side of the same demand picture. [[Trade Area Analysis (Retail)]] uses employment income as an input to retail expenditure potential. [[Four-Quadrant Model]] uses employment growth as the demand shock that shifts long-run rent equilibrium. [[Submarket Definition and Selection]] establishes the geographic unit against which employment data is measured.
