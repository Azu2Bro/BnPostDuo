# BnPostDuo image-access request procedure

## Public dataset

The official processed BnPostDuo CSV dataset is available on [Mendeley Data, Version 2](https://data.mendeley.com/datasets/6678wc3bs7/2) and contains **4,708 records** across eight classes. The public CSV package contains captions, raw and curated OCR, labels, pHash, and image dimensions. **Original Facebook images are not included**.

## How researchers request image access

1. Read the [public Version 2 dataset description](https://data.mendeley.com/datasets/6678wc3bs7/2) and identify the image-based or multimodal research purpose.
2. Complete the **[BnPostDuo image-access request form](https://forms.gle/wKSdaqRD4rpT5T6f7)**.
3. The BnPostDuo research team reviews the request and determines whether the relevant images may be shared for the requested use in accordance with applicable rights, privacy obligations, and platform rules.
4. **For approved requests where distribution is authorized**, the team sends the researcher a **private Google Drive link** to the relevant image collection. The image folder is not linked publicly from GitHub or Mendeley.
5. The researcher must follow the access terms provided by the team, including any restrictions on sharing or redistribution.

Submitting the form **does not guarantee approval or availability of images**. An access request or agreement does not itself provide permission to redistribute third-party copyrighted images. The team must establish its authority to share before supplying access.

## Dataset alignment

Where image access is approved, the researchers should preserve the correspondence between the image filenames and the `image_id` field in the Version 2 CSV. The eight category names are Educational, Entertainment, Marketing, Motivational, News, Political, Religious, and Social Awareness. A reproducible image-based study must document which corresponding images were actually available.

## Image rights and privacy

The images originated from publicly accessible Facebook content. Public availability alone does not imply permission for public redistribution, research-only distribution, or model training. The research team should verify that any proposed sharing is permitted and should not expose a public Google Drive URL without appropriate authorization. Sharing access with specific approved accounts is preferable to an unrestricted "anyone with the link" setting when controlled access is intended.

The Google Form is for access requests, not for granting automatic access. Researcher contact details collected through the form should be limited to information needed to evaluate and administer requests, handled appropriately, and not published in this repository.

## Repository roles

- **Mendeley Data:** public, citable Version 2 CSV dataset (4,708 records).
- **GitHub:** documentation, reproducibility scripts, reports, and this access procedure.
- **Google Form:** researcher request intake.
- **Restricted Google Drive:** delivery to approved researchers only where legally and ethically authorized.

This workflow does not change the contents or license of the public Mendeley Data deposit.
