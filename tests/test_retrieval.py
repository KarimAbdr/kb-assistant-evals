import pytest

pytestmark = pytest.mark.skip(reason="TODO(step-0.6)")


def test_bm25_finds_keyword(tiny_pages) -> None:
    from kb_assistant.chunking.splitter import ChunkingConfig, chunk_corpus
    from kb_assistant.retrieval.bm25 import BM25Retriever

    r = BM25Retriever()
    r.index(chunk_corpus(tiny_pages, ChunkingConfig()))
    top = r.retrieve("how many free sessions", k=1)
    assert top[0].chunk.doc_id == "total-rewards/demo-benefit"
    assert top[0].rank == 1


def test_tokenize_is_symmetric() -> None:
    from kb_assistant.retrieval.tokenize import tokenize

    assert tokenize("Parental Leave!") == tokenize("parental leave")
