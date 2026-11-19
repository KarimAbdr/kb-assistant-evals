# Engineering standards

## Module boundaries
- Packages talk only through types in `src/kb_assistant/types.py`. No module imports another module's private helpers.
- Dependencies point "down" the data flow: `eval` may import `retrieval`, never the reverse. `judge` and `generation` share only the `LLMProvider` protocol.
- Every external technology sits behind a protocol + factory (`Retriever`, `LLMProvider`, `Judge`).

## Configuration
- Every tunable lives in `configs/*.yaml`, never as a literal in code (exception: documented defaults in dataclasses that mirror the YAML).
- Experiments are override files in `configs/experiments/`. One experiment changes one variable.
- Each run writes `config.json` and a config fingerprint. No fingerprint means the result is not reportable.

## Determinism
- Sort inputs (files, ids); break score ties by `chunk_id`; `temperature=0`; no time or randomness in anything the gate reads.
- The corpus is pinned (`data/CORPUS_COMMIT`).

## Logging and artefacts
- `logging` module, logger per module (`logging.getLogger(__name__)`), no `print` in library code (CLI output is fine).
- Run artefacts: `runs/<UTC timestamp>_<fingerprint>/` with `metrics.json`, `per_query.jsonl`, `config.json`, and where relevant `trajectories.jsonl`.
- Reports in `reports/` quote artefact paths. Numbers are never typed by hand.

## Code style
- Python 3.12, type hints everywhere, `ruff` (line length 100).
- Docstring per public function: what it does, input/output, why it exists.
- Pure functions for metrics and the gate decision (no I/O), so they are trivial to test.

## Tests
- `pytest`; unit tests use the in-memory `tiny_pages` fixture, never the downloaded corpus.
- A stub's test is `skip`ped with `TODO(step-N)` and turned on in the step that implements it.

## How to add a new metric
1. Pure function in `eval/retrieval_metrics.py` (or a new module) + docstring explaining how to read it.
2. Hand-computed unit test with a tiny example.
3. Register it in the runner's metric list so it appears in `metrics.json`.
4. Add it to the report template. If it should block releases, write an ADR (superseding ADR-0005) and add a threshold to `configs/gate.yaml`.

## Git
- Golden-set / baseline changes and code changes go in separate commits.
- Commit message prefix by stage: `stage0:`, `s01:`, …
