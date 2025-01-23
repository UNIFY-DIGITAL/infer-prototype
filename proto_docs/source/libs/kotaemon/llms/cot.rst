.. _llms_cot:

============================
Chain of Thought (cot.py)
============================

The `cot.py` module implements Chain-of-Thought reasoning for LLM workflows. This file includes components that enable sequential reasoning by chaining prompts and responses together. It supports both individual thoughts and manually-defined chains of thoughts for complex reasoning workflows.

Classes
-------

Thought
~~~~~~~

This class represents an individual step in the Chain of Thought (CoT).

**Attributes:**
- `prompt (str)`: The template for the LLM prompt, supporting placeholders.
- `llm (LLM)`: The LLM model used to process the prompt.
- `post_process (Function)`: A function to post-process the LLM's response into a structured format.

**Methods:**
- `run(**kwargs) -> Document`: Executes the thought by filling the prompt, running the LLM, and applying the post-processor.
- `get_variables() -> List[str]`: Returns a list of variables in the prompt (currently unused).
- `__add__(next_thought: "Thought") -> "ManualSequentialChainOfThought"`: Chains the current thought with another.

**Example Usage:**

.. code-block:: python

    from kotaemon.llms.cot import Thought
    from kotaemon.llms import LCAzureChatOpenAI

    llm = LCAzureChatOpenAI(...)

    thought = Thought(
        prompt="Translate {word} to Japanese.",
        llm=llm,
        post_process=lambda response: {"translation": response},
    )

    output = thought(word="hello")
    print(output)

ManualSequentialChainOfThought
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This class chains multiple `Thought` components to execute sequential reasoning.

**Attributes:**
- `thoughts (List[Thought])`: A list of `Thought` instances.
- `llm (LLM)`: The LLM model used for all thoughts in the chain.
- `terminate (Callable)`: A callback function to determine when to stop the chain.

**Methods:**
- `run(**kwargs) -> Document`: Executes the chain of thoughts sequentially, updating the inputs at each step.
- `__add__(next_thought: Thought) -> "ManualSequentialChainOfThought"`: Adds a new thought to the chain.

**Example Usage:**

.. code-block:: python

    from kotaemon.llms.cot import Thought, ManualSequentialChainOfThought
    from kotaemon.llms import LCAzureChatOpenAI

    llm = LCAzureChatOpenAI(...)

    thought1 = Thought(
        prompt="Word {word} in {language} is ",
        post_process=lambda response: {"translation": response},
    )

    thought2 = Thought(
        prompt="Translate {translation} to Japanese.",
        post_process=lambda response: {"final_translation": response},
    )

    chain = ManualSequentialChainOfThought(thoughts=[thought1, thought2], llm=llm)

    output = chain(word="hello", language="French")
    print(output)

Source Code
-----------

.. code-block:: python

   from copy import deepcopy
   from typing import Callable, List

   from theflow import Function, Node, Param

   from kotaemon.base import BaseComponent, Document

   from .chats import LCAzureChatOpenAI
   from .completions import LLM
   from .prompts import BasePromptComponent

   class Thought(BaseComponent):
       """A thought in the chain of thought"""

       prompt: str = Param(...)
       llm: LLM = Node(LCAzureChatOpenAI, ...)
       post_process: Function = Node(...)

       def run(self, **kwargs) -> Document:
           prompt = self.prompt_template(**kwargs).text
           response = self.llm(prompt).text
           return Document(self.post_process(response))

       def __add__(self, next_thought: "Thought") -> "ManualSequentialChainOfThought":
           return ManualSequentialChainOfThought(
               thoughts=[self, next_thought], llm=self.llm
           )

   class ManualSequentialChainOfThought(BaseComponent):
       """Perform sequential chain-of-thought"""

       thoughts: List[Thought] = Param(...)
       llm: LLM = Param(...)
       terminate: Callable = Param(default=lambda _: False, ...)

       def run(self, **kwargs) -> Document:
           inputs = deepcopy(kwargs)
           for idx, thought in enumerate(self.thoughts):
               thought.llm = self.llm
               self._prepare_child(thought, f"thought{idx}")
               output = thought(**inputs)
               inputs.update(output.content)
               if self.terminate(inputs):
                   break

           return Document(inputs)
