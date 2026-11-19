import pytest

pytestmark = pytest.mark.skip(reason="TODO(step-4.4)")


def test_loop_detected() -> None:
    from kb_assistant.agent.trajectory import has_loop

    steps = [{"type": "tool", "tool_name": "search_kb", "tool_args": {"query": "pto"}}] * 2
    assert has_loop(steps)
