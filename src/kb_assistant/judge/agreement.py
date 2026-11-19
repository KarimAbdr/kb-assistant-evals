"""Judge vs human agreement (stage 02).

Accuracy alone is misleading when labels are imbalanced (if 80% of answers are "pass",
a judge that always says "pass" gets 0.8). Cohen's kappa corrects for chance agreement:
    kappa = (p_o - p_e) / (1 - p_e)
"""

from __future__ import annotations


def accuracy(human: list[int], judge: list[int]) -> float:
    """Share of exact matches. TODO(step-2.4)"""
    raise NotImplementedError("TODO(step-2.4)")


def cohens_kappa(human: list[int], judge: list[int], weights: str | None = None) -> float:
    """Unweighted (or "linear"/"quadratic" for the ordinal 0/1/2 scale). Implement by hand,
    then cross-check with sklearn.metrics.cohen_kappa_score in a test. TODO(step-2.4)"""
    raise NotImplementedError("TODO(step-2.4)")


def confusion_matrix(human: list[int], judge: list[int], labels: list[int]) -> list[list[int]]:
    """Rows = human, columns = judge. Shows WHERE the judge disagrees (too lenient vs too strict). TODO(step-2.4)"""
    raise NotImplementedError("TODO(step-2.4)")
