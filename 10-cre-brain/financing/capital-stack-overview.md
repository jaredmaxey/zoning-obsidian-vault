---
title: "Capital Stack Overview"
type: framework
tags: [cre/financing, cre/frameworks]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Framework for visualizing and analyzing the layered financing structure of a CRE transaction, mapping each capital source's priority, cost, and risk-return position.
inputs_required:
  - "Total project cost or acquisition price"
  - "Senior debt proceeds (LTV/LTC and product type)"
  - "Mezzanine debt or preferred equity proceeds (if any)"
  - "Common equity contribution (GP and LP)"
  - "Interest rates and preferred return targets by layer"
  - "Waterfall distribution mechanics"
outputs:
  - "Capital stack diagram (layers, amounts, percentages)"
  - "Blended cost of capital (WACC)"
  - "Equity requirement by layer"
  - "Return attribution by capital source"
related:
  - "Senior Debt"
  - "Mezzanine Debt"
  - "Preferred Equity"
  - "Common Equity"
  - "Waterfall Structures and Promote"
  - "Joint Venture Structures"
  - "Preferred Return Mechanics"
  - "GP Co-Invest and Promote Crystallization"
  - "Weighted Average Cost of Capital (WACC)"
  - "Internal Rate of Return (IRR)"
  - "Loan-to-Value (LTV)"
  - "Loan-to-Cost (LTC)"
  - "Debt Service Coverage Ratio (DSCR)"
---

# Capital Stack Overview

## Purpose

The capital stack framework is the foundational organizational tool for understanding how a CRE transaction is financed. Every dollar of project cost or acquisition price is funded by one or more capital sources, each with distinct legal priority, cost of capital, and risk-return expectations. The framework maps these sources in their correct order — from the most senior (first repaid, lowest risk, lowest return) to the most subordinate (last repaid, highest risk, highest return potential) — and allows practitioners to analyze the economics of each layer, the blended cost of the full stack, and the return implications for equity investors at any level of leverage.

The capital stack is not merely an accounting exercise. It governs who gets paid when, who absorbs losses first, and who has control in a distressed scenario. An analyst who can rapidly construct, stress-test, and optimize a capital stack is positioned to structure financings, evaluate competing offers, model returns for each capital source, and identify the binding constraints in a deal's financing plan.

## Inputs Required

- **Total project cost or acquisition price:** the denominator against which leverage is measured; for acquisitions, this is purchase price plus closing costs; for development, it is all-in cost including land, hard costs, soft costs, contingency, and carry.
- **Senior debt proceeds:** determined by LTV, LTC, DSCR, and debt yield tests applied by the senior lender; must specify product type (agency, CMBS, bank, debt fund) as product governs pricing, terms, and prepayment.
- **Mezzanine debt or preferred equity proceeds (if any):** the gap-filling subordinate layer between senior debt and equity; determined by combined LTC/LTV targets and mezzanine lender underwriting.
- **Common equity contribution:** residual after debt and preferred equity; broken into GP co-invest and LP equity, with their respective economic arrangements.
- **Pricing for each layer:** senior rate (fixed or floating + spread), mezzanine rate, preferred return rate, and GP/LP equity return expectations.
- **Waterfall mechanics:** the distribution logic that determines how cash flows from operations and sale proceeds are allocated among layers (see [[Waterfall Structures and Promote]]).

## Method

1. **Define total capitalization.** Begin with total project cost (development) or total deal cost (acquisition). Every component of the stack must sum to 100% of this total.

2. **Size the senior debt.** Apply the relevant lender's three-constraint framework: maximum loan under LTV (appraised/as-stabilized value × LTV limit), DSCR (NOI / (DSCR_min × debt constant)), and debt yield (NOI / DY_min). The binding constraint — the lowest of the three resulting loan amounts — sets senior debt proceeds. Express as a dollar amount and as a percentage of total cost.

3. **Determine subordinate debt or preferred equity (if applicable).** Compute whether the gap between senior debt proceeds and total equity needs to be split between preferred equity/mezz and common equity. Size the subordinate layer based on combined LTC targets and mezzanine lender underwriting. Compute the subordinate layer's annual cost (principal balance × rate) and add it to senior debt service to compute total debt service.

4. **Compute the equity requirement.** Common equity = Total Cost − Senior Debt − Mezzanine/Preferred Equity. Allocate between GP (co-invest percentage × total equity) and LP (residual). For institutional deals, LP equity is the key capital raise.

5. **Compute WACC across the stack.**
   - Plain text: `WACC = sum of (Layer_i_Amount / Total_Capital × Layer_i_Cost)` for all layers i
   - LaTeX: $$ WACC = \sum_{i} \frac{L_i}{C_{total}} \times r_i $$
   Where $L_i$ is each layer's balance and $r_i$ is each layer's cost (using preferred rate for preferred equity, equity IRR target for common equity).

6. **Stress-test the stack.** Run the stack at NOI haircuts (e.g., −10%, −20%), value declines (e.g., cap rate expansion of 50–100 bps), and interest rate increases (for floating-rate layers). Identify the scenarios in which each layer is impaired and the equity is wiped out.

7. **Build the return attribution.** Compute the projected returns to each layer given the expected business plan outcome: debt service coverage and yield for senior/mezzanine; preferred return multiple for preferred equity; IRR and equity multiple for common equity.

## Outputs

- **Capital stack diagram:** visual or tabular representation of each layer's name, dollar amount, percentage of total cost, cost of capital (yield/rate), and seniority.
- **Blended WACC:** the weighted average cost across all layers, useful for comparing deal structures and computing the spread to unlevered yield.
- **Equity requirement:** total equity and GP/LP split.
- **Return attribution:** projected IRR and multiple by layer under the base case and stress scenarios.

## Example Walkthrough

*(All figures are illustrative/hypothetical.)*

Assume a value-add multifamily acquisition:
- **Total deal cost:** $20,000,000 (purchase price + closing costs + renovation reserve)
- **As-stabilized value:** $24,000,000 (based on stabilized NOI of $1,440,000 at 6.0% cap rate)
- **Stabilized NOI:** $1,440,000/year (lender-underwritten)

**Senior debt sizing:**
- LTV test: 70% × $24M = $16,800,000
- DSCR test: $1,440,000 / (1.25 × 0.06) = $19,200,000 (but capped at LTV)
- Debt yield test: $1,440,000 / 0.090 = $16,000,000 (binding constraint at 9% DY floor)
- **Senior loan: $16,000,000** (80% LTC; 9.0% debt yield; lender pricing at 7.0% fixed rate)

**No mezzanine in this example.**

**Equity:** $20,000,000 − $16,000,000 = **$4,000,000** (20% LTC)
- GP co-invest: 10% × $4M = $400,000
- LP equity: $3,600,000

**Capital stack (illustrative):**

| Layer | Amount | % of Cost | Cost |
|---|---|---|---|
| Senior Debt | $16,000,000 | 80% | 7.0% fixed |
| Common Equity (LP) | $3,600,000 | 18% | Target 15%+ IRR |
| Common Equity (GP) | $400,000 | 2% | Target 15%+ IRR + promote |
| **Total** | **$20,000,000** | **100%** | |

**WACC:** (0.80 × 7.0%) + (0.20 × 15.0%) = 5.6% + 3.0% = **8.6%** blended cost (illustrative)

Note: actual WACC computation would use levered equity IRR once modeled — the 15% above is the assumed equity return target, not yet a realized return.

## Limitations

The capital stack framework is a static snapshot of financing structure and cost. It does not inherently model the time-value implications of draw schedules (construction), prepayment costs, or the dynamics of floating rates over the hold period — all of which must be added in a full DCF model. The framework also does not capture covenant risk, servicer flexibility, and relationship quality, which are qualitative factors that can be as important as economics in a distressed scenario.

WACC is useful for comparison but does not substitute for a full IRR analysis. The WACC computation assumes all layers are funded and outstanding simultaneously and continuously, which is rarely true in construction or value-add contexts where equity is funded first and senior debt is drawn against milestones.

## Related Frameworks

[[Waterfall Structures and Promote]] governs how cash flows within the equity portion of the stack are allocated between LP and GP. [[Joint Venture Structures]] covers the entity and governance framework surrounding common equity. [[Preferred Return Mechanics]] covers how the preferred return layer within equity is computed. [[Weighted Average Cost of Capital (WACC)]] provides the general WACC methodology applicable across industries. [[Debt Service Coverage Ratio (DSCR)]], [[Loan-to-Value (LTV)]], and [[Debt Yield]] are the metrics used in Step 2 of the method.
