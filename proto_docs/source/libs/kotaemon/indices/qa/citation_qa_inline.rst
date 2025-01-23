.. _citation_qa_inline:

`citation_qa_inline`
====================

The `citation_qa_inline` module provides functionality for answering questions with detailed responses and inline citations, leveraging evidence from a provided context.

Features
--------

- Processes evidence and provides inline citations for answers.
- Supports detailed prompts for QA tasks with specific formats.
- Includes functionalities like evidence matching, citation linking, and multimodal input handling.

Classes
-------

### `InlineEvidence`

.. autoclass:: InlineEvidence
   :members:
   :undoc-members:
   :show-inheritance:

Represents a single piece of evidence supporting an answer, containing `start_phrase`, `end_phrase`, and an index.

### `AnswerWithInlineCitation`

.. autoclass:: AnswerWithInlineCitation
   :members:
   :undoc-members:
   :show-inheritance:

A pipeline for generating answers with inline citations based on evidence. It extends `AnswerWithContextPipeline` and provides:
- **`get_prompt`**: Prepares the prompt for LLM.
- **`answer_to_citations`**: Extracts inline citations from the LLM-generated answer.
- **`replace_citation_with_link`**: Replaces citations with clickable links in the answer.
- **`stream`**: Streams the generated answer, handling evidence and context in real-time.
- **`match_evidence_with_context`**: Matches evidence from the answer with the context.

Constants
---------

- **`DEFAULT_QA_CITATION_PROMPT`**: The default prompt template for QA tasks.
- **`START_ANSWER`, `START_CITATION`, `CITATION_PATTERN`**: Constants for processing QA outputs.

Source Code
-----------

Below is the complete source code for this module:

.. code-block:: python

   import re
   import threading
   from collections import defaultdict
   from dataclasses import dataclass
   from typing import Generator

   import numpy as np

   from kotaemon.base import AIMessage, Document, HumanMessage, SystemMessage
   from kotaemon.llms import PromptTemplate

   from .citation_qa import CITATION_TIMEOUT, MAX_IMAGES, AnswerWithContextPipeline
   from .format_context import EVIDENCE_MODE_FIGURE
   from .utils import find_start_end_phrase

   DEFAULT_QA_CITATION_PROMPT = """
   Use the following pieces of context to answer the question at the end.
   Provide DETAILED ansswer with clear explanation.
   ...
   QUESTION: {question}\n
   ANSWER:
   """  # noqa

   START_ANSWER = "FINAL ANSWER"
   START_CITATION = "CITATION LIST"
   CITATION_PATTERN = r"citation【(\d+)】"
   START_ANSWER_PATTERN = "start_phrase:"
   END_ANSWER_PATTERN = "end_phrase:"

   ...

   class InlineEvidence:
       """List of evidences to support the answer."""

       start_phrase: str | None = None
       end_phrase: str | None = None
       idx: int | None = None

   class AnswerWithInlineCitation(AnswerWithContextPipeline):
       """Answer the question based on the evidence with inline citation"""

       qa_citation_template: str = DEFAULT_QA_CITATION_PROMPT

       def get_prompt(self, question, evidence, evidence_mode: int):
           ...

       def answer_to_citations(self, answer) -> list[InlineEvidence]:
           ...

       def replace_citation_with_link(self, answer: str):
           ...

       def stream(self, question: str, evidence: str, evidence_mode: int = 0, images: list[str] = [], **kwargs):
           ...

       def match_evidence_with_context(self, answer, docs) -> dict[str, list[dict]]:
           ...
