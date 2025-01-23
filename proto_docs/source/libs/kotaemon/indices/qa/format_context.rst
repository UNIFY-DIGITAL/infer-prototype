.. _format_context:

`format_context`
=================

The `format_context` module provides functionality for preparing evidence text from retrieved documents. This step is typically performed after the document retrieval pipeline, structuring the evidence for downstream tasks like question answering.

Overview
--------

This module includes:
- Constants for evidence modes to classify content (text, table, chatbot, figure).
- A pipeline class to process retrieved documents and prepare the evidence text, tables, figures, and other associated metadata.

Constants
---------

- **EVIDENCE_MODE_TEXT (0)**: Text-based evidence.
- **EVIDENCE_MODE_TABLE (1)**: Table-based evidence.
- **EVIDENCE_MODE_CHATBOT (2)**: Chatbot scenario evidence.
- **EVIDENCE_MODE_FIGURE (3)**: Figure/image-based evidence.

Classes
-------

### `PrepareEvidencePipeline`

#### Description
The `PrepareEvidencePipeline` processes a list of retrieved documents and structures the evidence text for further use. It handles:
- Text content.
- Tables.
- Figures/images.
- Chatbot scenarios.

#### Key Attributes:
- **`max_context_length`**: Maximum allowed context length (default: 32,000 tokens).
- **`trim_func`**: Optional callback or `TokenSplitter` instance to split long content into smaller chunks.

#### Key Method:
- **`run(docs: list[RetrievedDocument]) -> Document`**:
  Processes a list of `RetrievedDocument` objects and returns a `Document` object containing:
  - Evidence mode.
  - Processed evidence text.
  - List of associated images.

Example Usage
-------------

```python
from format_context import PrepareEvidencePipeline
from kotaemon.base import RetrievedDocument

# Instantiate the pipeline
pipeline = PrepareEvidencePipeline(max_context_length=2000)

# Mock retrieved documents
retrieved_docs = [
    RetrievedDocument(text="This is a sample text.", metadata={"file_name": "doc1.txt"}),
    RetrievedDocument(text="Table content here.", metadata={"type": "table", "file_name": "doc2.pdf"}),
]

# Run the pipeline
output_document = pipeline.run(retrieved_docs)

print(output_document.content)  # Outputs (evidence_mode, processed evidence, images)
