import pytest

pytestmark = pytest.mark.skip(reason="TODO(step-2.4)")


def test_kappa_perfect_and_chance() -> None:
    from kb_assistant.judge.agreement import cohens_kappa

    assert cohens_kappa([0, 1, 2, 1], [0, 1, 2, 1]) == pytest.approx(1.0)


def test_always_pass_judge_has_high_accuracy_but_zero_kappa() -> None:
    from kb_assistant.judge.agreement import accuracy, cohens_kappa

    human = [2, 2, 2, 2, 0]
    judge = [2, 2, 2, 2, 2]
    assert accuracy(human, judge) == 0.8
    assert cohens_kappa(human, judge) == pytest.approx(0.0)
