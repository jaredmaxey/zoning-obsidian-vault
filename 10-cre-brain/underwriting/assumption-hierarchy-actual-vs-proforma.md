---
title: "Assumption Hierarchy: Actual vs. Pro Forma"
aliases: ["Assumption Hierarchy: Actual vs. Pro Forma"]
type: concept
tags: [cre/underwriting]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: The principle governing when to rely on actual operating history versus pro forma projections in CRE underwriting, with a defined hierarchy of evidence credibility.
domain: underwriting
formula: false
related:
  - "Pro Forma Construction Method"
  - "Rent Roll Analysis"
  - "Expense Normalization"
  - "T-12 and T-3 Analysis"
  - "Sensitivity Analysis"
  - "Stress Testing"
  - "Net Operating Income (NOI)"
  - "Stabilized NOI"
  - "Going-In Cap Rate"
---

# Assumption Hierarchy: Actual vs. Pro Forma

## Definition

The assumption hierarchy in CRE underwriting is the discipline of assigning relative credibility to different types of evidence when building the underwriting model — and specifically, the question of how much weight to give demonstrated operating history (actuals) versus projected future performance (pro forma). The core principle is: actual, verified, in-place performance is more credible than projected performance and should serve as the underwriting anchor wherever it exists. Pro forma assumptions should only override actuals when there is a clear, articulable reason that past performance is not representative of forward performance — and that reason must be explicitly documented.

This hierarchy exists because CRE sellers, brokers, and developers naturally present their properties in the most favorable light. A seller's pro forma for a value-add acquisition shows the property after renovations, at market rents, with market vacancy — all of which are future events, not current reality. A buyer who pays based on that projected stabilized value has paid for execution risk that may or may not materialize. Institutional buyers apply the assumption hierarchy as a discipline to distinguish what the property demonstrably does from what it could theoretically do, and to price execution risk appropriately.

In practice, the hierarchy operates across four tiers of evidence: (1) verified actuals — T-12/T-3 operating statements reconciled against bank statements and rent rolls, representing the highest-confidence baseline; (2) in-place rent roll — current lease obligations that are legal contracts, not projections; (3) market-supported benchmarks — comparable rents, market vacancy rates, and expense ratios derived from third-party data for comparable properties in the same submarket; and (4) seller pro forma — the projected, fully-stabilized income statement presented by the seller or broker, representing the lowest-confidence tier. The analyst builds up from the bottom of this hierarchy: start with actuals, layer in market data to normalize for items that actuals can't reflect (e.g., post-sale tax reassessment), and explicitly identify where and why any element of the seller's pro forma is being accepted or rejected.

## When It's Used

The assumption hierarchy is the implicit framework every institutional underwriter applies when diligencing an acquisition or refinance. It becomes an explicit framework when there is a significant gap between the seller's underwrite and the buyer's underwrite — which is almost always. The gap analysis (seller's NOI vs. buyer's underwritten NOI) should be documented line by line, with each line item classified by which tier of evidence governs it in the buyer's model.

The hierarchy is particularly critical in value-add transactions, where the seller's underwrite is inherently pro forma (showing the stabilized future state), but the buyer is paying a price today, with execution risk sitting entirely on the buyer's side. In a [[Value-Add Acquisition]], the underwriter must explicitly bifurcate the current-state, verified-actuals NOI from the stabilized pro forma NOI, build a credible bridge between them (renovation budget, lease-up timeline, market rent achievement), and quantify the risk that the bridge scenario underperforms. The amount of premium the buyer pays for pro forma NOI (vs. current-state NOI) is essentially the price paid for that execution risk.

For development underwriting ([[Ground-Up Development]]), there are no actuals — the hierarchy collapses to market-supported benchmarks and developer assumptions. In this case, every assumption should be cross-referenced against comparable properties in the market (rental comparables, expense ratios for similar buildings, cap rates for comparable stabilized assets) and marked as a projection with explicit uncertainty ranges per [[Sensitivity Analysis]].

## Variations & Edge Cases

The hierarchy becomes more complex in several situations. For a fully leased NNN property with long-term investment-grade tenants, the in-place lease rent is a highly reliable income assumption — the hierarchy elevates the lease contract above the actuals because there is effectively no rollover risk during the lease term. For a property with chronic collection issues (actuals show rent rolls that are never fully collected), the actuals are informative about the downside but may not be the appropriate forward assumption if management will be replaced. Seasonality, as in hospitality, means a 3-month T-3 during the off-season should not be used as the annualized run rate.

One common source of tension is the use of "underwritten" or "pro forma" expenses at the analyst's own firm, where the analyst is not using actuals at all but is building to market benchmarks — common for development or when operating history is unavailable. In this case, the benchmarks themselves must be rigorous: sourced from [[Comparable Rents (Rent Comps)]], operating expense surveys, and local market data, not from the analyst's intuition or the seller's presentation.

## Common Mistakes

The most dangerous mistake is accepting the seller's pro forma NOI as the underwriting anchor — paying for projected stabilization without applying a haircut for execution risk. A less visible but equally damaging error is the reverse: being so skeptical of actuals that the analyst uses an overly conservative market-benchmark assumption when strong actuals would support a more aggressive income projection. Both errors produce a model that does not reflect reality.

A third common mistake is inconsistency: using actuals for income (because they are high) and pro forma for expenses (because they show a lean cost structure), without recognizing that the two were produced under different conditions. If actuals show high income because the property was managed exceptionally well during a peak period, the same quality of management may also explain the below-market expense ratio — and both should be treated as potentially non-repeatable for a new buyer.

## Related Concepts

[[T-12 and T-3 Analysis]] — the process for reviewing and validating actuals. [[Expense Normalization]] — the process for adjusting actuals to a sustainable baseline. [[Rent Roll Analysis]] — provides the in-place lease data (Tier 2). [[Pro Forma Construction Method]] — the framework in which assumption hierarchy decisions are executed. [[Stabilized NOI]] — the output the hierarchy is trying to produce credibly. [[Sensitivity Analysis]] — tests the return impact of assumption hierarchy choices.

## Sources

CCIM Institute, *Financial Analysis for Commercial Investment Real Estate* (CI 102). Urban Land Institute, *Real Estate Finance Basics*. Institutional underwriting practice in REPE due diligence.
