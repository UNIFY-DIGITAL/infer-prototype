LLM Reranking Module
=====================

The `llm` module defines an LLM-based reranking mechanism that filters documents based on their relevance to a query. This module is essential for prioritizing relevant documents in downstream tasks.

Key Class
---------

**LLMReranking**

The `LLMReranking` class utilizes a Language Model (LLM) to determine the relevance of documents to a query using a specified prompt template.

Attributes
~~~~~~~~~~
- **llm**: Instance of `BaseLLM` used to execute the reranking process.
- **prompt_template**: A `PromptTemplate` used to dynamically generate prompts for the LLM.
- **top_k**: Number of top relevant documents to retain if filtering results in an empty list.
- **concurrent**: Boolean flag to enable parallel processing of documents using threads.

Methods
~~~~~~~
- **run(documents: list[Document], query: str) -> list[Document]:**
  - Filters and reranks a list of documents based on their relevance to a query.

    **Parameters**:
      - `documents` (list[Document]): A list of documents to be reranked.
      - `query` (str): Query string used to assess document relevance.

    **Returns**:
      - `list[Document]`: List of reranked documents containing only those relevant to the query.

Implementation Details
~~~~~~~~~~~~~~~~~~~~~~
1. **Prompt Template**:
   - The `RERANK_PROMPT_TEMPLATE` is used to query the LLM. It evaluates the relevance of a context (document) to the query.
   - Example:
     ```plaintext
     Given the following question and context,
     return YES if the context is relevant to the question and NO if it isn't.

     > Question: {question}
     > Context:
     >>>
     {context}
     >>>
     > Relevant (YES / NO):
     ```

2. **Concurrency**:
   - The `concurrent` attribute determines whether documents are processed in parallel using `ThreadPoolExecutor`.
   - Each document is scored independently, improving efficiency when processing large document sets.

3. **Relevance Scoring**:
   - The `BooleanOutputParser` is used to parse LLM responses (e.g., "YES" or "NO") to determine document relevance.
   - Documents marked as "YES" are retained; others are discarded.

4. **Fallback for Empty Results**:
   - If no documents are deemed relevant, the top `k` documents (as defined by `top_k`) are returned to ensure non-empty output.

Source Code
-----------

.. literalinclude:: ../rankings/llm.py
   :language: python
   :linenos:
