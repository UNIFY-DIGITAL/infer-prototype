.. _kotaemon_llms_rerankings_tei_fast_rerank:

TEI Fast Reranking Module
=========================

This module implements the `TeiFastReranking` class, which uses the Hugging Face Text Embeddings Inference (TEI) API to rerank documents based on their relevance to a query.

Class Overview
--------------

`TeiFastReranking`
~~~~~~~~~~~~~~~~~~
.. autoclass:: TeiFastReranking
   :members:
   :undoc-members:
   :show-inheritance:

Details
-------

The `TeiFastReranking` class interacts with a deployed TEI service to rerank documents by assigning relevance scores based on the query.

**Attributes**:
- `endpoint_url`:
  - **Type**: `str`
  - **Required**: Yes
  - **Description**: The base URL of the TEI reranking service API.
- `model_name`:
  - **Type**: `Optional[str]`
  - **Description**: The ID of the model to use. Refer to the [Supported Models](https://github.com/huggingface/text-embeddings-inference#supported-models).
- `is_truncated`:
  - **Type**: `Optional[bool]`
  - **Default**: `True`
  - **Description**: Specifies whether to truncate the input texts.
- `max_tokens`:
  - **Type**: `Optional[int]`
  - **Default**: `512`
  - **Description**: Limits the number of tokens processed by the reranker model.

**Methods**:
- **`client(query, texts)`**:
  - Sends a request to the TEI reranking service to calculate relevance scores for a batch of texts.
  - **Parameters**:
    - `query`: The query string.
    - `texts`: A list of text documents.
  - **Returns**: The API response as a JSON object.
- **`run(documents, query)`**:
  - Reranks a list of `Document` objects based on their relevance scores from the TEI service.
  - **Parameters**:
    - `documents`: A list of `Document` objects to rerank.
    - `query`: A string representing the user's query.
  - **Returns**: A sorted list of `Document` objects, ordered by relevance scores.

**Usage Workflow**:
1. Provide the `endpoint_url` and optionally `model_name`, `is_truncated`, and `max_tokens` when initializing the class.
2. Call the `run` method with a list of documents and a query to rerank the documents.
3. Relevance scores are stored in each document's metadata under the key `reranking_score`.

**Behavior**:
- Documents are processed in batches to optimize API calls.
- If `is_truncated` is `True`, input texts are truncated to `max_tokens`.

**Error Handling**:
- Logs a warning and skips reranking if the `endpoint_url` is not provided.

**Example**:
```python
from kotaemon.rerankings.tei_fast_rerank import TeiFastReranking
from kotaemon.base import Document

reranker = TeiFastReranking(endpoint_url="https://api.example.com/tei")
documents = [Document(content="First document"), Document(content="Second document")]
query = "Relevant query text"

ranked_documents = reranker.run(documents, query)
for doc in ranked_documents:
    print(doc.content, doc.metadata["reranking_score"])
