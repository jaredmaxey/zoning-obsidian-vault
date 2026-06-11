---
title: "Joint Venture Structures"
aliases: ["Joint Venture Structures"]
type: framework
tags: [cre/financing, cre/frameworks]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Framework for designing and evaluating CRE joint venture entity structures, governance rights, contribution splits, and alignment mechanisms between operating partners and capital partners.
inputs_required:
  - "Deal type and business plan"
  - "Capital requirements (equity and debt)"
  - "GP and LP equity contributions and percentages"
  - "Preferred return and promote economics"
  - "Control and governance requirements"
  - "State of entity formation and tax considerations"
  - "LP investor profile and approval rights"
outputs:
  - "Entity structure diagram (fund, JV, co-invest)"
  - "GP/LP ownership percentages and economic splits"
  - "Governance rights by partner (major decision approval, removal rights)"
  - "Operating agreement term sheet"
  - "Waterfall economics summary"
related:
  - "Capital Stack Overview"
  - "Waterfall Structures and Promote"
  - "Preferred Return Mechanics"
  - "GP Co-Invest and Promote Crystallization"
  - "Common Equity"
  - "Preferred Equity"
  - "Internal Rate of Return (IRR)"
  - "Equity Multiple"
---

# Joint Venture Structures

## Purpose

A joint venture (JV) structure is the legal and economic framework through which multiple parties — typically an operating partner (GP) with deal-sourcing, execution, and management expertise, and one or more capital partners (LPs) providing the majority of equity — co-own a CRE asset or portfolio. JV structuring answers several critical questions simultaneously: Who controls day-to-day management and major decisions? How much capital does each party contribute, and in what proportion? How are distributions allocated across the hold period? What happens if one party wants to exit, underperforms, or defaults on obligations? The JV structure must balance the GP's need for operational control and economic upside (through the promote) against the LP's need for capital protection, governance rights, and transparency.

JV structuring is one of the most nuanced areas of CRE practice because the optimal design depends on the specific deal, the parties' relative sophistication, the asset type and business plan risk, the LP's institutional vs. private nature, and regulatory and tax considerations. There is no single standard structure — the market spans a spectrum from very GP-favorable (maximum control, maximum promote) to very LP-favorable (extensive approval rights, low promote, downside protection mechanisms) depending on leverage, track record, and capital market conditions (varies by market and vintage, current as of 2026-05-24).

## Inputs Required

- **Deal type and business plan:** determines the appropriate level of GP control and LP oversight; ground-up development requires more frequent major decision checkpoints than a stable core asset.
- **Capital requirements:** total equity needed, split between GP co-invest and LP equity, and whether any preferred equity or mezzanine is layered in.
- **GP and LP economics:** preferred return rate and compounding, hurdle IRR, promote percentage, catch-up provisions (see [[Waterfall Structures and Promote]]).
- **Control and governance:** which decisions require LP consent (major decisions list), which are GP discretion, and what constitutes a GP removal event.
- **Entity formation considerations:** LLC vs. LP, state of organization, tax treatment (partnership vs. REIT vs. C-corp), and any special considerations for foreign capital.
- **LP investor profile:** institutional vs. private, regulated entity (pension fund, insurance company), ERISA applicability, UBTI sensitivity, and reporting requirements.

## Method

1. **Select entity type.** Most institutional CRE JVs use a Delaware LLC as the joint venture entity because of Delaware's flexible LLC Act, well-developed case law, and ease of interstate operation. Limited partnerships (LPs) are less common for single-deal JVs but remain standard for funds. Tax considerations (e.g., avoiding UBTI for tax-exempt LP investors, FIRPTA for foreign investors) may influence structure. For large deals with multiple LP investors, a "feeder fund" structure (a fund entity that pools LP capital and then invests as a single LP into the deal JV) is common.

2. **Define the capital structure.** Establish the total equity contribution and GP/LP split. The GP co-invest percentage (typically 1%–10% of total equity for institutional deals, sometimes higher for smaller or more relationship-driven structures) is a critical alignment signal — LPs evaluate GP skin in the game as an indicator of conviction. Express ownership percentages in the operating agreement as "membership interests" (LLC) or "limited partnership interests" (LP).

3. **Draft the major decisions list.** Major decisions are actions that require LP consent or approval beyond GP's ordinary management authority. A standard major decisions list includes: sale or refinancing of the property, encumbering the property with new debt, making capital calls beyond a specified threshold, entering into material leases (above a defined square footage or term threshold), approving annual budgets above a variance threshold, and commencing litigation. The scope of the major decisions list is one of the most intensely negotiated provisions of any JV — GPs seek a short list (maximum control), LPs seek a long list (maximum oversight).

4. **Establish GP removal provisions.** Most JVs allow LP(s) to remove the GP without cause (but with loss of promote) and for cause (with or without loss of promote, depending on the severity of the cause event). Cause events typically include fraud, material misrepresentation, gross negligence, criminal conviction, and material breach of the operating agreement uncured within a specified period. Non-cause removal typically requires either a supermajority LP vote or a single institutional LP decision right. The consequences of removal — who manages the property thereafter, whether the GP can be bought out or must sell its interest — must be specified.

5. **Establish transfer and exit provisions.** The operating agreement must address: rights of first offer or first refusal (ROFR/ROFO) if either party wants to sell its interest; drag-along rights (the majority can force a sale of the whole property/entity); tag-along rights (a selling party must give the other the right to sell alongside at the same price); and lock-up periods that restrict transfer for an initial period. These provisions govern liquidity and exit for both parties.

6. **Document waterfall economics.** Embed the full distribution waterfall in the operating agreement with sufficient precision to avoid ambiguity — including the application order of operating distributions (return of capital first or preferred return first), the compounding convention, the catch-up mechanics, and the promote tiers. See [[Waterfall Structures and Promote]] for the computation framework.

7. **Establish reporting and transparency standards.** LPs expect regular financial reporting (monthly or quarterly property-level P&L and balance sheet, annual audited financials), major decision notice rights, and access rights to property books and records. Institutional LPs often require NCREIF-compliant performance reporting and may require co-investor consent for transactions above defined thresholds.

## Outputs

- **Entity structure diagram:** visual showing the JV LLC (or LP) entity, GP entity, LP investor(s), and any feeder fund structure above the JV.
- **GP/LP ownership percentages:** legal ownership in the JV entity (distinct from economic splits due to the promote structure).
- **Governance summary:** major decisions list, removal triggers, and LP approval thresholds.
- **Term sheet / operating agreement summary:** condensed economic and governance terms suitable for LP marketing or legal counsel engagement.
- **Waterfall economics summary:** see [[Waterfall Structures and Promote]] output.

## Example Walkthrough

*(All figures are illustrative/hypothetical.)*

**Scenario:** Institutional value-add multifamily acquisition. GP is a regional operator; LP is a single family office.

- **Entity:** Delaware LLC, manager-managed (GP entity is the manager).
- **Ownership:** GP 5% / LP 95% (legal economic ownership; promote adjusts effective economics).
- **Equity:** GP contributes $500,000; LP contributes $9,500,000; total equity $10,000,000.
- **Preferred return:** 8% simple, to LP only.
- **Promote:** 80/20 LP/GP after return of LP capital and full preferred return.
- **Major decisions requiring LP consent:** sale, refinancing, new debt, budget variance >10%, leases >5 years or >2,000 SF, capital expenditures >$250,000 unbudgeted.
- **GP removal:** LP can remove GP without cause with 60-day notice, GP loses promote on future accruals but retains earned promote; removal for cause (fraud/gross negligence) results in immediate removal with forfeiture of unearned promote.
- **Transfer:** ROFR to GP on LP interest sale; drag-along after year 3 if LP wants full exit; no transfer before year 1 without GP consent.

## Limitations

JV structure design is ultimately a legal document exercise — this framework provides the analytical inputs and term sheet components, but the operative language in the operating agreement is where precision matters. Seemingly minor drafting differences in defined terms (e.g., what constitutes "stabilized" for purposes of a conversion trigger, how "cause" is defined) can create enormous disputes in a distressed scenario. Engaging experienced real estate counsel is non-negotiable for institutional JV formation.

The framework assumes a single-asset JV. Programmatic JVs (where the same GP and LP structure is applied across multiple assets under a master agreement), fund-level structures, and multi-LP club deals add substantial complexity that requires customization beyond this single-deal model.

## Related Frameworks

[[Waterfall Structures and Promote]] provides the detailed distribution computation. [[Preferred Return Mechanics]] covers the preferred return computation layer. [[GP Co-Invest and Promote Crystallization]] addresses multi-deal fund-level promote timing. [[Capital Stack Overview]] covers the debt and equity layers that surround the JV equity. [[Common Equity]] and [[Preferred Equity]] describe the equity instruments within the JV structure.
