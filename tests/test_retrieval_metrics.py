import pytest

pytestmark = pytest.mark.skip(reason="TODO(step-1.3)")


def test_recall_at_k() -> None:
    from kb_assistant.eval.retrieval_metrics import recall_at_k

    assert recall_at_k(["a", "b", "c"], {"a", "z"}, k=2) == 0.5


def test_reciprocal_rank() -> None:
    from kb_assistant.eval.retrieval_metrics import reciprocal_rank

    assert reciprocal_rank(["x", "a"], {"a"}) == 0.5
    assert reciprocal_rank(["x"], {"a"}) == 0.0


def test_hit_rate() -> None:
    from kb_assistant.eval.retrieval_metrics import hit_rate_at_k

    assert hit_rate_at_k(["x", "a"], {"a"}, k=1) == 0.0
