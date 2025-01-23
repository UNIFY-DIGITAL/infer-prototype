.. _kotaemon_storages_docstores:

Docstores Module
================

This module provides various implementations of document stores to manage and query documents efficiently.

Contents:
---------

.. toctree::
   :maxdepth: 2
   :caption: Docstores Module Contents

   base
   elasticsearch
   in_memory
   lancedb
   simple_file

Module Overview
---------------

### `__init__.py`
The `__init__.py` file initializes the `docstores` module by importing the following classes:
- **`BaseDocumentStore`**: Abstract base class for implementing document stores.
- **`ElasticsearchDocumentStore`**: A document store leveraging Elasticsearch for scalable storage and queries.
- **`InMemoryDocumentStore`**: An in-memory storage implementation for quick prototyping.
- **`LanceDBDocumentStore`**: A document store that uses LanceDB with full-text search capabilities.
- **`SimpleFileDocumentStore`**: An extension of `InMemoryDocumentStore` with automatic saving to a JSON file.

**Source Code**:
.. literalinclude:: ../../../../../../../libs/kotaemon/kotaemon/storages/docstores/__init__.py
   :language: python
   :linenos:

The `docstores` folder contains the following implementations:

- **`base.py`**:
  - Defines the `BaseDocumentStore` abstract base class, which provides a blueprint for all document store implementations.
- **`elasticsearch.py`**:
  - Implements the `ElasticsearchDocumentStore` class, leveraging Elasticsearch for scalable and efficient document management.
- **`in_memory.py`**:
  - Implements the `InMemoryDocumentStore` class, which provides an in-memory storage solution for quick prototyping and testing.
- **`lancedb.py`**:
  - Implements the `LanceDBDocumentStore` class, which uses LanceDB for document storage and supports full-text search.
- **`simple_file.py`**:
  - Implements the `SimpleFileDocumentStore` class, extending `InMemoryDocumentStore` with automatic saving to a JSON file.

