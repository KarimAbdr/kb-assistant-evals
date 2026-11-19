"""Retriever interface shared by BM25 / vector / hybrid."""

from __future__ import annotations

from typing import Protocol

from kb_assistant.types import Chunk, RetrievedChunk


class Retriever(Protocol):
    """Anything that can index chunks and return top-k for a query."""

    def index(self, chunks: list[Chunk]) -> None:
        """Build the index (in memory for BM25; persisted for vector)."""
        ...

    def retrieve(self, query: str, k: int) -> list[RetrievedChunk]:
        """Return up to k chunks sorted by descending score, rank starting at 1."""
        ...


def build_retriever(cfg: dict) -> Retriever:
    """Factory: configs/retrieval.yaml mode -> concrete retriever. TODO(step-0.6)"""
    raise NotImplementedError("TODO(step-0.6)")
