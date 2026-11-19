# Report 02: Is the LLM judge trustworthy?

> Template. Fill from `kb judge validate` output.

## Setup

| Item | Value |
|---|---|
| Rubric | `judge/rubric.py` version `{TBD}`, criterion `{TBD}`, scale 0/1/2 |
| Human labels | `{TBD}` items by 1 annotator (me), `evals/labels/human_labels.jsonl` |
| Judge | `{TBD}` (FakeJudge fixtures now; a real model later) |
| Label distribution (human) | 0: {TBD} · 1: {TBD} · 2: {TBD} |

## 1. Agreement

| Metric | Value | How to read |
|---|---|---|
| Accuracy | {TBD} | share of exact matches; inflated when one class dominates |
| Cohen's kappa (unweighted) | {TBD} | chance-corrected; ~0.6+ is usually called substantial (Landis & Koch) |
| Cohen's kappa (quadratic) | {TBD} | penalises 0↔2 disagreements more than 1↔2 |

Confusion matrix (rows = human, columns = judge):

| | 0 | 1 | 2 |
|---|---|---|---|
| **0** | {TBD} | {TBD} | {TBD} |
| **1** | {TBD} | {TBD} | {TBD} |
| **2** | {TBD} | {TBD} | {TBD} |

Direction of errors: too lenient / too strict? `{TBD}`

## 2. Position bias

- Method: `{TBD}` pairs, each judged as (A,B) and (B,A).
- Consistency rate: `{TBD}` · first-position wins when inconsistent: `{TBD}`
- Mitigation applied: judge both orders, keep only consistent verdicts, otherwise "tie". Result after mitigation: `{TBD}`

## 3. Verbosity bias

- Method: `{TBD}` short correct answers vs `make_verbose()` versions (same facts + filler), both orders.
- Long-answer win rate: `{TBD}` (ideal: ties)
- Mitigation: `{TBD}` (rubric line "length is not quality", reference-based scoring instead of pairwise)

## 4. Verdict

- Can this judge be used for `{criterion}`? `{TBD}` · For which decisions it is NOT enough: `{TBD}`
- Limits: 1 annotator (no inter-annotator agreement), small n, so kappa has a wide confidence interval: `{TBD}`
