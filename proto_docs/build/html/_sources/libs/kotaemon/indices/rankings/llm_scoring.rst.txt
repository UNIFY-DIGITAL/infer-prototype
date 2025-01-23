LLM Scoring Module
==================

The `llm_scoring` module provides functionality to rerank documents using Language Model (LLM) scoring. It leverages prompt-based querying to determine the relevance of documents to a given query.

Key Class
---------

**LLMScoring**

The `LLMScoring` class filters and reranks documents by scoring their relevance to a query. It utilizes an LLM to generate scores and optionally filters documents based on those scores.

Attributes
~~~~~~~~~~
- **llm**: The LLM model used for scoring documents.
- **prompt_template**: Template for generating prompts to query the LLM.
- **concurrent**: Boolean flag to enable concurrent LLM queries using threads.

Methods
~~~~~~~
- **run(documents: list[Document], query: str) -> list[Document]:**
  - Filters and reranks a list of documents based on their relevance to the query.

    **Parameters**:
      - `documents` (list[Document]): A list of documents to be reranked.
      - `query` (str): The query string used to evaluate the relevance of the documents.

    **Returns**:
      - A list of documents, filtered and reranked by relevance scores.

Implementation Details
~~~~~~~~~~~~~~~~~~~~~~
1. **Prompt Generation**:
   - For each document, a query prompt is generated using the `prompt_template`.

2. **Scoring**:
   - LLM scores the documents, producing relevance scores.
   - Scores are calculated using log probabilities (`logprobs`) of the LLM output.

3. **Filtering**:
   - A `BooleanOutputParser` determines if the document is relevant.
   - If the document passes the threshold, it is added to the results.

4. **Concurrency**:
   - If `concurrent=True`, scoring is performed in parallel using a `ThreadPoolExecutor`.

5. **Default Fallback**:
   - If no documents are deemed relevant, the top `k` documents are returned as a fallback.

Source Code
-----------

.. literalinclude:: ../rankings/llm_scoring.py
   :language: python
   :linenos:
