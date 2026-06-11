---
title: Ground-Up Development — Key Metrics
aliases: ["Ground-Up Development — Key Metrics"]
type: asset-class
tags: [cre, asset/ground-up-development]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Defines and formulas for the eight core development metrics — yield on cost, development spread, profit margin, peak equity, LTC, cost per SF/unit, and hard-to-soft ratio — used to evaluate ground-up feasibility.
asset_class: ground-up-development
subtypes: []
related:
  - Ground-Up Development (Asset Class)
  - Ground-Up Development — Underwriting Norms
  - Ground-Up Development
  - Yield on Cost
  - Yield-on-Cost vs. Market Cap Spread
  - Development Spread
  - Loan-to-Cost (LTC)
  - Loan-to-Value (LTV)
  - Internal Rate of Return (IRR)
  - Equity Multiple
  - Net Operating Income (NOI)
  - Stabilized NOI
  - Exit Cap Rate
  - Cap Rate
  - Hard Costs
  - Soft Costs
  - Pro Forma Construction Method
  - Residual Land Value Method
  - Development Feasibility Test
  - Sensitivity Analysis
---

# Ground-Up Development — Key Metrics

## Overview

Development underwriting relies on a distinct metric set that does not have direct analogues in stabilized-asset analysis. Because the asset generates no income during the construction period, traditional acquisition metrics (going-in cap rate, DSCR, GRM) are inapplicable until stabilization. Instead, the developer tracks cost-basis and forward-looking return metrics that bridge the gap between today's capital outlay and the future stabilized value. The metrics below form the core analytical vocabulary for development feasibility.

---

### Yield on Cost (Untrended and Trended)

**Definition:** Yield on cost is the stabilized net operating income of the completed project divided by the total all-in development cost. It is the foundational development feasibility metric and the basis for the development spread calculation.

**Use:** Tests whether the project generates a sufficient return on the total capital deployed. Must exceed the prevailing exit cap rate by an acceptable margin. Untrended yield uses today's market rents; trended yield projects rents forward to the expected stabilization date.

**Formula (plain):**
```
Yield on Cost = Stabilized NOI ÷ Total Development Cost
```

**Formula (LaTeX):**
$$\text{Yield on Cost} = \frac{\text{Stabilized NOI}}{\text{Total Development Cost}}$$

Where Stabilized NOI uses market-rate occupancy (less stabilized vacancy), market rents, and normalized expenses. Total Development Cost includes land, hard costs, soft costs, financing costs, contingency, and developer fee. See [[Yield on Cost]] for the full concept note and [[Pro Forma Construction Method]] for the NOI build.

---

### Development Spread

**Definition:** Development spread is the difference between yield on cost and the prevailing exit cap rate at the time of stabilization. It quantifies the return premium the developer earns for undertaking development risk relative to simply buying a stabilized asset.

**Use:** Primary go/no-go test for institutional development. A positive spread confirms the project creates value; a spread below the minimum threshold (typically 100–200 bps for institutional capital) signals insufficient compensation for risk. Compression in development spreads is a key signal of late-cycle over-exuberance.

**Formula (plain):**
```
Development Spread = Yield on Cost − Exit Cap Rate
```

**Formula (LaTeX):**
$$\text{Development Spread} = \text{YOC} - \text{Cap Rate}_{\text{exit}}$$

See [[Development Spread]] and [[Yield-on-Cost vs. Market Cap Spread]] for detailed treatment of how spread is measured and what level is considered adequate.

---

### Profit Margin / Return on Cost

**Definition:** Profit margin (also called return on cost) is the total development profit expressed as a percentage of total development cost. Total profit is the difference between the stabilized asset value (or sale price) and the total cost to build.

**Use:** Primary return metric for merchant build-to-sell projects. Simple and intuitive; used alongside IRR for time-adjusted comparison. Typical institutional targets: 15%–25% of total cost. Does not account for time value of capital.

**Formula (plain):**
```
Profit Margin = (Stabilized Value − Total Development Cost) ÷ Total Development Cost
Stabilized Value = Stabilized NOI ÷ Exit Cap Rate
```

**Formula (LaTeX):**
$$\text{Profit Margin} = \frac{V_{\text{stabilized}} - C_{\text{total}}}{C_{\text{total}}} \quad \text{where} \quad V_{\text{stabilized}} = \frac{\text{NOI}_{\text{stabilized}}}{\text{Cap Rate}_{\text{exit}}}$$

---

### Peak Equity

**Definition:** Peak equity is the maximum amount of equity capital that is drawn during the development timeline — typically occurring near the end of construction before any income offsets carry costs. It represents the denominator for IRR and equity multiple calculations.

**Use:** Determines the actual capital at risk and the sizing of the equity commitment in the [[Joint Venture Structures|JV equity]] agreement. Higher peak equity relative to total project cost may indicate an inefficient capital structure or over-reliance on equity to fund cost overruns. Monitoring peak equity versus forecast is a key GP reporting metric.

**Formula (plain):**
```
Peak Equity = Total Development Cost − Maximum Construction Loan Balance Drawn
```

In practice, peak equity is derived from the monthly cash flow model by tracking cumulative equity contributions through the construction and lease-up period before sale or refinance proceeds are received.

---

### Loan-to-Cost (LTC)

**Definition:** Loan-to-cost is the maximum construction loan balance expressed as a percentage of total project cost. It is the primary leverage metric during the development period, analogous to [[Loan-to-Value (LTV)]] for stabilized assets.

**Use:** Determines the amount of debt a lender will advance against the project. Higher LTC means less equity required but more financial risk; lenders set LTC limits based on project type, pre-leasing, sponsor experience, and market conditions. Typical institutional range: 55%–70%. See [[Loan-to-Cost (LTC)]] for the full concept.

**Formula (plain):**
```
LTC = Maximum Loan Balance ÷ Total Development Cost
```

**Formula (LaTeX):**
$$\text{LTC} = \frac{\text{Max Loan Balance}}{C_{\text{total}}}$$

---

### Cost per Square Foot / Cost per Unit

**Definition:** Total development cost divided by the rentable square footage (for commercial/industrial) or number of units (for multifamily/residential). Provides a basis-per-unit benchmark that can be compared against comparable projects, replacement cost, and per-SF revenue assumptions.

**Use:** Benchmarking tool for identifying whether a project's cost structure is competitive. High cost-per-SF relative to achievable rents is the most common signal that a project will not pencil. Tracked separately for hard costs per SF, soft costs per SF, and land cost per SF.

**Formula (plain):**
```
Cost per SF = Total Development Cost ÷ Rentable SF
Cost per Unit = Total Development Cost ÷ Number of Units
```

**Formula (LaTeX):**
$$\text{Cost/SF} = \frac{C_{\text{total}}}{\text{RSF}} \qquad \text{Cost/Unit} = \frac{C_{\text{total}}}{\text{Units}}$$

Land cost per SF and hard cost per SF are tracked separately for benchmarking against market comparables and prior projects.

---

### Hard-to-Soft Cost Ratio

**Definition:** The proportion of total development cost (excluding land) allocated to hard costs (vertical construction, site work, utilities, FF&E) versus soft costs (architecture, engineering, permits, insurance, legal, financing, developer fees, carry costs). Expressed as a ratio (e.g., 70:30) or as a percentage of total cost (excluding land).

**Use:** Benchmarks the cost structure against comparable projects; flags potential soft-cost inflation or underestimation of hard costs. Soft costs that exceed 30–35% of total cost (excluding land) may indicate over-engineering, excessive carrying costs from delays, or developer fee structures that are out of market. Hard costs that seem too low relative to the scope may signal missing scopes or design-phase estimates that haven't been hardened. See [[Hard Costs]] and [[Soft Costs]] for component detail.

**Typical range:** Hard costs: 65%–75% of total cost (excluding land); Soft costs: 25%–35%. Varies by asset type — industrial tends toward higher hard-cost share; mixed-use and high-rise residential tend toward higher soft-cost share due to structural complexity and extended design timelines.

**Formula (plain):**
```
Hard:Soft Ratio = Hard Costs ÷ Soft Costs
```

These figures are tracked within the [[Pre-Development Budget]] and updated at each milestone from schematic design through construction closeout.
