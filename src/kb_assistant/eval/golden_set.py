"""Golden set I/O and validation (schema: evals/README.md)."""

from __future__ import annotations

from pathlib import Path

from kb_assistant.types import Chunk, GoldenItem


def load_golden_set(path: Path) -> list[GoldenItem]:
    """Read JSONL -> GoldenItem list; fail loudly on duplicate ids or missing fields. TODO(step-1.1)"""
    raise NotImplementedError("TODO(step-1.1)")


def validate_against_corpus(items: list[GoldenItem], doc_ids: set[str],
                            page_texts: dict[str, str]) -> list[str]:
    """Return human-readable problems: unknown doc_id, evidence quote not found in its page.
    Run after every corpus refresh (RAID D-01). TODO(step-1.1)"""
    raise NotImplementedError("TODO(step-1.1)")


def relevant_chunk_ids(item: GoldenItem, chunks: list[Chunk], min_overlap: float = 0.8) -> set[str]:
    """Chunks of relevant docs that contain >= min_overlap of an evidence quote (by char span).
    This derives chunk-level labels from chunking-invariant evidence (ADR-0004). TODO(step-1.1)"""
    raise NotImplementedError("TODO(step-1.1)")
