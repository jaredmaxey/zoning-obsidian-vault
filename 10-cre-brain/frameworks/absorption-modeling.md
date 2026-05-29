---
title: "Absorption Modeling"
type: framework
tags: [cre/frameworks]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Framework for estimating the pace at which new or vacant space will be leased (absorbed) in a defined submarket, used to project lease-up timelines and NOI ramp in pro formas.
inputs_required:
  - Total new or vacant space to be absorbed (SF or units)
  - Historical net absorption data for the submarket and asset class
  - Current submarket vacancy rate
  - Demand driver indicators (employment, household formation, population growth)
  - Supply pipeline (competing deliveries during the absorption period)
  - Subject property competitive positioning (quality, location, pricing)
outputs:
  - Projected absorption rate (SF or units per month/quarter)
  - Projected lease-up timeline (months to stabilization)
  - Occupancy ramp curve (month-by-month or quarter-by-quarter)
  - Market share capture rate assumption
related:
  - "Four-Quadrant Model"
  - "Real Estate Cycle and Phases"
  - "Development Feasibility Test"
  - "Yield Analysis Methodology"
  - "Absorption Rate"
  - "Net Operating Income (NOI)"
  - "Stabilized NOI"
  - "Submarket Definition and Selection"
  - "Demand Driver Analysis"
  - "Supply Pipeline Analysis"
  - "Employment and Jobs Analysis"
  - "Demographic Analysis"
  - "Pro Forma Construction Method"
  - "Discounted Cash Flow (DCF)"
---

# Absorption Modeling

## Purpose

Absorption modeling estimates how quickly new or vacant commercial or residential space will be occupied in a defined submarket, translating demand driver data and historical leasing patterns into a projected occupancy ramp. Every development pro forma and value-add acquisition underwriting depends on an absorption assumption: if a 200-unit apartment project leases 15 units/month rather than 25, the lease-up timeline extends by 8 months, carrying costs increase, and the levered IRR drops meaningfully. Institutional analysts who treat absorption as a plug number — "we'll stabilize in 12 months because that's our model" — rather than a market-derived estimate are the most common source of pro forma optimism bias.

The framework distinguishes two levels of absorption: **market absorption** (total net new leasing in the submarket, regardless of which projects benefit) and **project absorption** (the subject property's capture of market absorption). Both must be estimated. A project delivered into a market absorbing 2 million SF per year can expect to capture a fraction of that total — its share depends on its size relative to the total market, its competitive positioning, and whether it competes against simultaneously delivering projects. The absorption model links the demand-side analysis in [[Demand Driver Analysis]] and [[Employment and Jobs Analysis]] to the supply-side analysis in [[Supply Pipeline Analysis]], producing the occupancy ramp that feeds the NOI schedule in [[Pro Forma Construction Method]] and [[Discounted Cash Flow (DCF)]].

## Inputs Required

- **Total space to absorb:** gross leasable area or unit count for the subject project; and the total new supply delivering into the submarket over the lease-up period from [[Supply Pipeline Analysis]].
- **Historical net absorption:** trailing 5–10 years of annual net absorption (occupied SF or units) in the defined submarket, by asset class and quality tier. Source: broker market reports (CBRE, JLL, CoStar), institutional research.
- **Current vacancy:** starting vacancy at project delivery; from submarket data per [[Submarket Definition and Selection]].
- **Demand drivers:** employment growth (for office and industrial), household formation (for multifamily), retail spending growth (for retail). Quantify annual demand increments per [[Demand Driver Analysis]] and [[Employment and Jobs Analysis]].
- **Competitive set:** projects under construction and planned that will compete for the same tenants/residents during the lease-up window; from [[Supply Pipeline Analysis]].
- **Subject property competitive position:** quality tier, location advantage, pricing relative to market (above/at/below market rents), amenity package.

## Method

1. **Define the relevant submarket and absorption universe.** Using [[Submarket Definition and Selection]], establish the boundary of the competitive space market. Not all supply competes — a Class A downtown office project does not compete with Class B suburban office. The absorption universe should include only directly competing inventory.

2. **Calculate historical absorption rate.** Using 5–10 years of historical net absorption data, calculate the average annual net absorption and the standard deviation:
   - `Average Annual Net Absorption = Total Net Absorption over Period / Number of Years`
   - Note the range (peak year vs. trough year) and any structural breaks (e.g., pandemic impact on office from 2020 onward).
   - Identify whether the historical period was demand-led (absorption > supply → declining vacancy) or supply-led (supply > absorption → rising vacancy).

3. **Derive a forward demand estimate.** Project annual demand (net new space need) using demand drivers:
   - For **office:** `Demand = Net Job Growth in Office-Using Sectors × Average SF per Office Worker` (typically 150–200 SF/worker for modern layouts, varies by market and vintage, current as of 2026-05-24).
   - For **industrial:** `Demand = Net Goods-Handling Employment Growth × Benchmark SF/worker` plus e-commerce demand proxy.
   - For **multifamily:** `Demand = Household Formation Rate × Target Capture Rate for Rental Apartments`.
   - For **retail:** demand is driven by consumer spending growth and population growth in the trade area; see [[Trade Area Analysis (Retail)]].
   
   Compare forward demand estimate to historical average as a reasonableness check. If forward demand diverges significantly from history, document the structural driver.

4. **Estimate total market supply competing during the lease-up window.** Sum all competitive space delivering over the subject's projected lease-up period from [[Supply Pipeline Analysis]]. Add the subject's own space. Compute the supply-demand balance:
   
   `Net Demand/Supply Balance = Annual Demand − Annual Competitive Deliveries`
   
   A positive balance indicates demand is absorbing supply (declining vacancy); negative indicates oversupply (rising vacancy).

5. **Estimate the subject project's market capture rate.** The capture rate is the percentage of annual market absorption the subject project will receive. It is a function of:
   - Market share by size: `Subject SF or Units / Total Competitive Submarket Size`
   - Competitive adjustment: projects with superior location, amenities, or pricing capture more than their pro-rata share; inferior projects capture less.
   - Typical capture rates for a new development range from 5–25% of annual submarket absorption (varies widely by submarket size and asset class, current as of 2026-05-24).
   
   `Project Monthly Absorption = (Annual Submarket Absorption × Capture Rate) / 12`

6. **Build the occupancy ramp.** Starting from delivery date (0% occupancy), apply the monthly absorption rate to project the occupancy schedule:
   - Month 1: `Units/SF Leased = Project Monthly Absorption Rate`
   - Each subsequent month: accumulate until stabilized occupancy is reached (typically defined as market-standard vacancy, e.g., 5–7% for multifamily, 7–10% for Class A office, varies by market, current as of 2026-05-24).
   - `Months to Stabilization = (Total Units or SF × Stabilized Occupancy) / Monthly Absorption Rate`

7. **Validate against rule-of-thumb benchmarks.** Typical lease-up timelines (illustrative, varies by market and cycle): multifamily garden-style = 10–18 months; multifamily high-rise = 18–30 months; suburban industrial = 6–18 months; suburban office = 18–36+ months; retail = 12–24 months. If the modeled timeline is materially shorter than typical for the asset class, question the capture rate and demand assumptions.

8. **Translate to NOI ramp.** In the pro forma, apply the occupancy ramp to gross potential rent to derive effective gross income and then NOI by period. The NOI ramp is the key output for the [[Discounted Cash Flow (DCF)]] model and determines the cash flow deficit during the lease-up period that must be funded by equity or a construction/permanent loan structure.

## Outputs

- Historical average annual net absorption (SF or units) for the submarket.
- Forward annual demand estimate with driver basis.
- Supply-demand balance over the lease-up period.
- Project capture rate (%) with stated rationale.
- Monthly absorption rate (units or SF/month).
- Projected months to stabilization.
- Month-by-month (or quarter-by-quarter) occupancy ramp from delivery to stabilization.
- NOI ramp for input into the [[Pro Forma Construction Method]] and [[Discounted Cash Flow (DCF)]].

## Example Walkthrough

*All figures below are illustrative/hypothetical.*

**Project:** 180-unit Class A multifamily, urban Sun Belt submarket.

**Step 2 — Historical absorption:** The defined submarket absorbed an average of 800 Class A units/year over the trailing 5 years (range: 500–1,200 units, illustrative). Forward projection: metropolitan area adding 5,000 households/year, with 35% renter capture and 60% of renters seeking Class A → forward demand estimate ≈ 1,050 units/year (illustrative). Slightly above historical average, plausible given employment growth trends.

**Step 4 — Competitive supply:** Over the next 18 months (subject lease-up period), 420 competing Class A units are delivering in the defined submarket in addition to the subject's 180 units → total new supply = 600 units. Annual absorption of 1,050 units > annual supply of 600 × 2/3 years = 400 units → market is absorbing supply (healthy).

**Step 5 — Capture rate:** Subject is 180 units; total submarket is 8,000 Class A units → pro-rata share = 2.25%. Subject has superior location (walkable to employment center) → capture rate estimated at 15% of annual market absorption (above pro-rata). Monthly absorption = (1,050 × 15%) / 12 = **13.1 units/month** (illustrative).

**Step 6 — Occupancy ramp:**
- Stabilization target: 171 units occupied (95% of 180)
- Months to stabilization: 171 / 13.1 = **13 months** (illustrative)
- Month 6: 78 units (43%), Month 12: 157 units (87%), Month 13: stabilized

**NOI ramp (illustrative):** At $2,100/unit/month, Month 1 revenue = 13 × $2,100 = $27,300; growing monthly as units fill. Full stabilized NOI reached at Month 13. The 13-month lease-up creates a $1.8M revenue shortfall versus immediate stabilization (illustrative), which must be funded in the capital structure.

## Limitations

Absorption modeling is only as good as the demand driver data and historical comparables. Historical absorption is backward-looking and can be misleading when structural demand shifts occur (office remote work, retail e-commerce displacement). Forward demand projections based on employment-to-SF ratios should be cross-checked against [[Demographic Analysis]] and any available submarket forecast reports from institutional research providers.

Capture rates are subjective and project-specific. A new development may underperform its capture rate if the competitive set is larger than modeled, if the project has construction quality issues, or if the initial rent pricing is mis-set relative to market. Build a downside scenario with a 25–30% reduction in capture rate to stress-test lease-up timeline and carrying cost.

The framework models absorption in steady state. In reality, initial lease-up velocity often accelerates in the first months (pent-up demand and promotional pricing) and decelerates when the low-hanging fruit is exhausted. A more sophisticated model will use an S-curve absorption trajectory rather than a linear ramp, though the linear approximation is adequate for most institutional underwriting.

## Related Frameworks

- [[Four-Quadrant Model]] — absorption is the demand-side flow variable that drives the Rent Determination quadrant.
- [[Real Estate Cycle and Phases]] — cycle phase determines whether absorption is accelerating (Expansion) or decelerating (Hypersupply/Recession).
- [[Development Feasibility Test]] — uses the lease-up timeline from absorption modeling to size financing costs.
- [[Yield Analysis Methodology]] — the IRR is highly sensitive to the occupancy ramp produced by absorption modeling.
- [[Supply Pipeline Analysis]] — the competing-supply input that determines supply-demand balance in Step 4.
- [[Demand Driver Analysis]] — supplies the forward demand estimate used in Step 3.
