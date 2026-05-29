---
title: "Residual Land Value Method"
type: framework
tags: [cre/underwriting, cre/frameworks]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Development feasibility method that back-solves for the maximum land price a developer can pay while still achieving a target return, given projected revenues, costs, and yield requirements.
inputs_required:
  - Stabilized NOI or gross development value at completion
  - Total development cost (hard costs, soft costs, financing)
  - Required yield on cost or developer profit margin
  - Exit cap rate or market value at completion
outputs:
  - Residual land value (maximum supportable land price)
  - Development feasibility check (go/no-go)
  - Development spread (yield on cost vs. exit cap)
related:
  - "Direct Capitalization"
  - "Discounted Cash Flow (DCF)"
  - "Yield-on-Cost vs. Market Cap Spread"
  - "Development Spread"
  - "Pro Forma Construction Method"
  - "Yield on Cost"
  - "Cap Rate"
  - "Exit Cap Rate"
  - "Loan-to-Cost (LTC)"
  - "Construction Loan"
  - "Ground-Up Development"
  - "Development Feasibility Test"
  - "Residual Land Value Feasibility"
---

# Residual Land Value Method

## Purpose

The residual land value method is the foundational feasibility framework for ground-up development. It works backward from the projected market value of a completed development (or the stabilized NOI capitalized at an exit cap rate) to determine the maximum price a developer can pay for land while still achieving a required return on total investment. The "residual" in the name refers to land value being the residual — what is left over after all development costs and profit requirements have been satisfied from the projected value of the finished product.

This framework is the primary tool for land pricing, feasibility assessment, and seller negotiation in development deals. A developer uses it to determine their maximum bid for land before they will accept the site. A landowner uses it (often with an independent appraiser) to evaluate whether a developer's land offer reflects the site's value given its highest and best use. Lenders use a version of it to confirm that a proposed land price is rational given the development economics. At its core, it answers the question: given what this building will be worth when it is built, and given what it costs to build, what is the land worth?

## Inputs Required

- **Projected stabilized NOI or gross development value (GDV):** For income-producing developments, NOI at stabilization times a terminal cap rate. For for-sale residential, the aggregate market value of sellable units. Units: dollars.
- **Hard costs:** Construction contract cost (shell, tenant improvements, site work). Units: dollars; typically expressed per SF of gross building area.
- **Soft costs:** Architecture, engineering, permitting, legal, title, insurance during construction, marketing, developer overhead. Typically 15–25% of hard costs (varies by project complexity, market, and vintage as of 2026-05-24).
- **Financing costs:** Construction loan interest carry, origination fees, and financing reserves. Depends on loan-to-cost ratio, interest rate, and construction duration.
- **Developer profit / required yield on cost (YoC):** The return the developer requires for the development risk taken. Expressed either as a YoC spread above the exit cap rate (typically 150–250 bps; varies by market and risk as of 2026-05-24) or as a developer profit percentage (10–20% of total cost or GDV; varies by market and vintage).
- **Transaction costs:** Closing costs on land acquisition and eventual sale/refinance.

## Method

1. **Estimate the market value of the completed development (GDV or stabilized cap value).** For an income-producing asset: apply the exit cap rate to stabilized NOI.
   - Plain text: `Completed Value = Stabilized NOI / Exit Cap Rate`
   - LaTeX: $$ V_{completed} = \frac{NOI_{stab}}{R_{exit}} $$

2. **Determine the required developer profit or return.** Set either a minimum yield on cost (YoC) spread above the exit cap, or a minimum developer profit as a percentage of completed value or total cost. The developer profit is what makes the project worth building over acquisition of a stabilized asset — it compensates for construction risk, leasing risk, and time. Typical institutional development targets 150–250 bps of spread over the stabilized cap rate as the YoC premium (varies by risk profile and market as of 2026-05-24).

3. **Estimate total development cost excluding land (TDC ex-land).** Sum all hard costs, soft costs, financing costs, and transaction costs except the land purchase price.
   - Plain text: `TDC ex-land = Hard Costs + Soft Costs + Financing Costs + Other`
   - LaTeX: $$ TDC_{ex-land} = C_{hard} + C_{soft} + C_{fin} + C_{other} $$

4. **Back-solve for the residual land value.** The residual land value is the completed value minus TDC ex-land minus the required developer profit.
   - Plain text: `Residual Land Value = Completed Value − TDC ex-land − Developer Profit`
   - LaTeX: $$ RLV = V_{completed} - TDC_{ex-land} - Profit_{developer} $$
   - Where: RLV = residual land value (maximum supportable land price); V_completed = market value at stabilization; TDC_ex-land = total development cost excluding land; Profit_developer = required developer return in dollar terms.

5. **Perform the feasibility check.** If RLV > the seller's land price, the deal is feasible at the seller's ask. If RLV < 0 or < the seller's ask, the deal does not work at current values — the developer must either reduce costs, achieve higher rents, accept a lower return, or pass on the site.

6. **Compute yield on cost and development spread.** At the derived land price (or at a given land bid), compute the YoC and the spread over the exit cap.
   - Plain text: `YoC = Stabilized NOI / Total Development Cost (including land)`
   - LaTeX: $$ YoC = \frac{NOI_{stab}}{TDC_{incl-land}} $$
   - Development spread = YoC − Exit Cap Rate. See [[Development Spread]].

## Outputs

The residual land value method produces: (1) the residual land value (maximum supportable land bid); (2) a feasibility check (does the deal work at the seller's asking price?); (3) yield on cost at the underwritten land price; and (4) development spread (YoC minus exit cap).

## Example Walkthrough

*All figures below are illustrative and hypothetical — not derived from any real transaction.*

A developer underwrites a 200-unit multifamily development. Stabilized NOI: $1,600,000. Exit cap rate: 5.25%. Completed value: $1,600,000 / 0.0525 = $30,476,190. Hard costs: $22,000/unit × 200 = $4,400,000 (illustrative, excludes site work and TI). Total hard + soft + financing (ex-land): $20,000,000. Required developer profit: 15% of completed value = $4,571,429. Residual land value: $30,476,190 − $20,000,000 − $4,571,429 = $5,904,761. If the seller is asking $6,500,000 for the land, the deal does not work at these inputs — the developer would need to either reduce costs, achieve higher rents, or accept a lower profit margin. At the $5,904,761 land price, total development cost = $20,000,000 + $5,904,761 = $25,904,761. YoC = $1,600,000 / $25,904,761 = 6.17%. Development spread vs. 5.25% exit cap = 92 bps — below the typical 150 bps minimum, confirming the deal is marginal.

## Limitations

The residual land value method is extremely sensitive to the assumptions for completed value (cap rate and stabilized NOI) and total development cost. Hard costs, soft costs, and construction loan interest can all vary significantly; a 10% cost overrun or a 25 bps upward move in the exit cap rate can swing the RLV by 50% or more in thin-margin situations. The method also assumes a single development scenario at a point in time — it does not model the optionality of phased development, entitlement upside, or land price appreciation while holding. See [[Discounted Cash Flow (DCF)]] for a multi-period development model.

## Related Frameworks

[[Direct Capitalization]] — used to compute completed value in Step 1. [[Yield-on-Cost vs. Market Cap Spread]] and [[Development Spread]] — the spread metrics derived from the residual model. [[Discounted Cash Flow (DCF)]] — the multi-period complement for full development return modeling. [[Development Feasibility Test]] and [[Residual Land Value Feasibility]] — companion frameworks in the broader feasibility toolkit. See also [[Yield on Cost]], [[Cap Rate]], [[Exit Cap Rate]], and [[Ground-Up Development]].

## Sources

Appraisal Institute, *The Appraisal of Real Estate* (14th ed.) — Residual Land Valuation. ULI, *Real Estate Development: Principles and Process* (5th ed.). CCIM Institute development feasibility coursework.
