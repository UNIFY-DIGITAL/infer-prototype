.. _kotaemon_llms_completions_langchain_based:

LangChain-Based Completion Module
=================================

This module provides wrappers around LangChain completion models, supporting OpenAI, Azure OpenAI, and LlamaCpp integrations.

Mixin Overview
--------------

`LCCompletionMixin`
~~~~~~~~~~~~~~~~~~~
.. autoclass:: LCCompletionMixin
   :members:
   :undoc-members:
   :show-inheritance:

The `LCCompletionMixin` provides shared functionality for LangChain-based completion models, including:
- Initializing LangChain classes.
- Generating completions using `run`.
- Support for LangChain formatting via `to_langchain_format`.

Class Overview
--------------

`OpenAI`
~~~~~~~~
.. autoclass:: OpenAI
   :members:
   :undoc-members:
   :show-inheritance:

`AzureOpenAI`
~~~~~~~~~~~~~
.. autoclass:: AzureOpenAI
   :members:
   :undoc-members:
   :show-inheritance:

`LlamaCpp`
~~~~~~~~~~
.. autoclass:: LlamaCpp
   :members:
   :undoc-members:
   :show-inheritance:

Details
-------

**OpenAI**:
- Integrates OpenAI completion models (`text-davinci-003` and others) via LangChain.
- Key parameters include `openai_api_key`, `model_name`, and `temperature`.

**AzureOpenAI**:
- Provides Azure-specific OpenAI integrations with parameters like `azure_endpoint` and `deployment_name`.

**LlamaCpp**:
- Wraps LangChain's LlamaCpp models for on-device inference.

Source Code
-----------

.. literalinclude:: ../../../../../../libs/kotaemon/kotaemon/llms/completions/langchain_based.py
   :language: python
   :linenos:
