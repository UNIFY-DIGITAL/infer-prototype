Splitters
=========

The `splitters` module provides components for splitting and processing textual data into manageable chunks. These classes are useful for preprocessing large documents, enabling efficient indexing and analysis within the `kotaemon` pipeline.

Classes
-------

.. autoclass:: BaseSplitter
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: TokenSplitter
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: SentenceWindowSplitter
   :members:
   :undoc-members:
   :show-inheritance:

---

**Module Overview**

- **`BaseSplitter`**  
  A base class for all splitter components. It provides an abstract foundation for document splitting mechanisms.

- **`TokenSplitter`**  
  Splits text into smaller chunks based on token size, allowing overlap for context retention.  
  - **Parameters**:
    - `chunk_size` (int): Maximum size of each chunk in tokens.
    - `chunk_overlap` (int): Number of overlapping tokens between consecutive chunks.
    - `separator` (str): Separator used for splitting (e.g., whitespace).

  **Example Usage**:
  ```python
  splitter = TokenSplitter(chunk_size=512, chunk_overlap=128, separator="\n")
  chunks = splitter.run(documents)
