# CLAUDE.md — AI Handoff Document

**You are an AI session working in this vault. Read this file first, then [[Vault Conventions]] (`_CONVENTIONS.md`) for the rules every note follows.** Humans should start at the master index (`00-index.md`).

## 1. Vault purpose

This is a dual-purpose, **AI-readable-first** Obsidian knowledge base: (1) a **commercial real estate (CRE) development brain** covering all asset classes, financing, underwriting, market analysis, entitlement, construction, and operations; and (2) a **structured zoning & development-standards reference** organized by jurisdiction (Arizona built; Nevada and more to follow) using a pattern-driven structure so adding a state is mechanical. It exists so AI tools can reason about deals — yield analysis, project evaluation, highest-and-best-use, jurisdiction lookups, and citable regulatory data. Every design choice favors machine traversal: consistent YAML frontmatter, kebab-case filenames, explicit relational fields, predictable hierarchies.

## 2. How to read this vault as an AI

- **For structured/quantitative zoning queries about Phoenix**, query the companion zoning-intel SQLite DB at `MetroData/zoning-intel/data/zoning.db` first — it has 258 typed use-permission rows + 92 development-standard rows + 6 parking rules, all source-cited (see §6). Fall back to vault notes for cities not yet extracted (Scottsdale, Tempe, Tucson, Mesa, Chandler, Gilbert) or for narrative context.
- **Start from the relevant `00-index.md`** (or `00-overview.md` for an asset class or city) to orient, then follow wikilinks. The root `00-index.md` is the human TOC; the branch indexes are [[CRE Brain Index]], [[Jurisdictions Index]], [[Reference Index]].
- **Use frontmatter, not prose, for relational and quantitative queries.** Relationships live in `related` / `parent` / `children` (note **titles**, not paths). Quantitative zone data lives in typed fields (`max_height_ft`, `setbacks`, `parking_ratio`, etc.).
- **Trust by status:** `authoritative` > `reviewed` > `draft` > `stub`. Today almost everything is `draft` (AI-generated starter content) — treat it as solid orientation, **not citable fact**.
- **When citing any sourced/zoning value**, include its `source_url` and `source_last_verified`. **If `source_last_verified` is blank or older than 12 months, flag the answer as needing re-verification.** Right now it is blank everywhere.
- **Never present a numeric zoning standard from this vault as fact.** Every Arizona standard (height, setback, FAR, density, lot size, parking) is currently `TBD` + `needs-verification`. Only the Phoenix R1-x minimum lot sizes are populated (definitional), and even those say "verify".
- **For "highest and best use" or "yield analysis" questions, consult BOTH halves:** the asset-class notes in `10-cre-brain/asset-classes/` (what the use is worth and how it underwrites) AND the relevant jurisdiction zone notes in `20-jurisdictions/` (what is legally allowed). Neither alone is sufficient.
- **When writing new notes**, copy the matching template from `_templates/`, follow [[Vault Conventions]] exactly, and quote any frontmatter string containing `:`, `{`, `}`, `[`, `]` (a recurring YAML trap).

## 3. Folder map (with current counts)

```
/
├── 00-index.md                     # Human master TOC
├── CLAUDE.md                       # This file (AI handoff)
├── README.md · _CONVENTIONS.md     # Overview · rules (source of truth)
├── _templates/                     # 14 note templates
├── 00-meta/                        # changelog · glossary · data-sources (3)
├── 10-cre-brain/                   # CRE development brain — 242 notes
│   ├── 00-index.md
│   ├── concepts/ (25) · deal-types/ (12) · financing/ (19) · underwriting/ (13)
│   ├── market-analysis/ (10) · entitlement-and-approvals/ (11)
│   ├── construction-and-delivery/ (13) · operations-and-disposition/ (10)
│   ├── frameworks/ (9) · case-studies/ (index only)
│   └── asset-classes/ (109) — 9 primary classes + 10 specialty + indexes
├── 20-jurisdictions/               # Zoning/codes — 341 notes
│   ├── 00-index.md · _jurisdiction-pattern.md
│   ├── arizona/ — overview + 6 statutes + 7 counties + cities + 4 special districts
│   │   └── cities/ — 7 cities with enumerated zones (196 zone notes total):
│   │                 phoenix 22 · scottsdale 35 · mesa 34 · tempe 31 · tucson 28
│   │                 · gilbert 28 · chandler 18; each + overlays/standards/processes;
│   │                 + 18 overview-only cities
│   └── nevada/ — stub (NRS 278)
└── 30-reference/                   # Lookup tables (5)
    └── glossary handoff: see 00-meta/glossary.md · common-acronyms · density-metrics
        · parking-ratios-by-use · unit-conversions
```

**By folder:** 20-jurisdictions 341 · 10-cre-brain 242 (133 cross-cutting + 109 asset-classes) · 30-reference 5 · 00-meta 3 · root 2. **Total content notes: 593** (plus 14 templates + the pattern doc).

## 4. Status distribution

| Status | Count | Meaning |
|--------|-------|---------|
| `draft` | 524 | Substantive AI-generated content; not human-verified. |
| `reviewed` | 65 | **Scottsdale** (34) + **Tempe** (31) zone notes — standards transcribed from the owner-provided official ordinances with exact §/table citations. Spot-check before `authoritative`. |
| `authoritative` | 3 | [[Vault Conventions]], [[Changelog]], [[Jurisdiction Pattern]]. |
| `stub` | 1 | [[Nevada State Overview]] — intentional. |

**273 notes carry `needs-verification`** — the remaining Arizona zoning layer (Phoenix, Tucson, Mesa, Chandler, Gilbert + the next-tier overview cities). Scottsdale and Tempe are official-source-verified (see §5).

## 5. Known gaps & verification needs

In priority order:
1. **Zone numeric standards — in progress (owner providing official sources, city by city).**
   - **Scottsdale ✅ DONE from official source:** all 34 conventional/planned districts transcribed from the owner-provided **Scottsdale Zoning Ordinance Appendix B** with exact §-citations; `status: reviewed`. Only OS remains (not a district in the official doc — verify).
   - **Tempe ✅ DONE from official source:** all 31 districts transcribed from the owner-provided **Tempe ZDC development-standards tables** (4-202A residential / 4-202B multi-family / 4-202C mobile-home / 4-203A commercial / 4-203B mixed-use / 4-204 office-industrial); `status: reviewed`. The official tables corrected the earlier (web-sourced) claim that "Tempe R1 codes don't encode lot size" — they **do** (R1-6 = 6,000 SF, R1-7 = 7,000 SF, etc.).
   - **Phoenix ✅ NOW STRUCTURED-EXTRACTED into the companion zoning-intel system (see §6).** All 22 vault zones were classified, ingested, and extracted into a queryable SQLite database (258 use-permission rows + 92 development-standard rows + 6 parking rules), then regenerated as 104 atomic markdown notes under `MetroData/zoning-intel/normalized_vault/`. The underlying vault files in `arizona/cities/phoenix/zones/` are unchanged — extraction is non-destructive. Phoenix data is still `needs-verification` because the vault sources are AI-summarized rather than transcribed from the official ZO; the structured extraction faithfully reproduces what the vault notes contained (confidences capped at 0.85 to reflect that).
   - **Other cities — web-sourced/partial:** Tucson (2020 standards PDF), Mesa/Chandler/Gilbert (Municode/zoneomics). Residential zones mostly filled; **commercial/industrial/special largely `TBD`** (Municode blocks automated access). These remain `draft` + `needs-verification`.
   - **Next:** owner to provide each remaining city's official zoning code/standards (PDF, .docx, or pasted tables); fill from official source like Scottsdale and Tempe. Web-sourced rosters may contain errors (e.g., Scottsdale's earlier roster wrongly listed "OS" while "PCoC" turned out real at §5.2705; Tempe R1-15 had been wrongly populated with AG values — fixed from the official table).
2. **Zone-roster accuracy.** The 6 non-Phoenix rosters were built from web sources (often zoneomics.com / search snippets / official PDFs, because municode/amlegal blocked automated fetch) — codes & names are draft-verified, not officially confirmed. Confirm against the live official code. Specific flags in-note: Gilbert MU sub-codes (MU/S, MU/L, MU/R) inferred; Scottsdale W-P placement ambiguous; Tucson/Chandler some article numbers inferred.
3. **Zoning-code citation** (exact chapter/section) for every county and city is `TBD`.
4. **All citywide standards & process specifics** (parking ratios, fees, statutory timelines, decision-makers) — `TBD` across all 7 cities.
5. **Source URLs** in [[Data Sources Registry]] are best-effort and unverified.
6. **CRE-brain market figures** (cap-rate/expense ranges) are dated "current as of 2026-05-24" — refresh before underwriting.

## 6. Companion system: `zoning-intel/` (structured extraction + queryable DB)

A separate Python project at `C:\Users\jared\OneDrive\Desktop\MetroData\zoning-intel\` is now the canonical structured layer for this vault's zoning content. The Obsidian vault remains the **human editing + research workspace**; the zoning-intel system is the **canonical relational store** and a **regeneration target**. They are kept in lockstep by a one-way pipeline: vault → DB → atomic notes in `normalized_vault/`. The vault is never modified by the system.

### Pipeline
```
legacy vault (this folder)
   → classify_notes.py        → legacy_note_classifications  (593 rows)
   → ingest_markdown.py       → source_documents (593) + source_sections (5,309) + vault_links (12,175) + FTS5
   → extract_entities.py      → zoning_districts, use_types, use_permissions, development_standards, parking_rules
   → generate_notes.py        → normalized_vault/ atomic markdown (101 Phoenix notes so far + 4 overlays + 6 processes)
```

Every fact in the DB carries `source_document_id` + `source_section_id` + `extraction_run_id` + `raw_text` + `confidence`. The `extraction_runs` table is the full audit trail of every LLM/manual extraction call.

### Current state of the structured DB (schema v3)

| Table | Rows | Notes |
|---|---:|---|
| `legacy_note_classifications` | 593 | Whole vault categorized |
| `source_documents` | 593 | One per legacy markdown file |
| `source_sections` | 5,309 | Hierarchical heading-based split, FTS5-indexed |
| `vault_links` | 12,175 | Wikilinks + URLs + frontmatter relations |
| `jurisdictions` | 1 | `az.phoenix` (state AZ); Scottsdale/Mesa/etc. pending |
| `zoning_districts` | 22 | All Phoenix base zones, canonical IDs like `az.phoenix.zoning.c2` |
| `use_types` | 71 | Cross-jurisdictional vocabulary, slug-keyed; aliases table set up |
| `use_permissions` | 258 | (use × district × permission_type), all cited |
| `development_standards` | 92 | Height, FAR, lot size, setbacks, lot coverage where stated in vault |
| `parking_rules` | 6 | Phoenix multifamily 1.5 sp/du from R-2 through R-5 |
| `extraction_runs` | 66 | Audit; provider=`manual`, model=`claude-opus-4-7` |
| `notes` | 104 | Generated atomic markdown registry |

### Atomic notes produced (`normalized_vault/`)

| Folder | Count | What it is |
|---|---:|---|
| `Cities/` | 1 | `Phoenix.md` — index of all Phoenix zones with permission counts |
| `Zoning Codes/Phoenix/` | 22 | One per zone (`Phoenix C-2.md`, etc.) with permitted uses table, dev standards, parking, every fact cited back to its source section |
| `Use Types/` | 71 | Cross-zone view per use (`Mini-storage (self-storage).md`, etc.) — "where can I do this by right / by CUP / not at all?" |
| `Overlay Districts/` | 4 | Reference shells for Phoenix overlay notes |
| `Entitlement Processes/` | 6 | Reference shells for Phoenix process notes |

### How to query
- **Direct SQL** against `MetroData/zoning-intel/data/zoning.db` (SQLite, FTS5 enabled).
- **`scripts/_smoke_acceptance.py`** / **`scripts/_smoke_full_phoenix.py`** show example queries (e.g., "is self-storage permitted in Phoenix C-2?" → `conditional`, CUP, source-cited).
- **Generated markdown** in `normalized_vault/` is the human-facing surface — Obsidian-compatible frontmatter, wikilinks, source URLs.

### Key conventions (matters when adding cities or use types)
- **Canonical IDs** are dotted lowercase: jurisdictions like `az.phoenix`, districts like `az.phoenix.zoning.c2`, use types like `use.self_storage`. The pattern is enforced by Pydantic validators.
- **Source-grounding is required**: an extracted fact without `source_document_id` or `source_section_id` will fail Pydantic validation. The `notes` table can be wiped and regenerated; the `source_*` and `extraction_runs` tables are the durable record.
- **Idempotency by hash**: re-running `generate_notes.py` on unchanged data writes nothing. `last_extracted` timestamps are excluded from the content hash so disk modtimes don't churn.
- **The vault is read-only** to the pipeline. Never write into `CRE Knowledge Base/`. All output lands in `MetroData/zoning-intel/normalized_vault/`.

### What's left to build out (in zoning-intel)

In priority order:
1. **Run the API-based extractor on Scottsdale and Tempe** (`scripts/extract_entities.py --jurisdiction az.scottsdale --provider anthropic --model claude-sonnet-4-6`). Those two are the highest-quality verified vault content (§5 above) and would produce the cleanest second batch of structured data. Cost estimate: ~$0.50–$2 per city at Sonnet rates. The extractor is wired and tested; it just needs `ANTHROPIC_API_KEY` set.
2. **Curate the use-type vocabulary further.** 71 slugs after one pass; obvious next merges include `auto_sales_repair` vs `auto_service_repair`, and the various `assisted_living_*` and `accessory_*` variants. Edit `MERGES`/`DROPS` in `scripts/curate_use_types.py` and re-run; the `use_type_aliases` table picks up the merges so future extractions auto-apply.
3. **Promote `vault.*` canonical IDs on overlay/process docs.** The 4 Phoenix overlay notes and 6 process notes currently carry path-derived IDs like `vault.20_jurisdictions.arizona.cities.phoenix.overlays.overlay_transit_oriented_development`. Same migration pattern as `promote_stub_jurisdictions.py`, different table.
4. **Re-ingest from official ordinance sources.** When the owner provides the official Phoenix ZO §623 / §701 / §702 text, ingest those as new `source_documents` with `document_type='ordinance'`, then re-extract — the new facts will replace the vault-derived ones with much higher confidence and the same source-grounding contract.
5. **Build a CLI query interface** (e.g., `scripts/ask.py "where is self-storage permitted by right in az.phoenix?"`) wrapping the FTS5 + structured-DB joins shown in the smoke scripts.
6. **Add an overlay-fact extractor.** Currently overlays are passthrough reference shells. Real overlay extraction (which base-zone standards are modified, and how) is its own prompt + table — analogous to the existing zone extractor but with `modification_type` instead of `permission_type`.
7. **Add Nevada when ready.** The classifier already handles NV paths; the extractor will work the moment Nevada zone notes are populated in the vault.

## 7. Future phases (vault side)

- **Nevada full buildout** following [[Jurisdiction Pattern]]; then additional states. Once vault content lands, the zoning-intel pipeline above absorbs it automatically.
- **Case-study population** in `10-cre-brain/case-studies/`.
- **Periodic re-verification cycle** to refresh `source_last_verified` and aging market ranges.

## 8. Working with this vault: Do / Don't

**Do**
- Read this file → `_CONVENTIONS.md` → the relevant index, before writing.
- Use the matching `_templates/` template; populate structured frontmatter (`related`/`parent`/`children`/`source_url`).
- Mark new content `status: draft`; keep `needs-verification` on any unconfirmed numeric standard.
- Write `TBD — verify against {section}` instead of guessing a standard, code, or fee.
- Update this "Current state" section and [[Changelog]] at the end of each work session.
- Quote frontmatter strings containing `:`/`{`/`}`/`[`/`]`.

**Don't**
- Don't present any `TBD`/`draft` numeric zoning standard as fact.
- Don't fabricate zone codes, ordinance section numbers, fees, or dimensional standards.
- Don't promote a note to `reviewed`/`authoritative` — that is a human action.
- Don't backfill `source_last_verified` with an authoring date; leave blank until a human verifies.
- Don't put non-note items (e.g., an ordinance, a data provider) in `related:` — those belong in `source_url`/prose.
- Don't invent folders/files outside the documented structure; keep the scaffold strict.
- Don't touch `Welcome.md` or `.obsidian/`.

---
*Build history:*
- *Prompts 1–5 complete (2026-05-24 → 2026-05-25). Whole-vault audit 2026-05-25: 0 broken `related:` refs, 0 duplicate titles, 0 invalid types, all valid UTF-8.*
- *2026-05-26: companion `zoning-intel/` system built (Phases 0–4). All 593 vault notes classified and ingested; all 22 Phoenix zones extracted into structured DB (258 use-permissions, 92 dev standards, 6 parking rules) and regenerated as 104 atomic notes in `MetroData/zoning-intel/normalized_vault/`. Schema at v3, 48 tests passing. See `MetroData/zoning-intel/CLAUDE.md` for the project handoff.*
- *See [[Changelog]] for vault-side detail.*
