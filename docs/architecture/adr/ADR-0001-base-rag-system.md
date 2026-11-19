# ADR-0001: Base RAG system: adapt LocalSmartRAG

- **Status**: Accepted
- **Date**: 2026-11-19

## Context
The project's value is the evaluation layer, not a novel RAG implementation. We need a small,
readable, maintained open-source RAG in Python on LangChain, with clear places to change
chunking and retrieval, so that the eval experiments have real knobs to turn. The constraints
are no paid APIs and a licence that allows adaptation.

## Decision
We will adapt the design of **[LocalSmartRAG](https://github.com/ningmeng446/LocalSmartRAG)**
(MIT, last commit 2026-09, LangChain + rank_bm25 + Chroma + Ollama). We will mirror its module
split (`document_loader`, `text_cleaner`, `smart_splitter`, `retriever_hybrid`, `rag_chain`)
into our packages (`ingest`, `chunking`, `retrieval`, `generation`) and re-implement them step
by step for an English corpus. Concretely:

- tokenisation: `jieba` → English tokenizer (lowercase, stopwords, optional stemming);
- prompts: Chinese → English, same rules (answer only from numbered context, cite `[n]`, explicit refusal);
- LLM: hard-wired `ChatOllama` → `LLMProvider` (ADR-0003);
- default retrieval: hybrid → BM25 only, hybrid behind a flag (ADR-0002);
- drop Streamlit UI, session memory, PDF/DOCX loaders and reranker (out of scope).

## Consequences
- ➕ Retrieval design that has been thought through: per-query min-max normalisation before weighted fusion, RRF option, heading-first chunking with protected code blocks.
- ➕ MIT licence: ideas and code can be reused with the notice kept (THIRD_PARTY.md).
- ➖ Small project (≈50 stars), docs in Chinese, no tests: we read the code itself, not its docs, and write our own tests.
- ➖ Its chunk size and overlap defaults (800/150) were tuned for Chinese text. They have to be re-validated on English (stage 01).
- ⚖️ We are not tied to its runtime: nothing is imported from it.

## Alternatives considered
| Option | Pros | Cons | Why not |
|---|---|---|---|
| Official LangChain RAG tutorial (docs.langchain.com) | canonical, maintained, familiar vocabulary | current version is an agentic Deep-Agent example on OpenAI embeddings. The classic 2-step chain is only a fragment of it | less structure to adapt; needs paid embeddings by default |
| pixegami/rag-tutorial-v2 | very small, local Ollama, has quality tests | last commit 2024-08, no licence file | fails the "maintained" criterion; licence forbids copying |
| langchain-ai/rag-from-scratch | excellent concepts, 10k★ | notebooks, last push 2025-06, no licence | not a system to extend |
| Write from scratch | full control | no external reference point for the review | slower, less defensible "why this design" |

Detailed scoring: [tech-evaluation.md §1](../tech-evaluation.md).
