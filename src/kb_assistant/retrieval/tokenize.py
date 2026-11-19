"""Tokenisation for BM25.

LocalSmartRAG uses jieba (Chinese). For an English corpus we need: lowercase, split on
non-alphanumerics, drop English stopwords, optional stemming. The SAME function must be
applied to documents and queries, otherwise BM25 silently degrades.
"""

from __future__ import annotations

ENGLISH_STOPWORDS: frozenset[str] = frozenset(
    ["a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "has", "have", "how", "i", "in", "is", "it", "of", "on", "or", "that", "the", "to", "was", "what", "when", "where", "which", "who", "why", "will", "with"]
)


def tokenize(text: str, lowercase: bool = True, remove_stopwords: bool = True,
             stemming: bool = False) -> list[str]:
    """Text -> list of tokens. TODO(step-0.6)"""
    raise NotImplementedError("TODO(step-0.6)")
