Base Module
====================

The `base.py` module in the `indices` package provides abstract classes and mixins to define the foundation for indexing and retrieval pipelines. It also offers a framework for document transformation, enabling flexible operations on documents.

Purpose
-------
This module ensures consistency across all indexing and retrieval components in the `kotaemon.indices` package. It establishes:
- A shared interface for indexing and retrieval pipelines.
- Reusable components for document transformation.
- Integration with external libraries like `LlamaIndex`.

Classes and Mixins
------------------

### DocTransformer
A base class for document transformers that process and transform lists of documents.

- **Key Method**:
  - `run(documents: list[Document]) -> list[Document]`: Abstract method to implement the transformation logic.

- **Common Use Cases**:
  - Splitting large documents into chunks.
  - Adding metadata to documents.
  - Reducing a list of documents to a smaller subset.

---

### LlamaIndexDocTransformerMixin
A mixin for wrapping `LlamaIndex` components into `kotaemon` components.

- **Usage**:
  - Use this as the first parent class when defining subclasses.
  - Implement `_get_li_class` to specify the `LlamaIndex` component.

- **Key Methods**:
  - `run`: Processes documents using the specified `LlamaIndex` component.
  - `_get_li_class`: Returns the `LlamaIndex` class to be wrapped.

- **Example**:
  ```python
  class TokenSplitter(LlamaIndexDocTransformerMixin, DocTransformer):
      def _get_li_class(self):
          from llama_index.core.text_splitter import TokenTextSplitter
          return TokenTextSplitter
