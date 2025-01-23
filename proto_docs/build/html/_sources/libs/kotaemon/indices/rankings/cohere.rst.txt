Cohere Module
=============

The `cohere` module provides a reranking implementation using Cohere's reranking API.

Key Class
---------

**CohereReranking**

The `CohereReranking` class utilizes Cohere's `rerank-multilingual-v2.0` model to rerank documents based on their relevance to a given query.

Attributes
~~~~~~~~~~
- **model_name**: Name of the Cohere reranking model (default: `rerank-multilingual-v2.0`).
- **cohere_api_key**: API key for authenticating with Cohere's API.
- **use_key_from_ktem**: Boolean flag to use the Cohere API key from the `ktem` embeddings manager.

Methods
~~~~~~~
- **run(documents: list[Document], query: str) -> list[Document]:**
  - Reranks the input list of documents based on their relevance to the query using the Cohere API.

Dependencies
~~~~~~~~~~~~
- The `cohere` Python library is required. Install it using:

    ```bash
    pip install cohere
    ```



Source Code
-----------

.. literalinclude:: ../rankings/cohere.py
 :language: python
 :linenos: