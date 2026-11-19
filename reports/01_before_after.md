# Report 01: Retrieval weakness → fix → before/after

> Template. Every `{TBD}` is filled **from run artefacts** (`runs/<id>/metrics.json`), never by hand.

## Setup

| Item | Value |
|---|---|
| Corpus | GitLab Handbook subset, commit `{TBD}` (`data/CORPUS_COMMIT`), `{TBD}` pages, `{TBD}` chunks |
| Golden set | `evals/golden_set.jsonl`, `{TBD}` items (`{TBD}` answerable, `{TBD}` unanswerable) |
| k | `{TBD}` |
| Generator / judge | FakeProvider / FakeJudge (fixtures): triad numbers show the *harness* works, not model quality |
| Before run | `runs/{TBD}` (config fingerprint `{TBD}`) |
| After run | `runs/{TBD}` (config fingerprint `{TBD}`) |

## 1. Weakness found

- **Hypothesis**: `{TBD}` (for example, "200-char chunks with no overlap split eligibility rules from their heading, so BM25 misses them")
- **Evidence**: questions that missed: `{TBD ids}`, and why each one missed (error analysis from `per_query.jsonl`): `{TBD}`

## 2. Single change

- Changed: `{TBD}` (one variable only, e.g. `configs/experiments/chunk_small.yaml` → default heading-aware chunking)
- Not changed: corpus commit, golden set, k, tokenizer

## 3. Results

| Metric | Before | After | Δ |
|---|---|---|---|
| recall@k | {TBD} | {TBD} | {TBD} |
| MRR | {TBD} | {TBD} | {TBD} |
| hit rate@k | {TBD} | {TBD} | {TBD} |
| context relevance (judge) | {TBD} | {TBD} | {TBD} |
| groundedness (judge) | {TBD} | {TBD} | {TBD} |
| answer relevance (judge) | {TBD} | {TBD} | {TBD} |

Flipped miss → hit: `{TBD}` · Flipped hit → miss (regressions!): `{TBD}`

## 4. Interpretation and limits

- Is the delta bigger than noise? With ~30 questions, one question is about 3 percentage points of hit rate: `{TBD}`
- Risk of overfitting to the golden set: `{TBD}`
- Decision / ADR updated: ADR-0004 (`{TBD}`)
