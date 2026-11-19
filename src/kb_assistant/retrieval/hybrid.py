"""Hybrid retriever: BM25 + vector, fused by RRF (default) or min-max weighted sum.

Base design: LocalSmartRAG core/retriever_hybrid.py (MIT). Key point taken from it:
raw BM25 scores and cosine similarities live on different scales, so weighted fusion
needs per-query min-max normalisation; RRF avoids that by using ranks only.
"""

from __future__ import annotations

from kb_assistant.retrieval.base import Retriever
from kb_assistant.types import Chunk, RetrievedChunk


def rrf_fuse(rankings: list[list[RetrievedChunk]], k: int = 60) -> list[tuple[str, float]]:
    """Reciprocal Rank Fusion: score(d) = sum_i 1 / (k + rank_i(d)). Returns (chunk_id, score) desc. TODO(step-1.6)"""
    raise NotImplementedError("TODO(step-1.6)")


def weighted_fuse(sparse: list[RetrievedChunk], dense: list[RetrievedChunk],
                  alpha: float) -> list[tuple[str, float]]:
    """alpha * minmax(dense) + (1 - alpha) * minmax(sparse); missing score = 0. TODO(step-1.6)"""
    raise NotImplementedError("TODO(step-1.6)")


class HybridRetriever:
    """Combines two retrievers; candidate_k from each, top_k after fusion."""

    def __init__(self, sparse: Retriever, dense: Retriever, fusion: str = "rrf",
                 alpha: float = 0.6, rrf_k: int = 60, candidate_k: int = 20) -> None:
        self.sparse, self.dense = sparse, dense
        self.fusion, self.alpha, self.rrf_k, self.candidate_k = fusion, alpha, rrf_k, candidate_k

    def index(self, chunks: list[Chunk]) -> None:
        """Index both retrievers. TODO(step-1.6)"""
        raise NotImplementedError("TODO(step-1.6)")

    def retrieve(self, query: str, k: int) -> list[RetrievedChunk]:
        """Retrieve candidates from both, fuse, return top-k with retriever="hybrid". TODO(step-1.6)"""
        raise NotImplementedError("TODO(step-1.6)")
