# ADR-0004: Heading-aware chunking and evidence-based relevance labels

- **Status**: Accepted
- **Date**: 2026-11-19

## Context
Handbook pages are long Markdown with a deep heading structure. Eligibility rules, numbers
and exceptions often sit in short lists under a heading, and a fixed-size split separates
them from that heading. Chunking is also the parameter we expect to tune, so the golden-set
relevance labels **must survive chunking changes**. Labelling by `chunk_id` would make every
chunking experiment invalidate its own ground truth.

## Decision
1. Default strategy `markdown_headings` (design from LocalSmartRAG `smart_splitter`): split on `#`–`###`; keep ``` fences atomic; within a section cut at paragraph, then sentence boundaries; fall back to a character split with overlap. Defaults `chunk_size=800`, `chunk_overlap=150` characters, to be validated in stage 01.
2. Prefix each chunk with its **heading path** (`Leave > Parental leave > Eligibility`). It carries strong BM25 terms and makes citations readable.
3. Store **char offsets** on each chunk. The golden set labels **documents + verbatim evidence quotes**, and chunk relevance is derived at eval time (`relevant_chunk_ids`: a chunk is relevant if it contains ≥ 80% of an evidence span).
4. Keep `recursive_chars` (LangChain `RecursiveCharacterTextSplitter`) as the baseline for before/after and for the CI-gate break demo.

## Consequences
- ➕ Chunking experiments are a fair comparison: same labels, different chunks.
- ➕ Golden set is cheaper to write (copy a quote, not hunt chunk ids).
- ➖ Evidence quotes break when the source text changes. This is mitigated by a pinned corpus commit and `validate_against_corpus` (RAID D-01).
- ➖ An answer that needs two evidence spans in different chunks makes recall@k depend on k. The `multi-fact` tag makes this visible.
- ⚖️ Character-based sizes, not tokens: simpler and model-independent. Tokens are revisited if a real LLM context limit matters.

## Alternatives considered
| Option | Pros | Cons | Why not |
|---|---|---|---|
| Fixed-size recursive split only | simple, standard | cuts lists from headings | kept as baseline only |
| Semantic chunking (embedding breakpoints) | topic-coherent | needs embeddings, nondeterministic, slow | conflicts with ADR-0002 |
| Whole page = chunk | no splitting errors | long pages dilute BM25 and overflow context | poor precision |
| Labels = chunk ids | simplest metric code | labels rot on every chunking change | invalidates experiments |
