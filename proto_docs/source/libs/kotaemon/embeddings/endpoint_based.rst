Endpoint Embeddings
===================

The `kotaemon.embeddings.endpoint_based` module provides an implementation of embeddings generation by interfacing with an OpenAI-compatible API endpoint. This component uses an external API to generate embeddings for text or `Document` inputs.

---

**Overview**:
~~~~~~~~~~~~~
The `EndpointEmbeddings` class is designed to interact with OpenAI-compatible API endpoints to fetch embeddings. It supports batch processing and ensures that responses are converted into standardized `DocumentWithEmbedding` objects.

---

**Classes**:
~~~~~~~~~~~~

### `EndpointEmbeddings`

**Purpose**:
This class enables embeddings generation by sending input text or `Document` objects to an external API endpoint and retrieving the embeddings.

**Attributes**:
- **`endpoint_url`**: The URL of the OpenAI-compatible API endpoint. This is a required attribute and must point to a functional endpoint that adheres to the OpenAI API schema.

**Methods**:
1. **`run`**:
   - Processes input text or documents, sends them to the API, and returns the generated embeddings.
   - Supports single and batch inputs.
   - Converts the response into a list of `DocumentWithEmbedding` objects.

   **Signature**:
   .. code-block:: python

       def run(
           self, text: str | list[str] | Document | list[Document]
       ) -> list[DocumentWithEmbedding]:
           ...

   **Detailed Workflow**:
   - Inputs are normalized into a list (if not already a list).
   - For each input:
     1. A POST request is sent to the `endpoint_url` with the input text.
     2. The response JSON is parsed to extract:
        - Embeddings
        - Usage metadata (e.g., total tokens, prompt tokens)
   - Constructs a `DocumentWithEmbedding` object for each input.

2. **`invoke`**:
   - Not explicitly implemented in this class, but it inherits the functionality from the `run` method.

**Code Walkthrough**:
---------------------

Below is the complete source code for the `EndpointEmbeddings` class, including all defined methods.

.. code-block:: python

    import requests

    from kotaemon.base import Document, DocumentWithEmbedding

    from .base import BaseEmbeddings


    class EndpointEmbeddings(BaseEmbeddings):
        """
        An Embeddings component that uses an OpenAI API compatible endpoint.

        Attributes:
            endpoint_url (str): The URL of an OpenAI API compatible endpoint.
        """

        endpoint_url: str

        def run(
            self, text: str | list[str] | Document | list[Document]
        ) -> list[DocumentWithEmbedding]:
            """
            Generate embeddings from text.

            Args:
                text (str | list[str] | Document | list[Document]): Text to generate embeddings from.

            Returns:
                list[DocumentWithEmbedding]: Embeddings.
            """
            if not isinstance(text, list):
                text = [text]

            outputs = []

            for item in text:
                response = requests.post(
                    self.endpoint_url, json={"input": str(item)}
                ).json()
                outputs.append(
                    DocumentWithEmbedding(
                        text=str(item),
                        embedding=response["data"][0]["embedding"],
                        total_tokens=response["usage"]["total_tokens"],
                        prompt_tokens=response["usage"]["prompt_tokens"],
                    )
                )

            return outputs

---

**Use Cases**:
~~~~~~~~~~~~~~

1. **Embedding Generation for a Single Input**:
   - Example:
     .. code-block:: python

         endpoint = "https://api.example.com/v1/embeddings"
         embeddings_component = EndpointEmbeddings(endpoint_url=endpoint)
         text = "Sample input text"
         embeddings = embeddings_component.run(text)
         print(embeddings)

2. **Batch Processing**:
   - The `run` method supports batch processing, allowing multiple inputs to be sent in one call.
   - Example:
     .. code-block:: python

         texts = ["Input 1", "Input 2", "Input 3"]
         embeddings = embeddings_component.run(texts)
         for embedding in embeddings:
             print(embedding)

3. **Error Handling**:
   - If the API does not respond as expected (e.g., incorrect URL or schema), an exception is raised. Ensure that the `endpoint_url` points to a functional endpoint.

---

**Integration Notes**:
~~~~~~~~~~~~~~~~~~~~~~
- Ensure the endpoint is OpenAI-compatible and returns a response containing the following keys:
  - `data`: A list containing embedding information.
  - `usage`: Metadata about token usage.
- The input text or document must be convertible to a string format.

---

This refined version provides a structured and detailed explanation of the `EndpointEmbeddings` class, its attributes, and methods. The code is directly included at the end for reference. Let me know if you'd like further refinements or if we should move to the next file!
