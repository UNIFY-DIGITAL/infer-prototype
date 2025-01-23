Base Embeddings
===============

The `kotaemon.embeddings.base` module provides the foundation for embedding generation in the `kotaemon` framework. It introduces an abstract base class, `BaseEmbeddings`, that defines the core structure and methods to be implemented by derived classes for generating embeddings.

This module is crucial for ensuring consistency and standardization across various embedding implementations.

---

**Overview**:
~~~~~~~~~~~~~
The `BaseEmbeddings` class is designed to handle:
1. Input normalization: Ensures all input data is standardized into a list of `Document` objects.
2. Abstract methods for embedding generation:
   - `invoke`: To be implemented by subclasses for synchronous embedding generation.
   - `ainvoke`: To be implemented by subclasses for asynchronous embedding generation.
3. Support for both single and batch processing of inputs, including:
   - Single strings
   - Lists of strings
   - `Document` objects
   - Lists of `Document` objects

---

**Classes**:
~~~~~~~~~~~~

### `BaseEmbeddings`

**Purpose**:
The `BaseEmbeddings` class serves as an abstract blueprint for embedding generators. Derived classes must implement the `invoke` and `ainvoke` methods to define how embeddings are generated.

**Attributes**:
- None directly defined in this base class.

**Methods**:
1. **`run`**:
   - Entry point for generating embeddings.
   - Accepts input in various formats and delegates processing to the `invoke` method.
   - Returns a list of `DocumentWithEmbedding` objects.

   **Signature**:
   .. code-block:: python

       def run(
           self, text: str | list[str] | Document | list[Document], *args, **kwargs
       ) -> list[DocumentWithEmbedding]:
           ...

   **Usage**:
   - Can process single strings, lists of strings, or `Document` objects.
   - Returns embeddings as `DocumentWithEmbedding` objects.

2. **`invoke`** (Abstract Method):
   - To be implemented by subclasses.
   - Handles the actual embedding generation logic.

   **Signature**:
   .. code-block:: python

       def invoke(
           self, text: str | list[str] | Document | list[Document], *args, **kwargs
       ) -> list[DocumentWithEmbedding]:
           raise NotImplementedError

3. **`ainvoke`** (Abstract Method):
   - To be implemented by subclasses.
   - Handles asynchronous embedding generation.

   **Signature**:
   .. code-block:: python

       async def ainvoke(
           self, text: str | list[str] | Document | list[Document], *args, **kwargs
       ) -> list[DocumentWithEmbedding]:
           raise NotImplementedError

4. **`prepare_input`**:
   - A utility method to normalize inputs into a list of `Document` objects.
   - Converts:
     - Single strings → `Document(content=text)`
     - Lists of strings → List of `Document(content=text)`
     - Other inputs → Returns unchanged.

   **Signature**:
   .. code-block:: python

       def prepare_input(
           self, text: str | list[str] | Document | list[Document]
       ) -> list[Document]:
           ...

   **Usage**:
   - Ensures all inputs conform to the expected format for downstream processing.

**Code Walkthrough**:
---------------------
Here is the complete source code for the `BaseEmbeddings` class, including all defined methods.

.. code-block:: python

    from __future__ import annotations

    from kotaemon.base import BaseComponent, Document, DocumentWithEmbedding


    class BaseEmbeddings(BaseComponent):
        def run(
            self, text: str | list[str] | Document | list[Document], *args, **kwargs
        ) -> list[DocumentWithEmbedding]:
            return self.invoke(text, *args, **kwargs)

        def invoke(
            self, text: str | list[str] | Document | list[Document], *args, **kwargs
        ) -> list[DocumentWithEmbedding]:
            raise NotImplementedError

        async def ainvoke(
            self, text: str | list[str] | Document | list[Document], *args, **kwargs
        ) -> list[DocumentWithEmbedding]:
            raise NotImplementedError

        def prepare_input(
            self, text: str | list[str] | Document | list[Document]
        ) -> list[Document]:
            if isinstance(text, (str, Document)):
                return [Document(content=text)]
            elif isinstance(text, list):
                return [Document(content=_) for _ in text]
            return text

---

**Use Cases**:
~~~~~~~~~~~~~~

1. **Creating a Custom Embedding Generator**:
   - A subclass can inherit from `BaseEmbeddings` and implement the `invoke` and `ainvoke` methods to define how embeddings are generated.
   - Example:
     .. code-block:: python

         class MyEmbeddings(BaseEmbeddings):
             def invoke(self, text, *args, **kwargs):
                 # Custom logic for generating embeddings
                 ...

             async def ainvoke(self, text, *args, **kwargs):
                 # Custom async logic
                 ...

2. **Batch Processing**:
   - The `run` method supports processing multiple inputs in a single call, making it efficient for batch embedding generation.

---

This version adds detailed explanations of each method, including signatures, usage, and examples, making the documentation comprehensive and professional. Let me know if you’d like further adjustments or additional refinements!
