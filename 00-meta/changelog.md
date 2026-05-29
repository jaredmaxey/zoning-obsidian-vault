---
title: Changelog
type: reference
tags: [meta, changelog]
created: 2026-05-24
updated: 2026-05-24
status: authoritative
ai_summary: Reverse-chronological log of structural and content changes to the vault, one dated entry per significant build step.
---

# Changelog

Reverse-chronological. Newest entries on top. One dated heading per significant change; bullets beneath.

## 2026-05-25 (Tempe standards — official source)

- **Filled all 31 Tempe zone notes' dimensional standards from the OFFICIAL Tempe ZDC development-standards tables** (4-202A residential, 4-202B multi-family, 4-202C mobile-home, 4-203A commercial, 4-203B mixed-use, 4-204 office/industrial), provided by the owner as a .docx (extracted to text; tables parsed column-per-district). All 31 → `status: reviewed`, `needs-verification` removed, citations to the specific table, `source_last_verified: 2026-05-25`.
- **Corrected prior errors using the official tables:** R1-15 had been wrongly populated with AG values (43,560 sf → corrected to 15,000 sf). The earlier web-sourced claim that "Tempe R1 codes don't encode lot size" was **wrong** — the official Table 4-202A shows R1 codes DO encode lot size (R1-6 = 6,000 SF, R1-7 = 7,000 SF, R1-8 = 8,000 SF, etc.). CLAUDE.md §5 updated to reflect this.
- **Historical notes from the doc:** MU-4 was formerly MG; LID was formerly IBD; GID was formerly I-1/I-2; HID was formerly I-3.
- Verified: 0 BOM, 0 YAML errors, 0 broken links; R1-6 spot-check matches the worked example exactly (4 du/ac · 6,000 sf · 30 ft · 45%).
- Vault status after Tempe: `draft` 524 · `reviewed` 65 (Scottsdale 34 + Tempe 31) · `authoritative` 3 · `stub` 1.

## 2026-05-25 (Scottsdale standards — official source)

- **Filled all 35 Scottsdale zone notes' dimensional standards from the OFFICIAL Scottsdale Zoning Ordinance (Appendix B)**, provided by the owner as a .docx (extracted to text; standards live in each district's "Property development standards" §5.xxx4). 34 conventional/planned districts → `status: reviewed`, `needs-verification` removed, exact §-citations (e.g., C-2 §5.1404: FAR 0.80, 36 ft, 50-ft buffer from SF / 25-ft from MF), `source_last_verified: 2026-05-25`.
- **Corrected prior web-sourced errors** using the official text: e.g., R1-7 height 24→30 ft (§5.504), R1-5 multiple fixes (height 15→30 ft, setbacks), R1-130 lot width filled.
- **Roster corrections from the official doc:** "OS" is NOT a district in Appendix B → kept `draft`/`needs-verification` with a flag (likely earlier web-roster error). "PCoC" IS real (§5.2705) → filled. Planned districts (P-C, PNC, PCC, PRC, PCP, PUD) set to "n/a — per approved development plan".
- These 34 are the vault's first official-source-verified dimensional data; a human spot-check promotes them to `authoritative`. Workflow established for the remaining cities (owner provides official code → fill like Scottsdale).
- Verified: 0 BOM, 0 YAML errors, 0 duplicate titles, 0 broken links. Spot-check C-2/C-3 matched the ordinance exactly.

## 2026-05-25 (Zone dimensional standards — web-sourced)

- **Populated dimensional/development standards for the 196 zone notes** (Phoenix pilot + 6-city rollout, one agent per city) by WebSearch against each city's live ordinance. Direct WebFetch of official hosts (Municode/American Legal) returns 403, but WebSearch reads them; Phoenix used phoenix.municipal.codes (current — R1-6 amended Jan 2026).
- **~91 of 196 zones now have ≥1 confirmed core value** (height/lot/density/coverage/setbacks), concentrated in **residential** zones; ~105 (mostly commercial/industrial/special) remain core-`TBD` where standards tables were inaccessible. Every value cites its section; all remain `AI-sourced, not human-verified` (`needs-verification`, `source_last_verified` blank). **Discipline held: agents left `TBD` rather than guess.**
- Source notes: Tucson from the official 2020 dimensional-standards summary PDF; Tempe R1 codes do NOT encode lot size (R1-6 = 7,000 SF — flagged); Scottsdale R1-5 = 4,700 SF.
- **Bug fixes during verification:**
  - **Phoenix P-1/P-2 mischaracterized.** The roster build had labeled them PUD / Planned Community; they are actually **parking districts** (§639 surface parking; §640 parking structures). Rewrote both zone notes (name, summary, uses, related) and corrected the Phoenix overview's zone table.
  - **UTF-8 BOM** was prepended to 19 Mesa zone files by the Mesa agent, which hid their frontmatter from parsers (and Obsidian). Stripped the BOM from all 19.
- Final audit: 598 content notes, 0 YAML errors, 0 duplicate titles, 0 broken `related:`, 0 real broken wikilinks.

## 2026-05-25 (City zone rosters — web-fetched)

- **Enumerated base zoning districts for the 6 previously-scaffolded cities** via web research (one agent per city), bringing all 7 priority cities to enumerated zones. **174 new zone notes:** Scottsdale 35, Mesa 34, Tempe 31, Tucson 28, Gilbert 28, Chandler 18. Vault total now **593 content notes**, **196 zone notes**.
- Each agent fetched a live source for the roster and **cited it**; codes & names are draft-verified. Official code hosts (municode/amlegal) frequently blocked automated fetch, so rosters came largely from zoneomics.com mirrors, official PDFs, and search snippets — **confirm against the official code before relying on them.** In-note flags: Gilbert MU sub-codes inferred; Scottsdale W-P ambiguous; some Tucson/Chandler article numbers inferred.
- Every zone note: `status: draft`, `needs-verification`, all dimensional standards `TBD`, `source_last_verified` blank. Each city's `00-overview.md` Zone Districts Index replaced with a linked table; `children:` populated. (Zone-table links use Obsidian escaped-pipe syntax `[[Title\|alias]]` for clean table rendering.)
- Audit: 196 zones valid; 0 duplicate titles; 0 broken `related:`; 0 real broken wikilinks. `needs-verification` count now 338.

## 2026-05-25 (Finishing QA sweep)

- **Completeness sweep — verified nothing is inappropriately stubbed or missing content.** Scanned all 419 notes for stubs, thin notes (<350 content chars), empty sections, and leftover placeholders.
- Filled the two reference tables that were still stubs: [[Density Metrics]] (FAR, DUA, lot coverage, OSR, net vs. gross density — definitions + plain/LaTeX formulas + worked example) and [[Unit Conversions]] (area, intensity/buildable, density, parking & rate conversions). Both now `status: draft`.
- Confirmed **0 truly empty sections** (a level-aware re-scan showed the 27 initial flags were all sections whose content sits under `###` subheadings) and **0 leftover placeholder text** outside the changelog.
- Only remaining `stub` is [[Nevada State Overview]] — intentional (deferred buildout). Final status: `draft` 415 · `authoritative` 3 · `stub` 1.

## 2026-05-25 (Prompt 5 — finalization & polish)

- **Prompt 5 complete — vault finalized for ongoing use.**
- Rewrote `CLAUDE.md` from scratch: purpose, how-to-read-as-AI, folder map w/ counts, status distribution, known gaps & verification needs, future phases, do/don't.
- Built the human-facing master index at `00-index.md` (vault root).
- Populated [[Glossary]] (37 terms — 25 concepts via `ai_summary` + 12 zoning/dev terms) and [[Common Acronyms]] (60+ entries) by walking the vault.
- Converted [[Reference Index]] table references to wikilinks (they had been plain text → orphaned the lookup tables).
- **Sanity check:** deleted a 0-byte stray `Gilbert, Arizona.md` at root (agent write glitch; real note is `gilbert/00-overview.md`). Confirmed: 0 notes missing frontmatter, 0 invalid `type:` values, 0 broken `related:` refs, 0 duplicate titles. Orphans reduced to the root master index only (intentional — it is the entry point).
- **Final tallies:** 418 content notes — `draft` 413, `authoritative` 2, `stub` 3; 163 carry `needs-verification` (the Arizona zoning layer).

## 2026-05-25 (Prompt 4 — Arizona zoning buildout)

- **Prompt 4 complete — Arizona zoning knowledge base scaffolded (~165 notes, all `draft`).** Built via 12 parallel subagents across two waves.
- **Pattern:** rewrote `_jurisdiction-pattern.md` as the authoritative recipe (folder structure, naming, frontmatter per level, order of operations, quality gates) — sufficient to scaffold any future state.
- **State:** `arizona/00-state-overview.md` + 6 `state-statutes/` notes (A.R.S. Titles 9/11/32/33/45, Assured Water Supply).
- **Counties (7):** Maricopa, Pima, Pinal, Yavapai, Coconino, Mohave, Yuma.
- **Phoenix (full):** overview + 22 base-zone notes (21 base zones + Walkable Urban summary) + 4 overlays + 5 citywide standards + 6 entitlement processes.
- **6 scaffold cities** (Tucson, Scottsdale, Mesa, Tempe, Chandler, Gilbert): overview + overlays + standards + processes; `zones/` intentionally empty (deferred to a later code-fetch pass per user decision).
- **18 overview-only cities** + **4 special-districts** (tribal lands, military compatibility, CFDs, domestic water improvement districts). Nevada remains an intentional stub (NRS 278).
- **Anti-fabrication discipline enforced:** all numeric standards / section numbers / fees / deadlines are `TBD` + `needs-verification`; `source_last_verified` blank everywhere; only Phoenix R1-x definitional min-lot-sizes populated. Qualitative content (purpose, use categories, process flow) populated confidently.
- Seeded `30-reference/parking-ratios-by-use.md` with the Phoenix zone roster as a verification worklist (ratios TBD). Updated `20-jurisdictions/00-index.md` (full AZ tree), `arizona/00-state-overview.md` (Key Cities), `00-meta/data-sources.md` (AZ agency/county/city URLs, best-effort/unverified).
- **Bugs fixed during finalize:** removed 8 `related: ["Phoenix Zoning Ordinance"]` entries (a source, not a note → broken ref). Whole-vault audit (417 notes): 0 broken `related:` refs, 0 duplicate titles, all valid UTF-8; remaining ~16 path-style index wikilinks deferred to Prompt 5's link audit.

## 2026-05-24 (Prompt 3b — complete; finalization)

- **Prompt 3b complete — all 10 asset classes populated.** 108 `draft` notes across `10-cre-brain/asset-classes/`: nine primary classes (multifamily 11, office 11, retail 13, industrial 13, hospitality 13, self-storage 8, mixed-use 9, ground-up-development 10, land 9) each with the standard 6-note structure + topic notes; plus `specialty/` (10 single overviews + index). Generated via 10 parallel subagents (per-class detail in the per-class entries below).
- Created `10-cre-brain/asset-classes/00-index.md`; updated `10-cre-brain/00-index.md` to link it; consolidated the `CLAUDE.md` current-state section.
- **Bug fixed:** 9 asset-class notes had `related:` list items with colon-bearing titles ("Contingency: Hard vs. Soft", "Assumption Hierarchy: Actual vs. Pro Forma") written unquoted, so YAML parsed them as nested mappings. Quoted them. (Prose `[[wikilinks]]` were unaffected.)
- **Whole-vault audit:** 241 CRE-brain notes, all `status: draft`; 0 broken `related:` refs, 0 duplicate titles, all valid UTF-8, no leftover template scaffolding.
- Title-collision avoided: ground-up-development overview titled "Ground-Up Development (Asset Class)" vs. the deal-type "Ground-Up Development".

## 2026-05-24 (Prompt 3b — Hospitality)

- **Prompt 3b — Hospitality asset class populated.** Created 13 `status: draft` notes in `10-cre-brain/asset-classes/hospitality/`.
- **Standard notes (6):** `00-overview.md` (entry point, full template with UW ranges table, wikilinks to all companion notes and REGISTRY concepts), `subtypes.md` (6 subtypes profiled: full-service, select-service, limited-service, extended-stay, resort, boutique/lifestyle — including demand profile, deal profile, owners/flags per subtype), `underwriting-norms.md` (ranges table covering all subtypes + management/franchise agreement operating model + PIP treatment + departmental expense norms; dated disclaimer), `key-metrics.md` (8 metrics: ADR, Occupancy, RevPAR with formula RevPAR = ADR × Occupancy, TRevPAR, GOP/GOPPAR, NOI/flow-through, RevPAR index/penetration, FF&E reserve — definitions + plain + LaTeX formulas), `risks-and-considerations.md` (Market / Operational / Capital & Financing / Structural & Physical risk sections with mitigants — RevPAR cyclicality, supply pipeline, demand concentration, operator dependence, brand PIP capital calls, OTA dependency, lending market volatility, physical obsolescence, seasonality, ADA/life-safety), `regulatory-considerations.md` (franchise/brand agreements and area protection, transient occupancy tax, liquor licensing, ADA, health/safety inspections, labor/union, STR competition regulation, entitlement and development approvals).
- **Extra notes (7):** `full-service.md`, `select-service.md`, `limited-service.md`, `extended-stay.md`, `resort.md`, `boutique-and-lifestyle.md`, `brand-vs-independent.md` (full analysis of brand-affiliated vs. independent strategy including soft-brand middle path and decision framework table).
- All `related:` fields verified against REGISTRY canonical titles + class overview titles. Zero broken cross-links.
- Updated `CLAUDE.md` current-state section to reflect Hospitality folder completion.

## 2026-05-24 (Prompt 3b — Retail)

- **Prompt 3b — Retail asset class populated.** Created 13 `status: draft` notes in `10-cre-brain/asset-classes/retail/`.
- **Standard notes (6):** `00-overview.md` (entry point, full template with UW ranges table, wikilinks to all companion notes and REGISTRY concepts), `subtypes.md` (7 subtypes profiled: power center, grocery-anchored, neighborhood/strip, lifestyle, mall formats, STNL, urban street retail), `underwriting-norms.md` (ranges table by 7 formats + NNN/percentage-rent/co-tenancy/gross lease structures + OpEx/recovery norms; dated disclaimer), `key-metrics.md` (6 metrics: sales per SF, OCR/health ratio, percentage rent breakpoint, NNN recovery ratio, traffic/footfall, co-tenancy thresholds — definitions + plain + LaTeX formulas), `risks-and-considerations.md` (Market / Operational / Capital & Financing / Structural & Physical risk sections with mitigants — e-commerce displacement, anchor vacancy, co-tenancy cascade, lease obsolescence, format obsolescence, deferred maintenance), `regulatory-considerations.md` (ADA, zoning/use permits/CUP, signage, parking minimums, drive-thru restrictions, liquor licensing, exclusive-use clauses and CC&Rs/REAs).
- **Extra notes (7):** `power-center.md`, `grocery-anchored.md`, `lifestyle-center.md`, `strip-center.md`, `single-tenant-net-lease-stnl.md`, `mall-formats.md`, `urban-street-retail.md`.
- All `related:` fields verified against REGISTRY canonical titles + class overview titles. Zero broken cross-links.
- Updated `CLAUDE.md` current-state section to reflect Retail folder completion.

## 2026-05-24 (Prompt 3b — Industrial)

- **Prompt 3b — Industrial asset class populated.** Created 13 `status: draft` notes in `10-cre-brain/asset-classes/industrial/`.
- **Standard notes (6):** `00-overview.md` (entry point, full template with UW table, wikilinks to all companion notes), `subtypes.md` (7 subtypes profiled: bulk/big-box, last-mile, light industrial, flex/R&D, cold storage, manufacturing, IOS), `underwriting-norms.md` (full ranges table + NNN/absolute-net/modified-gross lease structures + OpEx recovery norms; dated disclaimer), `key-metrics.md` (7 metrics: clear height, dock-door ratio, truck court depth, trailer/auto parking, $/SF NNN rent, cubic utilization, power capacity — definitions + plain + LaTeX formulas), `risks-and-considerations.md` (Market / Operational / Capital & Financing / Structural & Physical risk sections with mitigants), `regulatory-considerations.md` (zoning/use conflicts, truck traffic, Phase I/II environmental, cold-storage refrigerant/EPA rules, fire/hazmat/ESFR codes, IOS zoning crackdowns).
- **Extra notes (7):** `bulk-warehouse.md`, `last-mile-logistics.md`, `light-industrial.md`, `flex-industrial.md`, `cold-storage.md`, `manufacturing.md`, `ios-industrial-outdoor-storage.md`.
- All `related:` fields verified against REGISTRY canonical titles + class overview titles. Zero broken cross-links.
- Updated `CLAUDE.md` current-state section to reflect Industrial folder completion.

## 2026-05-24 (Prompt 3b — Multifamily)

- **Prompt 3b — Multifamily asset class populated.** Created 11 `status: draft` notes in `10-cre-brain/asset-classes/multifamily/`.
- **Standard notes (6):** `00-overview.md` (entry point, full template with UW table, wikilinks to all 10 companion notes), `subtypes.md` (6 subtypes profiled), `underwriting-norms.md` (full ranges table + lease structures + OpEx norms by category), `key-metrics.md` (9 metrics with plain-text + LaTeX formulas), `risks-and-considerations.md` (4 risk categories with mitigants), `regulatory-considerations.md` (rent control, fair housing/ADA, landlord-tenant law, LIHTC, building codes, condo conversion).
- **Extra notes (5):** `garden-vs-midrise-vs-highrise.md` (side-by-side comparison tables), `build-to-rent-sfr.md` (BTR product types, demand, economics, operations), `student-housing.md` (by-the-bed structure, pre-leasing, enrollment risk), `senior-housing-spectrum.md` (full care continuum: active adult → IL → AL → MC → SNF), `affordable-housing-lihtc.md` (LIHTC mechanics, deal structure, compliance management).
- All `related:` fields verified against REGISTRY canonical titles + class overview titles. Zero broken cross-links.
- Updated `CLAUDE.md` current-state section to reflect Multifamily folder completion.

## 2026-05-24 (Prompt 3b — Office)

- **Prompt 3b — Office asset class populated.** Created 11 `status: draft` notes in `10-cre-brain/asset-classes/office/`.
- **Standard notes (6):** `00-overview.md` (entry point, full template with UW table), `subtypes.md` (6 subtypes profiled), `underwriting-norms.md` (full ranges table + lease structures + OpEx norms), `key-metrics.md` (7 metrics with formulas in plain + LaTeX), `risks-and-considerations.md` (4 risk sections with mitigants), `regulatory-considerations.md` (ADA, energy codes/benchmarking, zoning/parking, office-to-resi conversion incentives).
- **Extra notes (5):** `cbd-vs-suburban.md`, `medical-office-building-mob.md`, `life-sciences-lab.md`, `flex-office.md`, `post-covid-occupancy-trends.md`.
- All `related:` fields verified against REGISTRY canonical titles + class overview titles. Zero broken cross-links.
- Updated `CLAUDE.md` current-state section to reflect Office folder completion.

## 2026-05-24 (Prompt 3a)

- **Prompt 3a — cross-cutting CRE brain populated.** Created 122 `status: draft` notes + 9 section indexes across concepts (25), deal-types (12), financing (19), underwriting (13), market-analysis (10), entitlement-and-approvals (11), construction-and-delivery (13), operations-and-disposition (10), frameworks (9).
- Generated via 9 parallel subagents (one per folder), each working from `_CONVENTIONS.md` + its template against a shared canonical-title registry.
- Verified: all 131 new files have valid YAML and required fields; no leftover template scaffolding; **0 broken `related:` cross-links** across 132 notes.
- Created `10-cre-brain/case-studies/00-index.md` (empty, awaiting real write-ups). Updated `10-cre-brain/00-index.md` to link all section indexes with counts.
- Asset-class deep dives (`asset-classes/`) deferred to Prompt 3b.

- **Prompt 2 — template library complete.** Wrote all 14 templates into `_templates/`: concept, deal-type, asset-class, framework, case-study, jurisdiction-state/county/city, zone, development-standard, overlay, process, reference, index.
- Each template carries drop-in target-type frontmatter with `{{placeholders}}`, `status: stub`, namespace + `stub` tags, italic per-section guidance, and an `AI fill-in instructions` HTML comment block.
- Zone + development-standard templates use the fixed standards-table column order `| Standard | Requirement | Units | Code Citation | Notes |`.

## 2026-05-24

- **Vault initialized via Prompt 1.** Created the full folder hierarchy (`10-cre-brain/`, `20-jurisdictions/`, `30-reference/`, `00-meta/`, `_templates/`).
- Wrote `_CONVENTIONS.md` (naming, frontmatter, tagging, linking, sourcing, status lifecycle).
- Wrote `CLAUDE.md` (AI handoff + current-state tracking) and `README.md` (human overview).
- Initialized `00-meta/` files: `changelog.md`, `glossary.md` (stub), `data-sources.md` (pre-populated registry).
- Initialized branch index notes: `10-cre-brain/00-index.md`, `20-jurisdictions/00-index.md`, `30-reference/00-index.md`.
- Created stub files for later prompts: `_jurisdiction-pattern.md`, `arizona/00-state-overview.md`, `nevada/00-state-overview.md`, and the `30-reference/` lookup tables.
