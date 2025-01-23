.. _kotaemon_storages_vectorstores:

Vectorstores Module
===================

This module provides various implementations of vector stores to manage and query vector embeddings efficiently.

Contents:
---------

.. toctree::
   :maxdepth: 2
   :caption: Vectorstores Module Contents

   base
   chroma
   in_memory
   lancedb
   milvus
   qdrant
   simple_file

Module Overview
---------------

### `__init__.py`
The `__init__.py` file initializes the `vectorstores` module by importing the following classes:
- **`BaseVectorStore`**: Abstract base class for implementing vector stores.
- **`ChromaVectorStore`**: A vector store using Chroma for persistent storage and efficient queries.
- **`InMemoryVectorStore`**: An in-memory storage implementation for quick prototyping and testing.
- **`LanceDBVectorStore`**: A vector store leveraging LanceDB with full-text search capabilities.
- **`MilvusVectorStore`**: A vector store backed by Milvus for scalable and high-performance vector management.
- **`QdrantVectorStore`**: A vector store that uses Qdrant for fast and scalable vector operations.
- **`SimpleFileVectorStore`**: An extension of `InMemoryVectorStore` with persistent file-based storage.

**Source Code**:
.. literalinclude:: ../../../../../../../libs/kotaemon/kotaemon/storages/vectorstores/__init__.py
   :language: python
   :linenos:

The `vectorstores` folder contains the following implementations:

- **`base.py`**:
  - Defines the `BaseVectorStore` abstract base class, which provides a blueprint for all vector store implementations.
- **`chroma.py`**:
  - Implements the `ChromaVectorStore` class, using Chroma for vector storage and retrieval.
- **`in_memory.py`**:
  - Implements the `InMemoryVectorStore` class, providing an in-memory solution for vector embeddings.
- **`lancedb.py`**:
  - Implements the `LanceDBVectorStore` class, leveraging LanceDB for vector management with full-text search support.
- **`milvus.py`**:
  - Implements the `MilvusVectorStore` class, which connects to Milvus for scalable vector storage and queries.
- **`qdrant.py`**:
  - Implements the `QdrantVectorStore` class, which integrates with Qdrant for fast and efficient vector operations.
- **`simple_file.py`**:
  - Implements the `SimpleFileVectorStore` class, an extension of `InMemoryVectorStore` that supports automatic file persistence.
