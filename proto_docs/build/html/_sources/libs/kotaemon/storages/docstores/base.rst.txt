.. _kotaemon_storages_docstores_base:

Base Document Store Module
==========================

This module defines the `BaseDocumentStore` abstract base class, which provides a blueprint for implementing various document stores.

Class Overview
--------------

`BaseDocumentStore`
~~~~~~~~~~~~~~~~~~~
.. autoclass:: BaseDocumentStore
   :members:
   :undoc-members:
   :show-inheritance:

Details
-------

The `BaseDocumentStore` class serves as a blueprint for creating document stores that can store, manage, and query documents.

**Methods**:
- **`add(docs, ids=None, **kwargs)`**:
  - **Description**: Adds one or more documents to the document store.
  - **Parameters**:
    - `docs`: A single `Document` or a list of `Document` objects to add.
    - `ids`: Optional list or single ID corresponding to the documents. Defaults to `doc.doc_id`.
- **`get(ids)`**:
  - **Description**: Retrieves documents by their IDs.
  - **Parameters**:
    - `ids`: A single ID or a list of IDs for the documents to retrieve.
  - **Returns**: A list of `Document` objects.
- **`get_all()`**:
  - **Description**: Retrieves all documents in the document store.
  - **Returns**: A list of all `Document` objects.
- **`count()`**:
  - **Description**: Counts the number of documents in the store.
  - **Returns**: The total count of documents.
- **`query(query, top_k=10, doc_ids=None)`**:
  - **Description**: Searches the document store using a query string.
  - **Parameters**:
    - `query`: A string representing the search query.
    - `top_k`: Number of top results to return. Defaults to `10`.
    - `doc_ids`: Optional list of document IDs to restrict the search to.
  - **Returns**: A list of `Document` objects matching the query.
- **`delete(ids)`**:
  - **Description**: Deletes documents by their IDs.
  - **Parameters**:
    - `ids`: A single ID or a list of IDs for the documents to delete.
- **`drop()`**:
  - **Description**: Drops the entire document store, removing all documents.

**Usage**:
Subclasses of `BaseDocumentStore` must implement all abstract methods to provide concrete functionality.

**Example**:
```python
class MyDocumentStore(BaseDocumentStore):
    def __init__(self):
        self.store = {}

    def add(self, docs, ids=None, **kwargs):
        # Implementation for adding documents

    # Implement other abstract methods...
