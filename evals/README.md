# Evaluation data

| File | What | Committed? |
|---|---|---|
| `golden_set.example.jsonl` | 5 example items showing the schema (real quotes, handbook commit `5641a835`) | yes |
| `golden_set.jsonl` | the real golden set, ~30 items (step 1.2) | yes (short quotes, CC BY-SA attribution via doc_id -> URL) |
| `baseline.json` | metrics of the accepted baseline run, read by the CI gate | yes, changed only in reviewed commits |
| `labels/human_labels.jsonl` | my ~50 human labels (step 2.3) | yes |
| `fixtures/` | pre-recorded fake LLM answers / judge verdicts / agent scripts | yes |

## Golden item schema

```json
{
  "id": "q001",
  "question": "...",
  "reference_answer": "...",
  "relevant_doc_ids": ["total-rewards/benefits/modern-health"],
  "evidence": ["verbatim quote from the page that proves the answer"],
  "answerable": true,
  "tags": ["benefits", "number"]
}
```

Why `evidence` and not chunk ids: chunk ids change every time chunking changes, so labels
would silently rot exactly in the experiments we want to run (ADR-0004). A chunk counts as
relevant if it contains the evidence quote (`eval/golden_set.py::relevant_chunk_ids`).

## Coverage rules for the 30 items (step 1.2)

- mix of tags: `number`, `eligibility`, `multi-fact` (answer spans 2 sections), `country-specific`,
  `paraphrase` (question uses different words than the page: hard for BM25), `unanswerable` (≥ 3 items);
- at least 3 sections of the handbook;
- write questions as an employee would ask them, not by copying headings.
