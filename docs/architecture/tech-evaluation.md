# Technology evaluation

Method: weighted criteria, score 1–5, weighted total = Σ(weight × score) / 5 (max 100).
Scores are judgement calls by me, with the evidence noted. They are a way to force explicit
trade-offs, not a measurement.

## 1. Base RAG system

| Criterion | Weight | LocalSmartRAG | LangChain official tutorial | pixegami/rag-tutorial-v2 |
|---|---|---|---|---|
| Fit: explicit chunking + retrieval knobs (BM25, hybrid) | 30 | 5: BM25+vector, RRF/weighted, heading splitter | 3: splitter params only, vector only | 3: splitter + Chroma |
| Readability / size | 20 | 4: ~15 small modules, docstrings (Chinese) | 5: one page | 5: few files |
| Maintained (commits in last 12 months) | 20 | 5: 2026-09 | 5: docs updated 2026 | 1: 2024-08 |
| Licence allows adaptation | 15 | 5: MIT | 4: MIT (LangChain) | 1: no licence |
| Works without paid APIs | 15 | 5: Ollama local | 2: OpenAI embeddings by default | 5: Ollama |
| **Weighted total** | 100 | **96** | 76 | 60 |

Decision → ADR-0001.

## 2. Vector store (optional dense path)

| Criterion | Weight | Chroma | FAISS | Qdrant | pgvector |
|---|---|---|---|---|---|
| Zero-infrastructure local use | 30 | 5 | 5 | 3 (server/docker; has local mode) | 2 (Postgres) |
| LangChain integration | 20 | 5 | 5 | 5 | 4 |
| Metadata filtering (needed for section tool) | 25 | 4 | 2 (manual) | 5 | 5 |
| Production path | 25 | 3 | 2 | 5 | 5 |
| **Weighted total** | 100 | **85** | 70 | 88 | 78 |

Qdrant scores highest overall, but its production advantages don't matter in a learning scope
that is never deployed. **Chroma** is chosen for zero setup. A production recommendation would
be Qdrant or pgvector, depending on the existing stack: pgvector if the company already runs
Postgres.

## 3. Evaluation framework

| Criterion | Weight | Own harness | Ragas | DeepEval |
|---|---|---|---|---|
| Deterministic retrieval metrics without an LLM | 30 | 5 | 3: some non-LLM metrics, core metrics are LLM-based | 3: mostly LLM-based |
| Learning value / explainability in interview | 25 | 5 | 3 | 3 |
| Breadth of ready metrics (faithfulness, etc.) | 20 | 2 | 5 | 5 |
| CI integration | 15 | 4: own exit code | 3 | 5: pytest-style |
| Dependency weight | 10 | 5 | 3 | 3 |
| **Weighted total** | 100 | **85** | 68 | 74 |

**Decision**: write our own harness for retrieval metrics, the gate and judge validation,
because the gate must be deterministic and the point is to understand the metrics. Keep the
`Judge` interface compatible so that Ragas/DeepEval metrics can be added later as alternative
judges and their scores compared with ours. Not an ADR yet: revisit after stage 02.

## Recommendation summary

| Area | Choice now | Production recommendation |
|---|---|---|
| RAG base | LocalSmartRAG design, re-implemented | same structure; add ACL filter, reranker |
| Retrieval | BM25 (gate), hybrid optional | hybrid + reranker, gate stays deterministic |
| Vector store | Chroma | Qdrant or pgvector |
| Eval | own harness | own gate + a framework for LLM-based metrics |
