FastEmbed Embeddings
====================

The `kotaemon.embeddings.fastembed` module provides an implementation of embeddings generation using the `fastembed` library. This component is ideal for generating embeddings locally without requiring a GPU, making it efficient and lightweight for specific use cases.

---

**Overview**:
~~~~~~~~~~~~~
The `FastEmbedEmbeddings` class leverages the `fastembed` library to generate text embeddings. It supports a variety of pre-trained models, batch processing, and multi-threaded execution. This implementation is suitable for users seeking to generate embeddings efficiently without relying on external APIs.

Supported Models:
- Refer to the `fastembed` documentation for a list of supported models: [FastEmbed Supported Models](https://qdrant.github.io/fastembed/examples/Supported_Models/).

---

**Classes**:
~~~~~~~~~~~~

### `FastEmbedEmbeddings`

**Purpose**:
This class is designed to utilize the `fastembed` library for generating embeddings locally. It supports both synchronous and batch processing of input text or `Document` objects.

**Attributes**:
1. **`model_name`**:
   - **Type**: `str`
   - **Default**: `"BAAI/bge-small-en-v1.5"`
   - **Description**: Specifies the model to use for generating embeddings. Supported models are listed in the `fastembed` documentation.

2. **`batch_size`**:
   - **Type**: `int`
   - **Default**: `256`
   - **Description**: Determines the number of inputs processed in a single batch. Higher values increase memory usage but improve speed.

3. **`parallel`**:
   - **Type**: `Optional[int]`
   - **Default**: `None`
   - **Description**: Specifies the number of threads for parallel processing. Can be:
     - `> 1`: Enables data-parallel encoding using the specified number of threads.
     - `0`: Uses all available CPUs.
     - `None`: Uses the default threading configuration of `onnxruntime`.

4. **`client_`**:
   - **Type**: `TextEmbedding`
   - **Description**: Lazily initialized `fastembed` client for embedding generation.

**Methods**:
1. **`invoke`**:
   - Generates embeddings for the given input.
   - Normalizes the input into a list of `Document` objects, then calls the `embed` method of the `fastembed` client.

   **Signature**:
   .. code-block:: python

       def invoke(
           self, text: str | list[str] | Document | list[Document], *args, **kwargs
       ) -> list[DocumentWithEmbedding]:
           ...

   **Workflow**:
   - Prepares the input using `prepare_input`.
   - Calls the `embed` method of the `fastembed` client with the input text.
   - Returns a list of `DocumentWithEmbedding` objects.

2. **`ainvoke`**:
   - Asynchronous version of `invoke`. Note that `fastembed` does not support asynchronous APIs, so this method internally calls `invoke`.

   **Signature**:
   .. code-block:: python

       async def ainvoke(
           self, text: str | list[str] | Document | list[Document], *args, **kwargs
       ) -> list[DocumentWithEmbedding]:
           ...

   **Workflow**:
   - Delegates the call to `invoke`.

3. **`prepare_input`** (inherited from `BaseEmbeddings`):
   - Normalizes input into a list of `Document` objects.

4. **`client_`**:
   - Lazily initializes the `fastembed` client.
   - Requires `fastembed` to be installed (`pip install fastembed`).

---

**Code Walkthrough**:
---------------------

Below is the complete source code for the `FastEmbedEmbeddings` class, including all defined methods and attributes.

.. code-block:: python

    from typing import TYPE_CHECKING, Optional

    from kotaemon.base import Document, DocumentWithEmbedding, Param

    from .base import BaseEmbeddings

    if TYPE_CHECKING:
        from fastembed import TextEmbedding


    class FastEmbedEmbeddings(BaseEmbeddings):
        """Utilize fastembed library for embeddings locally without GPU.

        Supported model: https://qdrant.github.io/fastembed/examples/Supported_Models/
        Code: https://github.com/qdrant/fastembed
        """

        model_name: str = Param(
            "BAAI/bge-small-en-v1.5",
            help=(
                "Model name for fastembed. Please refer "
                "[here](https://qdrant.github.io/fastembed/examples/Supported_Models/) "
                "for the list of supported models."
            ),
            required=True,
        )
        batch_size: int = Param(
            256,
            help="Batch size for embeddings. Higher values use more memory, but are faster",
        )
        parallel: Optional[int] = Param(
            None,
            help=(
                "Number of threads to use for embeddings. "
                "If > 1, data-parallel encoding will be used. "
                "If 0, use all available CPUs. "
                "If None, use default onnxruntime threading. "
                "Defaults to None."
            ),
        )

        @Param.auto()
        def client_(self) -> "TextEmbedding":
            try:
                from fastembed import TextEmbedding
            except ImportError:
                raise ImportError("Please install FastEmbed: `pip install fastembed`")

            return TextEmbedding(model_name=self.model_name)

        def invoke(
            self, text: str | list[str] | Document | list[Document], *args, **kwargs
        ) -> list[DocumentWithEmbedding]:
            input_ = self.prepare_input(text)
            embeddings = self.client_.embed(
                [_.content for _ in input_],
                batch_size=self.batch_size,
                parallel=self.parallel,
            )
            return [
                DocumentWithEmbedding(
                    content=doc,
                    embedding=list(embedding),
                )
                for doc, embedding in zip(input_, embeddings)
            ]

        async def ainvoke(
            self, text: s
