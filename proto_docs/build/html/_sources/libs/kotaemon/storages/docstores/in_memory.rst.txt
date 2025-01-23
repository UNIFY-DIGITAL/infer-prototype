.. _kotaemon_storages_docstores_in_memory:

In-Memory Document Store
========================

This module implements the `InMemoryDocumentStore` class, which provides a simple in-memory implementation of a document store using a Python dictionary.

Class Overview
--------------

`InMemoryDocumentStore`
~~~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: InMemoryDocumentStore
   :members:
   :undoc-members:
   :show-inheritance:

Details
-------

The `InMemoryDocumentStore` class offers a lightweight, in-memory storage for managing documents. It is useful for quick prototyping and testing without requiring a persistent storage backend.

**Methods**:
- **`add(docs, ids=None, **kwargs)`**:
  - Adds one or more documents to the in-memory store.
  - **Parameters**:
    - `docs`: A single `Document` or a list of `Document` objects to add.
    - `ids`: Optional list or single ID for the documents. Defaults to `doc.doc_id`.
    - `exist_ok`: Boolean to allow overwriting existing documents with the same ID (default is `False`).
  - Raises `ValueError` if a document with the same ID already exists and `exist_ok` is `False`.
- **`get(ids)`**:
  - Retrieves documents by their IDs.
  - **Parameters**:
    - `ids`: A single ID or a list of IDs for the documents to retrieve.
  - **Returns**: A list of `Document` objects.
- **`get_all()`**:
  - Fetches all documents in the store.
  - **Returns**: A list of all `Document` objects.
- **`count()`**:
  - Counts the number of documents in the store.
  - **Returns**: The total count of documents.
- **`delete(ids)`**:
  - Deletes documents by their IDs.
- **`save(path)`**:
  - Saves the document store to a file in JSON format.
  - **Parameters**:
    - `path`: Path to the file where the store will be saved.
- **`load(path)`**:
  - Loads the document store from a file in JSON format.
  - **Parameters**:
    - `path`: Path to the file from which the store will be loaded.
  - **Note**: This method may lose information for subclasses of `Document`.
- **`query(query, top_k=10, doc_ids=None)`**:
  - Performs a full-text search on the document store. Currently, it returns an empty list as full-text search is not implemented.
- **`drop()`**:
  - Clears all documents from the store.

**Usage Workflow**:
1. Initialize the `InMemoryDocumentStore`.
2. Use `add` to store documents.
3. Retrieve documents with `get` or `get_all`.
4. Save or load the document store with `save` and `load`.

**Example**:
```python
from kotaemon.storages.docstores.in_memory import InMemoryDocumentStore
from kotaemon.base import Document

docstore = InMemoryDocumentStore()
doc1 = Document(text="This is a sample document", metadata={"author": "Alice"})
doc2 = Document(text="Another example document", metadata={"author": "Bob"})

# Add documents
docstore.add([doc1, doc2])

# Retrieve a document
retrieved_docs = docstore.get([doc1.doc_id])
for doc in retrieved_docs:
    print(doc.text, doc.metadata)

# Count documents
print("Total documents:", docstore.count())

# Save the document store
docstore.save("store.json")

# Load the document store
docstore.load("store.json")

# Clear the store
docstore.drop()
