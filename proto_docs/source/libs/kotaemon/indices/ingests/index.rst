Ingests
==============

The `ingests` module provides functionality to ingest and process various types of data files into structured `Document` objects for further processing and indexing. This module is a critical part of the `kotaemon` framework and handles various file formats and ingestion strategies.

Submodules
----------

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   files

Overview
--------

The `ingests` module is designed to manage the ingestion process for multiple types of documents, including text, PDFs, Excel files, and more. It includes components for reading files, parsing content, and splitting documents into manageable chunks.

Features
--------

- **Multi-format Support:** Handles a variety of document formats, including PDFs, Excel files, and Word documents.
- **Customizable Parsers:** Allows the use of document parsers for additional metadata extraction and content processing.
- **Text Splitting:** Splits large documents into smaller nodes for easier processing and indexing.

Module Structure
----------------

- `files`: Contains the implementation of the `DocumentIngestor` class, which is the core component for file ingestion and processing.

