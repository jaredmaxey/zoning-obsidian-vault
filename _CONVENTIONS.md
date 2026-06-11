---
title: Vault Conventions
aliases: ["Vault Conventions"]
type: reference
tags: [meta, conventions]
created: 2026-05-24
updated: 2026-05-24
status: authoritative
ai_summary: The canonical rule set for filenames, YAML frontmatter, tags, linking, source attribution, and status lifecycle that every note in this vault must follow.
---

# Vault Conventions

This is the **source of truth** for how every note in this vault is named, structured, tagged, and linked. AI sessions and humans must follow these rules exactly. When a template in `_templates/` and this file disagree, **this file wins** — fix the template.

The vault's primary consumer is AI tooling (Claude Code, Claude.ai, etc.); the secondary consumer is a human reading in Obsidian. Every rule below optimizes for **machine traversal first**: consistent frontmatter, predictable filenames, explicit relational fields, and plain markdown over Obsidian-only syntax.

---

## 1. Filename rules

- **All lowercase, kebab-case, `.md` extension.** Example: `cap-rate.md`, `yield-on-cost.md`.
- **No spaces. No underscores in note filenames.** Underscores are reserved for special folders and meta-files only (`_templates/`, `_CONVENTIONS.md`, `_jurisdiction-pattern.md`).
- **No special characters** other than hyphens. Strip apostrophes, slashes, parentheses, ampersands (write `and`).
- **Date-prefixed notes** (case studies, dated changelog entries) use ISO `YYYY-MM-DD-` prefix: `2026-05-24-acme-value-add.md`.
- **Index notes** are named `00-index.md` (or `00-overview.md` for asset-class and city entry points) so they sort to the top of their folder.
- **Jurisdiction notes** follow `{type}-{slug}.md`:
  - County: `county-maricopa.md`
  - City overview lives in a per-city folder as `00-overview.md` (folder name is the city slug, e.g., `phoenix/00-overview.md`).
  - Zone: `zone-{code-lowercased-hyphenated}.md` → `zone-r1-6.md`, `zone-c-2.md`.
  - Overlay: `overlay-{slug}.md` → `overlay-downtown.md`.
  - Statute: descriptive slug → `ars-title-9-municipal-zoning.md`.
- **Slugs** are derived from the human title: lowercase, replace spaces/punctuation with single hyphens, no leading/trailing hyphens, no doubled hyphens.

---

## 2. YAML frontmatter — universal fields (EVERY note has these)

Every note in the vault begins with this block. No exceptions — a note without frontmatter is invalid.

```yaml
---
title: Human-readable title
aliases: ["Human-readable title"]
type: concept | deal-type | asset-class | framework | case-study | jurisdiction | zone | standard | overlay | process | reference | index | template
tags: [tag1, tag2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: stub | draft | reviewed | authoritative
ai_summary: One-sentence summary for AI context windows.
---
```

Field rules:
- **title** — Title Case, human-readable. Not the filename. Two jurisdiction title conventions coexist: built-out cities use `{City}, Arizona` (e.g., `Chandler, Arizona`); scaffold-stage jurisdictions use the legal name `City of {X}` / `Town of {X}` (e.g., `City of Apache Junction`). When a scaffold is built out, retitle it to the `{City}, Arizona` form and update all referring links/frontmatter.
- **aliases** — REQUIRED whenever `title` differs from the filename (it almost always does, since filenames are kebab-case slugs). Must contain at least the exact `title` string. This is what makes title-based wikilinks resolve in Obsidian — see §5. Enforced by `40-data/_tools/add_aliases.py` (dry-run by default; `--apply` to fix).
- **type** — exactly one value from the enum above. These are the only legal `type` values in the vault. (See §3 for the fields each type adds.)
- **tags** — YAML list; see §4 for the taxonomy. Always omit the leading `#` inside the YAML array (`tags: [cre/financing, stub]`), but use `#` when tagging inline in prose.
- **created / updated** — ISO dates. `updated` changes every time the note's content materially changes.
- **status** — see §7.
- **ai_summary** — ONE declarative sentence (≤ 30 words). This is what an AI reads first to decide if the note is relevant. Make it specific and information-dense.

---

## 3. YAML frontmatter — type-specific fields

Each `type` adds required fields **on top of** the universal block. Optional fields are marked `(optional)`. Relational fields (`related`, `parent`, `children`) are always YAML lists of note **titles** (see §5).

### type: concept
For CRE concepts (cap rate, DSCR, yield on cost).
```yaml
domain: concepts | financing | underwriting | construction | operations   # which 10-cre-brain branch
formula: true | false            # does this concept have a formula?
related: []                      # titles of related notes
```

### type: deal-type
For deal archetypes (value-add acquisition, ground-up development).
```yaml
typical_hold_years: "X–Y"
risk_profile: core | core-plus | value-add | opportunistic
related: []
```

### type: asset-class
For asset-class deep dives.
```yaml
asset_class: multifamily | office | retail | industrial | hospitality | self-storage | mixed-use | ground-up-development | land | specialty
subtypes: []                     # list of subtype names
related: []
```

### type: framework
For analytical frameworks (highest-and-best-use, four-quadrant model).
```yaml
inputs_required: []              # list of input data the framework consumes
outputs: []                      # list of what it produces
related: []
```

### type: case-study
For deal write-ups.
```yaml
asset_class: <one of the asset_class values>
deal_type: <e.g., value-add acquisition>
location: "City, ST"
deal_size: "$XX.XM"              # total capitalization
outcome: realized | in-progress | hypothetical
key_lessons: []                  # list of one-line takeaways
related: []
```

### type: jurisdiction
For state / county / city overview notes.
```yaml
level: state | county | city
state: AZ | NV | ...             # two-letter postal
parent_jurisdiction: <title or null>   # e.g., a city's county; a county's state
population: <integer or "TBD">
zoning_authority: <name of governing body / department>
code_url: <URL to the zoning/land-use code, or TBD>
gis_url: <URL to the GIS / zoning map, or TBD>
source_url: <primary source, or TBD>
source_last_verified: YYYY-MM-DD | ""   # blank until a human verifies
related: []
children: []                     # e.g., a state's counties; a city's zones
```

### type: zone
The most important zoning type. For a single base zone district.
```yaml
jurisdiction: <city title, e.g., "City of Phoenix">
state: AZ
zone_code: R1-6
zone_name: "Single-Family Residence District"
permitted_uses: []              # high-level use categories permitted by-right
max_height_ft: <number or "TBD">
max_density_dua: <number or "TBD">       # dwelling units per acre
max_far: <number or "TBD">               # floor area ratio
min_lot_size_sf: <number or "TBD">
setbacks:                        # in feet; use "TBD" for unknown
  front: <number or "TBD">
  side: <number or "TBD">
  rear: <number or "TBD">
parking_ratio: <string, e.g., "2 per unit" or "TBD">
source_url: <URL to the ordinance section>
source_last_verified: YYYY-MM-DD | ""
related: []                      # adjacent/compatible zones, governing standards
parent: <city overview title>
```

### type: standard
For standalone development standards applying across zones (citywide parking, landscape ordinance).
```yaml
jurisdiction: <city/county/state title>
state: AZ
applies_to: []                  # zones or use types the standard governs
source_url: <URL>
source_last_verified: YYYY-MM-DD | ""
related: []
```

### type: overlay
For overlay districts (historic, transit, hillside).
```yaml
jurisdiction: <city title>
state: AZ
base_zones_affected: []         # zones the overlay can sit on top of
source_url: <URL>
source_last_verified: YYYY-MM-DD | ""
related: []
```

### type: process
For entitlement processes (CUP, variance, GPA, rezoning, site plan review).
```yaml
jurisdiction: <city/county/state title, or "general"> 
state: AZ | "" 
decision_maker: <body that decides, e.g., "Planning Commission">
appeal_path: <where appeals go>
source_url: <URL or TBD>
source_last_verified: YYYY-MM-DD | ""
related: []
```

### type: reference
For lookup tables in `30-reference/` and the meta registries.
```yaml
related: []                      # (optional)
```

### type: index
For hub/index notes.
```yaml
covers: <one-line description of what this index aggregates>
```

### type: template
For files in `_templates/`.
```yaml
template_for: <the type this template produces>
```

---

## 4. Tagging taxonomy

Hierarchical tags use `/`. In YAML frontmatter omit the leading `#`; in prose include it. Top-level namespaces:

- `cre/` — CRE brain content. Examples: `cre/financing`, `cre/underwriting`, `cre/concepts`, `cre/operations`.
- `asset/` — asset class. Examples: `asset/multifamily`, `asset/industrial`, `asset/office`.
- `juris/` — jurisdiction. Examples: `juris/az`, `juris/az/phoenix`, `juris/nv`.
- `zoning/` — zoning concept. Examples: `zoning/residential`, `zoning/commercial`, `zoning/mixed-use`.
- `standard/` — development standard. Examples: `standard/setback`, `standard/parking`, `standard/far`.
- `process/` — entitlement process. Examples: `process/cup`, `process/variance`, `process/rezoning`.
- `stub` — flat tag for notes that need filling in.
- `needs-verification` — flat tag for content (especially numeric standards) that requires source checking before it can be trusted.

Rules:
- Apply the most specific tags that fit. A Phoenix C-2 zone note carries `juris/az/phoenix`, `zoning/commercial`, and any `standard/*` tags for standards it documents.
- Every `status: stub` note must also carry the `stub` tag (and vice versa) so both queries find it.
- Numeric zoning values sourced from memory rather than a verified ordinance get `needs-verification`.

---

## 5. Linking conventions

- **Internal references use wikilinks** `[[note-title]]`, linking by **title**, not by path. This keeps links intact when notes move between folders.
- **Why `aliases` is mandatory (§2):** Obsidian resolves wikilinks by *filename or alias*, never by the `title:` frontmatter field. Because vault filenames are kebab-case slugs that differ from titles, a title-based link only resolves when the target note carries its title in `aliases`. Without it, links show as unresolved, backlinks/graph view break, and clicking a link creates a stray empty note at the vault root. Run `python 40-data/_tools/add_aliases.py` to audit (add `--apply` to fix).
- **Relational frontmatter is mandatory for AI queries.** In addition to prose wikilinks, populate the structured fields so a script can read relationships without parsing prose:
  - `related: []` — peer notes (lateral relationships).
  - `parent: <title>` — the containing/owning note (e.g., a zone's city; a subtype's asset class).
  - `children: []` — notes this one owns (e.g., a city's zones; a state's counties).
- Values in these fields are note **titles** (matching the `title:` frontmatter), not filenames or paths.
- A `related`/`parent`/`children` entry may point to a note that does not exist yet — that is a valid "to-be-written" marker, not an error. Prompt 5 audits these for true breakage.

---

## 6. Source attribution

Every fact pulled from an external code, ordinance, statute, or data source MUST be attributable. For such notes:

- `source_url:` in frontmatter — direct link to the governing section where possible.
- `source_last_verified: YYYY-MM-DD` in frontmatter — the date a **human** last confirmed the value against the live source. Leave **blank** (`""`) until verified; do not backfill with the authoring date.
- **Inline citation in prose** at the point of the claim:
  `(Source: Phoenix Zoning Ordinance § 608, verified 2026-05-24)`
  If unverified: `(Source: Phoenix Zoning Ordinance § 608 — UNVERIFIED)`.
- If you cannot confirm a numeric standard, write `TBD — verify against {ordinance section}` rather than guessing, and add the `needs-verification` tag.

---

## 7. Status lifecycle

`stub` → `draft` → `reviewed` → `authoritative`

- **stub** — placeholder. Frontmatter exists; body is empty or one or two sentences. Treat as **low confidence**. Carries the `stub` tag.
- **draft** — substantive AI-generated content present (real, useful starter content), but not human-verified. Numeric/source-dependent claims may still be unverified.
- **reviewed** — a human has read the note and confirmed the qualitative content is correct, but some sourced values may still be pending verification.
- **authoritative** — a human has verified all sourced/numeric values against live sources, `source_last_verified` is set and recent, and the note can be cited with confidence.

A note advances only when the bar for the next level is met. AI sessions may move a note from `stub`→`draft` by adding content, but **never** to `reviewed` or `authoritative` — those require human action.

---

## 8. AI usage notes

For any AI session working in this vault:

1. **Read `CLAUDE.md` first**, then this file. `CLAUDE.md` carries current-state and do/don't guidance; this file carries the rules.
2. Treat any note with `status: stub` as **low confidence** — do not cite it as settled fact.
3. Treat a note with `status: authoritative` **and** a recent `source_last_verified` as the best available source.
4. When citing a sourced value with `source_last_verified` blank or older than 12 months, **flag the answer as needing re-verification**.
5. When writing new notes, **copy the matching template from `_templates/` and follow it exactly** — do not invent structure.
6. Never fabricate numeric zoning standards. Use `TBD — verify against {section}` and the `needs-verification` tag.
7. Prefer structured frontmatter fields over prose for any relational or quantitative claim, so future automated traversal stays reliable.

---

## 9. Structured data layer (`40-data/`)

The vault carries a machine-first **structured data layer** in `40-data/` alongside the markdown. It exists so the vault can be queried, compared across jurisdictions, and synced with high fidelity — not just read. This folder is a deliberate, instructed extension of the top-level structure (it is the one sanctioned exception to "never invent top-level folders" in `CLAUDE.md`).

### 9.1 Layout

```
40-data/
  00-index.md            # index note describing the layer
  jurisdictions.csv      # CANONICAL — one row per jurisdiction
  source_registry.csv    # CANONICAL — every primary-source doc (machine-readable INDEX.html + data-sources.md)
  parking_standards.csv  # CANONICAL — parking ratios by use × jurisdiction
  zoning_standards.csv   # GENERATED — flat projection of zones/*.json (do not hand-edit)
  zones/{jurisdiction_id}.json   # CANONICAL — per-zone records (numbers + use lists + citations)
  _tools/                # schema + validate.py + sync.py
```

### 9.2 Canonical vs. derived (the anti-drift rule)

- **Canonical**, edited by hand or AI: `jurisdictions.csv`, `source_registry.csv`, `parking_standards.csv`, and the per-zone JSONs in `zones/`. The JSON is the single source of truth for a zone's dimensional numbers **and** its nested data (permitted/conditional/prohibited use lists, multi-value citations, overlay interactions).
- **Derived**, never hand-edited — regenerated by `sync.py`: `zoning_standards.csv` (flat numeric projection of the zone JSONs) and, inside each markdown zone note, the **Development Standards table + numeric frontmatter fields**, rewritten only between the markers `<!-- BEGIN:standards (generated) -->` … `<!-- END:standards -->`.
- **Canonical in markdown**, untouched by the script: all prose (`## Summary`, `## Development Implications`, `## Analytical Interpretation`, permitted-use narrative). Numbers flow data → markdown; prose stays in markdown.

After editing any canonical data file: run `python 40-data/_tools/validate.py`, then `python 40-data/_tools/sync.py`. Never hand-edit a generated region or `zoning_standards.csv`.

### 9.3 IDs

- `jurisdiction_id = az-{slug}` — e.g., `az-phoenix`, `az-maricopa-county`.
- `zone_id = {jurisdiction_id}:{zone_code-lowercased}` — e.g., `az-phoenix:r-3`.
- These join the CSVs, the JSONs, and the markdown notes (whose `title:`, e.g. "Phoenix R-3", is the human label).

### 9.4 Provenance & confidence (data-layer enforcement of §6)

Every zone record and standards row carries explicit lineage. This maps the §6 source-attribution rules into machine-readable columns and is how the layer prevents fabrication:

- `provenance`: `official-pdf` | `official-html` | `secondary-mirror` | `inferred` | `unknown`
- `confidence`: `verified-human` | `extracted` | `low` | `tbd`
- `source_doc` (registry id/title), `source_citation` (e.g., `§ 615`), `source_page` (PDF page), `extracted_date`
- `human_verified`: date or blank — the data-layer equivalent of `source_last_verified` (§6/§7).

**AI may set `confidence: extracted` with `provenance: official-pdf`/`official-html` when a value is pulled directly from an official document, but never `confidence: verified-human` and never a `human_verified` date** — only a human promotes, exactly as in §7. A value taken from a non-official mirror is `provenance: secondary-mirror, confidence: low`. When an official value supersedes an older mirror value, update the record and record the old value + supersession in `notes` (and `00-meta/changelog.md`) — never silently overwrite (per `CLAUDE.md`).

A zone note may advance `stub`→`draft` once its standards are extracted from an official source, but stays `needs-verification` until a human sets `human_verified`.
