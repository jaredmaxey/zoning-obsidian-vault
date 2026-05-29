---
title: "Common Equity"
type: concept
tags: [cre/financing]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: The residual ownership layer of the capital stack, bearing first losses and receiving distributions only after all debt and preferred equity obligations are satisfied.
domain: financing
formula: true
related:
  - "Preferred Equity"
  - "Capital Stack Overview"
  - "Waterfall Structures and Promote"
  - "Joint Venture Structures"
  - "GP Co-Invest and Promote Crystallization"
  - "Preferred Return Mechanics"
  - "Internal Rate of Return (IRR)"
  - "Equity Multiple"
  - "Cash-on-Cash Return"
  - "Net Operating Income (NOI)"
---

# Common Equity

## Definition

Common equity is the residual interest in a real estate asset or project — the layer of ownership that absorbs all losses before any other capital source is impaired, and receives all remaining cash flows and appreciation after every debt obligation and preferred return has been satisfied. In a standard institutional CRE transaction, common equity sits at the bottom of the capital stack in terms of repayment priority but at the top in terms of return potential. The risk-return profile is the inverse of senior debt: common equity investors take the first loss on value declines but capture unlimited upside if the business plan outperforms.

In a joint venture structure, common equity is typically divided between the general partner (GP), who manages the investment and contributes a relatively small co-investment (often 1%–10% of total equity), and limited partners (LPs) or co-investors, who provide the majority of equity capital. The GP typically earns a promoted interest — a disproportionate share of profits above a specified hurdle — as compensation for sourcing, structuring, and executing the deal. This promote mechanism is what makes common equity particularly valuable to experienced sponsors even at a small dollar contribution (see [[Waterfall Structures and Promote]] and [[GP Co-Invest and Promote Crystallization]]).

The size of the common equity contribution as a percentage of total capitalization varies widely by deal type and leverage level. In a fully leveraged institutional acquisition with senior debt and mezzanine, common equity might represent 15%–25% of total cost. In a conservative core acquisition with low leverage, common equity might represent 40%–60%. The equity requirement is the mathematical residual of the capital stack: total cost minus all debt proceeds and any preferred equity raised. Managing the equity requirement is therefore central to return engineering.

## Formula

Common equity returns are most often measured via IRR and equity multiple, computed on the net equity cash flows after all debt service and preferred equity distributions.

**Net Equity Cash Flow (simplified annual):**

- Plain text: `Equity_CF = NOI - Debt_Service - Preferred_Distributions`
- LaTeX: $$ \text{Equity CF} = \text{NOI} - \text{Debt Service} - P_{distributions} $$

**Equity Multiple:**

- Plain text: `EM = Total_Distributions_to_Equity / Total_Equity_Invested`
- LaTeX: $$ EM = \frac{\sum_{t=0}^{T} D_t}{E_0} $$

**Levered IRR (solved for r such that NPV = 0):**

- Plain text: `0 = -Equity_Invested + sum of (Equity_CF_t / (1+r)^t) for t=1 to T`
- LaTeX: $$ 0 = -E_0 + \sum_{t=1}^{T} \frac{\text{Equity CF}_t}{(1+r)^t} $$

Where:
- **NOI** = Net Operating Income in each period
- **Debt Service** = principal and interest on all mortgage and subordinate debt
- **P_distributions** = preferred return and principal distributions to preferred equity investors
- **D_t** = equity distributions in period t (operating cash flows plus net sale/refi proceeds)
- **E_0** = total equity invested at inception
- **r** = equity IRR (solved iteratively)
- **T** = hold period in years

## When It's Used

Common equity is present in every CRE transaction — it is the foundational ownership interest. From a capital formation standpoint, it is the hardest component to raise for deals with elevated risk profiles because investors bear first loss. Institutional equity (pension funds, endowments, family offices, sovereign wealth funds) tends to concentrate on core and core-plus deals where the common equity is less levered and income-oriented. Value-add and opportunistic deals draw equity from sponsors, high-net-worth syndicators, and funds that target higher-IRR, higher-risk positions.

In a GP/LP joint venture, the LP's common equity check is the primary capital event that determines whether a deal closes. LPs underwrite the GP's business plan, track record, and alignment of interest (reflected in the GP co-invest percentage and promote structure) before committing. Understanding what return metrics LPs are targeting — IRR hurdles, equity multiple floors, and preferred return levels — is essential to structuring a deal the market will fund. Target LP equity returns for common equity vary significantly: a core deal might target a levered 8%–12% IRR; an opportunistic ground-up development might need to underwrite to a 15%–20%+ IRR to attract capital (varies by market and vintage, current as of 2026-05-24).

## Variations & Edge Cases

The distinction between GP equity and LP equity is a formal legal distinction within the common equity layer: both hold common equity interests, but their economic rights and governance authorities differ. GPs typically manage the asset, control major decisions (subject to LP approval thresholds), and earn promote; LPs provide the bulk of capital, have limited governance rights, and rely on the GP's fiduciary duty and operating agreement protections. Some structures allow an LP to convert to a GP role upon specified default conditions, creating a hybrid that blurs the line.

Co-investment (where an LP is offered a direct interest alongside the main fund vehicle) is a form of common equity that bypasses management fees and carries — effectively giving the co-investor a more direct exposure to the asset's economics. This has grown significantly in importance as large institutional LPs seek fee savings on their large commitments. Understanding the difference between fund-level common equity and co-investment-level common equity is important for modeling realistic return attribution.

## Common Mistakes

Sponsors frequently present gross (unlevered) IRR or pre-promote return metrics to LPs without clearly distinguishing the net-to-LP return after promote distributions. A deal that shows a 20% gross levered IRR may deliver a 14%–16% net-to-LP return after the GP takes a 20% promote above a 10% preferred return. LPs focus on the net number; failing to present both clearly erodes credibility in fundraising.

A second mistake is treating the equity requirement as fixed at deal inception. Equity is actually a residual: loan proceeds shrink if appraisals come in below purchase price, if construction cost escalation reduces LTC, or if market repricing occurs at refinance. Sponsors who undersize equity reserves or fail to model equity burn-up in stress scenarios can face capital calls at inopportune moments.

## Related Concepts

See [[Preferred Equity]] for the higher-priority equity layer. [[Capital Stack Overview]] provides the full layering context. [[Waterfall Structures and Promote]] governs how common equity distributions are structured. [[GP Co-Invest and Promote Crystallization]] covers how the GP's equity interest is managed. [[Internal Rate of Return (IRR)]] and [[Equity Multiple]] are the primary return metrics for common equity. [[Preferred Return Mechanics]] explains how the preferred return hurdle shapes common equity distributions.

## Sources

Common equity structure and GP/LP dynamics are addressed in David Geltner et al., *Commercial Real Estate Analysis and Investments*, 3rd ed. (OnCourse Learning), and in the Urban Land Institute's *Real Estate Finance Fundamentals*. NCREIF and NAREIM publish benchmarking data on institutional equity return targets by property type and risk profile. The ILPA (Institutional Limited Partners Association) publishes best-practice guidelines on fee structures, promote mechanics, and GP/LP alignment that inform common equity structuring conventions.
