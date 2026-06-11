---
title: "Equity Multiple"
aliases: ["Equity Multiple"]
type: concept
tags: [cre/concepts]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Equity multiple is the ratio of total cash distributions received to total equity invested, expressing how many times an investor gets their capital back over the entire hold period.
domain: concepts
formula: true
related:
  - "Internal Rate of Return (IRR)"
  - "Cash-on-Cash Return"
  - "Equity Multiple"
  - "Waterfall Structures and Promote"
  - "Preferred Return Mechanics"
  - "Net Operating Income (NOI)"
  - "Exit Cap Rate"
---

# Equity Multiple

## Definition

The equity multiple (EM) — also called the multiple on invested capital (MOIC) — is the ratio of the total cumulative cash distributions an investor receives over the life of an investment to the total equity capital they contributed. An equity multiple of 2.0x means the investor received twice their original equity back; a 1.5x means they earned 50 cents for every dollar invested; a multiple below 1.0x means a loss of principal. Unlike IRR, equity multiple is completely agnostic to timing — it is a raw scalar that measures total wealth creation, not annualized return.

Equity multiple and IRR are complementary metrics that answer different questions. IRR answers "at what annualized rate did my capital compound?" Equity multiple answers "how many times did I get my money back?" A deal with a short hold period can show a high IRR but modest equity multiple; a long-hold deal may show a moderate IRR but a large equity multiple. Best-practice institutional underwriting always presents both metrics together, with the hold period, so investors can assess the tradeoff between rate and magnitude of return.

Equity multiples are reported on a levered basis (equity invested and distributions to equity holders only, net of debt service) in most LP/GP deal presentations. Some contexts also report on an unlevered basis (total project cost vs. total project proceeds) for an asset-level, capital-structure-neutral view.

## Formula

- Plain text: `Equity Multiple = Total Cash Distributions / Total Equity Invested`
- LaTeX: $$ \text{EM} = \frac{\sum \text{Cash Distributions}}{\text{Total Equity Invested}} $$

**Where:**
- **Total Cash Distributions** — the sum of all cash flows received by the equity investor over the entire hold period: annual operating distributions plus the net equity proceeds at sale (after repaying the loan balance and all closing costs).
- **Total Equity Invested** — the total equity contributed, including the initial down payment, all subsequent capital calls (renovations, carry shortfalls, reserves), and any other equity contributions during the hold.

If the investment has staged equity contributions (common in development), total equity invested is the sum of all contributions, not just the day-one check.

## When It's Used

Equity multiple is the standard summary statistic in deal marketing materials, fund performance reports, and investment committee presentations. Investors use it as a sanity check on IRR: a high IRR is more credible when accompanied by a meaningful equity multiple. Conversely, a high multiple achieved over a very long hold may reflect low IRR.

In waterfall structures, some promote hurdles are structured around equity multiple thresholds rather than (or in addition to) IRR hurdles — for example, the GP might earn a promoted interest once LPs achieve a 1.8x multiple. This eliminates the IRR sensitivity to hold-period timing that can cause disputes over promote calculations. See [[Waterfall Structures and Promote]].

For distressed and opportunistic strategies — where a large portion of return comes from the terminal exit rather than ongoing distributions — equity multiple captures the full value creation in a single intuitive number. For a 3-year value-add deal targeting 1.7–1.9x and a 5-year development targeting 1.8–2.2x (all figures vary by market, vintage, and leverage), equity multiple provides an immediately interpretable benchmark.

## Variations & Edge Cases

**Gross vs. net multiple:** Gross equity multiple is pre-promote and pre-carried-interest, reflecting asset-level performance. Net multiple is what the LP actually receives after the GP's carried interest and management fees. LPs should always ask for net multiples. The spread between gross and net varies with the waterfall structure, promote percentage, and fee load.

**Levered vs. unlevered multiple:** Levered EM is equity-level (more common in fund reporting); unlevered EM is project-level. Positive leverage increases the levered multiple above the unlevered multiple when the cap rate exceeds the mortgage constant.

**Partially realized investments:** For in-process deals (unrealized), equity multiple includes only distributions received to date plus the current market value mark, making it partly estimated. Some fund managers report DPI (Distributed to Paid-In) separately from TVPI (Total Value to Paid-In = DPI + RVPI, where RVPI is residual value) to distinguish realized from unrealized components.

Equity multiple targets in institutional CRE range widely by deal type: core deals may target 1.4–1.6x over 7–10 years; value-add deals 1.7–2.2x over 3–7 years; opportunistic/development deals may target 2.0x+ over 3–5 years (varies by market and vintage; current as of 2026-05-24).

## Common Mistakes

**Using equity multiple without specifying the hold period.** A 2.0x multiple over 3 years is very different from a 2.0x multiple over 10 years. Without the hold period, the multiple is context-free.

**Reporting gross multiples to LPs without disclosing the promote structure.** Gross multiples from the sponsor's marketing materials must be adjusted for the actual fee and waterfall structure to arrive at the LP's net return. Conflating gross and net understates the investor's real outcome.

**Ignoring capital calls in the denominator.** If the deal required additional equity contributions for capex, carry, or reserves, these must be included in total equity invested. Omitting them overstates the multiple.

## Related Concepts

- [[Internal Rate of Return (IRR)]] — the time-weighted rate that complements the equity multiple's size measurement
- [[Cash-on-Cash Return]] — the current-period income yield; equity multiple aggregates the full stream including reversion
- [[Exit Cap Rate]] — the terminal value assumption that often determines whether the equity multiple clears the target
- [[Waterfall Structures and Promote]] — the distribution mechanism that converts deal returns into LP vs. GP allocations
- [[Preferred Return Mechanics]] — the LP priority return hurdle that must be cleared before the GP earn promote

## Sources

Equity multiple conventions are covered in CCIM Institute's financial analysis curriculum, ULI's real estate finance materials, and standard private equity fund reporting frameworks (ILPA guidelines). Market return targets vary by fund strategy, vintage, and market cycle (varies by market and vintage; current as of 2026-05-24).
