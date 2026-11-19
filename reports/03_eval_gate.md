# Report 03: Eval gate in CI

> Template. Fill from `kb gate` output and the GitHub Actions run (or a local run before pushing).

## Gate definition

| Metric | Threshold (floor) | Max regression vs baseline | Baseline |
|---|---|---|---|
| recall@k | {TBD} | 0.02 | {TBD} |
| MRR | {TBD} | 0.02 | {TBD} |
| hit rate@k | {TBD} | 0.02 | {TBD} |

Why these metrics block and the triad does not: ADR-0005.

## Demo: a breaking change is blocked

| Run | Branch / change | recall@k | MRR | hit rate | Gate |
|---|---|---|---|---|---|
| Baseline | `main` | {TBD} | {TBD} | {TBD} | ✅ |
| Breaking | `demo/break-chunking` (`chunk_size: 100, overlap: 0`) | {TBD} | {TBD} | {TBD} | ❌ |
| Fixed | revert | {TBD} | {TBD} | {TBD} | ✅ |

Gate output (paste from the run): `{TBD}`

## Determinism check

Two consecutive runs on the same commit produce identical metrics: `{TBD}` (yes/no + hashes)

## Operating rules

- The baseline is updated only by `kb gate --update-baseline` in a separate, reviewed commit with a reason.
- Golden-set changes and code changes go in separate PRs (otherwise a regression can hide behind new questions).
