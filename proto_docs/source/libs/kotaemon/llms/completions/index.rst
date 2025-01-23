.. _kotaemon_llms_completions:

Completions Module
==================

This module provides foundational and LangChain-based functionality for generating completions, supporting backends like OpenAI, Azure OpenAI, and LlamaCpp.

Contents:
---------

.. toctree::
   :maxdepth: 2
   :caption: Completions Module Contents

   __init__
   base
   langchain_based

Module Overview
---------------

The `completions` folder includes the following files:

### `__init__.py`
This file initializes the completions module, importing key classes such as:
- **`LLM`**: The base class for completion models.
- **`OpenAI`**: A wrapper for OpenAI's completion models.
- **`AzureOpenAI`**: A wrapper for Azure OpenAI's completion models.
- **`LlamaCpp`**: A wrapper for LangChain's LlamaCpp completion models.
- **`LCCompletionMixin`**: Provides shared functionality for LangChain-based completions.


- **`base.py`**: Defines the `LLM` class, the foundation for completion models.
- **`langchain_based.py`**: Implements wrappers for LangChain-based completion models, supporting OpenAI, Azure OpenAI, and LlamaCpp.

Source Code
-----------

.. literalinclude:: ../../../../../../libs/kotaemon/kotaemon/llms/completions/__init__.py
   :language: python
