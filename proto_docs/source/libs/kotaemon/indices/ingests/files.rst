Files Module
============

The `files` module provides functionality to ingest and process files into a structured `Document` format suitable for indexing and further processing. This module supports various file formats, implements multiple document parsers, and integrates text splitting utilities for managing large files.

Classes
-------

### `DocumentIngestor`

The `DocumentIngestor` class is a core component for ingesting and processing files into `Document` objects. It supports multiple file types and extraction methods.

**Supported Document Types:**

- PDF
- Excel (`xlsx`, `xls`)
- Word (`docx`, `doc`)
- Text (`txt`, `md`)

**Arguments:**

- `pdf_mode`: The mode for PDF extraction. Options include:
  - `normal`: Parse PDF text.
  - `mathpix`: Parse PDF text using Mathpix.
  - `ocr`: Parse PDF images using OCR tools.
  - `multimodal`: Use AdobeReader for multimodal PDF parsing.
- `doc_parsers`: A list of document parsers (`BaseDocParser`) for additional parsing and metadata extraction.
- `text_splitter`: A splitter for dividing the document into manageable text nodes.
- `override_file_extractors`: A dictionary of custom file extractors for specific file extensions.

**Methods:**

- `run(file_paths: list[str | Path] | str | Path) -> list[Document]`:
  Ingests the provided file paths into a list of `Document` objects. This method reads files, extracts their content using appropriate readers, and splits the text into manageable nodes.

- `_get_reader(input_files: list[str | Path]) -> DirectoryReader`:
  Determines the appropriate readers for the input files based on their file extensions and the `pdf_mode`.

### Explanation of the Code

The `DocumentIngestor` class has the following key functionalities:

#### 1. **File Reading**

The `_get_reader` method determines the appropriate reader for each file type based on its extension. It uses the `KH_DEFAULT_FILE_EXTRACTORS` dictionary to map file extensions to their respective readers. The `pdf_mode` determines how PDF files are processed, offering modes such as `normal`, `ocr`, `mathpix`, or `multimodal`.

#### 2. **Document Parsing**

The `run` method processes input files and converts them into `Document` objects. These objects represent the extracted content from the files. The process includes:
- Reading files using the `_get_reader` method.
- Splitting the extracted text into smaller nodes using the `text_splitter`.
- Applying document parsers (if any) to process the nodes further.

#### 3. **Customizability**

The `DocumentIngestor` allows customization through:
- `doc_parsers` for additional processing of the extracted nodes.
- `override_file_extractors` to replace default readers with custom implementations.

### Code Example

Here's an example usage of the `DocumentIngestor` class:

```python
    from pathlib import Path
    from kotaemon.indices.ingests.files import DocumentIngestor

    ingestor = DocumentIngestor(pdf_mode="ocr")
    documents = ingestor.run(file_paths=["sample.pdf", "document.docx"])
    print(f"Processed {len(documents)} documents.")
