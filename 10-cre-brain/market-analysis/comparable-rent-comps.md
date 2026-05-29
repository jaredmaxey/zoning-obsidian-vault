---
title: "Comparable Rents (Rent Comps)"
type: framework
tags: [cre/market-analysis, cre/underwriting]
created: "2026-05-24"
updated: "2026-05-24"
status: draft
ai_summary: Framework for sourcing, adjusting, and reconciling comparable lease transactions to establish achievable market rents for a subject property.
inputs_required:
  - Subject property attributes (type, size, age, quality class, floor plate, amenities)
  - Lease comparables (CoStar, CBRE/JLL deal sheets, LoopNet, broker interviews)
  - Submarket boundary (from Submarket Definition and Selection)
  - Lease structure details (gross vs. NNN, free rent, TI allowances, term)
  - Current submarket vacancy and asking rent trends (CoStar)
  - Concession market data (free rent months, TI per SF; CoStar, broker surveys)
outputs:
  - Rent comp grid with adjusted effective rents per SF or per unit per month
  - Market rent conclusion (point estimate or range) for use in pro forma
  - Concession and lease structure summary
  - Rent trend narrative for investment memo
related:
  - "Submarket Definition and Selection"
  - "Comparable Sales (Sales Comps)"
  - "Rent Roll Analysis"
  - "Net Operating Income (NOI)"
  - "Vacancy and Collection Loss"
  - "Absorption Modeling"
  - "Demand Driver Analysis"
---

# Comparable Rents (Rent Comps)

## Purpose

Comparable rent analysis establishes the market rent achievable for a subject property by examining what tenants have recently agreed to pay for similar space in the same or adjacent submarket. It is the foundational step in building a pro forma income projection: every downstream assumption — effective gross income, NOI, yield on cost, and capitalized value — flows from the market rent conclusion. For acquisitions, rent comps reveal whether a property's in-place rents are above (mark-to-market risk), at, or below (mark-to-market upside) achievable market levels. For development, rent comps provide the revenue assumption the entire feasibility analysis rests upon.

Rent comps are more nuanced than they appear because commercial leases vary widely in structure: a gross lease, a modified gross lease, and a triple-net lease for nominally the same rent produce very different economics. Multifamily rent comps must account for unit mix, amenity packages, and concession packages (months of free rent) that do not appear in headline asking rents. This framework covers both commercial (office, industrial, retail) and multifamily rent analysis, noting the methodological differences between the two. The output feeds [[Rent Roll Analysis]] for existing assets and the revenue section of any pro forma supporting [[Direct Capitalization]] or [[Discounted Cash Flow (DCF)]].

## Inputs Required

- **Subject property attributes:** Property type, rentable area (SF) or unit count and mix, year built, quality class, floor level (for office), clear height and dock doors (for industrial), frontage and anchor co-tenancy (for retail), unit size and amenity package (for multifamily).
- **Lease comparable database:** CoStar lease comps, CBRE or JLL deal sheets, LoopNet recent leases, and broker interviews for off-market or confidential deals. Target transactions executed within the prior 24 months; extend to 36 months in thin markets.
- **Submarket boundary:** From [[Submarket Definition and Selection]]; comps should be drawn from the same competitive set geography.
- **Lease structure details:** For commercial leases: lease type (gross/NNN/modified gross), base rent, term, commencement date, free rent months, tenant improvement (TI) allowance, renewal options, escalation structure. For multifamily: monthly rent by unit type, lease term, concessions (free months, waived fees), inclusion/exclusion of utilities.
- **Asking rent and vacancy data:** CoStar submarket statistics for current asking rent trends, vacancy rate, and absorption to contextualize where individual comps sit in the market cycle.
- **Concession data:** CoStar concession reports or broker surveys quantifying prevailing free rent periods and TI allowances (varies by market and vintage; current as of 2026-05-24).

## Method

1. **Define the search parameters.** Set geographic scope (submarket and immediate adjacency), property type and quality class (±1 class), size range (±30–50% of subject SF or matching unit types for multifamily), and time window (24–36 months for commercial; 12–18 months for multifamily where market moves faster).

2. **Pull and screen the raw comp set.** Export lease comps from CoStar and supplement with broker deal sheets. Screen out: related-party leases, below-market leases tied to special circumstances (government incentives, anchor deals with unusual economics), and renewal options exercised below market (these reflect contractual rights, not market evidence).

3. **Convert all rents to a common basis.** For commercial leases, convert all rents to a net effective rent basis or a gross rent basis, whichever is more common for the subject's property type and market:
   - **Net effective rent** = Base rent minus the amortized value of free rent and TI allowance over the lease term.
   - Formula (illustrative, plain text): Net Effective Rent = Base Rent − (Free Rent Months × Monthly Base Rent / Lease Term Months) − (TI Allowance / Lease Term Months × 12)
   For multifamily, express as monthly rent per unit and as $/SF/month to allow cross-unit-type comparison.

4. **Build the comp grid.** Record: property name, address, distance from subject, property type, size (SF leased or unit type), year built, quality class, lease execution date, base rent ($/SF/yr for commercial; $/month for multifamily), lease type, free rent (months), TI ($/SF), effective rent, lease term (months), and any notable lease conditions.

5. **Make qualitative adjustments.** For each comp, note differences from the subject (superior location, newer vintage, better amenities = downward adjustment; inferior = upward adjustment). Quantify where comparable transaction evidence supports specific adjustment amounts; otherwise note direction only. Document every adjustment with a stated rationale.

6. **Calculate adjusted effective rents.** Apply adjustments to each comp's effective rent to produce an adjusted rent — the rent the comp would have achieved if it were the subject property.

7. **Reconcile to a market rent conclusion.** Identify the range of adjusted effective rents. Weight the 2–3 most similar comps most heavily. State a market rent conclusion as a range (e.g., $X.XX–$X.XX NNN/SF/yr for commercial; $X,XXX–$X,XXX/month for multifamily), then reconcile to a point estimate or narrow range for pro forma use. For a new development, this is the "achievable market rent" at delivery; for an acquisition, compare to in-place rents.

8. **Document the concession market.** Separately summarize prevailing concession levels (free rent, TI) so an analyst building a pro forma can model the effective vs. face rent distinction correctly.

## Outputs

The primary output is a **rent comp grid** — a table with one row per comparable lease and columns covering all relevant metrics plus the adjusted effective rent. This supports a **market rent conclusion** — a stated range and point estimate for pro forma use, with a brief supporting narrative. A **concession summary** captures prevailing free rent and TI levels. Together these feed the revenue assumptions in any pro forma, [[Rent Roll Analysis]] for an existing asset, and the income side of [[Comparable Sales (Sales Comps)]] cap rate analysis.

## Example Walkthrough

The following numbers are illustrative and hypothetical, labeled as such throughout.

Suppose the subject is a hypothetical 25,000 SF Class B office suite in a suburban office park, built in 2001, seeking a 5-year NNN lease. The analyst pulls 7 office lease comps from the prior 24 months in the submarket. After screening, 5 are arm's-length and comparable. The raw base rents range hypothetically from $18.00 to $26.00 NNN/SF/yr. After converting to net effective rents (accounting for free rent of 2–4 months and TI allowances of $25–$45/SF across the comp set), effective rents narrow to $15.50–$22.00/SF/yr. The analyst applies downward adjustments to 2 superior comps (newer vintage, better amenity package) and upward adjustments to 1 inferior comp (older, less functional floor plate). Adjusted effective rents range hypothetically from $17.00 to $21.00/SF/yr. The analyst concludes a market effective rent of $18.00–$19.50 NNN/SF/yr for the subject, noting the subject's 2001 vintage and below-average lobby finishes justify positioning below the midpoint of the adjusted range.

## Limitations

Lease comp data is less transparent than sales comp data: many lease terms, particularly for large or institutional tenants, are confidential or only partially reported to databases. CoStar coverage is more complete for institutional-quality assets in major markets and thins significantly for secondary and tertiary markets and for smaller private transactions. Reported rents may reflect asking rents rather than executed rents, overstating market. The conversion from gross to net rent requires assumptions about operating expense levels that may not be uniformly applied across comps. For multifamily, concession packages (free rent, amenity discounts) can change rapidly in response to supply events, making trailing 12-month comps less reliable as forward indicators than current asking-rent surveys.

## Related Frameworks

[[Comparable Sales (Sales Comps)]] applies the market rent conclusion to derive a going-in cap rate via NOI capitalization. [[Rent Roll Analysis]] compares in-place rents to the market rent conclusion established here. [[Submarket Definition and Selection]] defines the geographic scope. [[Demand Driver Analysis]] and [[Vacancy and Collection Loss]] provide the occupancy and absorption context that explains why market rents are trending in a particular direction.
