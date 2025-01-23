.. _kotaemon_storages_docstores_lancedb:

LanceDB Document Store
======================

This module implements the `LanceDBDocumentStore` class, which uses LanceDB for document storage and supports full-text search (FTS).

Class Overview
--------------

`LanceDBDocumentStore`
~~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: LanceDBDocumentStore
   :members:
   :undoc-members:
   :show-inheritance:

Details
-------

The `LanceDBDocumentStore` class provides methods for storing and querying documents in a LanceDB instance. It supports full-text search and efficient filtering.

**Initialization**:
- Connects to a LanceDB database using the provided `path`.
- Initializes a collection for storing documents.

**Attributes**:
- `path`: The database path. Default is `"lancedb"`.
- `collection_name`: The name of the document collection. Default is `"docstore"`.

**Methods**:
- **`add(docs, ids=None, refresh_indices=True, **kwargs)`**:
  - Adds or updates documents in the LanceDB collection.
  - **Parameters**:
    - `docs`: A single `Document` or a list of `Document` objects to add.
    - `ids`: Optional list or single ID for the documents. Defaults to `doc.doc_id`.
    - `refresh_indices`: Boolean to recreate the FTS index after adding documents.
- **`query(query, top_k=10, doc_ids=None)`**:
  - Executes a full-text search query.
  - **Parameters**:
    - `query`: A string representing the search query.
    - `top_k`: Number of top results to return. Default is `10`.
    - `doc_ids`: Optional list of document IDs to filter the search results.
  - **Returns**: A list of `Document` objects matching the query.
- **`get(ids)`**:
  - Retrieves documents by their IDs.
  - **Parameters**:
    - `ids`: A single ID or a list of IDs for the documents to retrieve.
  - **Returns**: A list of `Document` objects.
- **`delete(ids, refresh_indices=True)`**:
  - Deletes documents by their IDs.
  - **Parameters**:
    - `ids`: A single ID or a list of IDs for the documents to delete.
    - `refresh_indices`: Boolean to recreate the FTS index after deletion.
- **`drop()`**:
  - Deletes the entire collection.
- **`count()`**:
  - Not implemented.
- **`get_all()`**:
  - Not implemented.

**Usage Workflow**:
1. Initialize the `LanceDBDocumentStore` with the database path and collection name.
2. Use `add` to store documents.
3. Query documents using `query`.
4. Retrieve specific documents with `get`.
5. Manage documents with `delete` or drop the entire store with `drop`.

**Example**:
```python
from kotaemon.storages.docstores.lancedb import LanceDBDocumentStore
from kotaemon.base import Document

docstore = LanceDBDocumentStore(path="lancedb", collection_name="my_docs")
doc1 = Document(text="This is a sample document", metadata={"author": "Alice"})
doc2 = Document(text="Another example document", metadata={"author": "Bob"})

# Add documents
docstore.add([doc1, doc2])

# Query documents
results = docstore.query("sample", top_k=2)
for doc in results:
    print(doc.text, doc.metadata)

# Delete a document
docstore.delete([doc1.doc_id])

# Drop the document store
docstore.drop()
