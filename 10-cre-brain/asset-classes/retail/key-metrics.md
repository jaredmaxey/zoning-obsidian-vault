---
title: Retail — Key Metrics
type: asset-class
tags: [cre, asset/retail]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Definitions, formulas, and interpretive context for the six primary retail-specific operating metrics — sales per SF, occupancy cost ratio, percentage rent breakpoint, NNN recovery ratio, traffic/footfall, and co-tenancy thresholds.
asset_class: retail
subtypes: []
related:
  - Retail
  - Retail — Underwriting Norms
  - Net Operating Income (NOI)
  - Effective Gross Income (EGI)
  - Vacancy and Collection Loss
  - Cap Rate
  - Going-In Cap Rate
  - Trade Area Analysis (Retail)
  - Traffic Counts and Visibility
  - Rent Roll Analysis
  - Comparable Rents (Rent Comps)
  - Comparable Sales (Sales Comps)
  - Sensitivity Analysis
---

# Retail — Key Metrics

Retail real estate uses a set of operating and financial metrics that differ meaningfully from other asset classes. These metrics reflect the unique characteristics of retail: tenant performance is directly observable through sales reporting, occupancy cost sustainability is testable against revenue, and landlord income is partially variable through percentage rent. Each metric below is defined, placed in context, and accompanied by a formula where applicable.

### Sales per Square Foot

**Definition.** Sales per SF (also written $/SF) measures a retail tenant's gross sales volume normalized to occupied gross leasable area (GLA). It is the most fundamental measure of tenant health and the primary driver of whether a retail location is sustainable, at risk, or a candidate for backfill.

**Use.** Sales per SF is used in three contexts: (1) evaluating individual tenant lease sustainability — lower sales per SF relative to industry benchmarks signals potential closure risk; (2) calculating the occupancy cost ratio (see below); (3) determining when percentage rent overage is triggered. Landlords typically require tenants to report annual gross sales; institutional leases often require quarterly or monthly reporting.

**Benchmarks.** Industry benchmarks vary widely by retail category and center quality. Grocery anchors typically report $500–$800+ PSF; discount/dollar stores $150–$250 PSF; pharmacy $400–$700 PSF; QSR/fast-casual $350–$700 PSF; soft-goods inline $200–$500 PSF for healthy tenants. These are general ranges — compare to the specific tenant's portfolio average and the center's competitive context.

**Formula (plain).** Sales per SF = Annual Gross Sales / Occupied SF

**Formula (LaTeX).**
$$\text{Sales per SF} = \frac{\text{Annual Gross Sales}}{\text{Occupied GLA (SF)}}$$

### Occupancy Cost Ratio (OCR)

**Definition.** The occupancy cost ratio — sometimes called the "health ratio" or "rent-to-sales ratio" — measures total occupancy cost (base rent plus NNN recovery charges) as a percentage of the tenant's gross annual sales. It is the single most important indicator of whether a tenant can sustain its rent obligation and whether the lease is economically viable for the retailer.

**Use.** Underwriters use OCR in two ways: (1) assessing existing tenant lease health — a persistently high OCR signals that a tenant is paying more in occupancy cost than its business model can support, raising renewal risk; (2) setting new lease rent levels — when negotiating a new lease or renewal, landlords target an OCR that leaves the tenant healthy enough to operate long-term. An OCR above the tenant's historical tolerance threshold is a leading indicator of default or non-renewal. Institutional investors stress-test portfolios by identifying tenants with OCRs above sector norms and modeling the renewal-at-lower-rent or vacancy scenario.

**Healthy OCR ranges by category.** Grocery anchors: 1%–3%; pharmacy: 2%–5%; QSR/fast-casual: 8%–12%; soft-goods fashion: 10%–15%; jewelry/accessories: 10%–18%; restaurants (full service): 6%–10%. These are indicative ranges — individual tenants and formats vary.

**Formula (plain).** OCR = Total Annual Occupancy Cost / Annual Gross Sales × 100

**Formula (LaTeX).**
$$\text{OCR} = \frac{\text{Total Annual Occupancy Cost}}{\text{Annual Gross Sales}} \times 100$$

Where Total Annual Occupancy Cost = Base Rent + NNN Charges (CAM + Insurance + Taxes).

### Percentage Rent Breakpoint

**Definition.** The percentage rent breakpoint is the sales volume at which a tenant's percentage rent obligation begins. Below the breakpoint, the tenant pays only base rent. Above it, the tenant pays an additional rent equal to a stated percentage of sales exceeding the threshold. The "natural breakpoint" is calculated by dividing base rent by the percentage rate; a "negotiated breakpoint" may be set above the natural breakpoint as a concession.

**Use.** Breakpoints matter in underwriting when projecting total revenue. Underwriters model tenant-level sales forecasts and assess how much, if any, of a portfolio is likely to generate overage rent. For high-performing tenants (grocery, QSR, pharmacy) with strong sales per SF, percentage rent can be a meaningful NOI component. For below-average tenants, the percentage rent breakpoint may never be reached, and overage is not a realistic cash flow projection.

**Formula (plain — natural breakpoint).** Natural Breakpoint = Base Rent / Percentage Rate

**Formula (LaTeX).**
$$\text{Natural Breakpoint} = \frac{\text{Annual Base Rent}}{\text{Percentage Rate}}$$

**Example.** A tenant paying $60,000/year in base rent at a 6% rate has a natural breakpoint of $1,000,000. If sales total $1,300,000, percentage rent = ($1,300,000 – $1,000,000) × 6% = $18,000.

### NNN Recovery Ratio

**Definition.** The NNN recovery ratio measures the share of total operating expenses (real estate taxes, insurance, CAM) recovered from tenants as reimbursements, expressed as a percentage of total operating expenses. A 100% recovery ratio means the property operates at zero net operating expense for the landlord; a ratio below 100% means the landlord is absorbing a portion of operating costs.

**Use.** Recovery ratio is a key driver of NNN-adjusted NOI. When analyzing a retail center's income, gross revenue less vacancy equals [[Effective Gross Income (EGI)]]; subtracting unrecovered operating expenses yields NOI. A center with high vacancy has lower recovery ratios because vacant space generates no reimbursements — making the recovery ratio a function of occupancy as well as lease structure. Anchor tenants often carry below-proportional recovery obligations (or fixed recovery caps), which effectively transfers a share of occupancy cost to inline tenants or the landlord.

**Formula (plain).** NNN Recovery Ratio = Total Tenant Reimbursements / Total Operating Expenses × 100

**Formula (LaTeX).**
$$\text{NNN Recovery Ratio} = \frac{\text{Total Tenant Reimbursements}}{\text{Total Operating Expenses}} \times 100$$

**Typical ranges.** 85%–100% for well-occupied NNN centers; 70%–85% for centers with anchor tenants on below-proportional recovery; 60%–80% for centers with meaningful vacancy dragging down reimbursements.

### Traffic / Footfall Counts

**Definition.** Traffic counts measure the volume of vehicles or pedestrians passing a retail location — typically reported as average daily or annual vehicle counts (ADT) at access points for auto-oriented retail, or as pedestrian counts for urban or transit-adjacent locations. Footfall specifically refers to consumer counts entering a mall, center, or store, measured by sensor systems.

**Use.** Traffic counts are a critical input in [[Trade Area Analysis (Retail)]] and [[Traffic Counts and Visibility]] analysis. In retail site underwriting, minimum traffic thresholds are non-negotiable for most tenant categories: QSR and convenience retail typically require 20,000–50,000+ ADT on primary frontage; big-box and power center anchors require major arterial or freeway proximity. In existing property analysis, year-over-year footfall trends are a leading indicator of center health — declining footfall often precedes tenant closure decisions and NOI deterioration. Mall operators (Simon, Brookfield) track footfall extensively as a performance metric.

**No single universal formula** — traffic counts are typically obtained from state DOT counts, third-party data providers (Placer.ai, CoStar), or commissioned traffic studies for development projects.

### Co-Tenancy Thresholds

**Definition.** Co-tenancy thresholds are lease provisions that specify minimum occupancy or tenancy conditions under which a tenant's rent obligation is modified or terminated. Two types are common: (1) anchor co-tenancy — the tenant's rent is reduced (typically to a percentage-of-sales basis) or the tenant may terminate if a named anchor vacates; (2) center occupancy co-tenancy — the tenant's rent is reduced if center occupancy falls below a stated percentage (commonly 75%–85% of total GLA).

**Use.** Co-tenancy provisions are material risk items that must be inventoried for every multi-tenant retail center underwriting. The key underwriting tasks are: (1) identify all tenants with co-tenancy provisions and the triggering conditions; (2) estimate the financial impact under each scenario — how many tenants flip to percentage-of-sales rent, and what is the resulting NOI floor; (3) assess the probability of trigger events based on anchor lease terms and center occupancy trajectory. Co-tenancy cascades — where one anchor departure triggers multiple inline rent reductions, further reducing center occupancy and triggering additional co-tenancy provisions — are the mechanism by which an anchor closure can impair NOI by 25%–50% or more in a short period.

**Formula (NOI impact estimate — plain).** Co-Tenancy NOI Impact = Sum over affected tenants of (Base Rent − Sales-Only Rent) × Probability of Trigger

This is modeled tenant by tenant in a [[Sensitivity Analysis]] or stress test rather than as a single-formula calculation; see [[Stress Testing]] for methodology.
