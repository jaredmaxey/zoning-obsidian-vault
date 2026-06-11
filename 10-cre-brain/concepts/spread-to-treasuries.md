---
title: "Spread to Treasuries"
aliases: ["Spread to Treasuries"]
type: concept
tags: [cre/concepts]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Spread to Treasuries is the risk premium embedded in CRE cap rates and debt yields above the 10-year Treasury rate, used to assess relative value between real estate and fixed income and to gauge market pricing cycles.
domain: concepts
formula: true
related:
  - "Cap Rate"
  - "Going-In Cap Rate"
  - "Discount Rate"
  - "Debt Yield"
  - "Spread to Treasuries"
  - "Loan-to-Value (LTV)"
  - "Real Estate Cycle and Phases"
  - "Four-Quadrant Model"
---

# Spread to Treasuries

## Definition

Spread to Treasuries (or cap rate spread) is the difference between a CRE asset's cap rate and the prevailing 10-year U.S. Treasury yield, expressed in basis points. It represents the risk premium an investor earns for accepting the illiquidity, management burden, operational complexity, and asset-specific risk of owning real property versus holding a risk-free government bond. When the spread is wide (cap rates significantly exceed Treasury yields), real estate appears attractively priced relative to alternatives — more income per dollar of investment relative to the risk-free rate. When the spread is thin or inverted, real estate income yield offers little compensation over Treasuries, raising questions about whether the asset class is over-priced relative to fixed income alternatives.

The spread to Treasuries is one of the most useful macro-level diagnostics in CRE capital markets. It helps answer the question: "given where interest rates are today, is the current market cap rate appropriate?" In the 2011–2021 period, historically low Treasury yields allowed cap rates to compress significantly while maintaining or widening spreads — providing a risk-premium buffer for real estate investors. When Treasury yields rose sharply in 2022–2023, cap rates were slow to reprice, causing spreads to compress dramatically and in some cases briefly turn negative in certain markets, signaling overvaluation or distress. The subsequent repricing cycle illustrated how spread dynamics govern real estate capital markets cycles.

Spread analysis must be context-aware. Real estate offers unique attributes — inflation protection through rent growth, depreciation tax shields, leverage amplification, and control over asset operations — that justify a different spread requirement than a pure income comparison would suggest. Additionally, real estate spreads have historically included compensation for illiquidity (the inability to sell quickly at market price), which academic and practitioner research estimates at 50–150 basis points of additional required return.

## Formula

- Plain text: `Spread = Cap Rate − 10-Year Treasury Yield`
- LaTeX: $$ \text{Spread} = \text{Cap Rate} - r_f $$

**Where:**
- **Cap Rate** — the prevailing stabilized cap rate for a specific asset class and market (going-in or market average)
- **r_f** — the risk-free rate, typically the on-the-run 10-year U.S. Treasury yield (or the relevant sovereign yield for non-U.S. markets)
- **Spread** — expressed in basis points (bps); 1% = 100 bps

**Implied Value Framework:**
If investors require a fixed spread (s) above Treasuries: `Required Cap Rate = r_f + s`

A rise in r_f with constant required spread s would push cap rates higher (values lower), all else equal.

## When It's Used

Spread to Treasuries is used by institutional investors, fund managers, and investment committees to assess whether current market cap rates are appropriate for the prevailing interest rate environment. In a strategic asset allocation context, spread analysis helps portfolio managers decide whether to overweight or underweight real estate relative to fixed income or other alternatives.

In deal underwriting, spread analysis grounds the going-in cap rate assumption in macro context. A 5.0% cap rate looks very different against a 2.0% Treasury (300 bps spread) versus a 5.0% Treasury (0 bps spread). Lenders also monitor spread when underwriting loans: debt spreads above Treasuries (which determine mortgage rates) and cap rate spreads interact to determine whether leverage is additive (positive leverage) or destructive (negative leverage).

For market timing and cycle analysis, tracking spread compression and expansion over time provides one of the most powerful signals of real estate market cycles — see [[Real Estate Cycle and Phases]] and [[Four-Quadrant Model]].

## Variations & Edge Cases

**SOFR or bank spread vs. Treasury spread:** Debt pricing (mortgage rates) is sometimes benchmarked against SOFR, LIBOR legacy rates, or bank prime rather than Treasuries. Cap rate spreads are conventionally benchmarked against the 10-year Treasury regardless of financing cost benchmarks, since the 10-year Treasury is the standard risk-free reference for long-duration investment.

**Asset class spread differentials:** Different asset classes command different spread premiums above Treasuries, reflecting their underlying risk. As of 2026-05-24, industrial assets in strong logistics markets trade at compressed spreads (lower risk premium); some office markets with structural vacancy challenges trade at much wider spreads (higher risk premium). The spread differential between asset classes moves over time with demand fundamentals and capital flows (varies by market and vintage).

**Negative spread:** If cap rates fall below Treasury yields (negative spread), investors are accepting less income from real estate than from risk-free bonds — an inherently unusual and unsustainable relationship that typically implies either an expectation of very strong rent growth, mispriced risk, or temporary liquidity distortion. Negative spreads are a warning sign of market overheating.

## Common Mistakes

**Treating all real estate as equivalent in spread analysis.** A trophy multifamily asset in a gateway city has a different appropriate spread than a suburban Class B office building. Spread analysis should be asset-class and market specific, not applied as a single benchmark.

**Ignoring the direction of rate movement.** A current spread may look adequate, but if Treasury yields are rising rapidly, cap rates will need to follow — potentially compressing values. Underwriting in a rising rate environment requires sensitivity analysis on the spread assumption, not just a snapshot.

**Confusing cap rate spread with debt spread.** Mortgage spreads above Treasuries (the cost of financing) are a different concept from cap rate spreads. Positive leverage requires that the cap rate spread exceed the mortgage spread — which is not guaranteed in compressed-spread environments.

## Related Concepts

- [[Cap Rate]] — the yield against which the Treasury spread is measured
- [[Going-In Cap Rate]] — the acquisition-day cap rate; spread analysis contextualizes whether it is appropriate
- [[Discount Rate]] — the total required return, of which the risk-free rate is the base component
- [[Debt Yield]] — lender's income yield metric; mortgage spreads above Treasuries relate to debt yield
- [[Real Estate Cycle and Phases]] — spread compression and expansion are leading indicators of cycle positioning
- [[Four-Quadrant Model]] — the macro framework for understanding real estate as a capital market asset

## Sources

Treasury yield data is published by the U.S. Federal Reserve (FRED), Bloomberg, and the U.S. Treasury. Cap rate spread analysis is published by CBRE Research, JLL Capital Markets, NCREIF, and academic real estate finance literature (Geltner, Fisher, et al.). Historical spread data and cycle analysis is available from PREA and CoStar Analytics. Specific spread levels are market- and cycle-dependent (varies by market and vintage; current as of 2026-05-24).
