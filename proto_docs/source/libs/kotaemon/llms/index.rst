.. _llms_index:

===========================
llms
===========================

The `kotaemon/llms` folder provides the core functionality and utilities for interacting with various LLMs (Large Language Models). It includes foundational components, branching mechanisms, and tools for conversation handling, prompt management, and completions.

This module consists of the following files and subfolders:

.. toctree::
   :maxdepth: 1

   base
   branching
   cot
   linear
   chats/index
   completions/index
   prompts/index

Modules
-------

**`__init__.py`**

The `__init__.py` file initializes the `llms` package, exposing key components and modules for seamless integration. It re-exports:

- **Base Components**:
  - `BaseLLM`: The foundational interface for all LLM interactions.
- **Chat-Specific Components**:
  - `ChatLLM`, `AzureChatOpenAI`, `ChatOpenAI`, and others for handling chat-based interactions.
- **Completion-Specific Components**:
  - `LLM`, `OpenAI`, and `AzureOpenAI` for text generation workflows.
- **Prompt-Specific Components**:
  - `PromptTemplate` and `BasePromptComponent` for reusable prompts.
- **Pipelines**:
  - `SimpleLinearPipeline`, `GatedLinearPipeline`, and branching mechanisms like `SimpleBranchingPipeline`.
- **Chain-of-Thought**:
  - `ManualSequentialChainOfThought` and `Thought` for reasoning tasks.

For a detailed list of all components, see the source code.

**`base.py`**

Contains the base classes and foundational utilities for interacting with LLMs.

**`branching.py`**

Implements branching mechanisms for managing complex LLM workflows.

**`cot.py`**

Handles Chain-of-Thought (CoT) reasoning workflows for LLMs.

**`linear.py`**

Provides linear interaction mechanisms for sequential LLM processing.

Subfolders
----------

**`chats/`**

Manages chat-based interactions with LLMs.

**`completions/`**

Handles completions and other text generation workflows.

**`prompts/`**

Stores and manages reusable prompts for LLM interactions.

Source Code
-----------

.. literalinclude:: ../../../libs/kotaemon/kotaemon/llms/__init__.py
   :language: python
   :linenos:
