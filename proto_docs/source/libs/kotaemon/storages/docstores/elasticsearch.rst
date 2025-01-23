.. _kotaemon_storages_docstores_elasticsearch:

Elasticsearch Document Store
============================

This module implements the `ElasticsearchDocumentStore` class, which leverages Elasticsearch as a backend for storing and querying documents using the BM25 similarity algorithm.

Class Overview
--------------

`ElasticsearchDocumentStore`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: ElasticsearchDocumentStore
   :members:
   :undoc-members:
   :show-inheritance:

Details
-------

The `ElasticsearchDocumentStore` class provides methods for managing and querying documents stored in an Elasticsearch instance.

**Initialization**:
- Creates an Elasticsearch client.
- Configures a custom BM25 similarity algorithm.
- Initializes an index with specific settings and mappings.

**Attributes**:
- `collection_name`: The name of the Elasticsearch index. Default is `"docstore"`.
- `elasticsearch_url`: The URL of the Elasticsearch server. Default is `"http://localhost:9200"`.
- `k1`: BM25 parameter controlling term frequency saturation.
- `b`: BM25 parameter controlling document length normalization.

**Methods**:
- **`add(docs, ids=None, refresh_indices=True, **kwargs)`**:
  - Adds or updates documents in the index.
  - Refreshes the index by default.
- **`query(query, top_k=10, doc_ids=None)`**:
  - Executes a search query using the BM25 algorithm.
  - Returns a list of top-ranked documents.
- **`query_raw(query)`**:
  - Executes a raw Elasticsearch query.
- **`get(ids)`**:
  - Retrieves documents by their IDs.
- **`get_all()`**:
  - Fetches all documents from the index.
- **`count()`**:
  - Returns the total number of documents in the index.
- **`delete(ids)`**:
  - Deletes documents by their IDs.
- **`drop()`**:
  - Deletes the entire index.

**Usage Workflow**:
1. Initialize the `ElasticsearchDocumentStore` with the required parameters.
2. Use `add` to store documents.
3. Query documents using `query` or `query_raw`.
4. Manage documents with methods like `get`, `delete`, and `drop`.

**Example**:
```python
from kotaemon.storages.docstores.elasticsearch import ElasticsearchDocumentStore
from kotaemon.base import Document

docstore = ElasticsearchDocumentStore(collection_name="my_docs")
doc1 = Document(text="This is a sample document", metadata={"author": "Alice"})
doc2 = Document(text="Another document example", metadata={"author": "Bob"})

# Add documents
docstore.add([doc1, doc2])

# Query documents
results = docstore.query("sample", top_k=2)
for doc in results:
    print(doc.text, doc.metadata)

# Get document count
print("Total documents:", docstore.count())

# Drop the document store
docstore.drop()
