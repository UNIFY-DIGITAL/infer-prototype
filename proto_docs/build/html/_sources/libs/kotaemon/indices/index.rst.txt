Indices
=======

The `indices` module is a core part of the `kotaemon` framework. It provides functionalities for indexing, retrieving, ranking, and managing documents. This module enables efficient storage and retrieval of documents, as well as advanced querying capabilities.

.. note::

   The `indices` module is designed to handle various document formats, embedding types, and ranking strategies.

Contents
--------

.. toctree::
   :maxdepth: 1
   :caption: Submodules:

   base
   vectorindex
   extractors/index
   ingests/index
   qa/index
   rankings/index
   retrievers/index
   splitters/index

Key Components
--------------

The `indices` module exports several key classes and functions:

- **VectorIndexing**: Handles document ingestion and embedding storage in a vector store.
- **VectorRetrieval**: Supports retrieval of documents based on embeddings or other strategies.
- **BaseIndexing**: Defines the interface for indexing pipelines.
- **BaseRetrieval**: Defines the interface for retrieval pipelines.
- **DocTransformer**: A base class for transforming documents, such as splitting or metadata augmentation.
- **LlamaIndexDocTransformerMixin**: Integrates LlamaIndex components into the `kotaemon` framework.

Submodules Overview
-------------------

- **Extractors**: Handles document parsing and information extraction.
- **Ingests**: Manages document ingestion pipelines.
- **QA**: Provides question-answering capabilities with optional citation support.
- **Rankings**: Contains classes for document reranking using LLMs or other strategies.
- **Retrievers**: Implements various retrieval mechanisms, including web search.
- **Splitters**: Contains utilities for splitting large documents into smaller chunks.
