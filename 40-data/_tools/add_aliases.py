#!/usr/bin/env python3
"""add_aliases.py — make title-based wikilinks resolve in Obsidian.

The vault's convention links notes by frontmatter title (e.g. [[Chandler SF-33]]),
but Obsidian resolves wikilinks by filename or alias. For every note whose title
differs from its filename, this script inserts `aliases: ["<title>"]` immediately
after the title line so Obsidian backlinks/graph/preview work without renaming files.

Usage (from the vault root):
    python 40-data/_tools/add_aliases.py            # dry run: report what would change
    python 40-data/_tools/add_aliases.py --apply    # write changes

Idempotent: notes that already have an aliases field are skipped.
"""

import argparse
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

SKIP_DIRS = {".git", ".obsidian", "_templates"}
TITLE_RE = re.compile(r'^title:\s*"?(.+?)"?\s*$')


def vault_root() -> Path:
    # 40-data/_tools/add_aliases.py -> vault root is two levels up from _tools
    return Path(__file__).resolve().parent.parent.parent


def process(path: Path, apply: bool):
    """Returns one of: 'added', 'skip-has-alias', 'skip-match', 'skip-no-title'."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return "skip-no-title"

    title = None
    title_idx = None
    in_fm = True
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            break
        m = TITLE_RE.match(line.rstrip("\r\n"))
        if m and title is None:
            title = m.group(1).strip()
            title_idx = i
        if re.match(r"^aliases\s*:", line):
            return "skip-has-alias"
    else:
        in_fm = False
    if not in_fm or title is None:
        return "skip-no-title"

    if title.lower() == path.stem.lower():
        return "skip-match"

    eol = "\r\n" if lines[title_idx].endswith("\r\n") else "\n"
    escaped = title.replace('"', r"\"")
    alias_line = f'aliases: ["{escaped}"]{eol}'
    if apply:
        lines.insert(title_idx + 1, alias_line)
        path.write_text("".join(lines), encoding="utf-8", newline="")
    return "added"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write changes (default: dry run)")
    args = parser.parse_args()

    root = vault_root()
    counts = {"added": 0, "skip-has-alias": 0, "skip-match": 0, "skip-no-title": 0}
    no_title = []
    for path in sorted(root.rglob("*.md")):
        if SKIP_DIRS & set(p.name for p in path.parents):
            continue
        result = process(path, args.apply)
        counts[result] += 1
        if result == "skip-no-title":
            no_title.append(path.relative_to(root))

    mode = "APPLIED" if args.apply else "DRY RUN"
    print(f"add_aliases.py [{mode}]")
    print(f"  alias added:            {counts['added']}")
    print(f"  already has aliases:    {counts['skip-has-alias']}")
    print(f"  title matches filename: {counts['skip-match']}")
    print(f"  no frontmatter title:   {counts['skip-no-title']}")
    for p in no_title:
        print(f"    - {p}")


if __name__ == "__main__":
    main()
