# BnPostDuo: A Bengali Multimodal Social Media Dataset

BnPostDuo was constructed from **4,800 Bengali Facebook posts** collected from publicly accessible pages and groups during **2025–2026**. Each original record was associated with an image, caption, OCR-extracted image text, category label, and image metadata.

**This GitHub repository provides supporting documentation, reproducibility utilities, and quality-control summaries.** The public research data are hosted separately on Mendeley Data. The original Facebook images are **not redistributed**.

## Data in Brief manuscript authors

The **Data in Brief manuscript** lists the following **eight authors**, in manuscript order:

1. Imam Abu Zubaer
2. Tafhimul Azwad
3. Fatema Jannat Rup
4. Poushi Das
5. Mahfuzulhoq Chowdhury
6. Dipta Deb Nath
7. Md. Tanvir Rahaman Sani
8. Jannatul Ferdous

**Authorship note:** The eight-person article author list and the contributor list on the Mendeley Data deposit are separate records. Cite the published Mendeley dataset using its official version-specific metadata; the names above identify the article manuscript authors. The research team should ensure manuscript and submission-system authorship details agree.

## Dataset access and versions

- **Mendeley Data, published Version 2 (current public dataset):** [BnPostDuo Version 2](https://data.mendeley.com/datasets/6678wc3bs7/2) — **4,708 records** after duplicate screening and removal. This is the dataset version described in the current manuscript.
- **Mendeley Data, published Version 1 (original release):** [10.17632/6678wc3bs7.1](https://doi.org/10.17632/6678wc3bs7.1) — **4,800 records**, initially 600 per category. Cite this version only if you actually used it.

GitHub does not host a separate copy of the full CSV dataset. Download the officially released data from Mendeley Data.

## Requesting access to the original images

The **published Mendeley Data Version 2 contains CSV records and image metadata, not the original Facebook images**. Researchers who need images for image-based or image–text experiments may submit a request through the **[BnPostDuo image-access request form](https://forms.gle/wKSdaqRD4rpT5T6f7)**.

The research team reviews requests. **If a request is approved and the team is authorized to share the relevant images**, access is provided by a **restricted Google Drive image-folder link**, shared privately with the approved researcher. The Drive link is **not published openly** in this repository. Form submission does not guarantee access; access and permitted uses are subject to relevant rights, privacy, and platform restrictions.

Full request and access procedure: [documentation/image_access.md](documentation/image_access.md).

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
| `documentation/image_access.md` | Google Form request procedure and controlled Google Drive delivery policy |
| `CITATION.cff` | Citation metadata; use Mendeley version-specific DOI |
| `LICENSE` | License for repository's original software scripts only |

The scripts are **reproducibility/verification utilities prepared after the dataset's construction**. Their publication does not imply they are the exact historical data-collection or OCR scripts.

## Reproducing checks

Use **Python 3.10+** (standard library only). Put the dataset downloaded from Mendeley Data under an ignored local folder, such as `local_data/`.

```bash
python scripts/validate_version2.py --csv local_data/BnPostDuo_combined.csv --output local_data/validation.json

python scripts/calculate_fleiss_kappa.py --csv local_data/annotation_votes.csv --annotators A1_category A2_category A3_category --output local_data/agreement.json
```

The 480-record annotation-vote CSV is required for the second command; it is **not included in this repository at present**. The research team should approve a privacy-reviewed, vote-only public extract before it is released.

For recreating V2 from an authorized copy of V1, see [the preprocessing instructions](documentation/preprocessing.md). The final keep/remove decisions must be checked against the researchers' manual review records.

## Data access, reuse and privacy

The research was based on third-party public Facebook posts. Public visibility does not automatically provide redistribution rights. **Original images are not included in the Mendeley or GitHub public releases**; use the [image-access request form](https://forms.gle/wKSdaqRD4rpT5T6f7) to ask the team about controlled access. Approved, authorized requests are fulfilled privately through Google Drive. The pHash field does not reconstruct source images. See [data access and ethical notes](documentation/data_access_and_ethics.md). Consult Mendeley for the applicable data license; this GitHub repository does not license third-party material.

## Citation

This repository provides [CITATION.cff](CITATION.cff) and a [software-only LICENSE](LICENSE). They do not license Facebook images, captions, or the official Mendeley dataset.


Cite the **Mendeley Data dataset version actually used** in your work. **Current Version 2:** https://data.mendeley.com/datasets/6678wc3bs7/2 (4,708 records). **Historical Version 1:** https://data.mendeley.com/datasets/6678wc3bs7/1 (4,800 records).
