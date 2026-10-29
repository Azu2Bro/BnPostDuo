# BnPostDuo: A Bengali Multimodal Social Media Dataset

BnPostDuo was constructed from **4,800 Bengali Facebook posts** collected from publicly accessible pages and groups during **2025–2026**. Each original record was associated with an image, caption, OCR-extracted image text, category label, and image metadata.

**This GitHub repository provides supporting documentation, reproducibility utilities, and quality-control summaries.** The public research data are hosted separately on Mendeley Data. The original Facebook images are **not redistributed**.

## Dataset access and versions

- **Mendeley Data, published Version 1:** [10.17632/6678wc3bs7.1](https://doi.org/10.17632/6678wc3bs7.1) — 4,800 records, 600 in each of eight categories.
- **Preprocessed Version 2:** 4,708 records after researcher-confirmed duplicate removal. The **Version 2 Mendeley DOI should be added after that version is published**. Do not cite the Version 1 DOI as though it identifies Version 2.

GitHub does not host a separate copy of the full CSV dataset. Download the officially released data from Mendeley Data.

## Version 2 at a glance

| Category | Records |
| --- | ---: |
| Educational | 593 |
| Marketing | 581 |
| Motivational | 600 |
| Religious | 551 |
| Political | 598 |
| Social Awareness | 590 |
| News | 598 |
| Entertainment | 597 |
| **Total** | **4,708** |

The initial 4,800 records contained **80 groups (172 records)** with identical perceptual hashes. The research team reports visually reviewing these groups and confirming duplicate content. One record per group was retained; **92 records** were removed. The resulting Version 2 CSV has no repeated *identical* pHash values. This does **not** establish the absence of all near-duplicates.

## Released fields

`image_id`, `caption`, `raw_ocr`, `main_ocr`, `phash`, `image_width`, `image_height`, `label`.

- `raw_ocr`: automatic OCR output from EasyOCR.
- `main_ocr`: meaningful image-embedded text transcribed/curated with reference to the source image; it is not necessarily an exhaustive transcription.
- `phash`: compact perceptual hash useful for image-similarity screening; it does not reconstruct the image.

See [the field dictionary](documentation/data_dictionary.md).

## Human annotation

**Initial labeling:** The research team reports that three annotators categorized the original **4,800 posts** into eight predefined content categories. Ambiguous category assignments were discussed to select an appropriate final label. These initial labeling activities are distinct from the separate reliability assessment.

**Independent reliability assessment:** After duplicate removal, a stratified sample of **480 records was selected from the 4,708-record preprocessed dataset** (60 from each of eight categories). Three annotators independently evaluated these records with the original category labels hidden. The recorded votes yield **Fleiss' κ = 0.8905** (411 unanimous and 69 two-to-one). The majority-vote labels matched the stored labels for all 480 sampled records. This κ applies to **the 480-post assessment**, not the full 4,800-post labeling stage.

See [annotation and agreement documentation](documentation/annotation_and_agreement.md).

## Repository contents

| Path | Purpose |
| --- | --- |
| `documentation/` | Field dictionary, construction/preprocessing notes, annotation and release considerations |
| `scripts/prepare_version2.py` | Auditable duplicate-removal plan and CSV export; requires confirmation of manual image review |
| `scripts/validate_version2.py` | Recheck Version 2 counts, required columns, missing values, repeated hashes and IDs |
| `scripts/calculate_fleiss_kappa.py` | Recalculate agreement from the separately held annotation votes |
| `reports/version2_validation.md` | Results checked on the supplied preprocessed CSV files |
| `figures/` | Final four-panel workflow diagram in editable draw.io format |
| `CITATION.cff` | Citation metadata; use Mendeley version-specific DOI |
| `LICENSE` | License for repository's original software scripts only |

The scripts are **reproducibility/verification utilities prepared after the dataset's construction**. Their publication does not imply they are the exact historical data-collection or OCR scripts.

## Reproducing checks

Use **Python 3.10+** (standard library only). Put the dataset downloaded from Mendeley Data under an ignored local folder, such as `local_data/`.

```bash
python scripts/validate_version2.py --csv local_data/COMBINED_V2.csv --output local_data/validation.json

python scripts/calculate_fleiss_kappa.py --csv local_data/annotation_votes.csv --annotators A1_category A2_category A3_category --output local_data/agreement.json
```

The 480-record annotation-vote CSV is required for the second command; it is **not included in this repository at present**. The research team should approve a privacy-reviewed, vote-only public extract before it is released.

For recreating V2 from an authorized copy of V1, see [the preprocessing instructions](documentation/preprocessing.md). The final keep/remove decisions must be checked against the researchers' manual review records.

## Data access, reuse and privacy

The research was based on third-party public Facebook posts. Public visibility does not automatically provide redistribution rights. **Original images are not included**, and the pHash fields do not support direct image-model training. See [data access and ethical notes](documentation/data_access_and_ethics.md). Consult the current Mendeley record for the **actual license of the published dataset**; no third-party content is licensed merely by appearing in this GitHub repository.

## Citation

This repository provides [CITATION.cff](CITATION.cff) and a [software-only LICENSE](LICENSE). They do not license Facebook images, captions, or the official Mendeley dataset.


Cite the **Mendeley Data dataset version actually used** in your work. Currently documented published record: https://doi.org/10.17632/6678wc3bs7.1. A Version 2 citation should be updated with its own published DOI.
