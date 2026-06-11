---
title: "Contingency: Hard vs. Soft"
aliases: ["Contingency: Hard vs. Soft"]
type: concept
tags: [cre/construction]
created: "2026-05-24"
updated: "2026-05-24"
status: draft
ai_summary: Separate reserve line items buffering hard cost overruns (design gaps, unforeseen conditions) and soft cost overruns (carry, fees, market shifts) in a development budget.
domain: construction
formula: true
related: ["Hard Costs", "Soft Costs", "General Conditions", "GMP vs. Cost-Plus vs. Lump-Sum", "Construction Schedule and Critical Path", "Pro Forma Construction Method", "Development Feasibility Test", "Construction Loan"]
---

# Contingency: Hard vs. Soft

## Definition

In development budgeting, contingency is a reserve set aside to absorb cost overruns that cannot be precisely identified at the time of budgeting. Industry practice distinguishes between a **hard cost contingency**—applied against the construction budget to cover physical cost uncertainties—and a **soft cost contingency** (sometimes called "developer's contingency" or "project contingency")—applied against the non-physical budget to absorb fee escalation, carry extensions, entitlement surprises, and general development risk. The two reserves serve different purposes, are sized differently, and are often drawn down by different parties under different circumstances.

Hard cost contingency exists because construction budgets are never complete when a project is financed. At GMP execution with 100% construction documents, there is still residual risk from subsurface conditions, design errors and omissions, supply chain volatility, subcontractor default, and owner-directed changes. At earlier design stages (Schematic Design, Design Development), the contingency must be larger because the design is incomplete and the cost estimate is correspondingly uncertain. Contingency is not a slush fund—disciplined developers require formal change order requests and budget adjustments before contingency is accessed.

Soft cost contingency covers the non-construction risks: permit delays that extend carry, interest rate movements that change loan costs, unanticipated consultant fees, legal disputes, and market conditions that extend the lease-up timeline. Because soft costs are dominated by time-sensitive costs (loan interest, carry, property taxes), schedule risk directly drives soft contingency needs—a project that runs six months over budget experiences both hard cost contingency draws (from change orders) and soft cost contingency draws (from extended carry).

## Formula

Contingency is typically sized as a percentage of the cost base it protects. Common benchmarks in institutional practice (varies by design stage, project type, market, and vintage; current as of 2026-05-24):

**Hard cost contingency:**
- Plain text: `Hard Contingency = Hard Costs × Hard Contingency %`
- LaTeX: $$ \text{Hard Contingency} = \text{Hard Costs} \times \text{HC\%} $$

Where HC% commonly ranges:
- Schematic Design: 10–20% of hard costs
- Design Development: 7–12% of hard costs
- Construction Documents (pre-GMP): 5–10% of hard costs
- Post-GMP (in the contract): 3–7% of hard costs remaining in the contract

**Soft cost contingency:**
- Plain text: `Soft Contingency = Soft Costs × Soft Contingency %`
- LaTeX: $$ \text{Soft Contingency} = \text{Soft Costs} \times \text{SC\%} $$

Where SC% commonly ranges 5–15% of total soft costs, with higher percentages in markets with volatile entitlement timelines or uncertain interest rate environments. Some institutions maintain a single "project contingency" line equal to 3–5% of total project cost rather than splitting it by hard/soft.

## When It's Used

Contingency is modeled from the first feasibility pro forma and maintained through project completion. In early underwriting using the [[Pro Forma Construction Method]], total project contingency is modeled as a percentage of hard costs or total costs; this feeds the total development cost, which drives [[Yield on Cost]] analysis and the [[Development Feasibility Test]].

During construction loan underwriting, the lender scrutinizes contingency allocation carefully. [[Construction Loan]] lenders typically require a minimum contingency reserve (often 5–10% of hard costs post-GMP, varying by lender and project type) and may control draw access to contingency—requiring lender approval before contingency is released. Some lenders hold contingency in a separate holdback rather than funding it into the initial loan commitment.

Contingency tracking is a key function of construction management. The construction manager or developer's representative maintains a contingency log tracking approved change orders, pending change orders, and remaining contingency balance. When contingency erodes below a threshold (often 50% depleted), it is a warning signal that triggers owner review and potentially contract restructuring.

## Variations & Edge Cases

The distinction between hard and soft contingency breaks down when a single "project contingency" or "developer's contingency" line is used. This is common in simpler budgets and smaller projects. While adequate for rough feasibility, a single contingency line obscures where risks are concentrated—it cannot signal, for example, that hard cost uncertainty is under control while carry risk remains elevated.

On [[GMP vs. Cost-Plus vs. Lump-Sum]] contracts, the GC may also carry their own contingency within the contract (GC contingency or allowance)—this is different from and in addition to the owner's hard cost contingency. GC contingency is the GC's reserve for cost uncertainty within their scope; owner contingency covers cost uncertainty the GC cannot foresee or is not responsible for. These must not be double-counted.

In value-add and rehabilitation projects (see [[Adaptive Reuse]]), hard cost contingency is typically higher than in ground-up work because of the elevated risk of hidden conditions—asbestos, lead, structural deficiencies—that are not visible until demolition begins. Experienced developers in renovation projects carry 15–25%+ hard cost contingency before walls are opened.

## Common Mistakes

The most frequent error is releasing contingency too early—treating unused contingency as project profit before project completion and CO issuance. Contingency should remain fully intact until substantial completion; only after final accounting should residual contingency be released to the developer or lender.

A second mistake is budgeting contingency as a percentage of one cost base while exposing it to risk from another. For example, using a small hard cost contingency while ignoring that a schedule extension would also blow through the soft cost budget. Hard and soft contingency should both be stress-tested in schedule delay scenarios.

Failing to replenish contingency after draws is a structural problem in under-budgeted projects. Each change order that draws contingency must be assessed not just for the cost of that specific change, but for what residual contingency remains to absorb future events. Running the project to near-zero contingency mid-construction is a high-risk condition.

## Related Concepts

[[Hard Costs]] and [[Soft Costs]] are the cost bases from which contingency is sized. [[GMP vs. Cost-Plus vs. Lump-Sum]] determines how contingency risk is allocated between owner and GC. [[Construction Schedule and Critical Path]] explains how schedule delays trigger both hard and soft contingency draws. [[Construction Loan]] lenders impose minimum contingency requirements as loan conditions. [[Pro Forma Construction Method]] and [[Development Feasibility Test]] show how contingency flows into total project cost.

## Sources

- Urban Land Institute, *Real Estate Development: Principles and Process*, 5th ed. (Washington, DC: ULI, 2015). Contingency budgeting and cost control.
- CCIM Institute, *CI 104: Investment Analysis for Commercial Investment Real Estate*. Pro forma construction budget structure.
- AIA (American Institute of Architects), construction contract cost control documentation and owner's representative best practices.
- Construction Management Association of America (CMAA), *Owner's Guide to Project Delivery Methods*. Contingency allocation guidance by delivery method.
