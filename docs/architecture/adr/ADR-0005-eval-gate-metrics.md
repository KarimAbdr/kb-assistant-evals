# ADR-0005: Eval gate on deterministic retrieval metrics only

- **Status**: Accepted
- **Date**: 2026-11-19

## Context
We want CI to prevent quality regressions: a PR that changes chunking, tokenisation or k
must not quietly reduce answer quality. A gate that fails randomly gets ignored or disabled.
LLM-judge scores vary between runs and cost money with a real model. Retrieval metrics on a
fixed corpus and golden set are exact.

## Decision
The **blocking** gate uses retrieval metrics only, at k from `configs/gate.yaml`:
- **recall@k**: did we fetch the evidence the answer needs? (primary: the generator cannot use what was not retrieved);
- **hit rate@k**: at least one relevant chunk per question (user-facing "did we find anything");
- **MRR**: is the relevant chunk ranked near the top (matters because of lost-in-the-middle and smaller k).

A PR fails if any metric is **below its absolute floor** or **drops more than `max_regression`
(0.02) from `evals/baseline.json`**. The baseline changes only in a separate, reviewed commit
(`kb gate --update-baseline`). Triad/judge metrics are **reported, not blocking**, until the
judge is validated (stage 02 kappa) and a real model is attached.

## Consequences
- ➕ Deterministic, fast, free; a red check always means a real regression.
- ➕ Two-sided rule: floors catch "bad", regression limit catches "worse than before" even above the floor.
- ➖ Does not catch generation-only regressions (prompt change that increases hallucination). That is a known gap (RAID R-04), covered later by a non-blocking triad job.
- ➖ ~30 questions are coarse: one question is about 3 percentage points of hit rate. `max_regression=0.02` therefore means "no question may flip from hit to miss". This is strict on purpose.
- ⚖️ Overfitting risk: tuning only to pass the gate. Mitigation: keep a held-out subset not used for tuning (RAID R-05).

## Alternatives considered
| Option | Pros | Cons | Why not |
|---|---|---|---|
| Gate on judge triad | measures answers, not just retrieval | flaky, costs money, judge unvalidated | breaks trust in CI |
| Absolute thresholds only | simple | allows slow decline above the floor | no regression protection |
| Statistical test (bootstrap CI) vs baseline | principled | overkill for n≈30; harder to explain | later, if golden set grows |
| No gate, dashboard only | zero friction | regressions are found after release | defeats the purpose |
