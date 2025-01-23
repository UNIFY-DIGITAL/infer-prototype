.. _kotaemon_storages_vectorstores_qdrant:

Qdrant Vector Store
===================

This module implements the `QdrantVectorStore` class, which provides an interface for working with the Qdrant vector database using LlamaIndex.

Class Overview
--------------

`QdrantVectorStore`
~~~~~~~~~~~~~~~~~~~
.. autoclass:: QdrantVectorStore
   :members:
   :undoc-members:
   :show-inheritance:

Details
-------

The `QdrantVectorStore` class integrates with Qdrant, a scalable and fast vector database, to store and query vector embeddings. It extends the `LlamaIndexVectorStore` with additional features for managing collections and deleting embeddings.

**Initialization**:
- Connects to a Qdrant instance using a collection name, URL, and optional API key.

**Attributes**:
- `collection_name`: The name of the Qdrant collection.
- `url`: Optional URL of the Qdrant server.
- `api_key`: Optional API key for authentication.
- `_client`: Qdrant client instance.
- `_kwargs`: Additional parameters passed during initialization.

**Methods**:
- **`add(embeddings, metadatas=None, ids=None)`**:
  - Inherited from `LlamaIndexVectorStore`. Adds vector embeddings to the Qdrant vector store.
- **`delete(ids, **kwargs)`**:
  - Deletes vector embeddings by their IDs using the Qdrant API.
  - **Parameters**:
    - `ids`: List of IDs to delete.
    - `kwargs`: Additional parameters for Qdrant-specific operations.
- **`drop()`**:
  - Deletes the entire Qdrant collection.
- **`count()`**:
  - Returns the total number of embeddings in the collection.
- **`__persist_flow__()`**:
  - Serializes the vector store configuration for persistence.

**Usage Workflow**:
1. Initialize the `QdrantVectorStore` with the collection name and optional URL or API key.
2. Add vector embeddings using `add`.
3. Query embeddings using `query` (inherited from `LlamaIndexVectorStore`).
4. Manage collections using `delete` or `drop`.

**Example**:
```python
from kotaemon.storages.vectorstores.qdrant import QdrantVectorStore

# Initialize the Qdrant vector store
vector_store = QdrantVectorStore(
    collection_name="my_vectors", url="http://localhost:6333"
)

# Add embeddings
embeddings = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]]
vector_store.add(embeddings=embeddings)

# Query embeddings
query_embedding = [0.1, 0.2, 0.3]
top_k_results = vector_store.query(embedding=query_embedding, top_k=2)

# Count embeddings
print("Total embeddings:", vector_store.count())

# Delete embeddings
vector_store.delete(ids=["vector_id_1"])

# Drop the collection
vector_store.drop()
