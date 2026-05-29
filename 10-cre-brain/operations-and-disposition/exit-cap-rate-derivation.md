---
title: "Exit Cap Rate Derivation"
type: concept
tags: [cre/operations]
created: "2026-05-24"
updated: "2026-05-24"
status: draft
ai_summary: The process of estimating the cap rate at which a property will sell at the end of the projected hold period, a critical assumption that drives terminal value in DCF models.
domain: operations
formula: true
related:
  - "Cap Rate"
  - "Going-In Cap Rate"
  - "Hold vs. Sell Analysis"
  - "Broker Selection and BOV"
  - "Net Operating Income (NOI)"
  - "Stabilized NOI"
  - "Discounted Cash Flow (DCF)"
  - "Direct Capitalization"
  - "Internal Rate of Return (IRR)"
  - "Real Estate Cycle and Phases"
---

# Exit Cap Rate Derivation

## Definition

The exit cap rate (also called the terminal cap rate or reversion cap rate) is the capitalization rate assumed to apply at the end of the projected hold period when the property is sold, used to calculate the terminal sale price in a discounted cash flow (DCF) model. It is arguably the single most sensitive assumption in any CRE investment model: a 25-basis-point change in the exit cap rate on a $20 million stabilized NOI property changes the terminal value by $10–25 million depending on the absolute cap rate level, which can swing the projected IRR by 100–200 basis points. Because the exit cap rate is inherently a forecast of market conditions several years in the future, it introduces irreducible uncertainty into any long-horizon projection.

The exit cap rate differs from the going-in cap rate (the cap rate at which the property is acquired; see [[Going-In Cap Rate]]) in two ways. First, it is typically set 25–75 basis points higher than the going-in cap rate to reflect the asset's aging and the uncertainty premium embedded in future-year projections—a convention sometimes called the "cap rate premium for age." Second, it reflects the expected market cap rate environment at the assumed sale date, not today's market. In practice, institutional underwriting conventions often set the exit cap rate at the going-in cap rate plus a buffer (25–50 bps for core, 50–75 bps for value-add), though some practitioners derive it independently from submarket trend analysis and then cross-check against the going-in spread.

## Formula

**Terminal value from exit cap rate:**

Plain text:
`Terminal Value = Year N+1 NOI / Exit Cap Rate`

$$
\text{Terminal Value} = \frac{\text{NOI}_{N+1}}{\text{Exit Cap Rate}}
$$

Where:
- **NOI\_{N+1}** = projected net operating income in the year immediately following the sale date (i.e., the buyer's year-one income) — NOT the seller's final-year NOI
- **Exit Cap Rate** = the assumed market cap rate at the time of sale, expressed as a decimal

**Implied going-in cap for the buyer:**

The exit cap rate is the cap rate from the buyer's perspective at the time of the projected sale, applied to the next year's NOI. Using the current year's NOI (the seller's final year) in the numerator and applying the exit cap directly produces the same result only if NOI is flat; if NOI is growing, using the seller's final-year NOI will understate the terminal value relative to how a real buyer will underwrite the acquisition.

$$
\text{Net Sale Proceeds} = \text{Terminal Value} - \text{Selling Costs}
$$

Where selling costs typically run 1.5–3.0% of gross sale price (broker commission, transfer taxes, legal, closing costs; varies by market and deal structure; current as of 2026-05-24).

## When It's Used

The exit cap rate is set during initial underwriting of any deal where the return analysis relies on a future disposition—which includes virtually all value-add, opportunistic, and core-plus investments and any [[Discounted Cash Flow (DCF)]] model. In acquisition underwriting, it defines the terminal value against which today's purchase price is benchmarked. In [[Hold vs. Sell Analysis]], it is used to project the future value of the asset under a "hold" scenario. In [[Broker Selection and BOV]], brokers apply their market view of current and near-term cap rates to derive today's BOV pricing, which serves as a proxy for the exit cap rate in a near-term sale scenario.

Sensitivity analysis around the exit cap rate is standard practice in institutional underwriting: models are run at base (e.g., +50 bps over going-in), bear (+100 bps), and bull (flat or negative spread) assumptions to stress-test the return profile. The spread between the base and bear-case IRR tells the investor how much return is at risk if cap rates expand.

## Variations & Edge Cases

**Asset-class conventions**: Exit cap rate spreads over going-in cap rates vary by asset class. Industrial and multifamily have historically traded at compressed spreads (0–50 bps) due to strong investor demand and stable income streams. Office, retail, and hospitality—which carry higher occupancy and income risk—typically require wider exit cap rate premiums to account for leasing uncertainty and buyer risk aversion at the time of future sale.

**Cycle timing effects**: The exit cap rate must be set in the context of where the real estate cycle (see [[Real Estate Cycle and Phases]]) is expected to be at the sale date. Buying at a cycle peak and projecting the exit at a trough implies cap rate expansion (higher exit cap) that compresses terminal value; buying at a trough and projecting the exit at a peak implies cap rate compression (lower exit cap) that inflates terminal value. The direction of the cycle relative to the hold period is the most important qualitative input to exit cap rate selection.

**Non-stabilized exit**: If the property is sold in a non-stabilized condition (partially leased, in renovation), buyers will apply a value-in-place cap rate to the actual in-place NOI plus a discount for execution risk—not a stabilized cap rate to a stabilized NOI. Models that assume a stabilized exit should also assume sufficient hold period for stabilization to actually be achieved.

## Common Mistakes

The most common and consequential error is setting the exit cap rate at or below the going-in cap rate to generate attractive return projections, without any analytical basis for why cap rates would compress over the hold period. This is sometimes called "buying the return with the exit cap"—the deal only works if the market becomes more aggressive than today, an assumption that is indefensible without strong cycle-timing conviction. Lenders and institutional investors reviewing models with aggressive exit caps will immediately adjust them, and deals that required an aggressive exit to pencil will typically be declined or repriced.

A second error is applying the exit cap rate to the seller's final-year NOI rather than the buyer's year-one NOI (i.e., failing to use the forward NOI). In a property with growing rents, this understates the terminal value; in a property with a known occupancy cliff (major lease expiration in year N), it can dramatically overstate the terminal value if the forward NOI includes the vacancy that will materialize for the next buyer's year one.

## Related Concepts

- [[Cap Rate]] — the parent concept; the exit cap rate is a forward-looking application of the cap rate
- [[Going-In Cap Rate]] — the acquisition cap rate from which the exit cap rate spread is typically measured
- [[Hold vs. Sell Analysis]] — the exit cap rate is the most sensitive assumption in the hold scenario
- [[Broker Selection and BOV]] — brokers apply market cap rate analysis to derive current BOV pricing
- [[Net Operating Income (NOI)]] — the numerator in the terminal value formula
- [[Stabilized NOI]] — the NOI basis used in exit cap rate valuation for stabilized dispositions
- [[Discounted Cash Flow (DCF)]] — the analytical framework in which the exit cap rate-derived terminal value is discounted back to present value
- [[Internal Rate of Return (IRR)]] — the return metric most sensitive to exit cap rate assumptions

## Sources

- Geltner, Miller, Clayton, Eichholtz: *Commercial Real Estate Analysis and Investments* — cap rate theory, terminal value mechanics, and sensitivity analysis.
- CCIM Institute: *CI 102 Market Analysis* and *CI 103 User Decision Analysis* — cap rate derivation and DCF terminal value methodology.
- NCREIF: historical cap rate data by asset class and geography (ncreif.org).
- Real Capital Analytics / CoStar: transaction-level cap rate benchmarks for exit cap rate derivation (rcanalytics.com, costar.com).
- ARGUS Enterprise documentation: industry-standard DCF software treatment of reversionary cap rates.
