.. _linear:

===========================
Linear Pipelines
===========================

The `linear.py` module provides implementations for linear pipelines that interact with prompts, language models, and optional post-processors. These pipelines enable sequential processing and include gated mechanisms to conditionally control execution.

Classes
=======

SimpleLinearPipeline
--------------------

**Description:**
A simple pipeline for executing a function with a prompt, a language model, and an optional post-processor.

**Attributes:**
- `prompt (BasePromptComponent)`: Generates the initial input.
- `llm (Union[ChatLLM, LLM])`: Language model component used for output generation.
- `post_processor (Union[BaseComponent, Callable[[IO_Type], IO_Type]])`: Optional post-processor.

**Methods:**
- `run`: Executes the pipeline with the given arguments and returns the final output as a `Document` object.
  - **Arguments:**
    - `llm_kwargs (dict)`: Additional arguments for the language model call.
    - `post_processor_kwargs (dict)`: Additional arguments for the post-processor.
    - `**prompt_kwargs`: Arguments for populating the prompt.
  - **Returns:**
    - `Document`: The output of the pipeline as a `Document` object.

**Example Usage:**

.. code-block:: python

   from kotaemon.llms import LCAzureChatOpenAI, BasePromptComponent

   def identity(x):
       return x

   llm = LCAzureChatOpenAI(
       openai_api_base="your openai api base",
       openai_api_key="your openai api key",
       openai_api_version="your openai api version",
       deployment_name="dummy-q2-gpt35",
       temperature=0,
       request_timeout=600,
   )

   pipeline = SimpleLinearPipeline(
       prompt=BasePromptComponent(template="what is {word} in Japanese ?"),
       llm=llm,
       post_processor=identity,
   )
   print(pipeline(word="lone"))

GatedLinearPipeline
-------------------

**Description:**
Extends SimpleLinearPipeline by adding a `condition` attribute to control pipeline execution.

**Attributes:**
- `condition (Callable[[IO_Type], Any])`: Represents the condition for pipeline execution.
- Inherits all attributes of SimpleLinearPipeline.

**Methods:**
- `run`: Executes the pipeline conditionally based on the `condition_text`.
  - **Arguments:**
    - `condition_text (str)`: The condition text to evaluate.
    - `llm_kwargs (dict)`: Additional arguments for the language model call.
    - `post_processor_kwargs (dict)`: Additional arguments for the post-processor.
    - `**prompt_kwargs`: Arguments for populating the prompt.
  - **Returns:**
    - `Document`: The output of the pipeline as a `Document` object if the condition is satisfied.
  - **Raises:**
    - `ValueError` if `condition_text` is not provided.

**Example Usage:**

.. code-block:: python

   from kotaemon.llms import LCAzureChatOpenAI, BasePromptComponent
   from kotaemon.parsers import RegexExtractor

   def identity(x):
       return x

   llm = LCAzureChatOpenAI(
       openai_api_base="your openai api base",
       openai_api_key="your openai api key",
       openai_api_version="your openai api version",
       deployment_name="dummy-q2-gpt35",
       temperature=0,
       request_timeout=600,
   )

   pipeline = GatedLinearPipeline(
       prompt=BasePromptComponent(template="what is {word} in Japanese ?"),
       condition=RegexExtractor(pattern="some pattern"),
       llm=llm,
       post_processor=identity,
   )
   print(pipeline(condition_text="some pattern", word="lone"))
   print(pipeline(condition_text="other pattern", word="lone"))

Source Code
===========

SimpleLinearPipeline
--------------------

.. code-block:: python

   from typing import Any, Callable, Optional, Union

   from ..base import BaseComponent
   from ..base.schema import Document, IO_Type
   from .chats import ChatLLM
   from .completions import LLM
   from .prompts import BasePromptComponent

   class SimpleLinearPipeline(BaseComponent):
       """
       A simple pipeline for running a function with a prompt, a language model, and an optional post-processor.
       """
       prompt: BasePromptComponent
       llm: Union[ChatLLM, LLM]
       post_processor: Union[BaseComponent, Callable[[IO_Type], IO_Type]]

       def run(
           self,
           *,
           llm_kwargs: Optional[dict] = {},
           post_processor_kwargs: Optional[dict] = {},
           **prompt_kwargs,
       ):
           ...

GatedLinearPipeline
-------------------

.. code-block:: python

   class GatedLinearPipeline(SimpleLinearPipeline):
       """
       A pipeline that extends the SimpleLinearPipeline class and adds a condition attribute.
       """
       condition: Callable[[IO_Type], Any]

       def run(
           self,
           *,
           condition_text: Optional[str] = None,
           llm_kwargs: Optional[dict] = {},
           post_processor_kwargs: Optional[dict] = {},
           **prompt_kwargs,
       ) -> Document:
           ...
