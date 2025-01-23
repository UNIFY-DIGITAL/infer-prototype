.. _kotaemon_storages_vectorstores_chroma:

Chroma Vector Store
===================

This module implements the `ChromaVectorStore` class, a wrapper around the `LlamaIndex` Chroma vector store with additional functionalities.

Class Overview
--------------

`ChromaVectorStore`
~~~~~~~~~~~~~~~~~~~
.. autoclass:: ChromaVectorStore
   :members:
   :undoc-members:
   :show-inheritance:

Details
-------

The `ChromaVectorStore` class allows for efficient storage, querying, and management of vector embeddings using Chroma. It extends the `LlamaIndexVectorStore` and provides additional methods for collection management.

**Initialization**:
- Connects to a persistent Chroma database at the specified path.
- Retrieves or creates a collection within the database.

**Attributes**:
- `path`: Path to the Chroma database. Default is `"./chroma"`.
- `collection_name`: Name of the Chroma collection. Default is `"default"`.
- `host`: Host for Chroma services. Default is `"localhost"`.
- `port`: Port for Chroma services. Default is `"8000"`.
- `ssl`: Boolean indicating whether SSL is used. Default is `False`.
- `headers`: Optional HTTP headers for requests.
- `collection_kwargs`: Optional additional arguments for collection creation.
- `stores_text`: Boolean indicating whether text data is stored. Default is `True`.
- `flat_metadata`: Boolean indicating whether metadata should be flattened. Default is `True`.

**Methods**:
- **`add(embeddings, metadatas=None, ids=None)`**:
  - Adds vector embeddings to the Chroma vector store.
  - Inherited from `LlamaIndexVectorStore`.
- **`delete(ids, **kwargs)`**:
  - Deletes vector embeddings by their IDs.
  - **Parameters**:
    - `ids`: List of IDs to delete.
    - `kwargs`: Additional parameters for Chroma-specific operations.
- **`drop()`**:
  - Deletes the entire Chroma collection.
- **`count()`**:
  - Returns the total number of vector embeddings in the collection.

**Usage Workflow**:
1. Initialize the `ChromaVectorStore` with the database path and collection name.
2. Add vector embeddings using `add`.
3. Query embeddings using `query` (inherited from `LlamaIndexVectorStore`).
4. Manage collections using `delete` or `drop`.

**Example**:
```python
from kotaemon.storages.vectorstores.chroma import ChromaVectorStore

# Initialize the Chroma vector store
vector_store = ChromaVectorStore(path="chroma_db", collection_name="my_vectors")

# Add embeddings
embeddings = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]]
vector_store.add(embeddings=embeddings)

# Query embeddings
query_embedding = [0.1, 0.2, 0.3]
top_k_results = vector_store.query(embedding=query_embedding, top_k=2)

# Count embeddings
print("Total embeddings:", vector_store.count())

# Drop the collection
vector_store.drop()
