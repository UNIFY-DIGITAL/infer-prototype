.. _kotaemon_llms_rerankings:

Rerankings
=================

This module provides various implementations for reranking documents based on their relevance to a query, using different backends like Cohere and Hugging Face TEI.

Contents:
---------

.. toctree::
   :maxdepth: 2
   :caption: Rerankings Module Contents

   base
   cohere
   tei_fast_rerank

Module Overview
---------------

### `__init__.py`
This file initializes the rerankings module by importing the following classes:
- **`BaseReranking`**: The abstract base class for implementing custom reranking logic.
- **`CohereReranking`**: A reranking implementation leveraging the Cohere API.
- **`TeiFastReranking`**: A reranking implementation using the Hugging Face Text Embeddings Inference (TEI) API.

**Source Code**:
.. literalinclude:: ../../../../../../libs/kotaemon/kotaemon/rerankings/__init__.py
   :language: python

---

The `rerankings` folder includes the following files:

- **`base.py`**:
  - Defines the `BaseReranking` class, which serves as the foundation for all reranking implementations.
- **`cohere.py`**:
  - Implements the `CohereReranking` class, which uses the Cohere API to assign relevance scores to documents.
- **`tei_fast_rerank.py`**:
  - Implements the `TeiFastReranking` class, which interacts with the Hugging Face TEI service to reorder documents.

