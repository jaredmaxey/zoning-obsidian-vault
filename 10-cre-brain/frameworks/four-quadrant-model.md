---
title: "Four-Quadrant Model"
aliases: ["Four-Quadrant Model"]
type: framework
tags: [cre/frameworks]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: DiPasquale-Wheaton equilibrium model linking property markets (rent, price) and asset markets (construction, stock) across four quadrants to explain real estate cycles.
inputs_required:
  - Current market rent and vacancy
  - Market cap rate (going-in)
  - Current space stock (SF or units)
  - New construction volume and pipeline
  - Demand drivers (employment, absorption trends)
  - Long-run construction cost benchmark
outputs:
  - Directional prediction of rent, price, and construction trends
  - Identification of current market phase within the cycle
  - Equilibrium rent and stock estimates
related:
  - "Real Estate Cycle and Phases"
  - "Highest and Best Use Analysis"
  - "Absorption Modeling"
  - "Cap Rate"
  - "Net Operating Income (NOI)"
  - "Going-In Cap Rate"
  - "Replacement Cost"
  - "Demand Driver Analysis"
  - "Supply Pipeline Analysis"
---

# Four-Quadrant Model

## Purpose

The Four-Quadrant (4Q) Model, developed by DiPasquale and Wheaton, is a spatial-equilibrium framework for understanding how commercial real estate markets move between the space market (where occupiers rent space) and the asset market (where investors buy and sell properties). It organizes market dynamics into four interacting panels: Rent Determination (northwest), Asset Valuation (northeast), Construction (southeast), and Stock Adjustment (southwest). Together they explain why rents, prices, vacancy, and new supply move in the directions they do — and allow an analyst to predict the direction of change given current conditions.

Practitioners reach for the 4Q model when they want to understand structural market positioning rather than just current-period metrics. It is most useful for explaining to capital partners why a market is over- or underbuilt, whether current cap rates are sustainable, and what the medium-term supply response to a rent spike will look like. While the model is often taught as a static equilibrium diagram, analysts apply it dynamically by tracking where actual market metrics sit relative to equilibrium values and reasoning about the path back to balance.

## Inputs Required

- **Current market rent ($/SF/year or $/unit/month):** observed effective rents from [[Comparable Rents (Rent Comps)]].
- **Vacancy rate:** space market absorption versus total inventory; sources include broker surveys and CoStar/CBRE/JLL market reports.
- **Market cap rate (going-in):** current trading cap rates for the asset class and submarket; see [[Going-In Cap Rate]] and [[Cap Rate]].
- **Current stock (SF or units):** total existing inventory in the defined submarket; from [[Submarket Definition and Selection]].
- **New construction volume:** permits issued, units/SF under construction, and pipeline per [[Supply Pipeline Analysis]].
- **Demand drivers:** employment growth, population trends, household formation; see [[Demand Driver Analysis]].
- **Long-run construction cost benchmark:** replacement cost per SF/unit (see [[Replacement Cost]]) sets the floor for new construction price.

## Method

1. **Map the four quadrants.** Draw or conceptualize the 4Q diagram with four panels arranged around a shared origin: NW (Rent Determination), NE (Asset Valuation), SE (Construction), SW (Stock Adjustment).

2. **Quadrant 1 — Rent Determination (NW).** Plot the demand curve for space: as stock (supply) increases, rents fall, and vice versa. Locate current stock on the horizontal axis and read off the equilibrium rent given current demand. If actual rent is above the curve, the market is supply-constrained (high occupancy drives rent); below it, the market is overbuilt.
   - Formula: `R = f(D, S)` where R = rent, D = demand (employment/absorption), S = stock.

3. **Quadrant 2 — Asset Valuation (NE).** Convert rent to asset price using the cap rate: `P = R / k` where P = price per SF/unit, R = NOI, and k = cap rate. A lower cap rate (investor demand for the asset class) raises prices relative to income. Plot P on the vertical axis.
   $$P = \frac{R}{k}$$

4. **Quadrant 3 — Construction (SE).** Construction activity is a function of asset price relative to replacement cost. When P > replacement cost, developers build; when P < replacement cost, construction shuts off. The construction function is typically upward-sloping: higher prices induce more supply. Read off the flow of new construction given current P.
   - Threshold: `P > C` (replacement cost) → construction starts. Varies by market and vintage (current as of 2026-05-24), but a common rule of thumb is that development spread over market cap rate must exceed 100–200 bps to justify new construction risk.

5. **Quadrant 4 — Stock Adjustment (SW).** New construction (flow) adds to existing stock (stock). Simultaneously, obsolescence and demolition remove stock. The stock adjustment equation is: `ΔS = C_new − δS` where δ = depreciation/obsolescence rate (typically 1–2% per year, varies by asset class and vintage, current as of 2026-05-24). Follow the diagonal back to the NW quadrant to see how new stock affects next-period rent.

6. **Identify current position.** Plot the market's current rent and stock against the equilibrium curves. Determine whether the market is in:
   - Phase 1 (Recovery): below-trend rents, falling vacancy, no new supply.
   - Phase 2 (Expansion): rising rents, declining vacancy, construction starts increase.
   - Phase 3 (Hypersupply): rents still high but new supply arriving, vacancy beginning to rise.
   - Phase 4 (Recession): rising vacancy, falling rents, construction stops.
   Cross-reference with [[Real Estate Cycle and Phases]] for the full cycle taxonomy.

7. **Project directional movement.** Given the current position, reason through the four-quadrant adjustments: does the current rent support current asset prices? Does the current asset price exceed replacement cost? If yes, when does new supply arrive and how much? How much does new stock push rents down from equilibrium? Use the supply pipeline from [[Supply Pipeline Analysis]] to calibrate.

## Outputs

- A directional narrative: rents rising/falling, construction accelerating/decelerating, asset prices sustainable/correcting.
- Identification of the current market phase (recovery, expansion, hypersupply, recession).
- Estimated equilibrium rent given current stock and demand drivers.
- A sanity check on whether current cap rates are consistent with fundamental value or reflect speculation.

## Example Walkthrough

*All figures below are illustrative/hypothetical.*

Consider an urban multifamily submarket with the following illustrative inputs:
- Current market rent: $2,200/month (NNN equivalent: ~$30/SF/year)
- Current vacancy: 4%
- Market cap rate: 5.0%
- Current stock: 50,000 units
- New construction pipeline: 3,000 units (6% of stock) delivering over 24 months
- Replacement cost: $350,000/unit; current market transaction price: $440,000/unit

**Quadrant 1 (Rent):** At 50,000 units and 4% vacancy, the market is supply-constrained. Effective rent of $2,200/month is above long-run equilibrium (illustratively, equilibrium at this demand level might be ~$2,000/month based on historical absorption/stock ratios).

**Quadrant 2 (Valuation):** `P = NOI / cap rate`. Assume NOI $18,000/unit/year → `P = $18,000 / 0.05 = $360,000/unit`. Market is trading at $440,000/unit, implying a cap rate of ~4.1% — below the modeled 5.0% equilibrium cap rate, suggesting investor sentiment is stretched.

**Quadrant 3 (Construction):** $440,000/unit >> $350,000 replacement cost → green light for new construction. Pipeline of 3,000 units is confirmed.

**Quadrant 4 (Stock Adjustment):** Adding 3,000 units to 50,000 = 53,000 units, a 6% increase. Demand growth (illustrative: 1,500 net new demand units annually) absorbs only 3,000 units over two years. Net new supply = 0 → no vacancy impact. But if demand growth slows to 500 units/year, pipeline will push vacancy from 4% to ~7%, which the rent-determination curve converts to a rent correction of roughly 8–10% (illustrative).

**Conclusion:** Market is in late Phase 2 / early Phase 3. Asset prices appear stretched versus fundamental rent support. Analysts should underwrite conservatively and stress-test rent with a 5–10% downside scenario.

## Limitations

The 4Q model is a stylized equilibrium framework, not a forecasting engine. It assumes rational construction responses and continuous markets, neither of which holds perfectly in practice. Construction lags (permitting, entitlement, build time typically 18–36 months) mean that supply overshoots equilibrium systematically, which the simple linear model understates.

The model treats "the market" as homogeneous, but submarkets, asset quality tiers, and micro-locations can be in very different phases simultaneously. An analyst who applies metro-level 4Q readings to a specific submarket may draw wrong conclusions. Always run the model at the submarket level using data from [[Submarket Definition and Selection]].

The model also has no explicit representation of capital market shocks (interest rate jumps, credit crunches) that can collapse asset prices and halt construction without any change in space-market fundamentals. In a rising-rate environment, the asset-valuation quadrant can shift violently even when rent and vacancy are stable.

## Related Frameworks

- [[Real Estate Cycle and Phases]] — operationalizes the 4Q cycle narrative into actionable phase descriptions and investment implications.
- [[Absorption Modeling]] — provides the demand-side flow data that drives the Rent Determination quadrant.
- [[Highest and Best Use Analysis]] — relies on 4Q context to assess whether current-period development is financially feasible.
- [[Development Feasibility Test]] — uses the construction-vs.-price comparison from Quadrant 3 as its core logic.
- [[Supply Pipeline Analysis]] — essential input to Quadrant 4; tracks new stock additions.
- [[Demand Driver Analysis]] — essential input to Quadrant 1; quantifies the demand curve shift.
