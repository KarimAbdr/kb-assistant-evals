"""Heading-aware Markdown splitter.

Base design: LocalSmartRAG core/smart_splitter.py (MIT):
  1. split by Markdown headings (#, ##, ###) so each chunk is semantically whole;
  2. keep ``` code fences atomic (never cut in the middle);
  3. inside a section, cut on paragraph boundaries, then sentence ends;
  4. fall back to fixed-size character split with overlap for very long paragraphs.
Our additions: heading_path prefix and char offsets (start/end) for evidence mapping.
"""

from __future__ import annotations

from dataclasses import dataclass

from kb_assistant.types import Chunk, Page


@dataclass(frozen=True)
class ChunkingConfig:
    """Mirror of configs/chunking.yaml."""

    strategy: str = "markdown_headings"
    chunk_size: int = 800
    chunk_overlap: int = 150
    max_heading_level: int = 3
    keep_heading_path: bool = True
    protect_code_blocks: bool = True


def split_by_headings(text: str, max_level: int) -> list[tuple[str, int, int]]:
    """Return (heading_path, start, end) sections. Preamble before first heading = its own section. TODO(step-0.5)"""
    raise NotImplementedError("TODO(step-0.5)")


def split_section(text: str, cfg: ChunkingConfig) -> list[tuple[int, int]]:
    """Split one section into (start, end) spans <= chunk_size, honouring paragraph/sentence
    boundaries, atomic code fences and overlap. TODO(step-0.5)"""
    raise NotImplementedError("TODO(step-0.5)")


def chunk_page(page: Page, cfg: ChunkingConfig) -> list[Chunk]:
    """Page -> chunks with chunk_id f"{doc_id}#{i}" and heading_path prefix. TODO(step-0.5)"""
    raise NotImplementedError("TODO(step-0.5)")


def chunk_corpus(pages: list[Page], cfg: ChunkingConfig) -> list[Chunk]:
    """Chunk all pages; log count and size distribution (min/median/max chars). TODO(step-0.5)"""
    raise NotImplementedError("TODO(step-0.5)")
