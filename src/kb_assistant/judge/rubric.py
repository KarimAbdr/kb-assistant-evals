"""Frozen grading rubric (version it: changing the rubric invalidates old human labels)."""

from __future__ import annotations

RUBRIC_VERSION = "v1"

# 0/1/2 scale per criterion. Wording is final once human labelling starts (step 2.1).
RUBRIC: dict[str, dict[int, str]] = {
    "correctness": {
        2: "Answer matches the reference answer on all key facts.",
        1: "Partially correct: some key facts missing or imprecise, nothing contradictory.",
        0: "Wrong, contradicts the reference, or refuses an answerable question.",
    },
    "groundedness": {
        2: "Every claim is supported by the cited context.",
        1: "Mostly supported; minor unsupported detail.",
        0: "Contains claims not supported by the context (hallucination).",
    },
}


def render_rubric(criterion: str) -> str:
    """Rubric text inserted into the judge prompt and shown in the labelling CLI. TODO(step-2.1)"""
    raise NotImplementedError("TODO(step-2.1)")
