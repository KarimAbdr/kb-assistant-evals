import pytest

pytestmark = pytest.mark.skip(reason="TODO(step-0.5)")


def test_code_block_is_never_split(tiny_pages) -> None:
    from kb_assistant.chunking.splitter import ChunkingConfig, chunk_page

    chunks = chunk_page(tiny_pages[0], ChunkingConfig(chunk_size=20, chunk_overlap=5))
    assert any("```\ncode block\n```" in c.text for c in chunks)


def test_chunk_ids_are_deterministic(tiny_pages) -> None:
    from kb_assistant.chunking.splitter import ChunkingConfig, chunk_corpus

    cfg = ChunkingConfig()
    assert [c.chunk_id for c in chunk_corpus(tiny_pages, cfg)] == [c.chunk_id for c in chunk_corpus(tiny_pages, cfg)]


def test_heading_path_present(tiny_pages) -> None:
    from kb_assistant.chunking.splitter import ChunkingConfig, chunk_page

    assert any("Leave > Parental leave" in c.heading_path for c in chunk_page(tiny_pages[0], ChunkingConfig()))
