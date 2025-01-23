LLM Trulens Scoring Module
==========================

The `llm_trulens` module provides functionality to rerank documents using Language Model (LLM) scoring, focusing on relevance scoring based on a user-defined system and user prompt.

Key Class
---------

**LLMTrulensScoring**

The `LLMTrulensScoring` class utilizes LLMs to score documents based on their relevance to a query. It extracts relevance scores between 0 and 10, normalizes them, and reranks documents accordingly.

Attributes
~~~~~~~~~~
- **llm**: Instance of the Language Model (LLM) used for scoring.
- **system_prompt_template**: Template defining the system behavior for scoring.
- **user_prompt_template**: Template defining how queries and contexts are passed to the LLM.
- **concurrent**: Boolean flag to enable parallel execution using threads.
- **normalize**: The value used to normalize relevance scores.
- **trim_func**: A function to trim context length to fit within the maximum allowed context size for the LLM.

Methods
~~~~~~~
- **run(documents: list[Document], query: str) -> list[Document]:**
  - Filters and reranks a list of documents based on their relevance to the query.

    **Parameters**:
      - `documents` (list[Document]): List of documents to rerank.
      - `query` (str): Query string used to evaluate document relevance.

    **Returns**:
      - `list[Document]`: List of reranked documents with updated metadata.

Implementation Details
~~~~~~~~~~~~~~~~~~~~~~
1. **Prompt Templates**:
   - Two prompt templates (`SYSTEM_PROMPT_TEMPLATE` and `USER_PROMPT_TEMPLATE`) define the scoring behavior.
   - Prompts are populated dynamically based on the query and document content.

2. **Concurrency**:
   - Supports parallel processing using `ThreadPoolExecutor`.
   - Each document's content is trimmed using the `trim_func` to fit within the LLM's maximum context length.

3. **Relevance Extraction**:
   - Extracts relevance scores from the LLM output using the `re_0_10_rating` function.
   - Scores are normalized (e.g., divided by 10) and stored in each document's metadata.

4. **Reranking**:
   - Documents are reranked based on their normalized relevance scores.
   - Handles metadata updates and logs reranking results.

5. **Validation**:
   - The `validate_rating` function ensures that relevance scores fall within the expected range (0-10).

Source Code
-----------

.. literalinclude:: ../rankings/llm_trulens.py
   :language: python
   :linenos:
