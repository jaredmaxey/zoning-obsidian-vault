---
title: "{{title}}"
aliases: ["{{title}}"]  # required when title differs from filename - makes Obsidian resolve title-based wikilinks
type: framework
tags: [cre/frameworks, stub]
created: "{{date}}"
updated: "{{date}}"
status: stub
ai_summary: "{{one-sentence summary, <=30 words}}"
inputs_required: []     # list of input data the framework consumes
outputs: []             # list of what it produces
related: []
---

# {{title}}

## Purpose
*1–2 paragraphs: what question this framework answers and when an analyst reaches for it.*

## Inputs Required
*List every input the framework consumes, with units and where each is sourced (market data, pro forma, jurisdiction notes). Mirror in `inputs_required:` frontmatter.*

## Method
*Numbered, reproducible steps. Be precise enough that two analysts with the same inputs reach the same output. Include any formulas in plain text + LaTeX.*

1. Step one.
2. Step two.
3. Step three.

## Outputs
*What the framework produces — a number, a ranking, a go/no-go, a land value. State units and how to interpret the result. Mirror in `outputs:` frontmatter.*

## Example Walkthrough
*A worked example with illustrative (clearly-labeled hypothetical) numbers showing the method end to end. Mark all figures as illustrative.*

## Limitations
*Where this framework breaks down, its key assumptions, and what it ignores. When to use a different approach.*

## Related Frameworks
*Wikilink to complementary or competing frameworks and the concepts they rely on. Mirror in `related:` frontmatter.*

<!--
AI FILL-IN INSTRUCTIONS (type: framework)
- Required frontmatter: title, type=framework, tags (cre/frameworks + stub), created, updated, status, ai_summary, inputs_required, outputs, related.
- The Method section MUST be numbered and reproducible; include formulas in plain text AND LaTeX.
- Example Walkthrough numbers MUST be explicitly labeled illustrative/hypothetical — never present as real deal data.
- Populate inputs_required: and outputs: frontmatter lists to match the body sections.
- Set status: draft when the method and at least one walkthrough are complete.
- SUCCESS CRITERIA: another analyst could execute the framework from this note alone, knows exactly what inputs to gather and what the output means, and understands when not to use it.
-->
