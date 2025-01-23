TEI Endpoint-Based Embeddings
=============================

The `kotaemon.embeddings.tei_endpoint_embed` module provides an integration with the Text-Embedding-Inference (TEI) API for generating embeddings. It supports both synchronous and asynchronous embedding requests.

---

**Overview**:
~~~~~~~~~~~~~
This module defines the `TeiEndpointEmbeddings` class for embedding generation via a TEI-compatible endpoint. It supports key features like:
- **Normalization**: Ensures embeddings are normalized to unit length.
- **Truncation**: Truncates embeddings to a fixed/default length for compatibility.

**Reference**:
`TEI GitHub Repository <https://github.com/huggingface/text-embeddings-inference>`_

---

**Classes**:
~~~~~~~~~~~~

### **`TeiEndpointEmbeddings`**

**Purpose**:
A component that interfaces with a TEI API-compatible endpoint to generate text embeddings. 

**Key Attributes**:
- `endpoint_url`: URL for the TEI embedding service (required).
- `normalize`: Boolean flag to normalize embeddings to unit length (default: `True`).
- `truncate`: Boolean flag to truncate embeddings to a fixed/default length (default: `True`).

**Key Methods**:

#### **`invoke`**
- **Description**:
  Synchronously sends text input to the TEI endpoint for embedding generation.
- **Parameters**:
  - `text`: A string, list of strings, `Document`, or list of `Document` objects.
- **Returns**:
  - A list of `DocumentWithEmbedding` objects containing the text and its embeddings.

#### **`ainvoke`**
- **Description**:
  Asynchronously sends text input to the TEI endpoint for embedding generation.
- **Parameters**:
  - `text`: A string, list of strings, `Document`, or list of `Document` objects.
- **Returns**:
  - A list of `DocumentWithEmbedding` objects containing the text and its embeddings.

#### **`client_`**
- **Description**:
  Handles the asynchronous POST request to the TEI endpoint with necessary parameters.
- **Parameters**:
  - `inputs`: A list of strings to embed.
- **Returns**:
  - A list of embeddings returned by the TEI service.

---

**Code Walkthrough**:
~~~~~~~~~~~~~~~~~~~~~

Below is the complete source code for the `tei_endpoint_embed.py` module.

.. code-block:: python

    import aiohttp
    import requests

    from kotaemon.base import Document, DocumentWithEmbedding, Param

    from .base import BaseEmbeddings

    session = requests.session()


    class TeiEndpointEmbeddings(BaseEmbeddings):
        """An Embeddings component that uses an
        TEI (Text-Embedding-Inference) API compatible endpoint.

        Ref: https://github.com/huggingface/text-embeddings-inference

        Attributes:
            endpoint_url (str): The url of an TEI
                (Text-Embedding-Inference) API compatible endpoint.
            normalize (bool): Whether to normalize embeddings to unit length.
            truncate (bool): Whether to truncate embeddings
                to a fixed/default length.
        """

        endpoint_url: str = Param(None, help="TEI embedding service api base URL")
        normalize: bool = Param(
            True,
            help="Normalize embeddings to unit length",
        )
        truncate: bool = Param(
            True,
            help="Truncate embeddings to a fixed/default length",
        )

        async def client_(self, inputs: list[str]):
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    url=self.endpoint_url,
                    json={
                        "inputs": inputs,
                        "normalize": self.normalize,
                        "truncate": self.truncate,
                    },
                ) as resp:
                    embeddings = await resp.json()
            return embeddings

        async def ainvoke(
            self, text: str | list[str] | Document | list[Document], *args, **kwargs
        ) -> list[DocumentWithEmbedding]:
            if not isinstance(text, list):
                text = [text]
            text = self.prepare_input(text)

            outputs = []
            batch_size = 6
            num_batch = max(len(text) // batch_size, 1)
            for i in range(num_batch):
                if i == num_batch - 1:
                    mini_batch = text[batch_size * i :]
                else:
                    mini_batch = text[batch_size * i : batch_size * (i + 1)]
                mini_batch = [x.content for x in mini_batch]
                embeddings = await self.client_(mini_batch)  # type: ignore
                outputs.extend(
                    [
                        DocumentWithEmbedding(content=doc, embedding=embedding)
                        for doc, embedding in zip(mini_batch, embeddings)
                    ]
                )

            return outputs

        def invoke(
            self, text: str | list[str] | Document | list[Document], *args, **kwargs
        ) -> list[DocumentWithEmbedding]:
            if not isinstance(text, list):
                text = [text]

            text = self.prepare_input(text)

            outputs = []
            batch_size = 6
            num_batch = max(len(text) // batch_size, 1)
            for i in range(num_batch):
                if i == num_batch - 1:
                    mini_batch = text[batch_size * i :]
                else:
                    mini_batch = text[batch_size * i : batch_size * (i + 1)]
                mini_batch = [x.content for x in mini_batch]
                embeddings = session.post(
                    url=self.endpoint_url,
                    json={
                        "inputs": mini_batch,
                        "normalize": self.normalize,
                        "truncate": self.truncate,
                    },
                ).json()
                outputs.extend(
                    [
                        DocumentWithEmbedding(content=doc, embedding=embedding)
                        for doc, embedding in zip(mini_batch, embeddings)
                    ]
                )
            return outputs
