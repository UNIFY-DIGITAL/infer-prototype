.. _kotaemon_llms_chats_langchain_based:

LangChain-Based Chat Module
===========================

This module implements various LangChain-based chat integrations using a mixin architecture. It provides support for multiple LangChain-compatible chat models, including OpenAI, Azure, Anthropic, Google Gemini, and Cohere.

Mixin Overview
--------------

`LCChatMixin`
~~~~~~~~~~~~~
.. autoclass:: LCChatMixin
   :members:
   :undoc-members:
   :show-inheritance:

The `LCChatMixin` provides core functionalities for handling LangChain-based chat models, including:
- Preparing messages for LangChain models.
- Processing responses into `LLMInterface` objects.
- Supporting both synchronous and asynchronous invocation and streaming.

Class Overview
--------------

`LCChatOpenAI`
~~~~~~~~~~~~~~
.. autoclass:: LCChatOpenAI
   :members:
   :undoc-members:
   :show-inheritance:

`LCAzureChatOpenAI`
~~~~~~~~~~~~~~~~~~~
.. autoclass:: LCAzureChatOpenAI
   :members:
   :undoc-members:
   :show-inheritance:

`LCAnthropicChat`
~~~~~~~~~~~~~~~~~
.. autoclass:: LCAnthropicChat
   :members:
   :undoc-members:
   :show-inheritance:

`LCGeminiChat`
~~~~~~~~~~~~~~
.. autoclass:: LCGeminiChat
   :members:
   :undoc-members:
   :show-inheritance:

`LCCohereChat`
~~~~~~~~~~~~~~
.. autoclass:: LCCohereChat
   :members:
   :undoc-members:
   :show-inheritance:

Details
-------

**Common Features Across Models**:
- **Methods**:
  - `run`: Executes the chat workflow, handling both synchronous and streaming responses.
  - `invoke` and `ainvoke`: Synchronous and asynchronous invocation methods.
  - `stream` and `astream`: Synchronous and asynchronous streaming methods.
- **Attributes**:
  - API-specific parameters like `api_key`, `model_name`, and `temperature`.

**Individual Models**:
- `LCChatOpenAI`:
  - Supports OpenAI's chat models.
  - Auto-detects between `langchain_openai` and `langchain.chat_models`.
- `LCAzureChatOpenAI`:
  - Integrates with Azure OpenAI chat endpoints.
  - Supports deployment-specific configurations like `deployment_name` and `openai_api_version`.
- `LCAnthropicChat`:
  - Implements Anthropic Claude models.
  - Uses `langchain_anthropic` for integration.
- `LCGeminiChat`:
  - Connects to Google Gemini chat models using `langchain_google_genai`.
- `LCCohereChat`:
  - Interfaces with Cohere chat models using `langchain_cohere`.

Source Code
-----------

.. literalinclude:: ../../../../../../libs/kotaemon/kotaemon/llms/chats/langchain_based.py
   :language: python
   :linenos:
