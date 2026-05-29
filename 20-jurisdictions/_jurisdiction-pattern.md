---
title: Jurisdiction Pattern
type: reference
tags: [juris, conventions]
created: 2026-05-24
updated: 2026-05-24
status: authoritative
ai_summary: Canonical recipe for scaffolding any state's zoning knowledge — folder structure, naming, frontmatter, order of operations, and quality gates.
---

# Jurisdiction Pattern

The canonical recipe for adding a state's zoning and development-standards knowledge to this vault. **Giving a future AI session this file plus a state name is sufficient instruction to scaffold that state.** The structure is deliberately mechanical so every state looks identical and AI traversal stays predictable.

> **Governing principle — do not fabricate.** This is a regulatory knowledge base. Never state a numeric standard (height, setback, FAR, density/DUA, lot size, lot width, coverage, parking ratio), an ordinance section number, a fee, or a statutory deadline as fact unless it is definitional or you can cite a verified source. For every unconfirmed value write `TBD — verify against {ordinance section}`, keep the numeric frontmatter field as `TBD`, and add the `needs-verification` tag. Populate **qualitative** content (zone purpose, permitted-use categories, process flow, agency roles) confidently. `source_last_verified` stays blank until a **human** confirms the value against the live source — never backfill it with the authoring date.

---

## 1. Folder structure required per state

```
{state}/                              # lowercase full name: arizona, nevada
├── 00-state-overview.md              # template-jurisdiction-state
├── state-statutes/                   # one note per major land-use title/chapter
│   └── {slug}.md
├── counties/
│   └── county-{slug}.md              # template-jurisdiction-county per county
├── cities/
│   └── {city-slug}/
│       ├── 00-overview.md            # template-jurisdiction-city
│       ├── zones/
│       │   └── zone-{code}.md        # template-zone per base zone district
│       ├── overlays/
│       │   └── overlay-{slug}.md     # template-overlay per overlay district
│       ├── standards/
│       │   └── {slug}.md             # template-development-standard (citywide)
│       └── processes/
│           └── {slug}.md             # template-process (entitlement procedures)
└── special-districts/                # tribal, military, CFDs, water/improvement districts
    └── {slug}.md
```

A city built "overview-only" still gets its folder; create the `zones/overlays/standards/processes/` subfolders only when you populate them (or leave empty subfolders as placeholders per the pattern).

---

## 2. Naming conventions

- **State folder:** lowercase full name — `arizona`, `nevada`.
- **Statute note:** descriptive slug — `ars-title-9-municipal-zoning.md`.
- **County file:** `county-{slug}.md` — `county-maricopa.md`.
- **City folder:** `{city-slug}/` — `phoenix/`, `lake-havasu-city/`.
- **City overview:** `00-overview.md` inside the city folder.
- **Zone file:** `zone-{code-lowercased-hyphenated}.md` — `zone-r1-6.md`, `zone-c-2.md`.
- **Overlay file:** `overlay-{slug}.md` — `overlay-downtown.md`.
- **Standard file:** `{slug}.md` — `parking.md`, `landscape.md`, `signage.md`.
- **Process file:** `{slug}.md` — `conditional-use-permit.md`, `rezoning.md`.

**Canonical note titles (for wikilinks / `related` / `parent` / `children`):**
- State overview: `"{State} State Overview"` — e.g., `"Arizona State Overview"`.
- County: `"{County} County, {State}"` — e.g., `"Maricopa County, Arizona"`.
- City overview: `"{City}, {State}"` — e.g., `"Phoenix, Arizona"`.
- Zone: `"{City} {CODE}"` — e.g., `"Phoenix R1-6"`, `"Phoenix C-2"`.
- Overlay/standard/process: descriptive, city-scoped — e.g., `"Phoenix Downtown Overlay"`, `"Phoenix Parking Standards"`, `"Phoenix Conditional Use Permit"`.
City-scoping titles keeps them unique across cities and states so wikilinks never collide.

---

## 3. Required frontmatter by level

(Restated from `_CONVENTIONS.md` §3 for convenience. Universal fields — `title, type, tags, created, updated, status, ai_summary` — always apply.)

**State** (`type: jurisdiction`, `level: state`): `state` (postal), `parent_jurisdiction: null`, `population`, `zoning_authority`, `code_url`, `gis_url`, `source_url`, `source_last_verified` (blank until verified), `related`, `children` (county titles).

**County** (`type: jurisdiction`, `level: county`): `state`, `parent_jurisdiction` (state title), `population`, `zoning_authority`, `code_url`, `gis_url`, `source_url`, `source_last_verified`, `related`, `children` (city titles).

**City** (`type: jurisdiction`, `level: city`): `state`, `parent_jurisdiction` (county title), `population`, `zoning_authority`, `code_url`, `gis_url`, `source_url`, `source_last_verified`, `related`, `children` (zone/overlay/standard/process titles).

**Zone** (`type: zone`): `jurisdiction` ("City of X"), `state`, `zone_code`, `zone_name`, `permitted_uses` (categories), `max_height_ft`, `max_density_dua`, `max_far`, `min_lot_size_sf`, `setbacks{front,side,rear}`, `parking_ratio`, `source_url`, `source_last_verified`, `related`, `parent` (city title). Numeric fields default to `TBD` until verified.

**Standard** (`type: standard`): `jurisdiction`, `state`, `applies_to`, `source_url`, `source_last_verified`, `related`.

**Overlay** (`type: overlay`): `jurisdiction`, `state`, `base_zones_affected`, `source_url`, `source_last_verified`, `related`.

**Process** (`type: process`): `jurisdiction`, `state`, `decision_maker`, `appeal_path`, `source_url`, `source_last_verified`, `related`.

> **YAML trap:** any frontmatter string containing `:`, `{`, `}`, `[`, `]` (e.g., a title like `"Contingency: Hard vs. Soft"`) MUST be quoted, including inside list items (`related: ["Some: Title"]`). Unquoted, YAML mis-parses it as a nested mapping.

---

## 4. Order of operations when adding a state

1. **State folder + `00-state-overview.md`** (template-jurisdiction-state). Cover enabling statutes, home-rule vs. Dillon's-Rule status, state agencies, tax/closing norms, statewide programs.
2. **`state-statutes/` notes** for the major land-use titles/chapters (enabling authority for municipal and county zoning, real-estate licensing, property, water, etc.).
3. **`counties/` notes** — at minimum every county containing a major MSA. Focus on unincorporated-area zoning.
4. **Per priority city:** create the city folder, `00-overview.md`, then enumerate base zones in `zones/`, then `overlays/`, then citywide `standards/`, then entitlement `processes/`. Lower-priority cities may be overview-only until a later pass.
5. **Cross-link** via wikilinks AND frontmatter `related`/`parent`/`children` (by title).
6. **Add every source URL** to `00-meta/data-sources.md`.
7. **Update** the state overview (link all counties/cities), `20-jurisdictions/00-index.md`, and `CLAUDE.md` current state.

For numeric standards you cannot verify, follow the governing principle above (TBD + `needs-verification`). Enumerate a city's full zone roster only when you can do so accurately; otherwise build the overview + scaffold and defer zone enumeration to a later code-fetch/ingestion pass.

---

## 5. Quality gates (status lifecycle for jurisdiction notes)

- **`stub`** — frontmatter only, or a folder placeholder; no real content yet.
- **`draft`** — qualitative content populated from general knowledge (purpose, use categories, process flow). Numeric standards may still be `TBD`/`needs-verification`. **AI may produce notes up to this level.**
- **`reviewed`** — a human has confirmed the qualitative content and the zone roster is correct against the current code.
- **`authoritative`** — a human has verified **all** numeric standards and citations against the live ordinance, removed the `needs-verification` tag, set `source_last_verified` to the confirmation date, and filled every `TBD`. Only then may the note be cited as fact.

A zone note stays `draft` (not `authoritative`) as long as any dimensional standard is `TBD` or the `needs-verification` tag is present. Promotion to `reviewed`/`authoritative` is a **human action only**.
