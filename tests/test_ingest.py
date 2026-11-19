import pytest

pytestmark = pytest.mark.skip(reason="TODO(step-0.4)")


def test_doc_id_from_index_md() -> None:
    from pathlib import Path

    from kb_assistant.ingest.loader import path_to_doc_id

    root = Path("data/raw/handbook/content/handbook")
    assert path_to_doc_id(root / "people-policies/leave-of-absence/_index.md", root) == "people-policies/leave-of-absence"


def test_hugo_shortcodes_removed() -> None:
    from kb_assistant.ingest.cleaner import clean_markdown

    assert "{{%" not in clean_markdown('{{% panel header="x" %}}Secure{{% /panel %}}')
