---
title: "Site Selection Scorecard"
aliases: ["Site Selection Scorecard"]
type: framework
tags: [cre/frameworks]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Weighted multi-criteria scoring tool for ranking and comparing candidate sites across location, physical, market, and financial criteria before detailed underwriting.
inputs_required:
  - List of candidate sites with addresses and basic characteristics
  - Defined scoring criteria and weights (per asset class and strategy)
  - Demographic and demand driver data for each site's trade area
  - Zoning and entitlement status for each site
  - Comparable sales data for land pricing context
  - Access, visibility, and infrastructure assessments
outputs:
  - Weighted score for each candidate site
  - Ranked comparison matrix
  - Go/no-go recommendation for detailed underwriting
related:
  - "Highest and Best Use Analysis"
  - "Porter Five Forces Applied to CRE"
  - "Development Feasibility Test"
  - "Residual Land Value Feasibility"
  - "Submarket Definition and Selection"
  - "Demographic Analysis"
  - "Employment and Jobs Analysis"
  - "Trade Area Analysis (Retail)"
  - "Demand Driver Analysis"
  - "Zone Change (Rezoning)"
  - "Conditional Use Permit (CUP)"
  - "Ground-Up Development"
  - "Build-to-Suit"
  - "Land Banking"
---

# Site Selection Scorecard

## Purpose

The Site Selection Scorecard is a structured, weighted multi-criteria analysis tool used in the early stages of site acquisition to compare and rank candidate parcels before committing to detailed underwriting. By translating qualitative and semi-quantitative site attributes into a common numeric score, the scorecard enables an objective comparison of sites that may differ along many dimensions — location quality, physical constraints, entitlement risk, and financial attractiveness — preventing the cognitive bias of defaulting to the most familiar or most recently visited site.

The framework is particularly valuable when a developer or investor is simultaneously evaluating three or more sites for the same project type, or when an investment committee requires a documented justification for proceeding with one site over alternatives. The scorecard is not a substitute for detailed underwriting: it is a filter that surfaces the best one or two candidates for the [[Development Feasibility Test]] and [[Residual Land Value Feasibility]] frameworks. Different asset classes require different criterion weights — a retail site weights traffic counts and trade-area demographics heavily, while an industrial site emphasizes truck access, clear height availability, and labor shed proximity.

## Inputs Required

- **Site list:** candidate parcels with addresses, APN, owner, gross area, current use, asking price if known.
- **Zoning and entitlement:** current zoning classification, permitted uses, any pending applications; whether the intended use is by-right or requires entitlement action. Source: jurisdiction notes per [[Zone Change (Rezoning)]], [[Conditional Use Permit (CUP)]].
- **Demographic data:** population, household count, median HHI, age distribution within 1-, 3-, and 5-mile rings; from [[Demographic Analysis]].
- **Employment data:** job count and growth by sector within the labor shed; from [[Employment and Jobs Analysis]].
- **Traffic and access:** average daily traffic (ADT) counts, proximity to freeway interchange, rail, port, or airport (varies by asset class); from state DOT or broker reports.
- **Physical characteristics:** size, shape, topography, utility availability, flood zone status, soil conditions.
- **Market data:** submarket vacancy, absorption, and rent for the intended use; from [[Comparable Rents (Rent Comps)]] and [[Comparable Sales (Sales Comps)]].
- **Land pricing:** asking price or broker estimate per SF/acre; comparable land sales.

## Method

1. **Define criteria and categories.** Group scoring criteria into four standard categories. Suggested default criteria (customize per asset class and strategy):

   | Category | Sample Criteria | Weight Range |
   |---|---|---|
   | Location & Access | Visibility, traffic/ADT, proximity to demand generators, freeway access | 25–40% |
   | Physical | Size/shape adequacy, topography, utilities, flood/environmental | 15–25% |
   | Market & Demand | Submarket vacancy, rent growth, trade-area demographics, employment | 25–35% |
   | Financial & Entitlement | Land pricing vs. residual, entitlement risk, timeline to permits | 15–25% |

   Total weights must sum to 100%. Adjust weights based on asset class (retail: heavier on Location; industrial: heavier on Physical access; multifamily: heavier on Market & Demand).

2. **Assign criterion weights.** Within each category, distribute the category's total weight across individual criteria. Example (retail, illustrative): Location = 35% total, broken into Visibility (15%), Traffic/ADT (12%), Proximity to anchor (8%).

3. **Define the scoring scale.** Use a consistent 1–5 or 1–10 integer scale for every criterion. Document what each score means before scoring, to ensure consistency across sites and analysts. Example (1–5): 5 = best available in the market, 4 = above average, 3 = market-average, 2 = below average, 1 = disqualifying deficiency.

4. **Score each site against each criterion.** One analyst (or two independently for calibration) scores each candidate site on each criterion. Use available data; where data is insufficient, note the gap and score conservatively. Document the rationale for scores at the extremes (1 or 5).

5. **Calculate weighted scores.** For each site:
   - `Weighted Score = Σ (criterion weight × criterion score)`
   - A perfect 5 on all criteria would yield a weighted score of 5.0 (or 10.0 on a 10-point scale). A useful rough interpretation (1–5 scale): ≥4.0 = strong candidate, 3.0–3.9 = acceptable with identified mitigants, <3.0 = generally not recommended without significant upside driver.
   
   $$\text{Site Score} = \sum_{i=1}^{n} w_i \times s_i$$
   
   where $w_i$ = weight of criterion $i$ and $s_i$ = score (1–5) for criterion $i$, with $\sum w_i = 1$.

6. **Flag knockout criteria.** Certain criteria should be treated as knockouts regardless of overall score: active environmental contamination without a clear remediation path, zoning that cannot legally permit the use even with full entitlement effort, or flood zone AE/AO without flood insurance feasibility. A site that fails a knockout criterion is removed from the matrix regardless of its weighted score.

7. **Rank and compare.** Present the results in a comparison matrix table showing site name, score by category, overall weighted score, and top strength and top risk. Recommend the top one or two sites for detailed [[Development Feasibility Test]] underwriting.

8. **Document assumptions and data gaps.** Note where scores were based on limited data and identify verification steps needed. Sites with multiple "estimated" scores should be flagged for additional diligence before final selection.

## Outputs

- A weighted-score comparison matrix for all candidate sites, ranked highest to lowest.
- Knockout flags for disqualified sites with stated reasons.
- A tiered recommendation: Site A → proceed to detailed underwriting; Site B → backup if Site A falls through; Sites C, D → do not proceed.
- A data-gap log identifying what additional information is needed before committing to a site.

## Example Walkthrough

*All figures below are illustrative/hypothetical.*

A retail developer is evaluating three sites for a 15,000 SF neighborhood retail center in a growing suburban corridor. The scorecard uses a 1–5 scale with the following weights (illustrative):

| Criterion | Weight | Site 1 | Site 2 | Site 3 |
|---|---|---|---|---|
| Visibility from arterial | 15% | 5 | 3 | 4 |
| Traffic (ADT) | 12% | 4 | 5 | 3 |
| Proximity to anchor (grocery) | 8% | 5 | 2 | 3 |
| Trade area demographics (3-mi HHI) | 10% | 4 | 4 | 3 |
| Submarket vacancy | 10% | 4 | 3 | 4 |
| Site size adequacy | 8% | 4 | 5 | 3 |
| Topography / utilities | 7% | 3 | 4 | 5 |
| Flood zone / environmental | 8% | 5 | 4 | 3 |
| Land price vs. residual | 12% | 3 | 4 | 3 |
| Entitlement risk | 10% | 4 | 3 | 5 |
| **Weighted Score** | 100% | **4.04** | **3.65** | **3.52** |

Site 1 scores highest at 4.04 (illustrative). It excels on visibility, anchor proximity, and environmental cleanliness, and its entitlement path is straightforward (by-right C-2 zoning). Its weaker scores are land pricing (asking price is at the high end of residual) and topography (requires 4 feet of fill, estimated $200K in additional site work).

**Recommendation:** Advance Site 1 to [[Development Feasibility Test]] and [[Residual Land Value Feasibility]] underwriting. Commission a Phase I ESA and survey to verify the environmental and topography scores. Site 2 is backup if Site 1 LOI negotiations fail.

## Limitations

The scorecard produces an objective-looking output from inherently subjective inputs. Score assignment is vulnerable to anchoring (the first site evaluated sets the scale) and confirmation bias (analysts favor sites management has already expressed preference for). Requiring independent scoring by two analysts and documenting score rationale at every step mitigates but does not eliminate this risk.

Criterion weights are strategic choices that embed assumptions about what drives value for the intended use. Using retail weights for an industrial analysis — or using a prior project's scorecard without recalibration — will produce misleading results. Weights should be reset for each project type and reviewed by an investment committee before scoring begins.

The scorecard evaluates sites as of the scoring date. Market conditions, asking prices, and entitlement status can change rapidly. A site scored three months ago during earlier diligence may need to be rescored if material conditions have changed.

## Related Frameworks

- [[Highest and Best Use Analysis]] — the next step after site selection; determines the optimal use for the selected site.
- [[Development Feasibility Test]] — the detailed financial feasibility check run on the selected site.
- [[Residual Land Value Feasibility]] — quantifies the maximum land price supportable given the intended use.
- [[Porter Five Forces Applied to CRE]] — structural market analysis that informs the Market & Demand category scores.
- [[Trade Area Analysis (Retail)]] — essential for scoring trade-area criteria for retail sites.
- [[Demographic Analysis]] — primary data source for trade-area demographic criteria.
