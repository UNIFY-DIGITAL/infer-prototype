.. _kotaemon_storages_vectorstores_base:

Base Vector Store Module
========================

This module defines the `BaseVectorStore` abstract base class and the `LlamaIndexVectorStore` mixin class for working with vector embeddings.

Class Overview
--------------

`BaseVectorStore`
~~~~~~~~~~~~~~~~~
.. autoclass:: BaseVectorStore
   :members:
   :undoc-members:
   :show-inheritance:

`LlamaIndexVectorStore`
~~~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: LlamaIndexVectorStore
   :members:
   :undoc-members:
   :show-inheritance:

Details
-------

### `BaseVectorStore`

The `BaseVectorStore` class provides an abstract interface for managing vector embeddings. It is designed to be subclassed to implement specific vector store functionality.

**Methods**:
- **`add(embeddings, metadatas=None, ids=None)`**:
  - Adds vector embeddings to the store.
  - **Parameters**:
    - `embeddings`: A list of vector embeddings or `DocumentWithEmbedding` objects.
    - `metadatas`: Optional metadata for the embeddings.
    - `ids`: Optional IDs for the embeddings.
  - **Returns**: A list of IDs of the embeddings.
- **`delete(ids, **kwargs)`**:
  - Deletes vector embeddings by their IDs.
- **`query(embedding, top_k=1, ids=None, **kwargs)`**:
  - Retrieves the top-k most similar embeddings.
  - **Parameters**:
    - `embedding`: The query embedding.
    - `top_k`: Number of top matches to return.
    - `ids`: Optional list of IDs to filter the query.
  - **Returns**: A tuple containing matched embeddings, similarity scores, and IDs.
- **`drop()`**:
  - Drops the vector store.

### `LlamaIndexVectorStore`

The `LlamaIndexVectorStore` class serves as a mixin for vector stores based on LlamaIndex. It provides methods to add, delete, and query vector embeddings, leveraging the LlamaIndex vector store functionalities.

**Methods**:
- Inherits and implements the `BaseVectorStore` methods.
- **`add(embeddings, metadatas=None, ids=None)`**:
  - Adds vector embeddings to the LlamaIndex vector store, associating metadata and IDs as necessary.
- **`delete(ids, **kwargs)`**:
  - Deletes vector embeddings by their IDs from the LlamaIndex vector store.
- **`query(embedding, top_k=1, ids=None, **kwargs)`**:
  - Queries the LlamaIndex vector store for the top-k similar embeddings, supporting additional parameters for filtering and customization.

**Usage Workflow**:
1. Subclass the `BaseVectorStore` to implement a custom vector store.
2. Use `LlamaIndexVectorStore` for LlamaIndex-based implementations.

**Example**:
```python
class MyCustomVectorStore(BaseVectorStore):
    def __init__(self):
        # Initialize the vector store
        pass

    def add(self, embeddings, metadatas=None, ids=None):
        # Add vector embeddings
        pass

    def delete(self, ids, **kwargs):
        # Delete embeddings
        pass

    def query(self, embedding, top_k=1, ids=None, **kwargs):
        # Query the vector store
        pass

    def drop(self):
        # Drop the vector store
        pass
