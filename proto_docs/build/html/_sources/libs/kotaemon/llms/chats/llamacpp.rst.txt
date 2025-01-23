.. _kotaemon_llms_chats_llamacpp:

LlamaCpp Chat Module
=====================

This module provides a wrapper for the `llama-cpp-python` library to integrate Llama-based chat models. It includes support for model loading, message preparation, and generating chat completions.

Class Overview
--------------

`LlamaCppChat`
~~~~~~~~~~~~~~
.. autoclass:: LlamaCppChat
   :members:
   :undoc-members:
   :show-inheritance:

Details
-------

The `LlamaCppChat` class is designed to work with Llama models and integrates with the `llama-cpp-python` library.

**Attributes**:
- **`model_path`** (`Optional[str]`): Path to the model file. Required for loading the model.
- **`repo_id`** (`Optional[str]`): ID of a Hugging Face repository containing the model.
- **`filename`** (`Optional[str]`): Name of the model file in the repository.
- **`chat_format`** (`str`): Chat format to use (refer to `llama_cpp.llama_chat_format`).
- **`lora_base`** (`Optional[str]`): Path to the base LORA model.
- **`n_ctx`** (`Optional[int]`): Context size for text input (default is `512`).
- **`n_gpu_layers`** (`Optional[int]`): Number of model layers to offload to the GPU.
- **`use_mmap`** (`Optional[bool]`): Whether to use memory mapping (default is `True`).
- **`vocab_only`** (`Optional[bool]`): Whether to load only the vocabulary (default is `False`).

**Methods**:
- **`client_object()`**:
  - Returns the `llama-cpp-python` client object.
  - Handles model loading either from a file (`model_path`) or from Hugging Face (`repo_id` and `filename`).
- **`prepare_message(messages)`**:
  - Converts input messages (`str`, `BaseMessage`, or `list[BaseMessage]`) into the required chat format.
- **`invoke(messages, **kwargs)`**:
  - Synchronously generates a chat completion using the model.
  - **Returns**: `LLMInterface` with content, candidates, and token usage details.
- **`stream(messages, **kwargs)`**:
  - Streams responses from the model as they are generated.
  - **Returns**: An iterator of `LLMInterface` objects.

**Error Handling**:
- Raises `ImportError` if `llama-cpp-python` is not installed.
- Raises `ValueError` if required parameters like `model_path` or `chat_format` are missing.

**Usage**:
1. Load the Llama model using either a file path (`model_path`) or a Hugging Face repo (`repo_id` and `filename`).
2. Prepare the input messages using the `prepare_message` method.
3. Use `invoke` or `stream` to interact with the model and generate responses.

Source Code
-----------

.. literalinclude:: ../../../../../../libs/kotaemon/kotaemon/llms/chats/llamacpp.py
   :language: python
   :linenos:
