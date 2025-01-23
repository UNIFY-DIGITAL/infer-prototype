Langchain-Based Embeddings
==========================

The `kotaemon.embeddings.langchain_based` module provides a collection of classes that act as wrappers for various Langchain embedding models. These classes standardize the usage of embedding APIs (e.g., OpenAI, Azure OpenAI, Cohere, HuggingFace, Google GenAI) and offer integration with the `kotaemon` framework.

---

**Overview**:
~~~~~~~~~~~~~
This module introduces mixins and specific implementations for Langchain-based embedding models. It is designed to simplify the integration and customization of embeddings while exposing key parameters for each model.

---

**Classes**:
~~~~~~~~~~~~

### **`LCEmbeddingMixin`**

**Purpose**:
A base mixin class for integrating Langchain embeddings into the `kotaemon` framework.

**Key Methods**:
1. **`_get_lc_class`**:
   - Abstract method that must be implemented by subclasses to return the relevant Langchain embedding class.
2. **`run`**:
   - Processes input data, generates embeddings, and returns `DocumentWithEmbedding` instances.
3. **`dump`**:
   - Serializes the embedding class configuration for reproducibility.
4. **`specs`**:
   - Provides specifications for class parameters.

---

### **`LCOpenAIEmbeddings`**

**Purpose**:
Wrapper for Langchain's OpenAI embedding models.

**Attributes**:
- `model`: Specifies the OpenAI model name (default: `"text-embedding-ada-002"`).
- `openai_api_key`: OpenAI API key (required for authentication).
- `request_timeout`: Timeout for API requests (optional).

---

### **`LCAzureOpenAIEmbeddings`**

**Purpose**:
Wrapper for Langchain's Azure OpenAI embedding models.

**Attributes**:
- `azure_endpoint`: Endpoint for Azure OpenAI API.
- `deployment`: Deployment name for the model in Azure.
- `api_version`: Version of the Azure OpenAI API.

---

### **`LCCohereEmbeddings`**

**Purpose**:
Wrapper for Langchain's Cohere embedding models.

**Attributes**:
- `cohere_api_key`: API key for Cohere (required).
- `model`: Model name to use for embeddings (default: `"embed-english-v2.0"`).

---

### **`LCHuggingFaceEmbeddings`**

**Purpose**:
Wrapper for Langchain's HuggingFace embedding models.

**Attributes**:
- `model_name`: Model name from HuggingFace (default: `"sentence-transformers/all-mpnet-base-v2"`).

---

### **`LCGoogleEmbeddings`**

**Purpose**:
Wrapper for Langchain's Google GenAI embedding models.

**Attributes**:
- `google_api_key`: API key for Google AI Studio.
- `model`: Model name to use (default: `"models/text-embedding-004"`).

---

**Code Walkthrough**:
~~~~~~~~~~~~~~~~~~~~~

Below is the complete source code for the `langchain_based.py` module.

.. code-block:: python

    from typing import Optional

    from kotaemon.base import DocumentWithEmbedding, Param

    from .base import BaseEmbeddings


    class LCEmbeddingMixin:
        def _get_lc_class(self):
            raise NotImplementedError(
                "Please return the relevant Langchain class in in _get_lc_class"
            )

        def __init__(self, **params):
            self._lc_class = self._get_lc_class()
            self._obj = self._lc_class(**params)
            self._kwargs: dict = params

            super().__init__()

        def run(self, text):
            input_docs = self.prepare_input(text)
            input_ = [doc.text for doc in input_docs]

            embeddings = self._obj.embed_documents(input_)

            return [
                DocumentWithEmbedding(content=doc, embedding=each_embedding)
                for doc, each_embedding in zip(input_docs, embeddings)
            ]

        def __repr__(self):
            kwargs = []
            for key, value_obj in self._kwargs.items():
                value = repr(value_obj)
                kwargs.append(f"{key}={value}")
            kwargs_repr = ", ".join(kwargs)
            return f"{self.__class__.__name__}({kwargs_repr})"

        def __str__(self):
            kwargs = []
            for key, value_obj in self._kwargs.items():
                value = str(value_obj)
                if len(value) > 20:
                    value = f"{value[:15]}..."
                kwargs.append(f"{key}={value}")
            kwargs_repr = ", ".join(kwargs)
            return f"{self.__class__.__name__}({kwargs_repr})"

        def __setattr__(self, name, value):
            if name == "_lc_class":
                return super().__setattr__(name, value)

            if name in self._lc_class.__fields__:
                self._kwargs[name] = value
                self._obj = self._lc_class(**self._kwargs)
            else:
                super().__setattr__(name, value)

        def __getattr__(self, name):
            if name in self._kwargs:
                return self._kwargs[name]
            return getattr(self._obj, name)

        def dump(self, *args, **kwargs):
            from theflow.utils.modules import serialize

            params = {key: serialize(value) for key, value in self._kwargs.items()}
            return {
                "__type__": f"{self.__module__}.{self.__class__.__qualname__}",
                **params,
            }

        def specs(self, path: str):
            path = path.strip(".")
            if "." in path:
                raise ValueError("path should not contain '.'")

            if path in self._lc_class.__fields__:
                return {
                    "__type__": "theflow.base.ParamAttr",
                    "refresh_on_set": True,
                    "strict_type": True,
                }

            raise ValueError(f"Invalid param {path}")

    # Remaining classes omitted for brevity
    ...
