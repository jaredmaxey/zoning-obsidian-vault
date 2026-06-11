# CRE Knowledge Base

An Obsidian vault that doubles as (1) a commercial real estate development knowledge base across all asset classes, and (2) a structured, jurisdiction-by-jurisdiction zoning and development-standards reference (Arizona first, more states later).

The vault is built **AI-readable first** — consistent frontmatter, kebab-case filenames, and explicit relational fields — so AI tools can traverse it to run yield analyses, evaluate projects, do highest-and-best-use studies, and cite regulatory data. It's also a normal Obsidian vault you can read and edit by hand.

**Owner:** Jared Maxey (jaredmaxey@icloud.com)

## Where to start

- **Humans:** browse the branch indexes — `10-cre-brain/00-index.md`, `20-jurisdictions/00-index.md`, `30-reference/00-index.md`, and the structured data layer `40-data/00-index.md`.
- **Structured data:** `40-data/` holds machine-first CSV + JSON (jurisdiction registry, primary-source registry, per-zone dimensional standards). Edit the canonical files there, then run `python 40-data/_tools/validate.py` and `python 40-data/_tools/sync.py` to regenerate the cross-jurisdiction CSV and the standards tables embedded in the zone notes. See `_CONVENTIONS.md` §9.
- **For the full rules** (filenames, frontmatter, tags, linking, sourcing, status lifecycle), read **`_CONVENTIONS.md`**. That file is the source of truth.
- **AI sessions:** read **`CLAUDE.md`** first, then `_CONVENTIONS.md`.

## Status

Built via a numbered prompt series. See the "Current state" table in `CLAUDE.md` for what's populated vs. stubbed. As of 2026-05-24: Prompt 1 (architecture) complete; content population is in later prompts.
