---
title: "{{title}}"
aliases: ["{{title}}"]  # required when title differs from filename - makes Obsidian resolve title-based wikilinks
type: case-study
tags: [cre, "asset/{{slug}}", stub]
created: "{{date}}"
updated: "{{date}}"
status: stub
ai_summary: "{{one-sentence summary, <=30 words}}"
asset_class: multifamily          # one of the asset_class values
deal_type: "value-add acquisition"
location: "City, ST"
deal_size: "$XX.XM"               # total capitalization
outcome: hypothetical             # one of: realized | in-progress | hypothetical
key_lessons: []                   # list of one-line takeaways
related: []
---

# {{title}}

## Snapshot
*The headline numbers, pulled from frontmatter, in a quick-read block: asset class, deal type, location, size, basis, returns (projected or realized), hold period, outcome. Keep it scannable.*

## Site & Market Context
*The physical site and the market at the time of the deal — submarket fundamentals, demand drivers, supply pipeline, why this site. Anonymize as needed.*

## Deal Structure
*Sponsor, capital stack (debt + equity), JV terms, promote/waterfall, key business terms. Use ranges/approximations if anonymizing.*

## Underwriting
*The underwriting thesis: going-in basis, rent/expense assumptions, value-creation plan, exit assumptions, projected returns. Note which assumptions proved right or wrong.*

## Execution Timeline
*The actual sequence of events from acquisition through stabilization/exit, with approximate dates and milestones.*

## Outcome
*What actually happened (or is projected) — realized returns vs. underwriting, value created, exit. Be candid about variance from plan.*

## Key Lessons
*The transferable takeaways. Mirror each one-liner in the `key_lessons:` frontmatter list.*

## Could-Have Gone Wrong
*The risks that didn't materialize but could have, and the near-misses. What would have broken the deal.*

<!--
AI FILL-IN INSTRUCTIONS (type: case-study)
- Filename MUST be YYYY-MM-DD-{slug}.md and live in 10-cre-brain/case-studies/.
- Required frontmatter: title, type=case-study, tags (cre + asset/<slug> + stub), created, updated, status, ai_summary, asset_class, deal_type, location, deal_size, outcome, key_lessons, related.
- outcome must be realized | in-progress | hypothetical. NEVER fabricate a "realized" deal — if invented for teaching, set outcome: hypothetical and say so.
- Anonymize sensitive specifics; approximate figures are fine and preferred over fabricated precision.
- Mirror Key Lessons bullets into the key_lessons: frontmatter list.
- Set status: draft when the write-up is substantive.
- SUCCESS CRITERIA: the case reads as a complete, honest deal narrative with transferable lessons; no fabricated precision; outcome flag is accurate.
-->
