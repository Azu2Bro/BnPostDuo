#!/usr/bin/env python3
"""Validate the specified BnPostDuo V2 combined CSV (standard library only)."""
import argparse
import csv
import json
import statistics
from collections import Counter
from pathlib import Path

EXPECTED = {"Educational":593,"Marketing":581,"Motivational":600,"Religious":551,
            "Political":598,"Social Awareness":590,"News":598,"Entertainment":597}
FIELDS = ["image_id","caption","raw_ocr","main_ocr","phash","image_width","image_height","label"]


def validate(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        missing_columns = sorted(set(FIELDS)-set(reader.fieldnames or []))
        if missing_columns:
            raise ValueError(f"Missing columns: {missing_columns}")
        rows = list(reader)
    labels = Counter(row["label"] for row in rows)
    missing = {field:sum(not (r.get(field) or "").strip() for r in rows) for field in FIELDS}
    repeated_ids = {k:v for k,v in Counter(r["image_id"] for r in rows).items() if v > 1}
    hashes = [(r["phash"] or "").strip().lower() for r in rows]
    repeated_hashes = {k:v for k,v in Counter(hashes).items() if k and v > 1}
    bad_dims = []
    bad_hashes = []
    for idx,r in enumerate(rows,2):
        try:
            if int(r["image_width"]) <= 0 or int(r["image_height"]) <= 0:
                bad_dims.append(idx)
        except (ValueError,TypeError):
            bad_dims.append(idx)
        if len((r["phash"] or "").strip()) != 16 or any(c not in "0123456789abcdef" for c in (r["phash"] or "").strip().lower()):
            bad_hashes.append(idx)
    lengths = {}
    for key in ("caption","raw_ocr","main_ocr"):
        lengths[key] = {"word_median": statistics.median(len(r[key].split()) for r in rows) if rows else None,
                        "word_max":max((len(r[key].split()) for r in rows),default=None),
                        "character_max":max((len(r[key]) for r in rows),default=None)}
    issues = []
    if len(rows) != 4708: issues.append("Expected 4,708 rows")
    if dict(labels) != {k:v for k,v in EXPECTED.items()}: issues.append("Unexpected category counts")
    if any(missing.values()): issues.append("Blank required fields")
    if repeated_ids: issues.append("Repeated image identifiers")
    if repeated_hashes: issues.append("Repeated exact pHash values")
    if bad_dims: issues.append("Invalid image dimensions")
    if bad_hashes: issues.append("Invalid pHash values")
    return {"source_filename":Path(path).name,"record_count":len(rows),"category_counts":dict(labels),
            "missing_required_values":missing,"repeated_image_ids":repeated_ids,
            "repeated_exact_phash_groups":len(repeated_hashes),
            "invalid_dimension_lines":bad_dims[:30],"invalid_phash_lines":bad_hashes[:30],
            "text_length_statistics":lengths,"issues":issues,"status":"PASS" if not issues else "REVIEW",
            "limits":"Structural check only; does not verify original images, true duplicates or OCR transcription accuracy."}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--csv", type=Path, required=True)
    ap.add_argument("--output", type=Path)
    a = ap.parse_args()
    result = validate(a.csv)
    payload = json.dumps(result,ensure_ascii=False,indent=2)+"\n"
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(payload,encoding="utf-8")
    print(payload)
    if result["issues"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
