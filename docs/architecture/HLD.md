# High-Level Design: KB Assistant with Evaluation

| | |
|---|---|
| Document status | Draft v0.1 (learning project) |
| Owner | {author} |
| Last updated | 2026-11-19 |
| Related | [ADRs](adr/), [RAID](RAID.md), [Diagrams](diagrams/), [Tech evaluation](tech-evaluation.md), [Review](architecture-review.md) |

## 1. Purpose

Employees spend time searching internal documentation (HR policies, benefits, processes), and
a chat assistant only helps if its answers are **correct, grounded and traceable to a
source**. The system has two parts:

1. a retrieval-augmented **knowledge assistant** over internal documentation (stand-in corpus: GitLab Handbook);
2. an **evaluation and quality-gate platform** that measures retrieval and answer quality, validates the automated judge, and blocks releases that regress.

Part 2 is the focus. Part 1 is kept minimal and replaceable.

## 2. Scope

**In scope**
- Ingestion of Markdown documentation from a pinned source snapshot
- Heading-aware chunking, BM25 retrieval (default), optional dense and hybrid retrieval
- Answer generation behind an `LLMProvider` abstraction, with citations and refusal
- Golden-set retrieval metrics (recall@k, MRR, hit rate), RAG triad via a judge interface
- Judge validation against human labels (Cohen's kappa, accuracy, position and verbosity bias)
- CI eval gate on deterministic retrieval metrics
- Tool-using agent with trajectory logging and trajectory metrics (stage 2)

**Out of scope**
- Production UI, authentication/SSO, multi-tenancy
- Document-level access control (ACL-aware retrieval): see RAID R-06 and §7.4
- Paid LLM APIs, fine-tuning, online A/B testing, real-time ingestion
- Multilingual support

## 3. Context

Users (employees) ask questions. The assistant reads from the documentation source and calls
an LLM through the provider abstraction. Engineers change the code or config, and CI runs the
eval gate before merging. See [System Context diagram](diagrams/01-system-context.md).

| Actor / system | Interaction |
|---|---|
| Employee | asks questions, receives answers with citations |
| Knowledge engineer (me) | maintains golden set, labels judge outputs, tunes config |
| Documentation source (GitLab Handbook repo) | Markdown at a pinned commit, read-only |
| LLM runtime (fake now; Ollama/API later) | text generation, judge verdicts |
| CI (GitHub Actions) | runs tests + eval gate on every PR |

## 4. Building blocks

See [Container](diagrams/02-container.md) and [Component](diagrams/03-component-rag-eval.md) diagrams.

| Component | Responsibility | Key decision |
|---|---|---|
| `ingest` | Markdown → `Page` (doc_id, url, section, cleaned text) | deterministic order; Hugo shortcode cleanup |
| `chunking` | `Page` → `Chunk` with heading path and char offsets | heading-aware, 800/150 chars (ADR-0004) |
| `retrieval` | query → top-k chunks | BM25 default; vector/hybrid optional (ADR-0002) |
| `generation` | prompt with numbered context, citations, refusal | `LLMProvider` + fake provider (ADR-0003) |
| `eval` | golden set, retrieval metrics, triad, runner, gate | evidence-span labels; retrieval-only gate (ADR-0005) |
| `judge` | rubric, judge interface, agreement, bias probes | judge must be validated before use |
| `labeling` | CLI for human labels | judge scores hidden while labelling |
| `agent` | 2 tools, step-budgeted loop, JSONL trajectories | hand-written loop for observability |

Base RAG design adapted from LocalSmartRAG (ADR-0001).

## 5. Data flows

1. **Indexing** (offline): source @ commit → ingest → clean → chunk → BM25 index (in memory; vector index persisted if enabled).
2. **Query** (online): question → tokenize → retrieve top-k → render prompt → `LLMProvider.generate` → parse citations → answer or refusal. See [sequence](diagrams/04-sequence-query.md).
3. **Evaluation** (offline/CI): golden set → for each item retrieve (+ generate + judge) → per-query results → aggregate metrics → run artefact `runs/<id>/`.
4. **Gate** (CI): metrics vs thresholds and baseline → pass/fail. See [sequence](diagrams/05-sequence-ci-gate.md).
5. **Judge validation**: generated answers → human labels (CLI) + judge verdicts → kappa/accuracy/bias report.

### Data model (core)

`Page(doc_id, url, title, section, text)` → `Chunk(chunk_id, doc_id, heading_path, start, end, text)` →
`RetrievedChunk(chunk, score, rank)` → `RagAnswer(answer, contexts, citations, refused)`.
Golden: `GoldenItem(id, question, reference_answer, relevant_doc_ids, evidence[], answerable)`.

## 6. Non-functional requirements

| NFR | Target (learning scope) | How it is addressed |
|---|---|---|
| **Reliability / correctness** | answers grounded in retrieved context; refusal when not found | citation prompt, refusal text, groundedness metric, unanswerable items in golden set |
| **Reproducibility** | same commit + config + corpus ⇒ identical retrieval metrics | pinned corpus commit, deterministic BM25 + tie-break, config fingerprint in artefacts |
| **Regression safety** | no merge that drops retrieval quality | CI gate: floors + max regression vs baseline (ADR-0005) |
| **Latency** | interactive p95 `{TBD}` once a real LLM is attached | BM25 in memory; top-k bounded; LLM dominates latency |
| **Cost** | 0 € in development and CI | fake LLM/judge; no API keys; cached corpus in CI |
| **Security / privacy** | no secrets in repo; no data leaves the machine | no external LLM calls; `.env` ignored; corpus is public. Production: ACL-aware retrieval and PII handling (§7.4) |
| **Maintainability** | a stage can change without touching others | typed contracts in `types.py`, config-driven, factories, [standards](standards.md) |
| **Observability** | every eval/agent run is inspectable after the fact | per-query JSONL, trajectories JSONL, metrics.json with fingerprints |
| **Licensing compliance** | respect CC BY-SA 4.0 of the corpus, MIT of the base | corpus not redistributed; attribution via URLs; THIRD_PARTY.md |

## 7. Cross-cutting concerns

### 7.1 Configuration
YAML in `configs/`. Experiments are small override files. Each run records a config fingerprint.

### 7.2 Evaluation strategy
Two layers. **Deterministic** retrieval metrics are cheap, stable and gate-able. **Judge-based**
triad scores are richer but stochastic: they are reported and not gated until the judge is
validated (stage 02) and a real model is attached.

### 7.3 Failure handling
Missing fixture ⇒ hard error, never a silent default. Judge parse failure ⇒ one retry, then
the item is marked `judge_error` and counted, not dropped. Agent step budget ⇒ forced stop,
counted as a failure mode.

### 7.4 Path to production (not implemented)
ACL-aware retrieval (filter by document permissions before ranking), PII redaction in logs,
incremental re-indexing on document change, prompt-injection defence for documents, online
monitoring (answer feedback, refusal rate, citation click-through), golden set refreshed from
real user questions.

## 8. Deployment view

| Environment | What runs | Notes |
|---|---|---|
| Local dev | CLI `kb …`, venv (uv), Python 3.12 | corpus in `data/raw` |
| CI | GitHub Actions `eval-gate.yml`: install → corpus (cached by commit) → pytest → `kb gate` | no secrets required |
| Production (hypothetical) | API service + vector store + LLM endpoint + scheduled re-index + eval job | see §7.4, not built |

## 9. Open questions

- Gate thresholds: set after first baseline (step 3.2). `{TBD}`
- Is hybrid retrieval worth its non-determinism outside CI? Answered by the stage 01 experiment. `{TBD}`
- Which real local model for the judge (later): `{TBD}`
