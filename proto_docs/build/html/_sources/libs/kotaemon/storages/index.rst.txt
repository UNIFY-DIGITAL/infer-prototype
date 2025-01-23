.. _kotaemon_storages:

Storages
===============

The `storages` module provides a comprehensive set of tools to manage and query both document and vector data. It is divided into two main submodules: `docstores` and `vectorstores`.

Contents:
---------

.. toctree::
   :maxdepth: 2
   :caption: Storages Module Contents

   docstores/index
   vectorstores/index

Module Overview
---------------

The `storages` module contains the following submodules:

### `docstores`
This submodule provides various implementations of document stores to efficiently store and retrieve textual data. The available classes include:
- **`BaseDocumentStore`**: Abstract base class for document stores.
- **`ElasticsearchDocumentStore`**: Leverages Elasticsearch for scalable document storage.
- **`InMemoryDocumentStore`**: Provides an in-memory storage solution for quick prototyping.
- **`LanceDBDocumentStore`**: Uses LanceDB for document storage and full-text search.
- **`SimpleFileDocumentStore`**: Extends `InMemoryDocumentStore` with file-based persistence.

For detailed documentation, see :ref:`kotaemon_storages_docstores`.

### `vectorstores`
This submodule provides various implementations of vector stores for managing and querying vector embeddings. The available classes include:
- **`BaseVectorStore`**: Abstract base class for vector stores.
- **`ChromaVectorStore`**: A vector store using Chroma for persistent storage.
- **`InMemoryVectorStore`**: An in-memory vector store for prototyping and testing.
- **`LanceDBVectorStore`**: Leverages LanceDB for managing vector embeddings with full-text search.
- **`MilvusVectorStore`**: Connects to Milvus for scalable vector operations.
- **`QdrantVectorStore`**: Integrates with Qdrant for efficient vector storage and queries.
- **`SimpleFileVectorStore`**: A file-backed vector store extending `InMemoryVectorStore`.

For detailed documentation, see :ref:`kotaemon_storages_vectorstores`.
