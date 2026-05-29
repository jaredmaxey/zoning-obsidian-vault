---
title: "Comparable Sales (Sales Comps)"
type: framework
tags: [cre/market-analysis, cre/underwriting]
created: "2026-05-24"
updated: "2026-05-24"
status: draft
ai_summary: Framework for sourcing, screening, and adjusting comparable sales transactions to bracket a subject property's market value on a per-SF, per-unit, or cap rate basis.
inputs_required:
  - Subject property attributes (type, size, age, quality class, occupancy, NOI)
  - Comparable sales transactions (CoStar, MSCI/RCA, CREXI, county recorder)
  - Submarket boundary (from Submarket Definition and Selection)
  - Market cap rate trends by property type and quality tier (CoStar, MSCI/RCA, CBRE/JLL surveys)
  - Comparable property operating data (NOI, occupancy) where available
  - Time of sale and market conditions at time of sale
outputs:
  - Adjusted comparable sales grid with per-SF, per-unit, and cap rate metrics
  - Value indication range for subject property
  - Narrative reconciliation supporting a point estimate or bracketed range
  - Cap rate trend commentary for investment memo
related:
  - "Submarket Definition and Selection"
  - "Comparable Rents (Rent Comps)"
  - "Cap Rate"
  - "Going-In Cap Rate"
  - "Net Operating Income (NOI)"
  - "Price per Square Foot"
  - "Price per Unit"
  - "Direct Capitalization"
  - "Discounted Cash Flow (DCF)"
---

# Comparable Sales (Sales Comps)

## Purpose

Comparable sales analysis — commonly called "sales comps" — is the market evidence framework for estimating what a subject property would likely sell for in arm's-length conditions today. It is the CRE equivalent of the sales comparison approach in appraisal methodology, adapted for the analyst's underwriting workflow. The analyst searches for recent, similar transactions and uses them to bracket the subject's likely pricing on a per-square-foot (PSF), per-unit, or going-in cap rate basis, making qualitative and quantitative adjustments for differences in location, age, quality, occupancy, and market timing. The result anchors the acquisition price, calibrates the exit cap rate assumption in a DCF, or supports a developer's land residual calculation.

Sales comps are essential in every acquisition underwrite: they establish whether the asking price is at, above, or below where the market is actually clearing for similar assets. Analysts also return to comps at hold periods and refinancing events to benchmark current market pricing. The framework works in tandem with [[Comparable Rents (Rent Comps)]] — rent comps establish the income side, while sales comps establish the pricing multiple the market applies to that income. Together they support [[Direct Capitalization]] and [[Discounted Cash Flow (DCF)]] exit assumptions.

## Inputs Required

- **Subject property attributes:** From CoStar or county assessor: property type, rentable square footage or unit count, year built, quality class, current occupancy, in-place NOI or estimated NOI.
- **Comparable transaction database:** CoStar Comps, MSCI/RCA Analytics, CREXI transaction history, or county recorder deed/transfer records. Ideally pull transactions from the prior 24–36 months; extend to 48 months in illiquid markets or when the submarket has seen few trades.
- **Submarket boundary:** From [[Submarket Definition and Selection]]; sales should be sourced from within or immediately adjacent to the defined submarket.
- **Market cap rate surveys:** CBRE Cap Rate Survey, JLL Capital Markets reports, CoStar cap rate trend data by property type and tier — used to calibrate time adjustments and assess where the subject's implied cap rate sits relative to the market.
- **Transaction details:** Sales price, buyer/seller identity (flag portfolio or entity sales as potentially non-arm's-length), confirmed cap rate or NOI at sale, allocated price PSF or per unit, financing terms (all-cash vs. assumed debt).

## Method

1. **Define the search parameters.** Set geographic scope (submarket plus reasonable adjacency), property type, quality class (±1 class from the subject), size range (typically ±30–50% of the subject's SF or unit count), and time window (24–36 months preferred; note that older comps will require time adjustments).

2. **Pull the raw comp set.** Search CoStar Comps and RCA/MSCI for sales meeting the criteria. Cross-check with county recorder data for any sales not in commercial databases (common for smaller private transactions). Target 5–10 transactions for a focused submarket; extend to 15+ if the submarket is thin.

3. **Screen for arm's-length conditions.** Exclude: distressed/foreclosure sales, portfolio sales where individual prices are allocated, related-party transactions, and sales with unusual financing (seller carry at below-market rates). Flag but do not automatically exclude partial-interest or JV recapitalization sales.

4. **Build the comp grid.** For each comparable, record: address, property type, size (SF or units), year built, quality class, sale date, sale price, price PSF or per unit, occupancy at sale, confirmed NOI at sale (if available), and implied cap rate (NOI ÷ Sale Price). Calculate each metric for the subject's asking price as well.

5. **Make time adjustments.** If market conditions have materially changed since the sale date, apply a time adjustment. Use a percentage-per-year shift derived from market cap rate trends or price index data (CoStar CPPI, MSCI/RCA CPPI; varies by market and vintage; current as of 2026-05-24). State the basis for the adjustment in a footnote.

6. **Make qualitative adjustments.** For each comp, note how it differs from the subject on quality, location, occupancy, and functional features, and apply directional adjustments (superior comp = downward adjustment to indicate subject is worth less; inferior comp = upward adjustment). For institutional-quality analysis, quantify adjustments; for preliminary screening, directional notation suffices.

7. **Calculate the indicated value range.** After adjustments, identify the high and low of the adjusted comp set on each metric (PSF, per unit, cap rate). The subject's value indication falls within this range, refined by the analyst's weighting of the most comparable transactions.

8. **Reconcile and state the conclusion.** Write 2–3 paragraphs reconciling the comp evidence and stating a supported value range (or point estimate if the comp evidence is tight). Identify the 2–3 comps that are most similar and weight them most heavily.

## Outputs

The primary output is an **adjusted comparable sales grid** — typically a spreadsheet or table with 5–15 rows (one per comp) and columns for all relevant metrics plus adjustments. This supports a **value indication range** stated as a PSF range, per-unit range, and/or cap rate range. The **narrative reconciliation** (2–3 paragraphs) explains which comps are most relevant and why. In an investment memo, this section typically appears as a 1–2 page "Market Pricing" section supporting the acquisition price or exit assumption.

## Example Walkthrough

The following numbers are illustrative and hypothetical, labeled as such throughout.

Suppose the subject is a hypothetical 120-unit Class B multifamily community built in 2005 in a mid-size Sun Belt metro, 92% occupied, with an estimated in-place NOI of $1.1M. The analyst pulls 8 comparable multifamily sales from the prior 30 months in the same submarket. After screening, 6 pass the arm's-length test. The raw comp grid shows prices ranging hypothetically from $130,000 to $175,000 per unit, with implied cap rates of 4.5%–5.8% (varies by market and vintage; current as of 2026-05-24). The analyst applies a modest downward time adjustment to the 2024 trades (market was stronger then), adds upward adjustments for two comps that were superior in quality, and downward adjustments for two comps that were newer. After adjustment, the indicated value range narrows to hypothetically $145,000–$165,000 per unit, implying a value of $17.4M–$19.8M. The analyst reconciles toward the midpoint ($18.6M) given the subject's below-average quality relative to the comp set, resulting in a going-in cap rate of approximately 5.1%–5.9%.

## Limitations

Sales comp analysis is only as good as the quality and quantity of available transaction data. In illiquid markets, thin comp sets force analysts to rely on older sales or geographically distant comps, both of which require larger and more speculative adjustments. Private transactions (seller carry, portfolio deals) may be excluded from databases or may close at non-market pricing. Cap rate adjustments between properties with different occupancy levels are particularly sensitive to NOI normalization assumptions — two analysts applying different stabilized vacancy assumptions will reach different implied cap rates. The framework assumes comparable assets are liquid and trade frequently; for specialty or niche property types, comparable sales may be rare or geographically dispersed enough that PSF or per-unit benchmarks have limited reliability.

## Related Frameworks

[[Comparable Rents (Rent Comps)]] establishes the income side that investors capitalize when bidding on assets. [[Submarket Definition and Selection]] defines the geographic scope. [[Direct Capitalization]] and [[Discounted Cash Flow (DCF)]] are the underwriting methods that rely on cap rate evidence derived from sales comps. The concepts of [[Cap Rate]], [[Going-In Cap Rate]], [[Price per Square Foot]], [[Price per Unit]], and [[Net Operating Income (NOI)]] are the metrics measured and compared in this framework.
