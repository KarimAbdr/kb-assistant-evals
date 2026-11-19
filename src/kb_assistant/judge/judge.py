"""Judge interface + implementations.

The judge is just another LLMProvider client with a structured output contract
(JSON: {"score": int, "rationale": str}). FakeJudge reads pre-recorded verdicts.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class Verdict:
    score: int
    rationale: str
    raw: str  # raw judge output, kept for debugging parse failures


class Judge(Protocol):
    def grade(self, criterion: str, question: str, answer: str, context: str = "",
              reference: str = "") -> Verdict: ...

    def compare(self, question: str, answer_a: str, answer_b: str) -> str:
        """Pairwise preference: returns "A", "B" or "tie" (used by bias tests)."""
        ...


class FakeJudge:
    """Fixture-backed judge (evals/fixtures/fake_judgements.jsonl), keyed by (item_id, criterion)."""

    def __init__(self, verdicts_path: str) -> None:
        self.verdicts_path = verdicts_path

    def grade(self, criterion: str, question: str, answer: str, context: str = "",
              reference: str = "") -> Verdict:
        """TODO(step-1.5)"""
        raise NotImplementedError("TODO(step-1.5)")

    def compare(self, question: str, answer_a: str, answer_b: str) -> str:
        """TODO(step-2.5)"""
        raise NotImplementedError("TODO(step-2.5)")


class LLMJudge:
    """Real judge over any LLMProvider (later). Prompt = rubric + inputs + strict JSON format."""

    def __init__(self, provider: object, rubric_version: str = "v1") -> None:
        self.provider, self.rubric_version = provider, rubric_version

    def grade(self, criterion: str, question: str, answer: str, context: str = "",
              reference: str = "") -> Verdict:
        """TODO(step-beyond): render prompt, call provider, parse JSON, retry once on parse error."""
        raise NotImplementedError("TODO(step-beyond)")

    def compare(self, question: str, answer_a: str, answer_b: str) -> str:
        """TODO(step-beyond)"""
        raise NotImplementedError("TODO(step-beyond)")
