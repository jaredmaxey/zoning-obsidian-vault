---
title: "Internal Rate of Return (IRR)"
aliases: ["Internal Rate of Return (IRR)"]
type: concept
tags: [cre/concepts]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: IRR is the discount rate that sets the net present value of all cash flows (including the reversion) to zero, serving as the primary total-return metric for CRE hold-period analysis.
domain: concepts
formula: true
related:
  - "Equity Multiple"
  - "Cash-on-Cash Return"
  - "Cap Rate"
  - "Discount Rate"
  - "Exit Cap Rate"
  - "Net Operating Income (NOI)"
  - "Discounted Cash Flow (DCF)"
  - "Weighted Average Cost of Capital (WACC)"
  - "Waterfall Structures and Promote"
  - "Sensitivity Analysis"
---

# Internal Rate of Return (IRR)

## Definition

The internal rate of return (IRR) is the annualized discount rate that makes the net present value (NPV) of all future cash flows from an investment equal to zero — or equivalently, the rate at which the present value of all inflows exactly equals the present value of all outflows. In CRE, IRR is the primary total-return metric: it captures both the periodic income generated during a hold period and the terminal value (reversion) received at disposition, expressed as a single annualized percentage.

IRR is more informative than a simple average annual return because it weights the timing of cash flows — money received sooner is worth more than money received later. A deal that returns capital quickly (low reversion multiple, high early distributions) will have a higher IRR than a deal of equal total return that returns most proceeds at the end. This time-value sensitivity is both the strength and the limitation of IRR.

IRR is computed on either a levered or unlevered basis, and the distinction is critical. Unlevered IRR (property-level) measures the return on the total project cost as if purchased all-cash; it is asset-level and capital-structure-neutral, useful for comparing assets across different financing scenarios. Levered IRR (equity-level) measures the return on equity capital after debt service, reflecting the actual investor experience including the amplifying (or damaging) effect of leverage. Most LP/GP waterfall promote structures reference levered IRR hurdles. See [[Waterfall Structures and Promote]].

## Formula

IRR is the value *r* that satisfies the following equation (solved iteratively — there is no closed-form solution):

- Plain text: `0 = CF0 + CF1/(1+r) + CF2/(1+r)^2 + ... + CFn/(1+r)^n`
- LaTeX:
$$
0 = \sum_{t=0}^{n} \frac{CF_t}{(1+r)^t}
$$

**Where:**
- **CF₀** — initial investment (negative; cash outflow at time zero)
- **CF₁ … CF_{n-1}** — net cash flows in each period (typically annual; positive in operating years, possibly negative in renovation/construction years)
- **CF_n** — final period cash flow including the net sale proceeds (reversion)
- **r** — the IRR (solved for; expressed as an annual rate)
- **n** — number of periods in the hold

In practice, IRR is always solved using a financial calculator, Excel (`XIRR` for irregular intervals, `IRR` for annual), or underwriting software. The `XIRR` function is preferred in CRE because cash flows and dates are rarely precisely annual.

## When It's Used

IRR is the universal language of institutional CRE returns. Equity fund mandates define their return targets in IRR terms: a value-add fund might target 12–16% levered IRR; a core fund might target 7–9% unlevered. When a sponsor presents a deal to LPs, the projected levered IRR — sensitivity-tested — is the primary return summary. See [[Sensitivity Analysis]].

In development underwriting, IRR is typically computed on the equity invested over the construction and lease-up period, using the projected stabilized value (derived from [[Exit Cap Rate]] and stabilized NOI) as the terminal cash flow. This allows an apples-to-apples comparison between development deals of different durations and cash flow profiles.

IRR is also used as a hurdle rate in waterfall structures: once the equity investors have achieved a specified IRR on their capital, the sponsor (GP) earns a disproportionate promoted interest (carry). See [[Preferred Return Mechanics]] and [[Waterfall Structures and Promote]].

## Variations & Edge Cases

**Levered vs. unlevered IRR:** The most important distinction. Always specify. Levered IRR is investor/equity IRR; unlevered IRR is property/asset IRR. Leverage amplifies IRR in positive-spread environments and destroys it when debt costs exceed returns.

**Multiple IRR problem:** If a cash flow series changes sign more than once (e.g., a project that has additional equity contributions mid-hold), the IRR equation can have multiple mathematical solutions. In such cases, use Modified IRR (MIRR) or NPV analysis instead.

**MIRR (Modified IRR):** Assumes reinvestment of intermediate cash flows at the cost of capital (not at the IRR itself, which is the implicit assumption in conventional IRR). MIRR is more conservative and theoretically sound for reinvestment assumptions; some institutional investors require it.

**IRR vs. NPV:** IRR does not account for deal size. A $5M deal at 20% IRR may be less valuable than a $50M deal at 15% IRR. Always pair IRR with [[Equity Multiple]] and absolute dollar profit to assess deal quality fully.

Return hurdles for institutional CRE vary significantly by deal type, vintage, and market. As of 2026-05-24, levered IRR targets commonly seen range from low single digits (core) to mid-teens or higher (opportunistic/development), with value-add targets in the 12–16% range — all highly dependent on leverage, asset class, and market cycle (varies by market and vintage).

## Common Mistakes

**Ignoring the impact of hold period on IRR.** A shorter hold period amplifies IRR even if total profit is the same. Comparing a 3-year and a 7-year deal solely on IRR without comparing equity multiples can be misleading.

**Using IRR as the sole return metric.** IRR says nothing about how much capital was at risk or how much total wealth was created. Always report alongside equity multiple, profit on cost, and peak equity exposure.

**Front-loading distributions to boost IRR.** Some waterfall structures incentivize sponsors to return capital quickly (via refinancings or asset sales) to trigger IRR-based promote, even when holding longer would maximize total value. Investors should be aware of this structural tension.

**Conflating levered and unlevered IRR.** Comparing one deal's levered IRR to another deal's unlevered IRR is an apples-to-oranges error.

## Related Concepts

- [[Equity Multiple]] — the total return scalar that pairs with IRR to capture magnitude as well as rate of return
- [[Cash-on-Cash Return]] — the current-period levered income yield; IRR extends this to include reversion
- [[Discount Rate]] — the rate used to compute NPV; IRR is the break-even discount rate
- [[Exit Cap Rate]] — the terminal value assumption that often drives the largest single component of levered IRR
- [[Discounted Cash Flow (DCF)]] — the analytical framework in which IRR is the primary output
- [[Net Operating Income (NOI)]] — the operating cash flows that are discounted
- [[Weighted Average Cost of Capital (WACC)]] — the blended cost of capital used as a benchmark discount rate
- [[Sensitivity Analysis]] — the methodology used to test IRR across assumption ranges

## Sources

IRR methodology is foundational in Brealey, Myers & Allen's *Principles of Corporate Finance* and the CCIM Institute's financial analysis curriculum. CRE-specific IRR benchmarks by deal type are published by NCREIF, PREA, and institutional fund managers (varies by market and vintage; current as of 2026-05-24).
