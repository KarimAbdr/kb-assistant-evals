"""RAG triad: context relevance, groundedness, answer relevance (judge-based).

    question --(context relevance)--> retrieved context
    context  --(groundedness)-------> answer      (is every claim supported?)
    question --(answer relevance)---> answer      (does it address the question?)

Scores come from a Judge (judge/judge.py); today a fixture-backed fake.
"""

from __future__ import annotations

from dataclasses import dataclass

from kb_assistant.judge.judge import Judge
from kb_assistant.types import RagAnswer


@dataclass(frozen=True)
class TriadScore:
    context_relevance: float
    groundedness: float
    answer_relevance: float
    rationale: dict[str, str]


def score_triad(answer: RagAnswer, judge: Judge) -> TriadScore:
    """Ask the judge three separate questions (one criterion per call reduces halo effect). TODO(step-1.5)"""
    raise NotImplementedError("TODO(step-1.5)")
