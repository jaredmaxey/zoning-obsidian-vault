---
title: "Absorption Rate"
aliases: ["Absorption Rate"]
type: concept
tags: [cre/concepts]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Absorption rate is the pace at which available space or units are leased or sold in a market over a period, used to project lease-up timelines in development and value-add underwriting.
domain: concepts
formula: true
related:
  - "Vacancy and Collection Loss"
  - "Stabilized NOI"
  - "Net Operating Income (NOI)"
  - "Effective Gross Income (EGI)"
  - "Supply Pipeline Analysis"
  - "Demand Driver Analysis"
  - "Absorption Modeling"
  - "Pro Forma Construction Method"
---

# Absorption Rate

## Definition

Absorption rate is the rate at which available space (for leasing) or units (for sale or lease) are leased or sold in a defined market or submarket over a given period. In commercial real estate, it appears in two closely related but distinct forms: **gross absorption** — the total square footage (or units) leased in a period regardless of vacancies opened; and **net absorption** — the net change in occupied space, calculated as space newly leased minus space vacated. Net absorption is the more meaningful indicator of market health, as it captures whether the overall demand for space exceeds or falls short of new supply entering the market.

For development and value-add underwriting, absorption rate is the critical assumption that determines how long it takes to lease up a project from vacant (or partially vacant) to stabilized occupancy. A 300-unit apartment community in a submarket absorbing 100 units per month from new supply has a theoretical lease-up period of roughly 3–4 months per building (accounting for retention, competition, and seasonal variation); a submarket absorbing 30 units per month from new supply may take 10–12 months or longer to stabilize a comparably sized project. This timing drives the interest carry, the equity contribution schedule, and the earliest feasible permanent loan refinancing.

Absorption rate is a function of demand (population growth, job creation, household formation) and supply (competing new deliveries in the pipeline). Understanding absorption at the submarket level — not just the market level — is essential for development underwriting; a strong metropolitan absorption rate means nothing if the specific submarket is oversupplied by competing projects delivering in the same window. See [[Supply Pipeline Analysis]] and [[Demand Driver Analysis]].

## Formula

**Net Absorption:**
- Plain text: `Net Absorption = Newly Occupied Space − Newly Vacated Space`
- LaTeX: $$ \text{Net Absorption} = \text{Space Newly Leased} - \text{Space Vacated} $$

**Months of Lease-Up:**
- Plain text: `Months to Stabilization = Units Available / Average Monthly Net Absorption per Building`
- LaTeX: $$ t = \frac{N_{\text{units}}}{\text{Absorption Rate (units/month)}} $$

**Where:**
- **Space Newly Leased** — square feet (or units) that transitioned from vacant/unoccupied to occupied in the measurement period
- **Space Vacated** — square feet (or units) that transitioned from occupied to vacant in the measurement period
- **Absorption Rate** — the average monthly or quarterly net leasing activity in the submarket, estimated from historical data or demand modeling
- **t** — estimated months to reach stabilized occupancy from initial delivery

## When It's Used

Absorption rate is used primarily in development and value-add underwriting to model the lease-up period. A developer building 250 multifamily units in a given submarket will analyze how many competitive units are delivering in the same timeframe, the submarket's historical monthly absorption rate for new Class A apartments, and the implied months to stabilize their project — then build a month-by-month occupancy ramp into the pro forma.

In market analysis, net absorption relative to new supply deliveries is a key indicator of market balance. Positive net absorption in excess of new supply deliveries signals tightening market conditions (rising rents, falling vacancy); negative net absorption or absorption well below new supply signals loosening conditions. Brokers, lenders, and appraisers track trailing quarterly and annual absorption data by submarket and asset class to form views on rent trajectory.

For development financing, construction lenders require a lease-up assumption in the underwriting; they want to confirm that the absorption assumption is consistent with submarket data and that the interest reserve adequately covers the projected lease-up period plus a buffer. An overly aggressive absorption assumption (faster than market history supports) will fail lender underwriting.

## Variations & Edge Cases

**Gross vs. net absorption:** In markets with high turnover (apartments, some office), gross absorption can look much stronger than net absorption because large volume of leasing activity is offset by equal or larger move-outs. Net absorption is the more meaningful underlying demand indicator.

**Shadow supply:** Absorption rate analysis should account for "shadow supply" — sublease space and other space being offered by tenants that does not appear in vacancy statistics but competes directly with new supply. In the post-pandemic office market, large shadow sublease supply significantly dampened effective absorption of new office space.

**Seasonality:** Multifamily absorption tends to peak in summer months (May–August) when household moves concentrate. Retail absorption around anchor lease-ups can be lumpy and non-linear. Development underwriting should model seasonal absorption patterns rather than assuming flat monthly absorption throughout the year.

## Common Mistakes

**Using market-level absorption to underwrite a submarket project.** A strong city-wide absorption rate may mask significant variation across submarkets. The relevant absorption data is the specific competitive submarket.

**Ignoring competing supply pipeline.** Absorption rate is only useful if you know both the demand side (historical absorption) and the supply side (competing deliveries). A high historical absorption rate in a market with 10,000 units delivering in the next 12 months means less than the same absorption rate with limited pipeline competition.

**Assuming linear absorption.** Lease-ups often show an S-curve: slow initial traction as the building opens, then faster absorption once amenities are complete and word-of-mouth builds, then a tail as the final 5–10% of units stabilize. Modeling flat monthly absorption may produce an unrealistic lease-up model.

## Related Concepts

- [[Vacancy and Collection Loss]] — the vacancy assumption in steady-state underwriting is the inverse of the stabilized occupancy rate that absorption predicts
- [[Stabilized NOI]] — the income achieved after the absorption/lease-up period concludes
- [[Supply Pipeline Analysis]] — the competing supply context that sets absorption rate expectations
- [[Demand Driver Analysis]] — the demand fundamentals that drive underlying absorption
- [[Absorption Modeling]] — the analytical framework for projecting absorption-based lease-up scenarios
- [[Pro Forma Construction Method]] — the month-by-month pro forma that uses absorption rate to model occupancy ramp

## Sources

Absorption data is published quarterly by CoStar, CBRE, JLL, Cushman & Wakefield, Yardi Matrix, and RealPage for multifamily. Local market absorption analysis is also produced by regional brokerage firms and market research consultants. All absorption figures are market- and submarket-specific (varies by market and vintage; current as of 2026-05-24).
