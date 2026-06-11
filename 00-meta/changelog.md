---
title: Changelog
type: reference
tags: [meta, changelog]
created: 2026-05-24
updated: 2026-06-08
status: authoritative
ai_summary: Reverse-chronological log of structural and content changes to the vault, one dated entry per significant build step.
---

# Changelog

Reverse-chronological. Newest entries on top. One dated heading per significant change; bullets beneath.

## 2026-06-08 (Pinal County extraction — all 10 jurisdictions, mirrors the Maricopa/Pima build)

- **Third county done.** Applied the same data-layer treatment to the new `Pinal County development standards/` source-of-truth folder. Added 10 jurisdictions to `jurisdictions.csv` + 23 rows to `source_registry.csv`, and extracted **163 base zones into `40-data/zones/`** (8 of 10 jurisdictions populated; 2 empty by necessity — see below). `validate.py` clean (**42 files / 815 zones** total across all three counties); `sync.py --check` clean.
  - **Municode JSON API:** Pinal County unincorporated — Development Services Code, Title 2 Zoning (50 zones, 48 with standards; the county runs two parallel active district series — pre-2010 "C-series" + 2010-modernized RU-/R-/AC-).
  - **American Legal (render-doc API):** Casa Grande — Code Title 17 (17 zones, 16 w/ standards); Eloy — City Code Ch. 21 (18 zones, all); Florence — Zoning & Development Code Ch. 150 (18 zones, all).
  - **General Code (Cloudflare — via Chrome):** City of Maricopa [Pinal, id `az-maricopa-city`] — City Code Title 18 (22 zones, 21 w/ standards).
  - **Local PDF:** Coolidge — folder's `Coolidge_ZoningCode.pdf` (17 zones, 15 w/ standards, `official-pdf`).
  - **Town websites:** Mammoth — Land Codes Art. 14 (5 zones; the SPA's JS bundle revealed per-section PDFs at `/documents/land-codes/14-N-*.pdf`); Superior — the 2024 Zoning Ordinance PDF linked off the P&Z page (16 zones, 15 w/ standards).
- **Honest gaps (flagged, not faked):**
  - **Town of Kearny — 0 zones.** Its Municode entry is a **document repository only** (MuniDocs: agendas/minutes/resolutions) with **no codified code of ordinances or zoning**. `az-kearny.json` left empty; overview flags the gap.
  - **Town of Winkelman — 0 zones.** The folder holds only the 2018 *Community Development Strategy* (a CDBG parcel survey + policy doc), **not a zoning code**. `az-winkelman.json` left empty; overview flags the gap. (Winkelman straddles Gila/Pinal; tracked under Pinal.)
  - For both, add an actual zoning ordinance to the source folder to enable extraction. As with Maricopa/Pima: FAR/stories/density are TBD wherever the codes don't state them; planned/PAD districts are all-TBD by nature; commercial/industrial "no minimum lot" recorded as TBD (not 0).
- **Markdown:** created 7 new city overviews (Coolidge, Eloy, Florence, Kearny, Mammoth, Superior, Winkelman); added Primary Sources + data-linked zone tables to Casa Grande + Maricopa-City overviews and the Pinal county note; expanded the county's `children` + Cities Within to all 9 municipalities (noting Apache Junction straddles Maricopa/Pinal, tracked under Maricopa).
- **Fixed** a one-row CSV misalignment in the Winkelman `jurisdictions.csv` row (13→14 fields) caught when sync reported "overview not found".
- **Arizona rollout status:** Maricopa (26) + Pima (6) + Pinal (10) = **42 jurisdictions, 815 zones** in the data layer, all AI-`extracted` / `needs-verification`. Counties still unbuilt in the data layer: Yavapai, Coconino, Mohave, Yuma (markdown county stubs exist).

## 2026-06-07 (Pima County extraction — all 6 jurisdictions, mirrors the Maricopa build)

- **Began the second county.** Applied the same data-layer treatment used for Maricopa to the new `Pima County development standards/` source-of-truth folder. Added 6 jurisdictions to `jurisdictions.csv` + 18 rows to `source_registry.csv`, and extracted **118 base zones, all official-sourced (`official-html`), into `40-data/zones/`** (5 of 6 jurisdictions populated; 1 empty by necessity — see below). `validate.py` clean (32 files / 652 zones); `sync.py --check` clean.
  - **American Legal (render-doc JSON API):** Pima County unincorporated — Title 18 (26 zones, 25 with ≥1 numeric standard); City of Tucson — UDC Article 4 / Tables 6.3-1.A–6.3-7.A (30 zones, 28 with standards); Town of Marana — LDC Title 17 §17-4 Tables 1–20 (23 zones, all with standards).
  - **General Code (Cloudflare — read via browser):** Town of Oro Valley — OVZC §23.1 + Tables 23-2A/2B (21 zones, 19 with standards).
  - **Code Publishing (browser):** Town of Sahuarita — Title 18 Ch. 18.05 + standards chapters (18 zones, 17 with standards).
- **Honest gaps (flagged, not faked):**
  - **City of South Tucson — 0 zones.** The folder's official source (Municode City Code **Chapter 24, Zoning**) currently publishes no district text — every section renders *"Chapter 24 is currently being updated and will post online soon."* `az-south-tucson.json` was created with an empty zone list rather than inventing data; the new overview flags the source gap. Re-run when Municode posts Chapter 24, or add an alternate official source to the folder.
  - **Tucson setbacks = TBD** by design — the UDC uses formula-based "perimeter yards" (height/adjacency multiples), not fixed numbers. **FAR/stories** TBD across most jurisdictions (these codes regulate by height-in-feet + coverage). Density (dua) recorded only where the code states a per-acre cap; per-square-foot/per-unit minimums left TBD with the basis in `notes`. Planned districts (Tucson PAD/PCD, Oro Valley PRD/PAD) and performance zones (Pima GC, Sahuarita GC) are all-TBD by nature.
  - **Tucson per-zone notes NOT wired.** Tucson's 28 existing `zones/*.md` notes carry richer, separately sourced setback formulas; `note_path` was left empty so `sync.py` does not overwrite them with the conservative (TBD-heavy) UDC extraction. The data-linked Zone Standards table in the overview reflects the new extraction.
- **Markdown:** added Primary Sources sections + data-linked Zone Standards tables to the Pima county note and the Tucson/Marana/Oro Valley/Sahuarita overviews; created a new South Tucson overview; added South Tucson to the county's children + Cities Within (Marana noted as straddling Pima/Pinal).
- **Pinal County is next** (deferred to a separate pass per the one-county-at-a-time review cadence). All Pima values remain AI-`extracted` / `needs-verification` until a human confirms against the live sources.

## 2026-06-06 (Maricopa extraction — batch 4: COMPLETE, all 26 jurisdictions)

- **Extracted the final 6 jurisdictions** (72 zones), completing **all 26 Maricopa jurisdictions: 534 zones, 533 official-sourced** (380 `official-html` + 153 `official-pdf`; the lone `secondary-mirror` is the Phoenix Walkable Urban placeholder). **506 of 534 zones (94%) carry at least one extracted core value.**
  - **American Legal (browser route):** El Mirage (9), Carefree (11), Guadalupe (10), Apache Junction was batch 3. American Legal's render-doc JSON API (`/api/render-doc/...`) returned the full intensity tables.
  - **Per-chapter city PDFs:** Cave Creek (13) — read directly from the Town's official chapter PDFs (current Ch. 2/3 eff. 12/4/25).
  - **Municipal Code Online:** Wickenburg (21) — official ordinance (Ord. 1221, 2021).
  - **Paradise Valley (8) — recovered.** The folder's `ParadiseValley_ZoningOrdinance_2023.pdf` is only a 1-page cover sheet, but the agent located the **official Article X PDFs on the Town's DocumentCenter** (Tables 1001-A1/A2, Ord. 2021-01) and extracted all base R-districts. PV has no commercial/industrial base zones (those run through Special Use Permits).
- **Honest gaps (flagged, not faked):** Guadalupe I-1/I-2 are established in §154.051 but the code contains no standards section for them (TBD); Carefree OS-R and El Mirage NR are "per site plan" / master-plan districts with no fixed table; PV/Carefree regulate by FAR (0.25 / lot-coverage) and height-in-feet rather than dua. Lot-size-based height schedules (PV) and tier-based standards (Wickenburg RM) recorded at the binding minimum with the full schedule in `notes`.
- Verified: `validate.py` clean (534 zones, 0 errors); `sync.py --check` clean; stray agent artifacts cleaned up.
- **Maricopa coverage is now complete.** Out of scope: Tucson (Pima County). Remaining future work is depth, not breadth: special/PUD/form-based districts (e.g. Phoenix WU transects), per-use parking ratios into `parking_standards.csv`, and human verification (promoting `extracted` → `verified-human`).

## 2026-06-06 (Maricopa extraction — batch 3: +9 jurisdictions, 20 of 26 done)

- **Extracted 9 more Maricopa jurisdictions from official sources** (~197 zones), bringing the data layer to **20 jurisdictions / 464 zones — 463 official-sourced** (330 `official-html` + 133 `official-pdf`; the lone `secondary-mirror` is the Phoenix Walkable Urban placeholder). 440 zones carry at least one extracted core value.
  - **Municode API:** Surprise (21), Avondale (22), Tolleson (12), Youngtown (8).
  - **General Code (Cloudflare — read via browser):** Goodyear (23), Fountain Hills (34).
  - **American Legal (read via browser User-Agent; WebFetch 403s):** Apache Junction (21), and **Peoria (25)** — which the agent discovered has **migrated off Municode to American Legal** (the Municode AZ client list no longer includes Peoria).
  - **Tempe (31)** brought in **non-destructively** as a carry-forward: its prior official-source-`reviewed` values were copied into the data layer with `note_path` empty, so the curated per-zone notes are untouched; data appears in `zoning_standards.csv` + the Tempe overview table.
- **Access-route map (for the remaining queue):** Municode HTML 403s but `api.municode.com` works; American Legal 403s WebFetch but serves a normal browser User-Agent / Chrome; General Code (`*.municipal.codes`, `*.town.codes`) is Cloudflare-gated — readable via Chrome. PDFs read directly.
- **Honest gaps (no fabrication):** Fountain Hills OSC/OSR/OSP and UT have TBD dimensions (Ch. 9 / Ch. 14 sections were Cloudflare-blocked and absent from the Wayback archive). Several small-town districts (Youngtown R/P, Tolleson I-1/I-2) legitimately have no codified lot-area/coverage standard → TBD. Setbacks that vary by ROW/adjacency were recorded as the binding minimum with the full schedule in `notes`.
- Verified: `validate.py` clean (464 zones, 0 errors); `sync.py --check` clean; non-scalar values normalized; `/`-bearing codes slugged.
- **Remaining (6 of 26):** Paradise Valley (still needs the full ordinance PDF — supplied file is a cover sheet), El Mirage, Carefree, Guadalupe (American Legal — browser route), Cave Creek (per-chapter PDFs on city site), Wickenburg (Municipal Code Online). Tucson stays out of scope (Pima County).

## 2026-06-06 (Maricopa extraction — batch 2: +7 jurisdictions)

- **Extracted base-zone standards for 7 more Maricopa jurisdictions from official sources** (153 zones), bringing the data layer to **11 jurisdictions / 268 zones — 267 official-sourced** (134 `official-html` + 133 `official-pdf`; the lone `secondary-mirror` is the Phoenix Walkable Urban transect placeholder).
  - **Local PDFs:** Gilbert (28 zones + added MF/H found in the code but missing from the roster), Queen Creek (29), Buckeye (23), Litchfield Park (20), Gila Bend (11). All page-cited.
  - **Municode backing API** (HTML 403-blocked, but `api.municode.com` works — same route Mesa used): Chandler (18) and Glendale (24).
- **Genuine upgrades + corrections to prior web/zoneomics drafts** (built-out cities Gilbert & Chandler had per-zone notes synced; the rest are new and populate the CSV + overview tables only). Chandler official-code corrections: MF-1/MF-2 coverage 55%→45%, MF-3 55%→50%; SF-10 is Art. VI.1 (not VI); SF-8.5 front-setback myth removed; I-1/I-2 have no numeric height cap; CCD section is §35-3204. Gilbert: added MF/H (50 du/ac, 55 ft).
- **Paradise Valley deferred:** the supplied `ParadiseValley_ZoningOrdinance_2023.pdf` is a 1-page cover sheet (lists Article X by title only), not the codified ordinance — the agent returned zero zones rather than fabricate. **Needs the full PV ordinance PDF to extract.**
- **New tooling guard:** `sync.py` now **skips any zone note with `status: reviewed`/`authoritative`** (prints a notice) so it can never overwrite human-curated standards — this protects Tempe (and the already-processed Scottsdale notes) going forward.
- Verified: `validate.py` clean (268 zones, 0 errors); `sync.py --check` clean; all 46 Gilbert/Chandler `note_path`s resolved; non-scalar setbacks (e.g. Gilbert "5&10") normalized to the binding minimum with detail kept in `notes`; `/`-bearing zone codes (MF/L, P/QP) slugged to hyphens in `zone_id` while keeping the official `zone_code`.
- **Remaining queue:** Tempe (already official-reviewed — bring into data layer non-destructively), Paradise Valley (need full PDF), the live-link-only cities (Surprise, Peoria, Goodyear, Avondale, Tolleson, Youngtown, Fountain Hills, Cave Creek, Carefree, Guadalupe, Apache Junction, El Mirage, Wickenburg — most are Municode/American Legal, try the API route), Maricopa County per-zone notes, and special/PUD/form-based districts.

## 2026-06-06 (Maricopa primary-source migration + structured data layer)

- **Adopted `Maricopa County development standards/` as the source of truth** for Maricopa jurisdictions (41 official PDFs + 36 live-code links + `INDEX.html`, compiled 2026-06-06), and **introduced a structured data layer at `40-data/`** — the one sanctioned new top-level folder (`_CONVENTIONS.md` §9; `CLAUDE.md` amended).
- **New data layer (hybrid model):** canonical = per-zone JSON (`40-data/zones/*.json`) + `jurisdictions.csv` (26 Maricopa jurisdictions) + `source_registry.csv` (77 primary-source docs) + `parking_standards.csv`. Generated = `zoning_standards.csv` (flat projection) and the **Development Standards table + numeric frontmatter** inside each zone note (between `<!-- BEGIN:standards -->` markers) + a **Zone Standards (data-linked)** table in each jurisdiction overview. Tooling: `40-data/_tools/validate.py` (schema + referential integrity) and `sync.py` (regenerates all derived artifacts; `--check` detects drift). Every record carries `provenance`/`confidence`/`source_citation`/`source_page`; AI extraction is capped at `extracted` — only a human sets `human_verified`.
- **Pilot extraction (base zones) from official sources — 112 zones across 4 jurisdictions:**
  - **Maricopa County** (21 zones) — from the official Zoning Ordinance **PDF** (§502/§504/§506 tables, page-cited); `official-pdf`/`extracted`.
  - **Phoenix** (24 zones) — from the official code at phoenix.municipal.codes (current, **amended Ord. G-7446 Jan 2026**); `official-html`/`extracted`. **Genuine upgrade over the prior web/zoneomics draft** — corrected several stale values (e.g., R-3 rear setback 20→15; district names; current densities) and confirmed P-1/P-2 are parking districts.
  - **Mesa** (37 zones) — from official Title 11 via Municode's backing API (Article 2 tables); `official-html`/`extracted`. Upgrade over prior zoneomics draft.
  - **Scottsdale** (35 zones) — live Municode/mirror were blocked (403/503), so values were **preserved** from the vault's prior official-source pass (Appendix B, 2026-05-25) and labeled `official-html`/`extracted` (NOT human-verified by this run). **Caveat:** the prior notes' richer "Notes"-column ordinance quotations in the standards table were replaced by the generated table; values + §-citations + the note's own `source_last_verified` are retained in frontmatter. Re-extract from official Appendix B when reachable to restore full per-row quotes.
- **Scaffolded all 26 Maricopa jurisdictions:** created 12 new city overviews (El Mirage, Tolleson, Litchfield Park, Youngtown, Wickenburg, Gila Bend, Fountain Hills, Cave Creek, Carefree, Paradise Valley, Guadalupe, Apache Junction) with Primary Sources; refreshed code/source links on 7 existing overview-only cities + the Maricopa County note. **Tucson flagged as Pima County** (outside this source set). Indexes updated: `20-jurisdictions/00-index.md`, root `00-index.md`, `README.md`, `00-meta/data-sources.md` (points to the canonical `source_registry.csv`).
- **Verification:** `validate.py` clean (112 zones, 0 errors); `sync.py --check` clean (no drift); spot-checked Phoenix R-3 (rear 15, §615) and Maricopa County RU-43 (43,560 sf, §502 p.70) against sources; confirmed hand-written prose in zone notes preserved (only the marked standards regions regenerate).
- **Known follow-ups:** remaining 22 Maricopa jurisdictions + special/PUD/form-based (e.g. Phoenix Walkable Urban transects) queued; new city notes use "City of…/Town of…" titles vs. older "City, AZ" titles (cosmetic inconsistency to normalize); General Plans / Engineering Standards content beyond registry rows not yet extracted.

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
