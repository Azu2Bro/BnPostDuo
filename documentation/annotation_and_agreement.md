# Annotation and inter-annotator agreement

## Initial annotation of the collected posts

The research team reports that **three annotators assigned category labels to all 4,800 initially collected posts**. Labels were based on the post image, caption and image-embedded text. When content fit multiple predefined categories, annotators discussed the ambiguity to select the most appropriate category. This initial classification process is separate from the blinded agreement assessment described below. Original per-item voting logs or adjudication records for the full collection have not been deposited here, so that stage is documented as researcher-reported methodology.

Following pHash screening, researchers manually reviewed duplicate-image groups and removed 92 redundant records, leaving **4,708 records**.

## Separate post-preprocessing reliability study

The researchers report an independent human agreement assessment on a stratified sample of **480 records from the preprocessed 4,708-record dataset** (60 from each of eight categories). Three annotators each assigned one of the eight class labels. The researchers report that the original labels were concealed from the annotators. The annotation inputs were the original image, accompanying caption, and curated image text.

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

All 480 studied records belong to the preprocessed Version 2 dataset. The voting result refers to that separate sample, not to the full collection. The computation verifies the statistic from the votes but cannot independently establish human provenance or blinding procedures.

## Reproduction

```bash
python scripts/calculate_fleiss_kappa.py --csv local_data/annotation_votes.csv --annotators A1_category A2_category A3_category --output local_data/agreement.json
```

The raw annotation-vote CSV is not committed here. Users must have a permitted copy of the recorded votes to reproduce the calculation.

## Clarification of study scope

The initial 4,800-post annotation and the post-preprocessing 480-post blinded evaluation are **two separate activities**. Although the researchers report three annotators in the initial labeling stage, only the 480-row independent voting dataset has been used here for a verified Fleiss' κ calculation. No κ value for the complete initial collection is claimed.

Two OCR fields in an earlier annotation CSV differed from the final retained data (`marketing/320.jpg` and `motivational/310.jpg`). These were data-field differences; recorded categorical votes and the computed coefficient were unchanged. If preparing a formal provenance statement, document the timing of those edits accurately.

The exact historical category codebook and decision rules should be added only after they have been recovered from the original team documentation.
