#!/usr/bin/env python3
"""Prepare an auditable exact-pHash duplicate removal plan for BnPostDuo.
One image per group is retained only after human review of original images.
Never overwrites the input; uses Python standard library only.
"""
import argparse
import csv
import json
from collections import defaultdict, Counter
from pathlib import Path

CATEGORIES = {"Educational":"educational.csv","Marketing":"marketing.csv",
              "Motivational":"motivational.csv","Religious":"religious.csv",
              "Political":"political.csv","Social Awareness":"socialawareness.csv",
              "News":"news.csv","Entertainment":"entertainment.csv"}
REQUIRED = ["image_id","caption","raw_ocr","main_ocr","phash","image_width","image_height","label"]


def read(path):
    with path.open(encoding="utf-8-sig",newline="") as f:
        reader=csv.DictReader(f)
        fields=reader.fieldnames or []
        return fields,list(reader)


def write(path,fields,rows):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",encoding="utf-8-sig",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=fields,extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def norm_id(image_id,label):
    return (label.strip().lower().replace(" ","")+"/"+image_id.replace("\\","/").split("/")[-1].strip().lower())


def annotation_ids(path):
    if path is None:return set()
    fields,rows=read(path)
    if not {"image_id","Original_label"}.issubset(fields):
        raise ValueError("Annotation CSV needs image_id and Original_label")
    return {norm_id(r["image_id"],r["Original_label"]) for r in rows}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--csv",required=True,type=Path)
    p.add_argument("--annotation",type=Path)
    p.add_argument("--out",required=True,type=Path)
    p.add_argument("--apply",action="store_true")
    p.add_argument("--confirm-reviewed",action="store_true")
    args=p.parse_args()
    fields,rows=read(args.csv)
    if not set(REQUIRED).issubset(fields):
        raise ValueError("Input CSV lacks required fields")
    if len({r["image_id"] for r in rows})!=len(rows):
        raise ValueError("Repeated image IDs in source dataset")
    if any(not (r["phash"] or "").strip() for r in rows):
        raise ValueError("Missing pHash in source dataset")
    if set(r["label"] for r in rows)-set(CATEGORIES):
        raise ValueError("Unexpected category label")
    sampled=annotation_ids(args.annotation)
    groups=defaultdict(list)
    for r in rows:
        groups[r["phash"].strip().lower()].append(r)
    repeated={h:g for h,g in groups.items() if len(g)>1}
    args.out.mkdir(parents=True,exist_ok=True)
    plan_path=args.out/"retention_plan.csv"
    plan_fields=["phash","group_size","category","all_image_ids","keep_image_id","keeper_is_annotated","review_note"]
    if not plan_path.exists():
        plan=[]
        for h,g in repeated.items():
            if len({r["label"] for r in g})!=1:
                raise ValueError(f"Cross-class pHash group {h}; review category assignments")
            in_sample=[r for r in g if norm_id(r["image_id"],r["label"]) in sampled]
            if len(in_sample)>1:
                raise ValueError(f"Multiple annotated records in {h}; review sampling implications")
            keeper=in_sample[0] if in_sample else g[0]
            plan.append({"phash":h,"group_size":len(g),"category":keeper["label"],
                         "all_image_ids":"; ".join(r["image_id"] for r in g),
                         "keep_image_id":keeper["image_id"],
                         "keeper_is_annotated":"YES" if in_sample else "NO",
                         "review_note":"Candidate only; original image review required"})
        write(plan_path,plan_fields,plan)
    preview={"input_records":len(rows),"candidate_groups":len(repeated),
             "records_in_candidate_groups":sum(map(len,repeated.values())),
             "proposed_removals":sum(len(g)-1 for g in repeated.values())}
    (args.out/"preview_summary.json").write_text(json.dumps(preview,indent=2)+"\n",encoding="utf-8")
    if not args.apply:
        print(json.dumps(preview,indent=2))
        print("Preview only. Inspect original images and the retention plan before --apply --confirm-reviewed.")
        return
    if not args.confirm_reviewed:
        raise ValueError("Require --confirm-reviewed after manual image review")
    pfields,plan=read(plan_path)
    if not {"phash","keep_image_id"}.issubset(pfields) or len(plan)!=len(repeated):
        raise ValueError("Invalid retention plan")
    keep={}
    for entry in plan:
        h=entry["phash"].strip().lower()
        ids={r["image_id"] for r in repeated.get(h,[])}
        if h in keep or entry["keep_image_id"] not in ids:
            raise ValueError(f"Invalid retained record for pHash {h}")
        keep[h]=entry["keep_image_id"]
    if set(keep)!=set(repeated):
        raise ValueError("Retention plan does not cover the same groups")
    retained=[]
    removed=[]
    for index,r in enumerate(rows,2):
        h=r["phash"].strip().lower()
        if h in keep and r["image_id"]!=keep[h]:
            removed.append({"original_csv_line":index,"phash":h,"category":r["label"],
                            "removed_image_id":r["image_id"],"retained_image_id":keep[h]})
        else:
            retained.append(r)
    if any(norm_id(x["removed_image_id"],x["category"]) in sampled for x in removed):
        raise ValueError("Plan would remove an annotation-sample record; reconsider keeper choices")
    if len({r["phash"].strip().lower() for r in retained})!=len(retained):
        raise AssertionError("Identical hashes remain")
    write(args.out/"COMBINED_V2.csv",fields,retained)
    for label,filename in CATEGORIES.items():
        selected=[]
        for r in retained:
            if r["label"]==label:
                row=dict(r)
                row["image_id"]=r["image_id"].replace("\\","/").split("/")[-1]
                selected.append(row)
        write(args.out/filename,fields,selected)
    write(args.out/"removed_records_audit.csv",
          ["original_csv_line","phash","category","removed_image_id","retained_image_id"],removed)
    result={**preview,"removed_records":len(removed),"retained_records":len(retained),
            "counts_by_category":dict(Counter(r["label"] for r in retained)),
            "note":"Researcher-confirmed manual review required; script only follows reviewed keeper decisions."}
    (args.out/"version2_preprocessing_summary.json").write_text(
        json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps(result,indent=2,ensure_ascii=False))


if __name__=="__main__":
    main()
