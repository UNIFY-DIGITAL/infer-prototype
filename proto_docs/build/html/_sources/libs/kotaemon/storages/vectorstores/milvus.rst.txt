.. _kotaemon_storages_vectorstores_milvus:

Milvus Vector Store
===================

This module implements the `MilvusVectorStore` class, which provides an interface for working with the Milvus vector database using LlamaIndex.

Class Overview
--------------

`MilvusVectorStore`
~~~~~~~~~~~~~~~~~~~
.. autoclass:: MilvusVectorStore
   :members:
   :undoc-members:
   :show-inheritance:

Details
-------

The `MilvusVectorStore` class integrates with Milvus, a scalable vector database, to store and query vector embeddings efficiently. It extends the `LlamaIndexVectorStore` with additional features for lazy initialization and dynamic management of dimensions.

**Initialization**:
- The client is initialized lazily to avoid requiring dimensions upfront.
- Connects to a Milvus instance using a URI or local path.

**Attributes**:
- `uri`: The URI or local path to the Milvus instance. Default is `"./milvus.db"`.
- `collection_name`: The name of the collection. Default is `"default"`.
- `token`: Optional token for authentication.
- `_inited`: Boolean to track initialization status.

**Methods**:
- **`add(embeddings, metadatas=None, ids=None)`**:
  - Adds vector embeddings to the Milvus collection.
  - Dynamically initializes the client based on the dimension of the embeddings.
- **`query(embedding, top_k=1, ids=None, **kwargs)`**:
  - Queries the Milvus vector store for the top-k similar embeddings.
  - Dynamically initializes the client if not already initialized.
- **`delete(ids, **kwargs)`**:
  - Deletes vector embeddings by their IDs.
- **`drop()`**:
  - Deletes the entire Milvus collection.
- **`count()`**:
  - Returns the total number of embeddings in the collection.
  - Initializes the client if required.
- **`__persist_flow__()`**:
  - Serializes the vector store configuration for persistence.

**Usage Workflow**:
1. Initialize the `MilvusVectorStore` with a URI or local path.
2. Add vector embeddings using `add`.
3. Query embeddings using `query`.
4. Manage collections using `delete` or `drop`.

**Example**:
```python
from kotaemon.storages.vectorstores.milvus import MilvusVectorStore

# Initialize the Milvus vector store
vector_store = MilvusVectorStore(uri="http://localhost:19530", collection_name="my_vectors")

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
