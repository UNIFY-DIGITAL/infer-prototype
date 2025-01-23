.. _llms_base:

===========================
Base Module
===========================

The `base.py` file defines the foundational components for interacting with Large Language Models (LLMs). It serves as the base class for all LLM-related operations, providing essential interfaces and methods to be extended by other components in the `llms` module.

Overview
--------

The `BaseLLM` class is the primary interface for interacting with LLMs. It provides abstract methods for synchronous and asynchronous invocation, streaming results, and integration with LangChain.

Classes
-------

**BaseLLM**

The `BaseLLM` class is an abstract base class for implementing interactions with LLMs. It includes methods for standard and advanced use cases like streaming and async processing.

- **Key Methods**:
  - `to_langchain_format`: Converts the current model to a LangChain-compatible format.
  - `invoke`: Processes a single input synchronously.
  - `ainvoke`: Processes a single input asynchronously.
  - `stream`: Provides a synchronous streaming interface.
  - `astream`: Provides an asynchronous streaming interface.
  - `run`: A wrapper for `invoke` to maintain API consistency.

Source Code
-----------

.. literalinclude:: ../../../libs/kotaemon/kotaemon/llms/base.py
   :language: python
   :linenos:
