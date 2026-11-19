import pytest

pytestmark = pytest.mark.skip(reason="TODO(step-3.1)")


def test_gate_fails_below_threshold() -> None:
    from kb_assistant.eval.gate import check

    r = check({"recall_at_k": 0.5}, {"recall_at_k": 0.8}, {"recall_at_k": 0.7}, {"recall_at_k": 0.02})
    assert not r.passed and r.failures


def test_gate_fails_on_regression_even_above_threshold() -> None:
    from kb_assistant.eval.gate import check

    r = check({"recall_at_k": 0.75}, {"recall_at_k": 0.85}, {"recall_at_k": 0.7}, {"recall_at_k": 0.02})
    assert not r.passed
