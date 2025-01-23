.. _kotaemon_storages_vectorstores_lancedb:

LanceDB Vector Store
====================

This module implements the `LanceDBVectorStore` class, a wrapper around the `LlamaIndex` LanceDB vector store with additional functionalities.

Class Overview
--------------

`LanceDBVectorStore`
~~~~~~~~~~~~~~~~~~~~
.. autoclass:: LanceDBVectorStore
   :members:
   :undoc-members:
   :show-inheritance:

Details
-------

The `LanceDBVectorStore` class extends the `LlamaIndexVectorStore` to provide a vector store implementation using LanceDB. It includes custom enhancements and monkey patches to handle specific use cases.

**Initialization**:
- Connects to a LanceDB database at the specified path.
- Retrieves or creates a table within the database.

**Attributes**:
- `path`: Path to the LanceDB database. Default is `"./lancedb"`.
- `collection_name`: Name of the LanceDB table. Default is `"default"`.
- `_client`: LanceDB client instance.
- `_kwargs`: Additional parameters passed during initialization.

**Methods**:
- **`add(embeddings, metadatas=None, ids=None)`**:
  - Inherited from `LlamaIndexVectorStore`. Adds vector embeddings to the LanceDB vector store.
- **`delete(ids, **kwargs)`**:
  - Deletes vector embeddings by their IDs.
  - **Parameters**:
    - `ids`: List of IDs to delete.
    - `kwargs`: Additional parameters for LanceDB-specific operations.
- **`drop()`**:
  - Deletes the entire LanceDB collection (table).
- **`count()`**:
  - Not implemented.
- **`__persist_flow__()`**:
  - Serializes the vector store configuration for persistence.

**Custom Enhancements**:
- **`custom_to_lance_filter`**:
  - A custom filter function to handle metadata filtering with enhanced support for list values.
- Monkey patches:
  - Skips table existence checks for faster initialization.
  - Customizes metadata filtering in `LILanceDBVectorStore`.

**Usage Workflow**:
1. Initialize the `LanceDBVectorStore` with the database path and collection name.
2. Add vector embeddings using `add`.
3. Query embeddings using `query` (inherited from `LlamaIndexVectorStore`).
4. Manage collections using `delete` or `drop`.

**Example**:
```python
from kotaemon.storages.vectorstores.lancedb import LanceDBVectorStore

# Initialize the LanceDB vector store
vector_store = LanceDBVectorStore(path="lancedb", collection_name="my_vectors")

# Add embeddings
embeddings = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]]
vector_store.add(embeddings=embeddings)

# Query embeddings
query_embedding = [0.1, 0.2, 0.3]
top_k_results = vector_store.query(embedding=query_embedding, top_k=2)

# Delete a vector by ID
vector_store.delete(ids=["vector_id_1"])

# Drop the collection
vector_store.drop()
