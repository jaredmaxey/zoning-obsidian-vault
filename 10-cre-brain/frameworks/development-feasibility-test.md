---
title: "Development Feasibility Test"
type: framework
tags: [cre/frameworks]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Go/no-go framework testing whether a ground-up development project creates value by comparing yield on cost to market cap rate and checking profit margin on total cost.
inputs_required:
  - Site cost (land price)
  - Hard construction costs (per SF/unit)
  - Soft costs (architecture, engineering, permits, financing)
  - Projected stabilized NOI (market rents, market vacancy, market expenses)
  - Market cap rate for the asset class and submarket
  - Construction loan terms and equity structure
  - Anticipated development timeline
outputs:
  - Yield on cost (%)
  - Development spread (bps)
  - Stabilized value at market cap rate ($)
  - Profit margin on total cost (%)
  - Go / no-go recommendation with stated threshold
related:
  - "Yield Analysis Methodology"
  - "Residual Land Value Feasibility"
  - "Highest and Best Use Analysis"
  - "Four-Quadrant Model"
  - "Real Estate Cycle and Phases"
  - "Yield on Cost"
  - "Cap Rate"
  - "Net Operating Income (NOI)"
  - "Stabilized NOI"
  - "Replacement Cost"
  - "Development Spread"
  - "Yield-on-Cost vs. Market Cap Spread"
  - "Pro Forma Construction Method"
  - "Sensitivity Analysis"
  - "Ground-Up Development"
  - "Build-to-Suit"
---

# Development Feasibility Test

## Purpose

The Development Feasibility Test is the primary go/no-go screening tool applied to any ground-up development project before committing to land acquisition and entitlement. It answers a single fundamental question: does the market support enough income to justify the cost of developing this project? If rents are too low, construction costs too high, or cap rates too compressed, a project destroys value rather than creating it — the developer would pay more to build than the market will pay to buy. The framework catches this condition before capital is deployed.

The test is mathematically simple — it compares yield on cost to the market cap rate — but its practical power lies in forcing precise estimates of all cost components and honest calibration of market rent and stabilization assumptions. It is typically run iteratively: first as a back-of-envelope screen using rough cost benchmarks, and then in increasing detail as the project advances through land control, design, and entitlement. At each iteration, the test becomes more reliable as soft cost estimates firm up and market data is refreshed. The [[Pro Forma Construction Method]] provides the detailed inputs; the Development Feasibility Test is the interpretive framework applied to those inputs.

## Inputs Required

- **Land cost:** contracted or estimated purchase price plus closing costs and carry through entitlement. Source: purchase contract, broker opinion, or [[Residual Land Value Feasibility]] result.
- **Hard construction costs:** direct building costs per gross square foot or per unit; from general contractor estimate or benchmark database. Ranges vary widely by asset class, construction type, and market — a wood-frame garden apartment in the Sun Belt may run $120–$160/SF hard cost while a concrete high-rise multifamily in a gateway market runs $300–$450+/SF, varies by market and vintage (current as of 2026-05-24).
- **Soft costs:** architecture, engineering, permits, impact fees, legal, marketing, developer fee. Typically 15–25% of hard costs, varies by project type and jurisdiction (current as of 2026-05-24).
- **Financing costs:** construction loan interest (I-C), origination fees, lender legal; carry costs during lease-up. Depends on loan terms, construction timeline, and lease-up pace.
- **Stabilized NOI:** market rent × leasable area × (1 − vacancy) − operating expenses. Use market rents and market vacancy, not the best-case scenario. See [[Stabilized NOI]].
- **Market cap rate:** going-in cap rate for comparable stabilized assets in the submarket. Source: [[Comparable Sales (Sales Comps)]], broker surveys. See [[Cap Rate]] and [[Going-In Cap Rate]].
- **Development timeline:** construction duration plus lease-up period; total months of capital deployment before stabilization.

## Method

1. **Assemble the Total Project Cost (TPC) budget.** Sum all cost components:

   `TPC = Land + Hard Costs + Soft Costs + Financing Costs + Developer Fee`
   
   $$\text{TPC} = C_{\text{land}} + C_{\text{hard}} + C_{\text{soft}} + C_{\text{financing}} + C_{\text{fee}}$$
   
   Use the most current contractor pricing for hard costs. Apply a contingency of 5–10% on hard costs for budget uncertainty (varies by project stage and market; higher in volatile materials environments, current as of 2026-05-24).

2. **Estimate Stabilized NOI.** Build a simplified stabilized income statement using market inputs:
   - Gross Potential Rent (GPR) = market rent/unit or /SF × total leasable units/SF
   - Less: vacancy and credit loss (market standard; typically 5–10% for multifamily, 5–15% for commercial, varies by asset class and market, current as of 2026-05-24)
   - Plus: other income (parking, ancillary)
   - Less: operating expenses (management, taxes, insurance, maintenance, reserves)
   - = Net Operating Income (NOI)

3. **Calculate Yield on Cost.** Divide stabilized NOI by TPC:

   `Yield on Cost = Stabilized NOI / TPC`
   
   $$\text{YoC} = \frac{\text{NOI}_{\text{stab}}}{\text{TPC}}$$

4. **Calculate Development Spread.** Subtract the market cap rate from the yield on cost:

   `Development Spread = Yield on Cost − Market Cap Rate`
   
   $$\text{Dev. Spread} = \text{YoC} - k_{\text{market}}$$
   
   A positive development spread means the project creates value. The threshold for institutional feasibility is typically 100–200 bps (varies by project risk, timeline, and market cycle, current as of 2026-05-24). Projects with <100 bps spread are marginal and typically infeasible unless the land was acquired at below-market cost. See [[Development Spread]] and [[Yield-on-Cost vs. Market Cap Spread]].

5. **Calculate Stabilized Value and Profit Margin.** Apply the market cap rate to stabilized NOI to derive the as-stabilized value:

   `Stabilized Value = Stabilized NOI / Market Cap Rate`
   
   $$V_{\text{stab}} = \frac{\text{NOI}_{\text{stab}}}{k_{\text{market}}}$$
   
   Profit = Stabilized Value − TPC. Profit margin = (Stabilized Value − TPC) / TPC. Institutional projects typically require a minimum profit margin of 15–20% on TPC (varies by strategy and market, current as of 2026-05-24).

6. **Apply the go/no-go test.** The project passes if ALL of the following are true:
   - Development spread ≥ minimum threshold (e.g., 150 bps)
   - Profit margin on TPC ≥ minimum (e.g., 15%)
   - Project generates a levered IRR above the investor's hurdle rate (per [[Yield Analysis Methodology]])
   
   If any condition fails, either restructure the deal (lower land cost, reduce soft costs, increase rents via better design) or pass on the project.

7. **Run sensitivity analysis.** Stress test the three most sensitive inputs: construction costs (+10–15%), stabilized rents (−5–10%), and market cap rate at stabilization (+50–100 bps). If the project still passes under stress, it has adequate margin of safety. A project that only works in the base case is at risk. Use [[Sensitivity Analysis]] for the full matrix.

8. **Iterate with land value.** If the project fails the test at the current asking land price, run the test backward: solve for the maximum supportable land price given the minimum required development spread. This is the [[Residual Land Value Feasibility]] calculation, which becomes the developer's maximum bid.

## Outputs

- Total Project Cost ($) broken down by component.
- Stabilized NOI ($) with assumptions stated.
- Yield on Cost (%) and Development Spread (bps).
- Stabilized value at market cap rate ($) and profit margin on TPC (%).
- Levered IRR and equity multiple from the full [[Discounted Cash Flow (DCF)]] model.
- Sensitivity table showing IRR/margin under cost overrun, rent, and exit cap rate stress scenarios.
- Go / No-Go recommendation with explicit threshold criteria stated.

## Example Walkthrough

*All figures below are illustrative/hypothetical.*

**Project:** 200-unit garden-style multifamily, suburban Sun Belt market.

**TPC Assembly (illustrative):**
- Land: $3.0M
- Hard costs: $150/SF × 200,000 GSF = $30.0M
- Soft costs (18% of hard): $5.4M
- Financing costs (12-month construction + 6-month lease-up): $2.1M
- Developer fee (3% of hard + soft): $1.1M
- **TPC = $41.6M** ($208,000/unit)

**Stabilized NOI (illustrative):**
- GPR: 200 units × $1,900/month × 12 = $4.56M
- Vacancy (5%): −$228K
- Other income: +$80K
- EGI = $4.412M
- Operating expenses (38% of EGI): −$1.677M
- **Stabilized NOI = $2.735M**

**Feasibility Test:**
- Yield on Cost = $2.735M / $41.6M = **6.57%**
- Market cap rate (illustrative, suburban multifamily): 5.0%
- Development Spread = 6.57% − 5.0% = **157 bps** — passes 150-bp threshold
- Stabilized value = $2.735M / 0.05 = **$54.7M**
- Profit = $54.7M − $41.6M = $13.1M; Profit margin = 31.5% — passes 15% threshold

**Stress test (illustrative):** Construction costs +10% (+$3.0M): TPC = $44.6M, YoC = 6.13%, spread = 113 bps — marginal. Rents −5% (−$95 GMR): NOI = $2.597M, YoC = 6.24%, spread = 124 bps — marginal. Combined stress: spread = ~85 bps — fails threshold. The project has adequate base-case margin but limited stress cushion; a contingency budget and locked subcontractor pricing are warranted before proceeding.

## Limitations

The Development Feasibility Test is a snapshot based on current market conditions. If the construction timeline is 24 months and the lease-up is another 12 months, the developer is pricing product into a market that is 3 years away. A test run in Expansion may produce a very different conclusion if the market enters Hypersupply before delivery. Always run the test using forward-looking rent and cap rate assumptions informed by [[Real Estate Cycle and Phases]] and [[Supply Pipeline Analysis]], not just current-period metrics.

The test also assumes the developer executes on budget and on schedule. Construction cost overruns of 10–20% are common (varies by market and contractor environment); timeline extensions of 3–6 months are frequent; lease-up can take twice as long as projected in a competitive environment. The minimum development spread threshold partly compensates for these risks but does not eliminate them.

The framework is silent on entitlement risk. A project with excellent post-entitlement economics can still fail if a rezoning takes two additional years or is denied. The full feasibility picture requires estimating entitlement probability and timeline, which is beyond the scope of the financial test itself. See [[Zone Change (Rezoning)]] and [[Conditional Use Permit (CUP)]].

## Related Frameworks

- [[Yield Analysis Methodology]] — provides the full suite of return metrics (IRR, equity multiple, CoC) that supplement the go/no-go spread test.
- [[Residual Land Value Feasibility]] — the inverse of this framework; solves for maximum land price given a required spread.
- [[Highest and Best Use Analysis]] — the prior step that determines which use type the feasibility test should be run on.
- [[Real Estate Cycle and Phases]] — provides the forward-looking market context essential for calibrating rent and cap rate assumptions.
- [[Sensitivity Analysis]] — the essential complement; converts point estimates into probability-weighted ranges.
- [[Pro Forma Construction Method]] — the detailed budgeting model that supplies TPC inputs.
