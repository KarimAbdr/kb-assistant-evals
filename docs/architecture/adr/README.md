# Architecture Decision Records

Format: Michael Nygard (Title, Status, Context, Decision, Consequences) + Alternatives considered.
An ADR is never edited after it is accepted. To change a decision, write a new ADR that supersedes it.

| ADR | Title | Status |
|---|---|---|
| [0001](ADR-0001-base-rag-system.md) | Base RAG system: adapt LocalSmartRAG | Accepted |
| [0002](ADR-0002-retrieval-bm25-vector-hybrid.md) | BM25 by default; vector and hybrid optional | Accepted |
| [0003](ADR-0003-llm-provider-abstraction.md) | `LLMProvider` abstraction with fake implementations | Accepted |
| [0004](ADR-0004-chunking-strategy.md) | Heading-aware chunking and evidence-based relevance labels | Accepted |
| [0005](ADR-0005-eval-gate-metrics.md) | Eval gate on deterministic retrieval metrics only | Accepted |

Template: [`template.md`](template.md)
