# Human labels

`human_labels.jsonl`, one record per (item_id, criterion), written by `kb label` (step 2.2):

```json
{"item_id": "q001", "criterion": "correctness", "score": 2, "note": "", "rubric_version": "v1", "labeled_at": "2026-..."}
```

Rules: label before looking at judge scores; never edit by hand after the fact; if the rubric
changes, bump `rubric_version` and relabel.
