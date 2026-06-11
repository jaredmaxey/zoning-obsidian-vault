---
title: "{{title}}"
aliases: ["{{title}}"]  # required when title differs from filename - makes Obsidian resolve title-based wikilinks
type: concept
tags: [cre/concepts, stub]
created: "{{date}}"
updated: "{{date}}"
status: stub
ai_summary: "{{one-sentence summary, <=30 words}}"
domain: concepts        # one of: concepts | financing | underwriting | construction | operations
formula: false          # true if this concept has a formula
related: []             # titles of related notes
---

# {{title}}

## Definition
*Define the concept in 1–3 plain-language paragraphs. Lead with the one-sentence essence, then add nuance. State what it measures or describes and why a CRE practitioner cares.*

## Formula
*If the concept has a formula, give it in BOTH plain text and LaTeX-friendly form, then define every variable. If there is no formula, delete this section and set `formula: false` in frontmatter.*

- Plain text: `result = numerator / denominator`
- LaTeX: `$$ result = \frac{numerator}{denominator} $$`

*Where: define each term, its units, and where it comes from (actuals vs. pro forma).*

## When It's Used
*Describe the situations in which this metric/concept is applied — acquisition screening, development underwriting, financing, disposition, etc. Note who relies on it (lenders, equity, appraisers).*

## Variations & Edge Cases
*Where the industry uses competing definitions, list each variant and who uses it. Note edge cases that change the calculation or interpretation (e.g., trailing vs. forward, in-place vs. stabilized).*

## Common Mistakes
*List the recurring errors practitioners make with this concept — wrong inputs, conflated definitions, missing adjustments — and how to avoid them.*

## Related Concepts
*Wikilink to related notes (e.g., [[NOI]], [[Cap Rate]]). Mirror these in the `related:` frontmatter field using note titles.*

## Sources
*Cite authoritative sources (textbooks, CCIM/ULI material, lender guidelines). Use the inline citation format from `_CONVENTIONS.md` §6 for any sourced figure.*

<!--
AI FILL-IN INSTRUCTIONS (type: concept)
- Required frontmatter: title, type=concept, tags (cre/<domain> + stub; drop stub once content is real), created, updated, status, ai_summary, domain, formula, related.
- Set status: draft once you write substantive content (1–3 paragraphs per section); keep stub only if genuinely thin.
- DOMAIN must match the folder the note lives in (concepts/financing/underwriting/construction/operations).
- FORMULA: if the concept has one, set formula: true and complete the Formula section in BOTH plain text and LaTeX. Otherwise set formula: false and delete the Formula section.
- Present ranges/figures as ranges with a "varies by market and vintage" qualifier; never invent precise deal data.
- Populate related: with the TITLES (not filenames) of notes you wikilink in Related Concepts.
- SUCCESS CRITERIA: a practitioner reading only this note understands what the concept is, how to compute/apply it, its variants, and what mistakes to avoid; every external figure has a source.
-->
