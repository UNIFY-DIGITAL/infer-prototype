.. _kotaemon_storages_docstores_simple_file:

Simple File Document Store
==========================

This module implements the `SimpleFileDocumentStore` class, which extends the `InMemoryDocumentStore` by adding automatic saving to a JSON file whenever the document store is modified.

Class Overview
--------------

`SimpleFileDocumentStore`
~~~~~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: SimpleFileDocumentStore
   :members:
   :undoc-members:
   :show-inheritance:

Details
-------

The `SimpleFileDocumentStore` class stores documents in memory but persists changes to a JSON file automatically. It supports adding, retrieving, deleting, and dropping documents, with the state of the store saved to disk after each modification.

**Initialization**:
- Creates the directory and file for storing documents if they don't already exist.
- Loads the document store from the file if it exists.

**Attributes**:
- `path`: The directory path where the document file is stored.
- `collection_name`: The name of the document collection. Default is `"default"`.
- `_save_path`: The path to the JSON file used for saving the document store.

**Methods**:
- **`add(docs, ids=None, **kwargs)`**:
  - Adds one or more documents to the store and saves the changes to the file.
  - **Parameters**:
    - `docs`: A single `Document` or a list of `Document` objects to add.
    - `ids`: Optional list or single ID for the documents. Defaults to `doc.doc_id`.
    - `exist_ok`: Boolean to allow overwriting existing documents with the same ID (default is `False`).
  - Raises `ValueError` if a document with the same ID already exists and `exist_ok` is `False`.
- **`get(ids)`**:
  - Retrieves documents by their IDs.
  - Reloads the document store from the file if a requested document is not in memory.
  - **Parameters**:
    - `ids`: A single ID or a list of IDs for the documents to retrieve.
  - **Returns**: A list of `Document` objects.
- **`delete(ids)`**:
  - Deletes documents by their IDs and saves the changes to the file.
- **`drop()`**:
  - Clears all documents from the store and deletes the JSON file.
- **`__persist_flow__()`**:
  - Serializes the document store's state for persistence.

**Usage Workflow**:
1. Initialize the `SimpleFileDocumentStore` with a file path and collection name.
2. Use `add` to store documents.
3. Retrieve documents with `get`.
4. Manage documents with methods like `delete` or `drop`.

**Example**:
```python
from kotaemon.storages.docstores.simple_file import SimpleFileDocumentStore
from kotaemon.base import Document

# Initialize the document store
docstore = SimpleFileDocumentStore(path="data", collection_name="my_docs")

# Create documents
doc1 = Document(text="This is a sample document", metadata={"author": "Alice"})
doc2 = Document(text="Another example document", metadata={"author": "Bob"})

# Add documents
docstore.add([doc1, doc2])

# Retrieve a document
retrieved_docs = docstore.get([doc1.doc_id])
for doc in retrieved_docs:
    print(doc.text, doc.metadata)

# Delete a document
docstore.delete([doc1.doc_id])

# Drop the document store
docstore.drop()
