Base Module
===========

The `base` module in the `rankings` folder provides the abstract base class for implementing reranking strategies. All reranking components should extend the `BaseReranking` class and implement the `run` method.

Key Class
---------

**BaseReranking**

The `BaseReranking` class is an abstract base class designed for custom reranking implementations. Subclasses must override the `run` method to define their reranking logic.

Methods
~~~~~~~
- **run(documents: list[Document], query: str) -> list[Document]:**
  - Abstract method to be implemented by subclasses.
  - Responsible for reranking or filtering a list of documents based on the given query.

Source Code
-----------

.. literalinclude:: ../rankings/base.py
   :language: python
   :linenos:
