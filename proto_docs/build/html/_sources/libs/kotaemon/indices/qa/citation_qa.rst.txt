.. _citation_qa:

`citation_qa`
=============

The `citation_qa` module provides a pipeline for answering questions with evidence-based context, generating citations, and preparing results for display on a user interface.

Overview
--------

This module enables detailed QA workflows, including:
- **Evidence-based Answering**: Leverages retrieved evidence to answer questions in various formats like text, tables, and multimodal contexts.
- **Citation Generation**: Links answers to evidence sources for transparency.
- **UI Preparation**: Formats citations and documents for display with highlights.

Classes
-------

### `AnswerWithContextPipeline`

.. autoclass:: AnswerWithContextPipeline
   :members:
   :undoc-members:
   :show-inheritance:

The `AnswerWithContextPipeline` class manages evidence-based QA with citations and supports the following:
- **`run`**: Executes the QA process.
- **`invoke`**: Generates answers using provided evidence and question.
- **`stream`**: Streams the answer generation process for real-time interaction.
- **`prepare_citations`**: Prepares cited and uncited documents for display.

Constants
---------

- **`DEFAULT_QA_TEXT_PROMPT`**: Default text-based QA prompt.
- **`DEFAULT_QA_TABLE_PROMPT`**: Table-focused QA prompt.
- **`DEFAULT_QA_CHATBOT_PROMPT`**: Chatbot scenario QA prompt.
- **`DEFAULT_QA_FIGURE_PROMPT`**: Multimodal QA prompt for figures.
- **`CITATION_TIMEOUT`**: Timeout for citation generation threads.
- **`CONTEXT_RELEVANT_WARNING_SCORE`**: Threshold for relevant document scores.

Features
--------

### Evidence Processing

1. **`get_prompt`**:
   Prepares prompts for different evidence modes:
   - **Text**: Default evidence mode.
   - **Table**: For tabular data.
   - **Figures**: For multimodal contexts.
   - **Chatbot**: For pre-defined scenarios.

2. **`match_evidence_with_context`**:
   Matches cited evidence with the context provided, identifying relevant spans in documents.

3. **`prepare_citations`**:
   Separates documents into those with and without citations, formatting them for UI display.

### Multimodal Support

- Handles textual, tabular, and visual evidence.
- Supports threaded operations for citation generation and mindmap creation.

Source Code
-----------

Below is the full source code of the module:

.. code-block:: python

   import threading
   from collections import defaultdict
   from typing import Generator

   import numpy as np
   from theflow.settings import settings as flowsettings

   from kotaemon.base import (
       AIMessage,
       BaseComponent,
       Document,
       HumanMessage,
       Node,
       SystemMessage,
   )
   from kotaemon.llms import ChatLLM, PromptTemplate

   from .citation import CitationPipeline
   from .format_context import (
       EVIDENCE_MODE_FIGURE,
       EVIDENCE_MODE_TABLE,
       EVIDENCE_MODE_TEXT,
   )
   from .utils import find_text

   ...

   class AnswerWithContextPipeline(BaseComponent):
       """Answer the question based on the evidence"""

       llm: ChatLLM = Node(default_callback=lambda _: llms.get_default())
       vlm_endpoint: str = getattr(flowsettings, "KH_VLM_ENDPOINT", "")
       ...

       def get_prompt(self, question, evidence, evidence_mode: int):
           """Prepare the prompt and other information for LLM"""
           ...

       def run(
           self, question: str, evidence: str, evidence_mode: int = 0, **kwargs
       ) -> Document:
           ...

       def prepare_citations(self, answer, docs) -> tuple[list[Document], list[Document]]:
           """Prepare the citations to show on the UI"""
           ...
