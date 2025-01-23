Base
====

The `kotaemon.base` module provides core functionality for the `kotaemon` framework. It includes foundational components, schemas, and utilities for building and managing the system's operations.

.. toctree::
   :maxdepth: 1
   :caption: Submodules:

   component
   schema

Exports
-------

The `__init__.py` file of the `kotaemon.base` module consolidates and re-exports key components and schemas for convenient access. Below is a summary of the exports:

Classes
~~~~~~~
- **`BaseComponent`**: A foundational class for building pipeline components.
- **`Document`**: Represents the core data structure for raw content.
- **`DocumentWithEmbedding`**: A `Document` subclass ensuring embeddings are included.
- **`BaseMessage`**: The base class for system, AI, and human messages.
- **`SystemMessage`**, **`AIMessage`**, **`HumanMessage`**: Specific message types for different roles.
- **`RetrievedDocument`**: A document subclass with retrieval-specific metadata.
- **`LLMInterface`**: Represents interactions with LLMs.
- **`ExtractorOutput`**: Captures the output of an extractor.

Utilities
~~~~~~~~~
- **`lazy`**: A utility for delayed computation or initialization.
- **`Param`**: Utility for defining configurable parameters.
- **`Node`**: Represents a node in the pipeline.

Refer to the detailed submodule documentation for more information:
- `component <component.html>`_
- `schema <schema.html>`_
