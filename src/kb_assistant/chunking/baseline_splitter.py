"""Naive baseline: LangChain RecursiveCharacterTextSplitter (strategy: recursive_chars).

Why keep it: it is the "before" in the stage 01 before/after experiment, and the
"breaking change" used in the stage 03 CI-gate demo.
"""

from __future__ import annotations

from kb_assistant.chunking.splitter import ChunkingConfig
from kb_assistant.types import Chunk, Page


def chunk_page_recursive(page: Page, cfg: ChunkingConfig) -> list[Chunk]:
    """Wrap langchain_text_splitters.RecursiveCharacterTextSplitter(add_start_index=True). TODO(step-1.6)"""
    raise NotImplementedError("TODO(step-1.6)")
