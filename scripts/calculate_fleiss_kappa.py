#!/usr/bin/env python3
"""Compute Fleiss' kappa from recorded categorical votes (Python standard library)."""
import argparse
import csv
import json
from collections import Counter
from pathlib import Path


def calculate(path, annotators):
    with Path(path).open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        required = set(annotators)
        if not required.issubset(reader.fieldnames or []):
            raise ValueError(f"Missing annotation columns: {required - set(reader.fieldnames or [])}")
        rows = list(reader)
    if not rows:
        raise ValueError("No annotation records")
    m = len(annotators)
    if m < 2:
        raise ValueError("At least two raters required")
    per_record, all_votes = [], Counter()
    unanimous = two_one = three_distinct = match_original = comparable = 0
    original = "Original_label" if "Original_label" in rows[0] else None
    for line, row in enumerate(rows, 2):
        votes = [(row.get(col) or "").strip() for col in annotators]
        if not all(votes):
            raise ValueError(f"Empty vote in CSV line {line}")
        c = Counter(votes)
        per_record.append(c)
        all_votes.update(votes)
        unanimous += len(c) == 1
        if m == 3:
            two_one += sorted(c.values()) == [1, 2]
            three_distinct += len(c) == 3
        if original:
            most = c.most_common(1)[0]
            if most[1] > m / 2:
                comparable += 1
                match_original += most[0] == (row[original] or "").strip()
    n = len(rows)
    chance = sum((v / (n*m))**2 for v in all_votes.values())
    observed = sum((sum(v*v for v in c.values())-m)/(m*(m-1)) for c in per_record)/n
    return {
        "record_count": n, "rater_count": m, "annotator_columns": annotators,
        "observed_mean_agreement": round(observed, 9),
        "chance_expected_agreement": round(chance, 9),
        "fleiss_kappa": round((observed-chance)/(1-chance), 9) if chance != 1 else None,
        "unanimous_records": unanimous,
        "two_to_one_records": two_one if m == 3 else None,
        "all_three_different_records": three_distinct if m == 3 else None,
        "majority_labels_comparable_to_original": comparable if original else None,
        "majority_labels_matching_original": match_original if original else None,
        "note": "Based on recorded votes only; script cannot verify provenance, blinding or rater independence."
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--csv", type=Path, required=True)
    ap.add_argument("--annotators", nargs="+", default=["A1_category", "A2_category", "A3_category"])
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    result = json.dumps(calculate(args.csv, args.annotators), indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(result, encoding="utf-8")
    print(result)


if __name__ == "__main__":
    main()
