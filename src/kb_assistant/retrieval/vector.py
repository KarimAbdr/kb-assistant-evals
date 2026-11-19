"""Optional dense retriever: HuggingFaceEmbeddings (bge-small-en-v1.5) + Chroma/FAISS.

Requires `pip install -e .[vector]`. Not used in CI: model downloads and float
non-determinism across hardware would make the gate flaky (RAID R-03).
"""

from __future__ import annotations

from kb_assistant.types import Chunk, RetrievedChunk


class VectorRetriever:
    """Embeds chunks locally and does cosine top-k."""

    def __init__(self, embedding_model: str, store: str = "chroma", persist_dir: str | None = None) -> None:
        self.embedding_model = embedding_model
        self.store = store
        self.persist_dir = persist_dir

    def index(self, chunks: list[Chunk]) -> None:
        """Embed and upsert chunks with chunk_id as the store id (idempotent re-index). TODO(step-1.6)"""
        raise NotImplementedError("TODO(step-1.6)")

    def retrieve(self, query: str, k: int) -> list[RetrievedChunk]:
        """bge models expect the query prefix "Represent this sentence for searching relevant passages: ". TODO(step-1.6)"""
        raise NotImplementedError("TODO(step-1.6)")
