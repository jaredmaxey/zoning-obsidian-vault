---
title: "Yield Analysis Methodology"
type: framework
tags: [cre/frameworks]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Institutional framework for calculating and interpreting yield metrics — cap rate, yield on cost, cash-on-cash, and IRR — to evaluate investment performance across acquisition and development.
inputs_required:
  - Purchase price or total project cost
  - Stabilized Net Operating Income (NOI)
  - Equity invested
  - Debt terms (rate, LTV, amortization)
  - Projected cash flows over hold period
  - Exit price or terminal cap rate assumption
  - Market cap rates for the asset class and submarket
outputs:
  - Going-in cap rate
  - Yield on cost (for development)
  - Cash-on-cash return (Year 1 and stabilized)
  - Equity multiple
  - IRR (levered and unlevered)
  - Development spread (yield on cost minus market cap rate)
related:
  - "Development Feasibility Test"
  - "Residual Land Value Feasibility"
  - "Cap Rate"
  - "Yield on Cost"
  - "Net Operating Income (NOI)"
  - "Internal Rate of Return (IRR)"
  - "Equity Multiple"
  - "Discount Rate"
  - "Going-In Cap Rate"
  - "Exit Cap Rate"
  - "Stabilized NOI"
  - "Weighted Average Cost of Capital (WACC)"
  - "Discounted Cash Flow (DCF)"
  - "Direct Capitalization"
  - "Pro Forma Construction Method"
  - "Sensitivity Analysis"
  - "Development Spread"
  - "Yield-on-Cost vs. Market Cap Spread"
---

# Yield Analysis Methodology

## Purpose

Yield Analysis is the systematic process of calculating, interpreting, and benchmarking the financial return metrics that institutional investors use to evaluate commercial real estate investments. The methodology encompasses the full suite of yield metrics — from the simple cap rate snapshot used in direct capitalization, to yield on cost for ground-up development, to the levered IRR used in discounted cash flow analysis — and explains how each metric is derived, what it measures, and when each is the appropriate tool for the decision at hand.

Different metrics serve different purposes and audiences. A cap rate is a market-price signal and a quick relative-value tool; it tells an investor whether they are buying at a premium or discount to the market but says nothing about leverage, timing, or exit. Yield on cost is the developer's primary feasibility test: it measures what income yield the completed project generates relative to all-in cost and compares it to the market cap rate to quantify the development spread. IRR and equity multiple are the investor return metrics that account for leverage, hold period, and the time value of money. Understanding when to use which metric — and how each can be gamed or misread — is the core competency this framework develops.

## Inputs Required

- **Purchase price or total project cost (TPC):** for acquisitions, the closing price inclusive of transaction costs; for development, TPC = land + hard costs + soft costs + financing costs + developer fee. Source: purchase contract, budget, [[Pro Forma Construction Method]].
- **Stabilized Net Operating Income (NOI):** NOI at full occupancy with market rents, standard vacancy allowance, and normalized operating expenses. See [[Net Operating Income (NOI)]] and [[Stabilized NOI]].
- **Market cap rate:** the prevailing cap rate for comparable assets in the submarket; from [[Comparable Sales (Sales Comps)]] and broker surveys. See [[Cap Rate]].
- **Equity invested:** total equity contribution (purchase price or TPC minus loan proceeds).
- **Debt terms:** loan amount, interest rate, amortization schedule, maturity; from [[Discounted Cash Flow (DCF)]] model.
- **Projected annual cash flows:** year-by-year NOI, less debt service, over the hold period; from the pro forma.
- **Exit cap rate:** the cap rate assumed at disposition; see [[Exit Cap Rate]].
- **Hold period:** typically 3–10 years for core/value-add; 2–5 years for development.

## Method

### Step 1 — Calculate Going-In Cap Rate

The going-in cap rate measures the initial yield on a stabilized or near-stabilized acquisition:

Plain text: `Going-in Cap Rate = Stabilized NOI / Purchase Price`

$$\text{Going-in Cap Rate} = \frac{\text{Stabilized NOI}}{\text{Purchase Price}}$$

Use trailing 12-month actual NOI if the property is stabilized, or a normalized/projected stabilized NOI for value-add acquisitions. Never use the first-year contractual NOI for a property with below-market leases without noting the distortion. Compare to market cap rates to determine whether the asset is priced at a premium (lower cap) or discount (higher cap) relative to comparable transactions.

### Step 2 — Calculate Yield on Cost (for Development/Value-Add)

Yield on cost measures the income return on total project investment — the developer's or value-add investor's equivalent of the going-in cap rate, but based on cost rather than market price:

Plain text: `Yield on Cost = Stabilized NOI / Total Project Cost`

$$\text{Yield on Cost} = \frac{\text{Stabilized NOI}}{\text{Total Project Cost}}$$

Total project cost includes land, all hard and soft costs, financing costs, and developer fee. Stabilized NOI uses market-rate rents and a market-standard vacancy allowance. See [[Yield on Cost]] for the full definition.

### Step 3 — Calculate Development Spread

The development spread is the margin between yield on cost and the current market cap rate. It quantifies the value created by the development risk:

Plain text: `Development Spread = Yield on Cost − Market Cap Rate`

$$\text{Development Spread} = \text{YoC} - \text{Market Cap Rate}$$

Institutional developers typically require a minimum development spread of 100–200 bps (1.0%–2.0%) to justify construction risk, with higher minimums for longer or more uncertain timelines. Ranges vary by market and vintage (current as of 2026-05-24). A positive spread means the project creates value; at stabilization, the asset is worth more than it cost to build. A zero or negative spread means the developer is building at or below replacement cost — a clear go/no-go failure unless a below-market land cost salvages the economics. See [[Development Spread]] and [[Yield-on-Cost vs. Market Cap Spread]].

### Step 4 — Calculate Cash-on-Cash Return

Cash-on-cash (CoC) measures the annual cash yield on equity invested, before consideration of appreciation:

Plain text: `Cash-on-Cash = Pre-Tax Cash Flow After Debt Service / Equity Invested`

$$\text{Cash-on-Cash} = \frac{\text{CFADS}}{\text{Equity Invested}}$$

where CFADS = cash flow after debt service (NOI minus annual debt service). Calculate for Year 1 (going-in), stabilized year, and each hold year. Typical stabilized CoC returns for institutional assets range from 5–9%, varies significantly by asset class, leverage, and market cycle (current as of 2026-05-24).

### Step 5 — Calculate Equity Multiple

The equity multiple measures total capital returned per dollar invested over the full hold period:

Plain text: `Equity Multiple = Total Distributions (including exit proceeds) / Equity Invested`

$$\text{Equity Multiple} = \frac{\sum \text{Distributions} + \text{Exit Proceeds}}{\text{Equity Invested}}$$

An equity multiple of 2.0x means the investor doubled their invested capital. Equity multiple does not account for time — a 2.0x over 3 years is vastly superior to 2.0x over 10 years. Typical targets range from 1.5x–2.5x for value-add strategies over a 5-year hold, varies by risk profile and vintage (current as of 2026-05-24). See [[Equity Multiple]].

### Step 6 — Calculate IRR (Levered and Unlevered)

The IRR is the discount rate that sets the net present value of all cash flows (including the initial equity outlay and the exit proceeds) to zero. It is the standard institutional performance metric because it accounts for the time value of money and the hold period:

Plain text: `0 = −Equity Invested + Σ [CFt / (1 + IRR)^t] + [Exit Proceeds / (1 + IRR)^n]`

$$0 = -E_0 + \sum_{t=1}^{n} \frac{CF_t}{(1+\text{IRR})^t} + \frac{P_n}{(1+\text{IRR})^n}$$

where $E_0$ = equity at close, $CF_t$ = annual CFADS in year $t$, $P_n$ = net exit proceeds in year $n$.

Calculate both **unlevered IRR** (using NOI before debt service and full asset purchase price, not equity) to assess asset-level performance independent of capital structure, and **levered IRR** (using CFADS and equity) to assess equity investor returns. Compare levered IRR to the investor's required return / [[Discount Rate]] or [[Weighted Average Cost of Capital (WACC)]]. Typical target levered IRRs: Core 7–9%, Core-plus 9–12%, Value-add 12–16%, Opportunistic 16%+, varies by market and vintage (current as of 2026-05-24). See [[Internal Rate of Return (IRR)]].

### Step 7 — Stress-Test and Interpret

Run [[Sensitivity Analysis]] on the key drivers: exit cap rate (±50 bps), rent growth (±200 bps/year), hold period (±2 years). Present the IRR and equity multiple under base, upside, and downside scenarios. A deal that only works in the upside scenario is not an investment — it is speculation. The base case should be achievable, not heroic.

## Outputs

The methodology produces the following return metrics for each scenario:
- Going-in cap rate (%)
- Yield on cost (%) and development spread (bps) — for development only
- Cash-on-cash by year (%)
- Equity multiple (x)
- Levered IRR (%) and unlevered IRR (%)

Present these in a summary dashboard alongside the minimum hurdle rates for each metric per the fund or investor mandate.

## Example Walkthrough

*All figures below are illustrative/hypothetical.*

**Development scenario (ground-up industrial):**
- Land: $3.0M; hard costs: $12.0M; soft costs: $2.0M; financing: $1.0M → TPC = $18.0M
- Stabilized NOI: $1.35M/year (illustrative rent $10.50/SF NNN on 150,000 SF, 5% vacancy, minimal OpEx)
- Market cap rate: 5.5%
- Yield on Cost = $1.35M / $18.0M = **7.5%**
- Development Spread = 7.5% − 5.5% = **200 bps** (meets minimum threshold — feasible)
- Stabilized value at market cap rate = $1.35M / 0.055 = **$24.5M** → value creation = $6.5M

**Acquisition scenario (same stabilized asset purchased at completion):**
- Purchase price: $24.5M; loan at 65% LTV: $15.9M at 6.0% I/O; equity: $8.6M
- Year 1 CFADS = $1.35M NOI − $954K debt service = $396K
- CoC Year 1 = $396K / $8.6M = **4.6%**
- Hold 5 years; NOI grows 3%/year → Year 5 NOI = $1.565M; exit at 5.75% cap → exit value = $27.2M; net exit proceeds after loan payoff = $11.3M
- Total distributions = $2.1M (5-year CFADS) + $11.3M = $13.4M
- Equity Multiple = $13.4M / $8.6M = **1.56x** (illustrative)
- Levered IRR ≈ **11.5%** (illustrative)

**Stress test:** If exit cap rate widens to 6.25%, exit value = $25.0M, net proceeds = $9.1M, equity multiple = 1.3x, IRR ≈ 7.2% (illustrative). Deals should be evaluated at the stress-test exit cap, not only the base case.

## Limitations

The yield analysis framework is mechanically precise but only as accurate as its inputs. The single most important assumption — the exit cap rate — can move IRR by hundreds of basis points. An analyst who anchors to today's market cap rate as the exit cap is embedding a bet on market conditions 5–10 years forward.

Equity multiple and IRR can diverge: a highly leveraged deal may show a high IRR on a small equity investment but return less absolute capital than a lower-leverage alternative. Always present both metrics. Similarly, development spread does not account for the risk that construction costs overrun or rents underperform — two outcomes that can transform a 200-bps spread into a loss. Pair with [[Sensitivity Analysis]] and contingency reserves.

The framework assumes stabilization occurs on schedule. Development delays, lease-up delays, or major tenant defaults extend the timeline, compressing the IRR even if the eventual stabilized value is achieved.

## Related Frameworks

- [[Development Feasibility Test]] — applies yield analysis as the go/no-go test for new development.
- [[Residual Land Value Feasibility]] — uses yield-on-cost logic to back into maximum supportable land price.
- [[Discounted Cash Flow (DCF)]] — the quantitative engine in which all these metrics are calculated.
- [[Sensitivity Analysis]] — essential companion to stress-test yield metric outputs.
- [[Pro Forma Construction Method]] — the underlying model that generates the inputs to yield analysis.
