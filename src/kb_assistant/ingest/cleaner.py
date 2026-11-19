"""Text cleaning for handbook Markdown.

Base design: LocalSmartRAG core/text_cleaner.py (MIT), adapted to Hugo Markdown.
Why: Hugo shortcodes ({{< ... >}}), HTML comments and link reference noise pollute BM25
term statistics and waste the LLM context window.
"""

from __future__ import annotations


def strip_hugo_shortcodes(text: str) -> str:
    """Remove {{< shortcode >}} / {{% shortcode %}} markup, keep inner text where meaningful. TODO(step-0.4)"""
    raise NotImplementedError("TODO(step-0.4)")


def normalize_whitespace(text: str) -> str:
    """Collapse 3+ newlines to 2, strip trailing spaces; never touch content inside ``` fences. TODO(step-0.4)"""
    raise NotImplementedError("TODO(step-0.4)")


def clean_markdown(text: str) -> str:
    """Full cleaning pipeline applied to every page body. TODO(step-0.4)"""
    raise NotImplementedError("TODO(step-0.4)")
