# Version 2 duplicate screening and preprocessing

## Researcher-reported decisions

The original **4,800** records included **80** identical-pHash groups containing **172** records in total (68 groups of size two and 12 of size three). The team reports manually examining all flagged image groups and determining that their content was duplicate. They retained **one** copy per group and removed the other **92** records, leaving **4,708** records.

The retained records were checked for structural consistency; there are no repeated **identical** pHash values in the combined Version 2 CSV. This does not prove that no near-duplicates with different hashes remain.

All **480** records in the agreement-study sample were retained. The preprocessing script supports preferential retention of records from this sample. The original files should be archived privately; do not overwrite them.

## Auditable procedure

1. Obtain the original `COMBINED.csv` and, if available, the 480-record annotation CSV in `local_data/`.
2. Run `scripts/prepare_version2.py` without `--apply` to generate a retention plan.
3. Compare every flagged group against the original images and confirm or adjust the `keep_image_id` entries to match documented human decisions.
4. Only after completing review, run the script with `--apply --confirm-reviewed`.
5. Run `scripts/validate_version2.py` on the resulting `COMBINED_V2.csv`.
6. Review row counts, class distributions, all audit records, and the 480-record sample membership before public release.

```bash
python scripts/prepare_version2.py --csv local_data/COMBINED.csv --annotation local_data/annotation_votes.csv --out local_data/version2
# Inspect retention_plan.csv and original images before proceeding:
python scripts/prepare_version2.py --csv local_data/COMBINED.csv --annotation local_data/annotation_votes.csv --out local_data/version2 --apply --confirm-reviewed
python scripts/validate_version2.py --csv local_data/version2/COMBINED_V2.csv --output local_data/version2/validation.json
```

`--confirm-reviewed` records the operator's acknowledgment; it is **not automated evidence** that images have been visually compared. The exact keep/remove selections and local audit should be preserved by the research team.

## Category counts

| Label | V1 | Removed | V2 |
| --- | ---: | ---: | ---: |
| Educational | 600 | 7 | 593 |
| Marketing | 600 | 19 | 581 |
| Motivational | 600 | 0 | 600 |
| Religious | 600 | 49 | 551 |
| Political | 600 | 2 | 598 |
| Social Awareness | 600 | 10 | 590 |
| News | 600 | 2 | 598 |
| Entertainment | 600 | 3 | 597 |
| **Total** | **4,800** | **92** | **4,708** |

The actual V2 Mendeley DOI must replace the placeholder in manuscript citations after publication.
