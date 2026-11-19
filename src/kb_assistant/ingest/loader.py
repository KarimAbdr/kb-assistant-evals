"""Load handbook Markdown files into Page objects.

Base design: LocalSmartRAG core/document_loader.py (MIT), reduced to Markdown only.
"""

from __future__ import annotations

from collections.abc import Iterator
from pathlib import Path

from kb_assistant.types import Page

HANDBOOK_URL = "https://handbook.gitlab.com/handbook/"


def iter_markdown_files(root: Path) -> Iterator[Path]:
    """Yield every .md file under data/raw/handbook/content/handbook in sorted order.

    Sorted order matters: deterministic ingestion => deterministic chunk ids => stable CI.
    TODO(step-0.4)
    """
    raise NotImplementedError("TODO(step-0.4)")


def path_to_doc_id(path: Path, root: Path) -> str:
    """content/handbook/people-policies/leave/_index.md -> "people-policies/leave". TODO(step-0.4)"""
    raise NotImplementedError("TODO(step-0.4)")


def doc_id_to_url(doc_id: str) -> str:
    """"people-policies/leave" -> https://handbook.gitlab.com/handbook/people-policies/leave/ . TODO(step-0.4)"""
    raise NotImplementedError("TODO(step-0.4)")


def load_page(path: Path, root: Path) -> Page:
    """Parse front matter (python-frontmatter), clean the body, build a Page. TODO(step-0.4)"""
    raise NotImplementedError("TODO(step-0.4)")


def load_corpus(root: Path) -> list[Page]:
    """Load all pages; skip empty pages and Hugo-only stubs (body shorter than ~200 chars).

    Output is also written to data/processed/pages.jsonl by `kb ingest`.
    TODO(step-0.4)
    """
    raise NotImplementedError("TODO(step-0.4)")
