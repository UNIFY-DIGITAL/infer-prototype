OpenAI-Based Embeddings
========================

The `kotaemon.embeddings.openai` module provides classes to integrate OpenAI's embedding services into the `kotaemon` framework. It includes support for OpenAI's API, Azure OpenAI models, and advanced functionality such as chunking for large text inputs.

---

**Overview**:
~~~~~~~~~~~~~
This module offers two main classes:
1. **`OpenAIEmbeddings`**:
   - For standard OpenAI API integration.
2. **`AzureOpenAIEmbeddings`**:
   - For embedding services hosted on Azure's OpenAI deployment.

Additionally, the module defines:
- **`BaseOpenAIEmbeddings`**:
  - A reusable base class with common functionality for OpenAI embeddings.
- Utility functions like `split_text_by_chunk_size` to handle tokenization and chunking of large text.

---

**Classes**:
~~~~~~~~~~~~

### **`BaseOpenAIEmbeddings`**

**Purpose**:
A base class for embedding models using OpenAI's API. This class provides reusable components for making API requests, handling retries, and chunking text for models with context limits.

**Key Attributes**:
- `api_key`: OpenAI API key (required).
- `timeout`: Request timeout (optional).
- `max_retries`: Maximum retry attempts for API requests (optional).
- `dimensions`: Desired embedding dimensions for specific models.
- `context_length`: Maximum context length for chunking text.

**Key Methods**:
- `prepare_client`: Abstract method to initialize the OpenAI client.
- `openai_response`: Abstract method to retrieve the response from OpenAI's API.
- `invoke`: Processes input text/documents, manages chunking, and retrieves embeddings.
- `ainvoke`: Async version of `invoke`.

---

### **`OpenAIEmbeddings`**

**Purpose**:
A concrete implementation of `BaseOpenAIEmbeddings` for OpenAI's standard embedding API.

**Key Attributes**:
- `model`: OpenAI model ID (e.g., `"text-embedding-ada-002"`) (required).
- `base_url`: Custom base URL for OpenAI API (optional).
- `organization`: OpenAI organization ID (optional).

**Key Methods**:
- `prepare_client`: Sets up the OpenAI client with necessary parameters.
- `openai_response`: Handles API requests and manages retries.

---

### **`AzureOpenAIEmbeddings`**

**Purpose**:
A concrete implementation of `BaseOpenAIEmbeddings` for Azure-hosted OpenAI models.

**Key Attributes**:
- `azure_endpoint`: HTTPS endpoint for the Azure OpenAI model (required).
- `azure_deployment`: Deployment name in Azure (required).
- `api_version`: Version of the Azure OpenAI model (required).
- `azure_ad_token`: Azure Active Directory token (optional).
- `azure_ad_token_provider`: Provider for generating Azure AD tokens (optional).

**Key Methods**:
- `prepare_client`: Sets up the Azure OpenAI client with required parameters.
- `openai_response`: Manages API requests and retries for Azure OpenAI.

---

**Utilities**:
~~~~~~~~~~~~~
### **`split_text_by_chunk_size`**

**Purpose**:
Splits input text into chunks of a specified size based on tokenization. Useful for handling models with limited context length.

**Parameters**:
- `text`: The input text to split.
- `chunk_size`: Maximum size of each chunk (in tokens).

**Returns**:
- A list of tokenized text chunks.

---

**Code Walkthrough**:
~~~~~~~~~~~~~~~~~~~~~

Below is the complete source code for the `openai.py` module.

.. code-block:: python

    from itertools import islice
    from typing import Optional

    import numpy as np
    import openai
    import tiktoken
    from tenacity import (
        retry,
        retry_if_not_exception_type,
        stop_after_attempt,
        wait_random_exponential,
    )
    from theflow.utils.modules import import_dotted_string

    from kotaemon.base import Param

    from .base import BaseEmbeddings, Document, DocumentWithEmbedding


    def split_text_by_chunk_size(text: str, chunk_size: int) -> list[list[int]]:
        """Split the text into chunks of a given size

        Args:
            text: text to split
            chunk_size: size of each chunk

        Returns:
            list of chunks (as tokens)
        """
        encoding = tiktoken.get_encoding("cl100k_base")
        tokens = iter(encoding.encode(text))
        result = []
        while chunk := list(islice(tokens, chunk_size)):
            result.append(chunk)
        return result


    class BaseOpenAIEmbeddings(BaseEmbeddings):
        """Base interface for OpenAI embedding model, using the openai library.

        This class exposes the parameters in resources.Chat. To subclass this class:

            - Implement the `prepare_client` method to return the OpenAI client
            - Implement the `openai_response` method to return the OpenAI response
            - Implement the params relate to the OpenAI client
        """
        # Remaining code omitted for brevity
