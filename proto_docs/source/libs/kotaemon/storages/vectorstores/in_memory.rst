.. _kotaemon_storages_vectorstores_in_memory:

In-Memory Vector Store
======================

This module implements the `InMemoryVectorStore` class, a simple vector store implementation that extends the `LlamaIndexVectorStore`.

Class Overview
--------------

`InMemoryVectorStore`
~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: InMemoryVectorStore
   :members:
   :undoc-members:
   :show-inheritance:

Details
-------

The `InMemoryVectorStore` class provides an in-memory implementation of a vector store, with optional persistence capabilities using the `fsspec` filesystem abstraction.

**Initialization**:
- Supports optional initialization with preloaded vector store data.
- Optionally connects to a filesystem for persistence.

**Attributes**:
- `_data`: The in-memory vector store data, an instance of `SimpleVectorStoreData`.
- `_fs`: Filesystem instance for saving and loading data.

**Methods**:
- **`add(embeddings, metadatas=None, ids=None)`**:
  - Inherited from `LlamaIndexVectorStore`. Adds vector embeddings to the store.
- **`save(save_path, fs=None)`**:
  - Saves the in-memory vector store data to disk.
  - **Parameters**:
    - `save_path`: Path to save the vector store.
    - `fs`: Optional filesystem instance.
- **`load(load_path, fs=None)`**:
  - Loads vector store data from disk.
  - **Parameters**:
    - `load_path`: Path to load the vector store from.
    - `fs`: Optional filesystem instance.
- **`drop()`**:
  - Clears all data from the vector store.
- **`__persist_flow__()`**:
  - Serializes the vector store data for persistence.

**Usage Workflow**:
1. Initialize the `InMemoryVectorStore` with optional preloaded data.
2. Add vector embeddings using `add`.
3. Save or load the vector store using `save` and `load`.
4. Clear the store with `drop`.

**Example**:
```python
from kotaemon.storages.vectorstores.in_memory import InMemoryVectorStore
from llama_index.core.vector_stores.simple import SimpleVectorStoreData

# Initialize the vector store
vector_store = InMemoryVectorStore()

# Add embeddings
embeddings = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]]
vector_store.add(embeddings=embeddings)

# Save the vector store to disk
vector_store.save("vector_store.json")

# Load the vector store from disk
vector_store.load("vector_store.json")

# Clear the store
vector_store.drop()
