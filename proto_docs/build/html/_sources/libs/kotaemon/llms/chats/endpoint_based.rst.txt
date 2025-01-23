.. _kotaemon_llms_chats_endpoint_based:

Endpoint Chat Module
====================

This module implements an endpoint-based chat functionality using the `EndpointChatLLM` class. It is designed to interact with an OpenAI-compatible API endpoint to generate responses.

Class Overview
--------------

`EndpointChatLLM`
~~~~~~~~~~~~~~~~~
.. autoclass:: EndpointChatLLM
   :members:
   :undoc-members:
   :show-inheritance:

Details
-------

The `EndpointChatLLM` class extends `ChatLLM` and uses a specified endpoint URL to interact with a chat API.

**Attributes**:
- `endpoint_url`:
  - **Type**: `str`
  - **Description**: The URL of an OpenAI-compatible API endpoint.
  - **Required**: Yes

**Methods**:
- `run(messages, **kwargs)`:
  - **Description**: Processes a history of messages to generate a response.
  - **Parameters**:
    - `messages`: A `str`, `BaseMessage`, or `list[BaseMessage]` containing the conversation history.
    - `**kwargs`: Additional arguments for the API request.
  - **Returns**: An instance of `LLMInterface` containing the generated response.
  - **Raises**: Validations and API-specific exceptions.
- `invoke(messages, **kwargs)`:
  - **Description**: An alias for the `run` method.
  - **Parameters**: Same as `run`.
  - **Returns**: Same as `run`.
- `ainvoke(messages, **kwargs)`:
  - **Description**: An asynchronous version of the `invoke` method.
  - **Parameters**: Same as `run`.
  - **Returns**: Same as `run`.

**Usage Workflow**:
1. The `run` method processes input messages:
   - Accepts inputs as a `str`, `BaseMessage`, or a list of `BaseMessage`.
   - Converts the inputs into a format compatible with the OpenAI API.
2. Sends the formatted request to the endpoint URL via an HTTP POST request.
3. Parses the response to extract:
   - Generated content
   - Candidate messages
   - Token usage details (`completion_tokens`, `total_tokens`, `prompt_tokens`)
4. Returns an `LLMInterface` object containing the processed response.

**Helper Function**:
- `decide_role`: Determines the role (`system`, `assistant`, or `user`) for a message based on its type (`SystemMessage`, `AIMessage`, or `HumanMessage`).

Source Code
-----------

.. literalinclude:: ../../../../../../libs/kotaemon/kotaemon/llms/chats/endpoint_based.py
   :language: python
   :linenos:

