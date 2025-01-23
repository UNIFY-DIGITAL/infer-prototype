.. _kotaemon_llms_rerankings_base:

Base Reranking Module
=====================

This module defines the `BaseReranking` class, which serves as the foundation for all reranking implementations.

Class Overview
--------------

`BaseReranking`
~~~~~~~~~~~~~~~
.. autoclass:: BaseReranking
   :members:
   :undoc-members:
   :show-inheritance:

Details
-------

The `BaseReranking` class provides an abstract method `run`, which must be implemented by subclasses to apply reranking or filtering logic to a list of documents.

**Methods**:
- **`run(documents, query)`**:
  - **Abstract Method**: Must be implemented in subclasses.
  - **Parameters**:
    - `documents`: A list of `Document` objects to process.
    - `query`: A string representing the user's query.
  - **Returns**: A list of `Document` objects after reranking or filtering.

**Usage**:
Subclasses of `BaseReranking` should override the `run` method to define specific reranking or filtering logic.

**Example**:
```python
class CustomReranking(BaseReranking):
    def run(self, documents: list[Document], query: str) -> list[Document]:
        # Custom reranking logic here
        return sorted(documents, key=lambda doc: len(doc.text))
