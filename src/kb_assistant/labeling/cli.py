"""Minimal terminal labelling tool: `kb label`.

Shows question, reference, context, answer and the rubric; asks for a 0/1/2 score + optional
note; appends to evals/labels/human_labels.jsonl. Resumable: skips already-labelled ids.
Judge scores are NOT shown during labelling (avoids anchoring the human).
"""

from __future__ import annotations

from pathlib import Path


def load_queue(answers_path: Path, labels_path: Path) -> list[dict]:
    """Items to label = answers minus already labelled (item_id, criterion). TODO(step-2.2)"""
    raise NotImplementedError("TODO(step-2.2)")


def label_one(item: dict, criterion: str) -> dict:
    """Render the item, read input via input(), validate it, return a label record
    {item_id, criterion, score, note, rubric_version, labeled_at}. TODO(step-2.2)"""
    raise NotImplementedError("TODO(step-2.2)")


def main(answers_path: Path, labels_path: Path, criterion: str = "correctness") -> None:
    """Loop until queue empty or user types q; append each label immediately (crash-safe). TODO(step-2.2)"""
    raise NotImplementedError("TODO(step-2.2)")
