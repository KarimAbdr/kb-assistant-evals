import pytest

pytestmark = pytest.mark.skip(reason="TODO(step-0.7)")


def test_fake_provider_is_deterministic() -> None:
    from kb_assistant.generation.provider import FakeProvider

    p = FakeProvider(responses=["a"])
    assert p.generate("x") == p.generate("y") == "a"


def test_out_of_range_citation_is_dropped() -> None:
    from kb_assistant.generation.prompt import parse_citations

    assert parse_citations("claim [7]", chunks=[]) == []
