Rankings
===============

The `rankings` module is a part of the `kotaemon.indices` package and provides components for re-ranking and scoring documents retrieved during indexing and retrieval workflows. It integrates with various reranking models, including Cohere and LLM-based approaches, and offers advanced scoring capabilities.

Contents
--------

.. toctree::
   :maxdepth: 1
   :caption: Submodules:

   base
   cohere
   llm
   llm_scoring
   llm_trulens

Exports
-------

The `__init__.py` file consolidates and re-exports the key components for ease of use. Below is a list of the exported classes and their functionalities:

- **BaseReranking**: Abstract base class for implementing custom reranking logic.
- **CohereReranking**: Reranking based on the Cohere LLM API.
- **LLMReranking**: Reranking logic that uses language models for scoring.
- **LLMScoring**: A scoring pipeline for evaluating documents using LLMs.
- **LLMTrulensScoring**: Trulens-based reranking and scoring for LLM outputs.

Source Code
-----------

.. literalinclude:: ../rankings/__init__.py
   :language: python
   :linenos:
