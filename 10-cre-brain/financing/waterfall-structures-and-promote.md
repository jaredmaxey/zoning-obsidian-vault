---
title: "Waterfall Structures and Promote"
type: framework
tags: [cre/financing, cre/frameworks]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Framework for structuring and computing the distribution waterfall in a CRE joint venture, including preferred return hurdles, catch-up provisions, and the GP promote split.
inputs_required:
  - "Total equity invested (LP and GP amounts)"
  - "Preferred return rate(s) and compounding convention"
  - "Hurdle IRR rate(s)"
  - "Promote split percentage(s) at each tier"
  - "Catch-up percentage (if applicable)"
  - "Projected cash flows from operations and sale"
  - "Hold period"
outputs:
  - "Distribution amounts by tier and party (LP vs. GP)"
  - "Net LP IRR and equity multiple"
  - "GP promote dollars and effective GP IRR"
  - "Promote as percentage of total deal profit"
related:
  - "Capital Stack Overview"
  - "Common Equity"
  - "Preferred Equity"
  - "Preferred Return Mechanics"
  - "Joint Venture Structures"
  - "GP Co-Invest and Promote Crystallization"
  - "Internal Rate of Return (IRR)"
  - "Equity Multiple"
  - "Cash-on-Cash Return"
  - "Net Operating Income (NOI)"
---

# Waterfall Structures and Promote

## Purpose

The distribution waterfall is the contractual mechanism in a CRE joint venture that specifies exactly how cash flows — from property operations and from refinancing or sale proceeds — are allocated among the capital partners. The waterfall is typically structured as a series of sequential "tiers," with each tier directing money to a specified recipient until a threshold is satisfied, then stepping to the next tier. The GP "promote" (also called "carried interest") is the disproportionate share of profits above a specified return threshold that is paid to the GP as compensation for sourcing, structuring, managing, and executing the investment. Understanding the waterfall is essential for both GPs (who must design structures that are marketable to LPs while maximizing their own economics) and LPs (who must model the net returns they will actually receive after the GP's promote is applied).

Waterfall design is a core competency for institutional CRE practitioners because slight changes in hurdle rates, compounding conventions, and promote percentages can translate into millions of dollars of difference in the distribution between LP and GP. The framework below walks through a standard two-tier waterfall with a preferred return and promote — the most common structure in institutional value-add deals — and then addresses more complex multi-tier structures.

## Inputs Required

- **Total equity invested:** LP contribution and GP co-invest, with timing (funded at closing vs. in draws).
- **Preferred return rate:** the annual preferred return percentage to LPs (e.g., 8%); the compounding convention (simple, compounding, or daily) materially affects the amount owed.
- **Hurdle IRR:** one or more IRR thresholds that must be achieved before the GP's promote kicks in.
- **Promote split:** the percentage of profits above the hurdle going to the GP (e.g., 20%, 30%, or tiered across multiple hurdles).
- **Catch-up percentage:** the fraction of distributions going to the GP to "catch up" to its promote share before LP and GP share pro rata (not universal; varies by deal).
- **Projected cash flows:** quarterly or annual operating distributions and a terminal distribution at sale or refinance, with specific amounts and timing.
- **Hold period:** the number of years the investment is modeled to be held.

## Method

1. **Return of capital.** Distribute all available cash to the LP until the LP has received 100% of its invested capital back. (Some waterfalls return GP capital pro rata; others pay LP capital first.) This tier is technically not a return "on" capital — it just returns the principal.

2. **Preferred return.** Distribute to the LP a preferred return on unreturned capital at the agreed rate and compounding convention (see [[Preferred Return Mechanics]] for computation detail), until the LP has received the full accrued preferred return. Under an "accrued and compounding" convention, unpaid preferred return accumulates and itself earns the preferred rate; under a "simple" convention, it does not compound.

   - Plain text: `Pref_Owed = LP_Capital × Pref_Rate × (Days_Outstanding / 365)` (simple)
   - LaTeX: $$ P_{owed} = E_{LP} \times r_{pref} \times \frac{d}{365} $$

3. **Catch-up (if present).** Distribute 100% (or a specified high percentage, e.g., 50%) of remaining proceeds to the GP until the GP has received its promote share of total profits earned so far. This provision "catches up" the GP so that the blended split of profits above the preferred return equals the promote percentage (e.g., 80/20 LP/GP). Not all waterfall structures include a catch-up; some move directly to the promote tier.

4. **Promote tier (residual split).** Distribute remaining proceeds at the promote split — typically 80% to LP and 20% to GP (an "80/20" promote structure is the most common in institutional value-add). Multi-tier waterfalls may increase the GP's share as LP IRR crosses successive hurdles (e.g., 80/20 up to 15% LP IRR, then 70/30 above 15%, then 60/40 above 20%).

5. **Compute net LP IRR and equity multiple.** Sum all LP distributions (return of capital, preferred return, residual) and compute the IRR and equity multiple on the LP's invested capital. This is the "net-to-LP" return, the number LPs use to evaluate the investment.

6. **Compute GP promote.** Total GP distributions = GP co-invest return + promote dollars. Promote dollars = GP distributions − pro rata share of profits (what the GP would have earned with no promote, just its co-invest percentage). Effective GP IRR can be computed on total GP capital deployed vs. total GP distributions.

## Outputs

- **Distribution by tier:** LP and GP distributions from each waterfall tier, in dollars and as a percentage of total distributions.
- **Net LP IRR and equity multiple:** the after-promote return to the LP; the primary LP evaluation metric.
- **GP promote dollars:** the total dollars the GP earns above its pro rata share (the economic value of the promote).
- **Effective GP economics:** GP effective IRR and equity multiple on co-invest capital, reflecting the promote uplift.
- **Promote as % of total deal profit:** the share of total investment profit captured by the GP; a key LP assessment metric for GP alignment.

## Example Walkthrough

*(All figures are illustrative/hypothetical.)*

**Deal structure:**
- LP equity: $9,000,000; GP equity: $1,000,000; total equity: $10,000,000
- Preferred return: 8% per annum, simple (non-compounding)
- Promote: 80/20 LP/GP after return of capital and 8% preferred return
- No catch-up provision
- Hold period: 5 years

**Projected distributions (illustrative):**
- Operating distributions years 1–5: $500,000/year ($50,000 to GP co-invest, $450,000 to LP per year, applied first to preferred return)
- Net sale proceeds at year 5: $14,000,000 total equity proceeds

**Waterfall computation:**

*Preferred return accrual (LP only):*
$9,000,000 × 8% × 5 years = $3,600,000 preferred return accrued to LP.

*Operating distributions (years 1–5):*
$450,000/year × 5 years = $2,250,000 to LP (applied first to preferred return — $2,250,000 of $3,600,000 pref satisfied). GP receives $50,000/year × 5 years = $250,000 (return of GP co-invest at pro rata).

*Sale proceeds — Tier 1 (return of LP capital):*
LP has received $2,250,000 in operating distributions; $9,000,000 − $2,250,000 = $6,750,000 LP capital still outstanding (assume operating distributions were applied first to preferred, so LP capital is full $9,000,000 depending on application order — waterfall terms govern; this example applies to preferred first). Use convention: operating CFs applied first to preferred return.

Sale proceeds = $14,000,000 (equity). Remaining pref: $3,600,000 − $2,250,000 = $1,350,000.
After preferred payoff: $14,000,000 − $1,350,000 = $12,650,000 remaining.
Return LP capital: $9,000,000. Remaining: $12,650,000 − $9,000,000 = $3,650,000.
Return GP capital: $1,000,000 − $250,000 = $750,000 remaining GP capital. Remaining: $3,650,000 − $750,000 = $2,900,000.
Split residual 80/20: LP gets $2,320,000; GP promote = $580,000.

*Total LP:* $2,250,000 (ops) + $1,350,000 (pref at sale) + $9,000,000 (capital) + $2,320,000 (residual) = $14,920,000. LP equity multiple: $14,920,000 / $9,000,000 = **1.66×** (illustrative). LP IRR: ~10.9% (illustrative).

*Total GP:* $250,000 (ops) + $750,000 (capital) + $580,000 (promote) = $1,580,000. GP equity multiple on $1,000,000 co-invest: **1.58×**; effective GP IRR including promote: ~9.5% (illustrative). Note promote dollars = $580,000; promote as % of deal profit: $580,000 / ($14,000,000 + $2,500,000 − $10,000,000) = substantial share of profit (illustrative).

## Limitations

The waterfall framework assumes precise contractual interpretation of the operating agreement. Real-world waterfalls are governed by extensive legal documentation and can involve dozens of edge cases: mid-hold refinancing distributions (recalibrating the preferred return), cure rights for missed preferred return payments, GP removal provisions that affect promote entitlement, and multi-asset fund structures that aggregate returns across the portfolio before applying promote splits. This framework covers the single-asset deal structure; fund-level waterfalls add another layer of complexity addressed in [[GP Co-Invest and Promote Crystallization]].

The framework also does not address the tax consequences of promote income (which is taxed as capital gain under carried interest rules in the U.S., subject to the two-year holding period requirement under IRC Section 1061) or the mechanics of promote realization in cases where the deal is partially realized through refinancing.

## Related Frameworks

[[Preferred Return Mechanics]] provides the detailed computation of the preferred return tier. [[Joint Venture Structures]] covers the entity and governance framework that houses the waterfall. [[GP Co-Invest and Promote Crystallization]] addresses multi-deal fund-level promote and timing of GP economic realization. [[Capital Stack Overview]] is the prerequisite framework establishing the equity position within the total financing structure. [[Internal Rate of Return (IRR)]] and [[Equity Multiple]] are the output metrics computed from the waterfall.
