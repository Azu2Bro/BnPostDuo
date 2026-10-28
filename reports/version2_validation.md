# BnPostDuo Version 2 — verification summary

**Scope:** Independent structural verification of the supplied `version2.zip` and its CSV/audit files. The team's manual image comparison was reported by the researchers; the original Facebook images were not provided for independent visual confirmation.

## Version 2 processing results

- Initial collection: **4,800** records (600 in each of eight categories).
- Matching exact-pHash groups: **80**, covering **172** records (68 two-image groups; 12 three-image groups).
- Researcher-reported manual inspection: all groups were considered duplicates.
- Duplicates removed: **92** (retaining one per group).
- Final Version 2 records: **4,708**.
- Exact repeated pHash values in Version 2: **0**.
- Duplicate `image_id` values: **0**.
- Blank values in the eight required fields: **0**.
- Invalid image dimensions and 16-character hexadecimal pHash strings: **0**.
- Eight category CSVs were verified against the combined CSV after normalizing category-relative image IDs.
- Removal audit: **92** removed IDs absent from the final CSV; the retained image ID for each group is present in the final CSV.
- All **480** agreement-study image IDs were retained.

## Counts after preprocessing

| Category | Version 1 | Removed | Version 2 |
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

## Recorded agreement assessment

Three votes per sampled record, **480** records: 411 unanimous, 69 two-to-one and zero all-distinct records. Fleiss' κ calculated from the votes was **0.890468584**; observed mean agreement **0.904166667**, chance expected **0.125060764**. The recorded majority-vote label matched the existing label for all 480 sampled records.

This numerical check does not itself establish human authorship, blinding, rater independence, or historical annotation workflow.

## Version 2 text lengths

Whitespace-separated word counts, not Bengali linguistic tokenization:

| Field | Median words | Max words | Max characters |
| --- | ---: | ---: | ---: |
| `caption` | 11 | 911 | 5719 |
| `raw_ocr` | 27 | 768 | 4584 |
| `main_ocr` | 11 | 488 | 3317 |

These maximums must be considered when updating manuscript figures and narrative.

## Cautions and pending documentation

1. **Two OCR-field differences** were observed between the previously supplied annotation CSV and final V2 records: `marketing/320.jpg` (raw and curated OCR) and `motivational/310.jpg` (raw OCR). The categorical votes were unchanged. The research team should document when these field corrections happened.
2. Removing exact-pHash duplicates does not establish that all visually similar images with **different** hashes are absent.
3. Image pixels were not included in the verification files: manual duplicate classifications and OCR accuracy were **not independently visually validated**.
4. The preprocessed V2 release **is not yet documented here as publicly deposited**. Until Mendeley Version 2 is published and its DOI is known, the existing version-specific DOI points only to the 4,800-record **Version 1**.
5. Raw researcher records (including original image files and underlying human votes) are intentionally not included in this public GitHub repository.

**Publication note:** When reporting these results, clearly distinguish research-team manual verification from code-generated structural checks.
