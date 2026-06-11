---
title: Structured Data Layer
aliases: ["Structured Data Layer"]
type: index
tags: [meta, data, juris/az]
created: 2026-06-05
updated: 2026-06-05
status: draft
ai_summary: Machine-first CSV + JSON layer holding the Maricopa jurisdiction registry, primary-source registry, and per-zone dimensional standards that sync into the markdown notes.
covers: The 40-data structured layer — registries, per-zone standards, and the validate/sync tooling.
---

# Structured Data Layer (`40-data/`)

The machine-first counterpart to the markdown vault. It makes the vault queryable and comparable across jurisdictions with explicit source lineage. Full rules: [[Vault Conventions]] §9.

## Files

| File | Role | Canonical? |
|------|------|-----------|
| `jurisdictions.csv` | One row per Maricopa jurisdiction (code host, URLs, vault path) | **Canonical** |
| `source_registry.csv` | One row per primary-source document (machine form of the Maricopa `INDEX.html`) | **Canonical** |
| `parking_standards.csv` | Parking ratios by use × jurisdiction | **Canonical** |
| `zones/{jurisdiction_id}.json` | Per-zone dimensional standards + use lists + citations | **Canonical** |
| `zoning_standards.csv` | Flat projection of all zone JSONs for Excel / cross-jurisdiction querying | _Generated_ |
| `_tools/validate.py` | Schema + referential-integrity checks | tool |
| `_tools/sync.py` | Regenerates the CSV projection, the markdown standards tables, and the parking reference | tool |
| `_tools/schema/` | `zone.schema.json` + `columns.md` column specs | spec |

## Source of truth

Primary sources live in `../Maricopa County development standards/` (official PDFs, live-code `.url` links, and `INDEX.html`). That library is authoritative for Maricopa jurisdictions and supersedes any secondary mirror (e.g. zoneomics) previously used in the zone notes.

## Workflow

1. Edit a **canonical** file (a `zones/*.json`, or one of the canonical CSVs).
2. `python 40-data/_tools/validate.py` — must exit 0.
3. `python 40-data/_tools/sync.py` — regenerates `zoning_standards.csv`, the `BEGIN/END:standards` regions + numeric frontmatter of the linked zone notes, and `30-reference/parking-ratios-by-use.md`.

Never hand-edit `zoning_standards.csv` or any region between the generated markers — `sync.py` overwrites them. Use `sync.py --check` to detect drift.

## Provenance & confidence

Every extracted value carries `provenance` (`official-pdf`/`official-html`/`secondary-mirror`/`inferred`/`unknown`) and `confidence` (`verified-human`/`extracted`/`low`/`tbd`). AI extraction is capped at `extracted`; only a human sets `human_verified`. See [[Vault Conventions]] §9.4.

## Coverage status

- **Registries:** all 26 Maricopa jurisdictions + 77 source documents loaded.
- **Zone extraction: COMPLETE — all 26 Maricopa jurisdictions, 534 base zones.** **533 of 534 carry official-source citations** (`official-pdf`/`official-html`; the lone exception is the Phoenix Walkable Urban placeholder). 506 (94%) have at least one extracted core value. None human-verified yet.
- **Depth work remaining (not breadth):** special/PUD/form-based districts (e.g. Phoenix WU transects), per-use parking ratios → `parking_standards.csv`, and human verification (promote `extracted` → `verified-human`, set `human_verified`). Tucson is out of scope (Pima County).
- **Source-access map (for re-verification):** Municode → `api.municode.com`; American Legal → browser User-Agent / `/api/render-doc/`; General Code (`*.municipal.codes`/`*.town.codes`) → Chrome (Cloudflare); Municipal Code Online → browser; PDFs → read directly.

## Related

- [[Jurisdictions Index]]
- [[Data Sources Registry]]
- [[Parking Ratios by Use]]
