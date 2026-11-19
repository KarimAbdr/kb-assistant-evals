"""Judge bias probes (stage 02).

Position bias:  compare(q, A, B) vs compare(q, B, A). A consistent judge flips its answer.
                Metric: consistency rate = share of pairs with a consistent preference.
                Mitigation: evaluate both orders, count only consistent verdicts (else "tie").
Verbosity bias: compare a short correct answer with a padded version (same facts + filler).
                Metric: share of pairs where the longer one wins. Ideal = ties.
                Mitigation: rubric says "length is not a quality", length-normalised prompts,
                or score correctness against the reference instead of pairwise.
"""

from __future__ import annotations

from dataclasses import dataclass

from kb_assistant.judge.judge import Judge


@dataclass(frozen=True)
class BiasReport:
    n_pairs: int
    rate: float          # consistency rate (position) or long-wins rate (verbosity)
    examples: list[dict]  # a few raw cases for the report


def position_bias(judge: Judge, pairs: list[tuple[str, str, str]]) -> BiasReport:
    """pairs = (question, answer_a, answer_b). TODO(step-2.5)"""
    raise NotImplementedError("TODO(step-2.5)")


def make_verbose(answer: str) -> str:
    """Deterministically pad an answer with content-free filler (no new facts). TODO(step-2.6)"""
    raise NotImplementedError("TODO(step-2.6)")


def verbosity_bias(judge: Judge, items: list[tuple[str, str]]) -> BiasReport:
    """items = (question, short_correct_answer); compares it with make_verbose(answer) in both orders. TODO(step-2.6)"""
    raise NotImplementedError("TODO(step-2.6)")
