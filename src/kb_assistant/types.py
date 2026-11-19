"""Shared data contracts between modules.

These are plain data containers (boilerplate, not logic). Every module talks to its
neighbours only through these types, so a stage can be re-implemented without touching
others (see docs/architecture/standards.md, "Module boundaries").
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal


@dataclass(frozen=True)
class Page:
    """One handbook page after ingestion.

    doc_id:  stable id = path relative to content/handbook without extension,
             e.g. "people-policies/leave". Golden set labels refer to doc_id.
    url:     public handbook URL (used for citations and CC BY-SA attribution).
    title:   front-matter title.
    text:    cleaned Markdown body.
    section: top-level section ("people-policies", "total-rewards", ...), used by agent tool #2.
    """

    doc_id: str
    url: str
    title: str
    text: str
    section: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class Chunk:
    """A retrievable unit.

    chunk_id:     f"{doc_id}#{chunk_index}" (changes when chunking changes, which is why the
                  golden set labels documents + evidence spans, not chunk ids; see ADR-0004).
    heading_path: "Leave > Parental leave > Eligibility".
    start/end:    char offsets in Page.text, used to map evidence spans to chunks.
    """

    chunk_id: str
    doc_id: str
    text: str
    heading_path: str
    start: int
    end: int
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class RetrievedChunk:
    """A chunk with its retrieval score and rank (1-based)."""

    chunk: Chunk
    score: float
    rank: int
    retriever: Literal["bm25", "vector", "hybrid"] = "bm25"


@dataclass(frozen=True)
class Citation:
    """Mapping of an [n] marker in the answer to the chunk it cites."""

    marker: int
    chunk_id: str
    url: str


@dataclass(frozen=True)
class RagAnswer:
    """Output of the RAG pipeline for one question."""

    question: str
    answer: str
    contexts: list[RetrievedChunk]
    citations: list[Citation]
    refused: bool = False  # True when the system said "not found in the documentation"


@dataclass(frozen=True)
class GoldenItem:
    """One golden-set entry (schema documented in evals/README.md).

    relevant_doc_ids: documents that contain the answer.
    evidence:         verbatim quotes from those documents; a chunk is "relevant" iff it
                      contains (most of) an evidence quote. This keeps labels valid when
                      chunking changes.
    answerable:       False for questions the corpus cannot answer (tests refusal).
    """

    id: str
    question: str
    reference_answer: str
    relevant_doc_ids: list[str]
    evidence: list[str]
    answerable: bool = True
    tags: list[str] = field(default_factory=list)
