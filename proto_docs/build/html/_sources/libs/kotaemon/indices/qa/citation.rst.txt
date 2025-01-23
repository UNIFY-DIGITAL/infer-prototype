.. _citation:

`citation`
==========

The `citation` module provides functionality for extracting precise citations from a given context, ensuring sourced and evidence-backed answers to user queries.

Overview
--------

This module features:
- **CitationPipeline**: A component that extracts cited evidence from provided context and questions.
- **CiteEvidence**: A data model defining the structure of cited evidence.

Classes
-------

### `CiteEvidence`

.. autoclass:: citation.CiteEvidence
   :members:
   :undoc-members:
   :show-inheritance:

This class defines a schema for extracted evidence, ensuring:
- **evidences**: A list of direct quotes (up to 5), each limited to a maximum of 15 words and drawn directly from the original context.

### `CitationPipeline`

.. autoclass:: citation.CitationPipeline
   :members:
   :undoc-members:
   :show-inheritance:

#### Key Methods:
- **`run`**: Executes the citation pipeline for a given context and question.
- **`prepare_llm`**: Prepares input messages and configurations for the LLM.
- **`invoke`**: Calls the LLM to process the question and context, returning extracted citations.
- **`ainvoke`**: (Not implemented) Placeholder for asynchronous invocation.

Features
--------

### Citation Workflow

1. **Prepare LLM Input**:
   The `prepare_llm` method structures input messages and settings:
   - Context and question are included.
   - A schema for cited evidence (`CiteEvidence`) is enforced.

2. **Invoke LLM**:
   The `invoke` method sends prepared messages to the specified LLM, processing the response to extract citations:
   - The LLM responds with citations using the `CiteEvidence` function.
   - Outputs are parsed into structured data for further use.

3. **Error Handling**:
   If the LLM fails or returns invalid responses, errors are caught, and the process terminates gracefully.

Example
-------

```python
from citation import CitationPipeline

# Instantiate pipeline with an LLM
pipeline = CitationPipeline(llm=your_llm_instance)

# Run the pipeline
context = "The Earth revolves around the Sun. The Moon orbits the Earth."
question = "What does the Earth do?"
result = pipeline.run(context, question)

if result:
    print(result.evidences)  # Output: ["The Earth revolves around the Sun."]
