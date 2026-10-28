# Annotation and inter-annotator agreement

## What is supported by the recorded study

The researchers report an independent human agreement assessment on a stratified sample of **480 records** (60 from each of eight original categories). Three annotators each assigned one of the eight class labels. The researchers report that the original labels were concealed from the annotators. The annotation inputs were the original image, accompanying caption, and curated image text.

The recorded 480-row vote file was used to calculate:

| Measure | Value |
| --- | ---: |
| Sampled records | 480 |
| Independent votes per sampled record | 3 |
| Unanimous votes | 411 |
| Two-to-one votes | 69 |
| Three different votes | 0 |
| Mean observed agreement | 0.904166667 |
| Chance-expected agreement | 0.125060764 |
| Fleiss' kappa | 0.890468584 |
| Majority labels matching original category labels | 480/480 |

The **same 480 image IDs remain in Version 2**, so deletion did not change this recorded vote calculation. The computation verifies the statistic from the votes but cannot independently establish human provenance or blinding procedures.

## Reproduction

```bash
python scripts/calculate_fleiss_kappa.py --csv local_data/annotation_votes.csv --annotators A1_category A2_category A3_category --output local_data/agreement.json
```

The raw annotation-vote CSV is not committed here. Users must have a permitted copy of the recorded votes to reproduce the calculation.

## Clarification of study scope

Do **not** interpret the 480-record reliability sample as evidence that three independent votes were collected for all 4,800 originally collected posts. The initial labeling workflow and the separate reliability study should be described distinctly.

Two OCR fields in an earlier annotation CSV differed from the final retained data (`marketing/320.jpg` and `motivational/310.jpg`). These were data-field differences; recorded categorical votes and the computed coefficient were unchanged. If preparing a formal provenance statement, document the timing of those edits accurately.

The exact historical category codebook and decision rules should be added only after they have been recovered from the original team documentation.
