.. _kotaemon_storages_vectorstores_simple_file:

Simple File Vector Store
========================

This module implements the `SimpleFileVectorStore` class, which provides a file-backed vector store using LlamaIndex.

Class Overview
--------------

`SimpleFileVectorStore`
~~~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: SimpleFileVectorStore
   :members:
   :undoc-members:
   :show-inheritance:

Details
-------

The `SimpleFileVectorStore` class extends the `LlamaIndexVectorStore` to provide a vector store backed by file storage. It offers similar functionality to an in-memory store but persists data to a file for long-term storage.

**Initialization**:
- Requires a file path and optional collection name.
- Automatically loads existing data from the file if available.

**Attributes**:
- `path`: The directory where vector store data is saved.
- `collection_name`: The name of the collection. Default is `"default"`.
- `_save_path`: The full file path for storing vector data.
- `_data`: In-memory representation of the vector data.
- `_fs`: Filesystem instance for saving and loading data.

**Methods**:
- **`add(embeddings, metadatas=None, ids=None)`**:
  - Adds vector embeddings to the store and persists the data to the file.
  - **Parameters**:
    - `embeddings`: List of vector embeddings or `DocumentWithEmbedding` objects.
    - `metadatas`: Optional metadata for the embeddings.
    - `ids`: Optional IDs for the embeddings.
  - **Returns**: A list of IDs of the embeddings.
- **`delete(ids, **kwargs)`**:
  - Deletes vector embeddings by their IDs and updates the file.
- **`drop()`**:
  - Clears all data and deletes the backing file.
- **`__persist_flow__()`**:
  - Serializes the vector store configuration for persistence.

**Usage Workflow**:
1. Initialize the `SimpleFileVectorStore` with a path and optional collection name.
2. Add vector embeddings using `add`.
3. Query embeddings using `query` (inherited from `LlamaIndexVectorStore`).
4. Manage collections using `delete` or `drop`.

**Example**:
```python
from kotaemon.storages.vectorstores.simple_file import SimpleFileVectorStore
from kotaemon.base import DocumentWithEmbedding

# Initialize the Simple File Vector Store
vector_store = SimpleFileVectorStore(path="vector_store", collection_name="my_vectors")

# Add embeddings
embeddings = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]]
vector_store.add(embeddings=embeddings)

# Query embeddings
query_embedding = [0.1, 0.2, 0.3]
top_k_results = vector_store.query(embedding=query_embedding, top_k=2)

# Delete embeddings
vector_store.delete(ids=["vector_id_1"])

# Drop the collection
vector_store.drop()
