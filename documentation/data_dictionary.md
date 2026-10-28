# BnPostDuo data dictionary

The published data are CSV files. Each row represents a collected Facebook post. Original image files are not redistributed.

| Field | Meaning | Notes |
| --- | --- | --- |
| `image_id` | Identifier of the original image | Combined CSV may use `category/filename.jpg`; category CSVs may use just the basename. It does not provide a downloadable image. |
| `caption` | Text accompanying the Facebook post | Text is supplied as available in the released record. |
| `raw_ocr` | Text automatically recognized in the image by EasyOCR | May contain errors, omitted words, or irrelevant text. |
| `main_ocr` | Meaningful image text curated against the source image | Manually corrected and selectively retained. **Not** an exhaustive ground-truth transcription of every image word. |
| `phash` | Perceptual image hash (16 hexadecimal characters in the checked release) | Used to flag visually similar images. Hash equality alone does not establish exact duplicates; it does not reconstruct an image. |
| `image_width` | Original image width | Positive integer, pixels. |
| `image_height` | Original image height | Positive integer, pixels. |
| `label` | Assigned content category | One of the eight class strings below. |

## Label strings

- `Educational`
- `Marketing`
- `Motivational`
- `Religious`
- `Political`
- `Social Awareness`
- `News`
- `Entertainment`

Version 1 included 4,800 records; the deduplicated Version 2 export contains 4,708 records. The latter is **not** balanced to 600 per class.

## Text-length calculation

The verification scripts use whitespace-separated tokens (`str.split()`) when reporting word counts. This is not a language-specific Bengali tokenizer. Descriptive plots should identify their counting method.
