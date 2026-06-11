---
title: "{{title}}"
aliases: ["{{title}}"]  # required when title differs from filename - makes Obsidian resolve title-based wikilinks
type: process
tags: ["process/{{slug}}", stub]
created: "{{date}}"
updated: "{{date}}"
status: stub
ai_summary: "{{one-sentence summary, <=30 words}}"
jurisdiction: "{{City of ___ | general}}"
state: "{{XX or empty}}"
decision_maker: "{{e.g., Planning Commission}}"
appeal_path: "{{where appeals go}}"
source_url: "TBD"
source_last_verified: ""
related: []
---

# {{title}}

## Summary
*1–2 paragraphs: what this entitlement process is (CUP, variance, GPA, rezoning, site plan review, subdivision), what it accomplishes, and when a developer needs it.*

## Triggering Conditions
*What triggers the requirement for this process — specific uses, thresholds, or proposed deviations from base zoning.*

## Decision-Maker
*Who decides (staff, hearing officer, planning commission, council) and whether it's administrative or legislative/quasi-judicial. Mirror in `decision_maker:` frontmatter.*

## Required Submittals
*The application package — plans, studies, fees, narratives. List the key items.*

## Typical Timeline
*Realistic timeline from application to decision, with the major milestones. Note as approximate.*

## Fees
*Application/processing fees. Mark "TBD — verify" unless confirmed.*

## Findings Required
*The findings the decision-maker must make to approve (e.g., the four variance findings). This is often the crux of approvability.*

## Appeal Path
*Where and how a decision is appealed, and the deadline. Mirror in `appeal_path:` frontmatter.*

## Common Pitfalls
*Where applicants commonly stumble — incomplete findings, neighborhood opposition, missing studies — and how to de-risk.*

## Sources
*Code citation + URL in source_url; inline-cite. Add to 00-meta/data-sources.md.*

<!--
AI FILL-IN INSTRUCTIONS (type: process)
- Filename: processes/{slug}.md within a city folder (or a general note if jurisdiction-agnostic). Required frontmatter per §3 process block.
- For a generic/cross-jurisdiction process note set jurisdiction: general and state: "".
- Findings Required is the highest-value section for quasi-judicial processes (variance/CUP) — be specific.
- Do NOT fabricate fees or statutory timelines — use "TBD — verify against {section}" + needs-verification when unsure.
- source_last_verified blank until verified.
- SUCCESS CRITERIA: a reader knows what triggers the process, who decides, what to submit, the findings needed to win, the timeline, and how to appeal.
-->
