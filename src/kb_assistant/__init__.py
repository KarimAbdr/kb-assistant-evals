"""kb_assistant: enterprise knowledge assistant (RAG) + evaluation harness.

Package map (data flows top to bottom):
    ingest      -> load + clean Markdown pages of the GitLab Handbook
    chunking    -> split pages into chunks with stable ids and heading paths
    retrieval   -> BM25 (default), optional vector and hybrid retrievers
    generation  -> LLMProvider abstraction, fake provider, prompt, RAG pipeline
    eval        -> golden set, retrieval metrics, RAG triad, runner, CI gate
    judge       -> LLM-as-judge, rubric, agreement with humans, bias tests
    agent       -> tool-using agent, trajectory logging, trajectory metrics
    labeling    -> CLI for human labels used to validate the judge
"""

__version__ = "0.1.0"
