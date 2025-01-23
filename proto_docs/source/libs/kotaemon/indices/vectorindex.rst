Vector Indexing
=============================

The `vectorindex` module provides functionalities for creating and querying vector indices. It supports embedding-based document storage and retrieval with optional question-answering capabilities.

Classes
-------

1. **VectorIndexing**
   Handles document ingestion, embedding generation, and storage.

   **Attributes**:
   - `cache_dir`: Directory for storing cached document chunks.
   - `vector_store`: Storage for vector embeddings.
   - `doc_store`: Optional storage for documents.
   - `embedding`: Embedding generation component.

   **Methods**:
   - `to_retrieval_pipeline`: Converts the indexing pipeline into a retrieval pipeline.
   - `write_chunk_to_file`: Caches document chunks as markdown files.
   - `add_to_docstore`: Adds documents to a document store.
   - `add_to_vectorstore`: Embeds documents and stores them in a vector store.
   - `run`: Processes input data, generates embeddings, and stores them.

   **Source Code**:
   .. code-block:: python

      [`VectorIndexing` code here]

2. **VectorRetrieval**
   Retrieves documents from the vector and document stores based on input queries.

   **Attributes**:
   - `vector_store`: Handles embedding-based querying.
   - `doc_store`: Optional document store for textual queries.
   - `embedding`: Component for generating embeddings.
   - `rerankers`: Sequence of reranking components for refining results.
   - `retrieval_mode`: Defines the mode of retrieval: `vector`, `text`, or `hybrid`.

   **Methods**:
   - `run`: Retrieves documents based on the query, mode, and additional parameters.

   **Source Code**:
   .. code-block:: python

      [`VectorRetrieval` code here]

3. **TextVectorQA**
   Combines retrieval and question-answering into a single pipeline.

   **Attributes**:
   - `retrieving_pipeline`: Handles document retrieval.
   - `qa_pipeline`: Processes questions and retrieved documents.

   **Methods**:
   - `run`: Retrieves documents and processes the question with the QA pipeline.

   **Source Code**:
   .. code-block:: python

      [`TextVectorQA` code here]
