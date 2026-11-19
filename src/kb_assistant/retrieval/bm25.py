"""BM25 retriever on rank_bm25.BM25Okapi.

Why default: no model, no network, fully deterministic -> the CI gate gives the same
numbers on every run (ADR-0002, ADR-0005).
"""

from __future__ import annotations

from kb_assistant.types import Chunk, RetrievedChunk


class BM25Retriever:
    """BM25 over chunk text (heading_path included, it carries strong keywords)."""

    def __init__(self, k1: float = 1.5, b: float = 0.75, **tokenize_kwargs: bool) -> None:
        self.k1 = k1
        self.b = b
        self.tokenize_kwargs = tokenize_kwargs
        self._chunks: list[Chunk] = []

    def index(self, chunks: list[Chunk]) -> None:
        """Tokenise every chunk and build BM25Okapi(k1, b). TODO(step-0.6)"""
        raise NotImplementedError("TODO(step-0.6)")

    def retrieve(self, query: str, k: int) -> list[RetrievedChunk]:
        """Score all chunks, return top-k. Ties broken by chunk_id for determinism. TODO(step-0.6)"""
        raise NotImplementedError("TODO(step-0.6)")
