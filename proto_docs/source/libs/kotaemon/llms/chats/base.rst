.. _kotaemon_llms_chats_base:

Base Chat Module
================

This module provides the base implementation for chat functionality using the `ChatLLM` class, which integrates with the base LLM components.

Class Overview
--------------

`ChatLLM`
~~~~~~~~~
.. autoclass:: ChatLLM
   :members:
   :undoc-members:
   :show-inheritance:

Details
-------

The `ChatLLM` class inherits from `BaseLLM` and provides a method to process and handle chat flows.

**Methods**:
- `flow()`: This method orchestrates the flow of input through the system. It performs the following:
  - Validates that the `inflow` is provided.
  - Ensures that `inflow` is an instance of `BaseComponent`.
  - Extracts text from the `inflow` component and processes it using the `__call__` method.

**Exceptions Raised**:
- `ValueError`: Raised when `inflow` is not provided or is not a valid `BaseComponent`.

Source Code
-----------

.. literalinclude:: ../../../../../../libs/kotaemon/kotaemon/llms/chats/base.py
   :language: python
   :linenos:

