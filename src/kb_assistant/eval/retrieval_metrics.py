"""Retrieval metrics over ranked chunk ids.

All functions are pure (no I/O) so they are trivially unit-testable with hand-made
examples. Unanswerable golden items are excluded from retrieval metrics.
"""

from __future__ import annotations


def recall_at_k(retrieved: list[str], relevant: set[str], k: int) -> float:
    """|relevant ∩ top-k| / |relevant|. Empty relevant set -> raise ValueError. TODO(step-1.3)"""
    raise NotImplementedError("TODO(step-1.3)")


def hit_rate_at_k(retrieved: list[str], relevant: set[str], k: int) -> float:
    """1.0 if any relevant id in top-k else 0.0 (averaged over queries = hit rate). TODO(step-1.3)"""
    raise NotImplementedError("TODO(step-1.3)")


def reciprocal_rank(retrieved: list[str], relevant: set[str]) -> float:
    """1 / rank of the first relevant id (1-based), 0.0 if none. Mean over queries = MRR. TODO(step-1.3)"""
    raise NotImplementedError("TODO(step-1.3)")


def aggregate(per_query: list[dict[str, float]]) -> dict[str, float]:
    """Mean of each metric across queries. TODO(step-1.3)"""
    raise NotImplementedError("TODO(step-1.3)")
