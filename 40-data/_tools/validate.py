#!/usr/bin/env python3
"""Validate the 40-data/ structured layer.

Checks (stdlib only, no external deps):
  - each zones/*.json parses and has required structure
  - jurisdiction_id exists in jurisdictions.csv and matches the filename
  - zone_id format + uniqueness; prefix equals the file's jurisdiction_id
  - category / provenance / confidence are in-enum
  - every zone's source_doc (or the file's default_source_doc) exists in source_registry.csv
  - numeric standard fields are number / empty / "TBD"
  - human_verified is blank or an ISO date; AI-confidence rows must not be verified-human

Exit code 0 = clean, 1 = one or more errors.
"""
import csv
import json
import re
import sys
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1]
ZONES_DIR = DATA_DIR / "zones"

CATEGORIES = {"residential", "commercial", "industrial", "mixed-use", "agricultural",
              "special", "downtown", "planned", "open-space", "overlay"}
PROVENANCE = {"official-pdf", "official-html", "secondary-mirror", "inferred", "unknown"}
CONFIDENCE = {"verified-human", "extracted", "low", "tbd"}
NUMERIC_FIELDS = {"min_lot_size_sf", "min_lot_width_ft", "max_density_dua", "max_far",
                  "max_lot_coverage_pct", "max_height_ft", "max_stories",
                  "front_setback_ft", "side_setback_ft", "rear_setback_ft"}
ZONE_ID_RE = re.compile(r"^az-[a-z0-9-]+:[a-z0-9.\-]+$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

errors = []
warnings = []


def load_csv_column(path, col):
    if not path.exists():
        errors.append(f"missing required file: {path.name}")
        return set()
    with path.open(newline="", encoding="utf-8") as f:
        return {row[col].strip() for row in csv.DictReader(f) if row.get(col, "").strip()}


def numeric_ok(v):
    return v is None or isinstance(v, (int, float)) or v == "TBD"


def main():
    jurisdiction_ids = load_csv_column(DATA_DIR / "jurisdictions.csv", "jurisdiction_id")
    source_ids = load_csv_column(DATA_DIR / "source_registry.csv", "source_id")

    seen_zone_ids = {}
    zone_files = sorted(ZONES_DIR.glob("*.json")) if ZONES_DIR.exists() else []

    for jf in zone_files:
        try:
            data = json.loads(jf.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"{jf.name}: invalid JSON — {e}")
            continue

        jid = data.get("jurisdiction_id", "")
        if jid != jf.stem:
            errors.append(f"{jf.name}: jurisdiction_id '{jid}' != filename stem '{jf.stem}'")
        if jid and jid not in jurisdiction_ids:
            errors.append(f"{jf.name}: jurisdiction_id '{jid}' not in jurisdictions.csv")
        default_src = data.get("default_source_doc")

        for z in data.get("zones", []):
            zid = z.get("zone_id", "<missing>")
            ctx = f"{jf.name} [{zid}]"
            for req in ("zone_id", "zone_code", "zone_name", "category", "provenance", "confidence"):
                if not z.get(req):
                    errors.append(f"{ctx}: missing required field '{req}'")
            if zid != "<missing>":
                if not ZONE_ID_RE.match(zid):
                    errors.append(f"{ctx}: zone_id fails pattern")
                elif not zid.startswith(jid + ":"):
                    errors.append(f"{ctx}: zone_id prefix != '{jid}'")
                if zid in seen_zone_ids:
                    errors.append(f"{ctx}: duplicate zone_id (also in {seen_zone_ids[zid]})")
                seen_zone_ids[zid] = jf.name
            if z.get("category") and z["category"] not in CATEGORIES:
                errors.append(f"{ctx}: category '{z['category']}' not in enum")
            if z.get("provenance") and z["provenance"] not in PROVENANCE:
                errors.append(f"{ctx}: provenance '{z['provenance']}' not in enum")
            if z.get("confidence") and z["confidence"] not in CONFIDENCE:
                errors.append(f"{ctx}: confidence '{z['confidence']}' not in enum")

            src = z.get("source_doc") or default_src
            if not src:
                errors.append(f"{ctx}: no source_doc and no default_source_doc")
            elif src not in source_ids:
                errors.append(f"{ctx}: source_doc '{src}' not in source_registry.csv")

            for k, v in (z.get("standards") or {}).items():
                if k == "parking_ratio":
                    if not (v is None or isinstance(v, str)):
                        errors.append(f"{ctx}: parking_ratio must be string/null")
                elif k in NUMERIC_FIELDS:
                    if not numeric_ok(v):
                        errors.append(f"{ctx}: {k}='{v}' must be number, empty, or 'TBD'")
                else:
                    errors.append(f"{ctx}: unknown standards field '{k}'")

            hv = z.get("human_verified", "")
            if hv and not DATE_RE.match(hv):
                errors.append(f"{ctx}: human_verified '{hv}' not ISO date")
            if z.get("confidence") == "verified-human" and not hv:
                errors.append(f"{ctx}: confidence verified-human requires human_verified date")
            if z.get("confidence") == "extracted" and z.get("provenance") not in ("official-pdf", "official-html"):
                warnings.append(f"{ctx}: confidence 'extracted' but provenance not official-*")

    print(f"validate.py: {len(zone_files)} zone file(s), {len(seen_zone_ids)} zone(s)")
    for w in warnings:
        print(f"  WARN  {w}")
    if errors:
        for e in errors:
            print(f"  ERROR {e}")
        print(f"FAILED with {len(errors)} error(s)")
        return 1
    print("OK — no errors")
    return 0


if __name__ == "__main__":
    sys.exit(main())
