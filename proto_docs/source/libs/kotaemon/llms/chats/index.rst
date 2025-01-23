.. _kotaemon_llms_chats:

Chats Module
============

This module contains various implementations for chat-based functionalities, supporting multiple backends like OpenAI, LlamaCPP, and LangChain.

Contents:
---------

.. toctree::
   :maxdepth: 2
   :caption: Chats Module Contents

   base
   endpoint_based
   langchain_based
   llamacpp
   openai

Module Overview
---------------

The `chats` folder includes the following files:

- **`base.py`**: Provides the base class for chat functionalities.
- **`endpoint_based.py`**: Handles chat functionality using endpoint-based models like OpenAI-compatible APIs.
- **`langchain_based.py`**: Implements LangChain-based chat integrations, supporting multiple LangChain-compatible backends.
- **`llamacpp.py`**: Wraps the `llama-cpp-python` library for Llama-based chat functionality.
- **`openai.py`**: Integrates OpenAI's chat models, including support for Azure OpenAI.

Source Code
-----------

.. literalinclude:: ../../../../../../libs/kotaemon/kotaemon/llms/chats/__init__.py
   :language: python
