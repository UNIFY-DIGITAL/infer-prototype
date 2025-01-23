.. _kotaemon_llms_chats_openai:

OpenAI Chat Module
==================

This module implements OpenAI-based chat integrations, supporting both OpenAI and Azure OpenAI chat models. It provides a unified interface for interaction with OpenAI's APIs using the `openai` library.

Class Overview
--------------

`BaseChatOpenAI`
~~~~~~~~~~~~~~~~
.. autoclass:: BaseChatOpenAI
   :members:
   :undoc-members:
   :show-inheritance:

`ChatOpenAI`
~~~~~~~~~~~~
.. autoclass:: ChatOpenAI
   :members:
   :undoc-members:
   :show-inheritance:

`AzureChatOpenAI`
~~~~~~~~~~~~~~~~~
.. autoclass:: AzureChatOpenAI
   :members:
   :undoc-members:
   :show-inheritance:

Details
-------

### `BaseChatOpenAI`
This base class provides the foundation for OpenAI chat model integrations. It defines the common parameters and methods required to interact with OpenAI's chat models.

**Attributes**:
- API-related parameters like `api_key`, `timeout`, `max_retries`, `temperature`, `max_tokens`, and more.
- Supports OpenAI-specific features such as `logprobs`, `logit_bias`, and `top_p`.

**Methods**:
- `prepare_message`: Converts input messages (`str`, `BaseMessage`, or `list[BaseMessage]`) to OpenAI's format.
- `prepare_output`: Converts OpenAI's response into an `LLMInterface` object.
- `prepare_client`: Must be implemented by subclasses to create the OpenAI client.
- `openai_response`: Must be implemented by subclasses to handle API responses.
- Supports synchronous and asynchronous invocation (`invoke`, `ainvoke`) and streaming (`stream`, `astream`).

---

### `ChatOpenAI`
Implements the OpenAI chat model interface for direct interaction with OpenAI's API.

**Additional Parameters**:
- `base_url`: The base URL for the OpenAI API.
- `organization`: The organization associated with the OpenAI API key.
- `model`: The specific OpenAI model to use.

**Methods**:
- Implements `prepare_client` to create OpenAI clients for synchronous or asynchronous interactions.

---

### `AzureChatOpenAI`
Extends `BaseChatOpenAI` to interact with Microsoft Azure OpenAI services.

**Additional Parameters**:
- `azure_endpoint`: The Azure OpenAI service endpoint.
- `azure_deployment`: The deployment name for the Azure OpenAI model.
- `api_version`: The version of the Azure OpenAI API.
- `azure_ad_token`: Optional Azure Active Directory token.
- `azure_ad_token_provider`: Optional provider for fetching Azure AD tokens.

**Methods**:
- Implements `prepare_client` and `prepare_params` to handle Azure-specific configurations and interactions.

---

**Usage Workflow**:
1. Create an instance of `ChatOpenAI` or `AzureChatOpenAI` with the necessary parameters.
2. Use `invoke` or `ainvoke` for synchronous or asynchronous response generation.
3. Use `stream` or `astream` to stream responses as they are generated.
4. Format inputs using `prepare_message` and handle responses with `prepare_output`.

Source Code
-----------

.. literalinclude:: ../../../../../../libs/kotaemon/kotaemon/llms/chats/openai.py
   :language: python
   :linenos:
