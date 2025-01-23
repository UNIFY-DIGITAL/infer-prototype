.. _kotaemon_llms_rerankings_cohere:

Cohere Reranking Module
=======================

This module implements the `CohereReranking` class, which uses the Cohere API to reorder documents based on their relevance to a query.

Class Overview
--------------

`CohereReranking`
~~~~~~~~~~~~~~~~~
.. autoclass:: CohereReranking
   :members:
   :undoc-members:
   :show-inheritance:

Details
-------

The `CohereReranking` class leverages Cohere's reranker model to reorder documents by assigning relevance scores.

**Attributes**:
- `model_name`: The ID of the Cohere reranker model to use. Default is `rerank-multilingual-v2.0`. Visit [Cohere Supported Models](https://docs.cohere.com/docs/rerank-2) for available models.
- `cohere_api_key`: The API key for accessing Cohere services. It is loaded from environment variables via `decouple.config`.

**Methods**:
- **`run(documents, query)`**:
  - **Description**: Uses the Cohere API to reorder documents based on relevance scores.
  - **Parameters**:
    - `documents`: A list of `Document` objects to rerank.
    - `query`: A string representing the user's query.
  - **Returns**: A list of `Document` objects reordered by relevance.
  - **Behavior**:
    - If no API key is provided, reranking is skipped, and the original list of documents is returned.
    - The relevance scores are stored in each document's metadata under the key `reranking_score`.

**Usage Workflow**:
1. Provide the required `cohere_api_key` and `model_name` when initializing the class.
2. Call the `run` method with a list of documents and a query to rerank the documents.

**Error Handling**:
- Raises `ImportError` if the `cohere` library is not installed.
- Logs a warning if the API key is missing or invalid.

**Example**:
```python
from kotaemon.rerankings.cohere import CohereReranking
from kotaemon.base import Document

reranker = CohereReranking(cohere_api_key="your_api_key")
documents = [Document(content="First document"), Document(content="Second document")]
query = "Relevant query text"

ranked_documents = reranker.run(documents, query)
for doc in ranked_documents:
    print(doc.content, doc.metadata["reranking_score"])
