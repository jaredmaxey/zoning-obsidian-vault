---
title: "Monte Carlo in CRE"
aliases: ["Monte Carlo in CRE"]
type: framework
tags: [cre/underwriting, cre/frameworks]
created: 2026-05-24
updated: 2026-05-24
status: draft
ai_summary: Probabilistic simulation method that runs thousands of pro forma iterations with randomized inputs to produce a return distribution and quantify the probability of achieving target outcomes.
inputs_required:
  - Base-case pro forma with all key assumptions identified
  - Probability distributions for each key variable (mean, standard deviation, distribution type)
  - Correlation matrix between variables (if applicable)
  - Minimum acceptable return hurdle
outputs:
  - Return distribution (IRR, equity multiple) across all simulations
  - Probability of exceeding target return hurdle
  - Probability of equity loss (equity multiple < 1.0×)
  - 5th/10th/50th/90th/95th percentile IRR and equity multiple
related:
  - "Sensitivity Analysis"
  - "Stress Testing"
  - "Pro Forma Construction Method"
  - "Internal Rate of Return (IRR)"
  - "Equity Multiple"
  - "Exit Cap Rate"
  - "Discount Rate"
---

# Monte Carlo in CRE

## Purpose

Monte Carlo simulation is a probabilistic analytical technique that replaces fixed-point assumptions in a CRE pro forma with probability distributions, then runs thousands of randomized iterations to produce a full distribution of possible outcomes. Where [[Sensitivity Analysis]] shows how returns change when specific variables change, and [[Stress Testing]] applies named adverse scenarios, Monte Carlo simulation answers a more complete question: given realistic uncertainty in all key inputs simultaneously, what is the probability of achieving the target return, what does the full distribution of outcomes look like, and what is the tail risk (probability of loss)?

Institutional real estate fund managers, public pension fund consultants, and sophisticated family office underwriters use Monte Carlo to move beyond single-point base-case projections that can obscure genuine outcome uncertainty. A deal that shows a 15% IRR in the base case but has a 40% probability of delivering less than 10% IRR — because it depends heavily on an uncertain exit cap rate assumption — may not merit the same capital allocation as a deal with a 13% base-case IRR but a much tighter distribution. Monte Carlo makes this distinction visible.

## Inputs Required

- **Base-case pro forma:** Fully built per [[Pro Forma Construction Method]], with all assumptions explicit and accessible as model inputs.
- **Variable distributions:** For each key variable, specify: (a) distribution type (normal, log-normal, triangular, uniform); (b) central tendency (mean or mode); and (c) dispersion (standard deviation, min/max, or 10th/90th percentile). Key variables typically include: annual rent growth rate, vacancy rate, exit cap rate, operating expense growth rate, lease-up timing (months), and interest rate at refinance. These should be calibrated to market data, historical volatility, and analyst judgment — not invented arbitrarily.
- **Correlation structure:** Cap rates and rent growth are negatively correlated (both decline in downturns, move together in expansions). Rent growth and vacancy are negatively correlated. Specifying a correlation matrix prevents the simulation from generating unrealistic combinations (e.g., rent growth of 5% paired with vacancy of 25%) that inflate the apparent upside.
- **Number of iterations:** Typically 5,000–20,000 for stable convergence; 1,000 minimum.
- **Return hurdle:** The minimum IRR or equity multiple the fund or investment strategy requires.

## Method

1. **Identify and parameterize the 3–7 highest-impact variables.** Start from the [[Sensitivity Analysis]] tornado chart — Monte Carlo adds the most value for variables that both drive high return impact and carry high uncertainty. Assign a distribution to each. For cap rates, a normal distribution around the base-case assumption with a standard deviation of 25–75 basis points is a common starting point (calibrated to historical market volatility; varies by market and vintage as of 2026-05-24).

2. **Build or link the simulation engine.** In Excel, this is typically implemented using add-in tools such as @Risk or Crystal Ball. In Python, the NumPy/SciPy random sampling functions are used. The engine samples each input independently from its distribution (and respects the correlation matrix if specified) for each iteration.

3. **Run the simulation.** For each iteration: (a) draw a random value for each variable from its distribution; (b) compute the full pro forma cash flows; (c) calculate the target return metrics (IRR, equity multiple). Store each iteration's output. Repeat for the specified number of iterations.

4. **Analyze the output distribution.** Sort all iteration outcomes and compute: (a) mean and median IRR; (b) 5th, 10th, 25th, 75th, 90th, 95th percentile IRRs; (c) percentage of iterations meeting or exceeding the return hurdle; (d) percentage of iterations where equity multiple < 1.0× (probability of loss). Plot a histogram and cumulative distribution function (CDF) of outcomes.

5. **Report results.** Present the output distribution alongside the base-case and a description of the variable assumptions. A typical output table:

   | Metric | P5 | P25 | P50 | P75 | P95 |
   |---|---|---|---|---|---|
   | Levered IRR | 4.2% | 9.1% | 13.8% | 18.9% | 26.4% |
   | Equity Multiple | 1.12× | 1.42× | 1.78× | 2.18× | 2.89× |

   Include: P(IRR ≥ hurdle) and P(Equity Multiple < 1.0×).

6. **Interpret results in the investment committee context.** The distribution informs position sizing, leverage level, and risk appetite. A deal with a median IRR of 14% but a 25% probability of loss should be sized differently from one with a median IRR of 12% and a 2% probability of loss.

## Outputs

Monte Carlo simulation produces: (1) a return distribution (histogram and CDF) for IRR and equity multiple; (2) percentile returns (P5 through P95); (3) probability of meeting the target return hurdle; (4) probability of capital loss; and (5) a sensitivity-ranked contribution of each variable to return variance. The full distribution output, not just the mean, is the key deliverable.

## Example Walkthrough

*All figures below are illustrative and hypothetical — not derived from any real transaction.*

A value-add multifamily acquisition is modeled with base-case 14.5% levered IRR. Key uncertain variables: exit cap (mean 5.75%, std dev 0.50%), rent growth (mean 2.5%, std dev 1.0%), lease-up timing (mean 12 months, std dev 3 months). 10,000 iterations are run. Results: mean IRR 14.2%, median IRR 13.8%. P10 (10th percentile): 8.5%. P90: 21.3%. Probability of IRR ≥ 12% hurdle: 68%. Probability of equity multiple < 1.0×: 6%. The 6% loss probability is flagged for the investment committee — the deal is attractive in the median but carries tail risk driven primarily by exit cap rate uncertainty, which accounts for 58% of return variance in the contribution analysis.

## Limitations

Monte Carlo is only as good as its input distributions. If the modeler selects distributions that are too narrow (underestimating uncertainty) or improperly specified (wrong distribution shape), the simulated output distribution is miscalibrated — potentially in a direction that misleads the committee. Specifying correlations correctly is difficult; incorrect correlation assumptions can generate unrealistic joint scenarios. The technique also requires more setup time and software investment than simple sensitivity tables, making it less common in smaller or less sophisticated shops. Finally, Monte Carlo does not capture structural scenario breaks (a major tenant bankruptcy, a regulatory change) that don't fit neatly into continuous distributions — those require [[Stress Testing]] in addition.

## Related Frameworks

[[Sensitivity Analysis]] — the parametric complement; Monte Carlo is the probabilistic extension. [[Stress Testing]] — the scenario-based complement for discontinuous risk events. [[Pro Forma Construction Method]] — the base model Monte Carlo randomizes.

## Sources

@Risk / Palisade documentation. Geltner et al., *Commercial Real Estate Analysis and Investments* (3rd ed.) — Chapter 19. Standard probabilistic investment analysis methodology.
