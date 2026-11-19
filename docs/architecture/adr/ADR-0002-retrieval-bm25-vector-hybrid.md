# ADR-0002: BM25 by default; vector and hybrid optional

- **Status**: Accepted
- **Date**: 2026-11-19

## Context
Retrieval quality is the main driver of RAG answer quality, and it is what the CI gate
measures. The gate must be **deterministic** and run on a free CI runner without model
downloads. HR/benefits questions are often keyword-heavy (entity names, "parental leave",
country names), and BM25 is strong on those. Paraphrased questions ("time off when my baby is
born") favour dense retrieval.

## Decision
We will use **BM25 (`rank_bm25.BM25Okapi`)** over chunk text plus heading path as the default
and CI retriever. Dense retrieval (`HuggingFaceEmbeddings`, `BAAI/bge-small-en-v1.5`, Chroma)
and **hybrid** (RRF by default, weighted min-max as an option) are available behind
`configs/retrieval.yaml: mode`, and their value is measured in stage 01 rather than assumed.

## Consequences
- ➕ Same metrics on every run → the gate cannot be flaky; no network, no GPU, no cost.
- ➕ Explainable: you can show exactly which terms matched.
- ➖ Weak on paraphrases and synonyms. The golden set includes `paraphrase`-tagged items to make this visible.
- ➖ Tokenisation choices (stopwords, stemming) change results. They are config, and covered by tests.
- ⚖️ If hybrid wins clearly in stage 01, production would use hybrid, with CI still gating BM25 plus a separate, non-blocking hybrid report (see ADR-0005).

## Alternatives considered
| Option | Pros | Cons | Why not (as default) |
|---|---|---|---|
| Dense only | handles paraphrase | model download in CI, float/hardware nondeterminism, less explainable | breaks the deterministic gate |
| Hybrid by default | usually best recall | inherits dense drawbacks | same; kept as an option |
| LangChain `BM25Retriever` | one-liner | less control over tokenisation and tie-breaking | we need deterministic tie-break by chunk_id |
| Elasticsearch/OpenSearch BM25 | production-grade | infrastructure overhead | overkill for ~200 pages |
