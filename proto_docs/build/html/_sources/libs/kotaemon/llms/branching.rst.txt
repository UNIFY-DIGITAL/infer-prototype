.. _llms_branching:

=====================================
Branching Pipelines
=====================================

This module provides branching mechanisms for executing multiple components or pipelines based on certain conditions. It includes two main classes: `SimpleBranchingPipeline` and `GatedBranchingPipeline`.

Module Contents
===============

.. contents::
   :local:
   :depth: 1

Classes
=======

SimpleBranchingPipeline
------------------------

A simple branching pipeline for executing multiple branches. Each branch represents a component that can process inputs and produce outputs.

**Attributes:**

- `branches (List[BaseComponent])`: A list of components representing the branches of the pipeline.

**Example Usage:**

.. code-block:: python

    from kotaemon.llms import (
        LCAzureChatOpenAI,
        BasePromptComponent,
        GatedLinearPipeline,
    )
    from kotaemon.parsers import RegexExtractor

    def identity(x):
        return x

    pipeline = SimpleBranchingPipeline()
    llm = LCAzureChatOpenAI(
        openai_api_base="your openai api base",
        openai_api_key="your openai api key",
        openai_api_version="your openai api version",
        deployment_name="dummy-q2-gpt35",
        temperature=0,
        request_timeout=600,
    )

    for i in range(3):
        pipeline.add_branch(
            GatedLinearPipeline(
                prompt=BasePromptComponent(template=f"what is {i} in Japanese ?"),
                condition=RegexExtractor(pattern=f"{i}"),
                llm=llm,
                post_processor=identity,
            )
        )
    print(pipeline(condition_text="1"))
    print(pipeline(condition_text="2"))

**Methods:**

- `add_branch(component: BaseComponent)`: Adds a new branch to the pipeline.
- `run(**prompt_kwargs)`: Executes all branches and returns their outputs as a list.

GatedBranchingPipeline
-----------------------

An extension of `SimpleBranchingPipeline` that introduces gating. It executes branches sequentially and stops when a branch produces a non-empty output.

**Attributes:**

- `branches (List[BaseComponent])`: A list of components representing the branches of the pipeline.

**Example Usage:**

.. code-block:: python

    from kotaemon.llms import (
        LCAzureChatOpenAI,
        BasePromptComponent,
        GatedLinearPipeline,
    )
    from kotaemon.parsers import RegexExtractor

    def identity(x):
        return x

    pipeline = GatedBranchingPipeline()
    llm = LCAzureChatOpenAI(
        openai_api_base="your openai api base",
        openai_api_key="your openai api key",
        openai_api_version="your openai api version",
        deployment_name="dummy-q2-gpt35",
        temperature=0,
        request_timeout=600,
    )

    for i in range(3):
        pipeline.add_branch(
            GatedLinearPipeline(
                prompt=BasePromptComponent(template=f"what is {i} in Japanese ?"),
                condition=RegexExtractor(pattern=f"{i}"),
                llm=llm,
                post_processor=identity,
            )
        )
    print(pipeline(condition_text="1"))

**Methods:**

- `run(condition_text: Optional[str], **prompt_kwargs)`: Executes branches sequentially until one produces a non-empty output.

Source Code
===========

.. code-block:: python

    from typing import List, Optional

    from kotaemon.base import BaseComponent, Document, Param

    from .linear import GatedLinearPipeline


    class SimpleBranchingPipeline(BaseComponent):
        """
        A simple branching pipeline for executing multiple branches.

        Attributes:
            branches (List[BaseComponent]): The list of branches to be executed.

        Example:
            ...
        """

        branches: List[BaseComponent] = Param(default_callback=lambda *_: [])

        def add_branch(self, component: BaseComponent):
            ...

        def run(self, **prompt_kwargs):
            ...

    class GatedBranchingPipeline(SimpleBranchingPipeline):
        """
        A simple gated branching pipeline for executing multiple branches based on a
            condition.
        """

        def run(self, *, condition_text: Optional[str] = None, **prompt_kwargs):
            ...
