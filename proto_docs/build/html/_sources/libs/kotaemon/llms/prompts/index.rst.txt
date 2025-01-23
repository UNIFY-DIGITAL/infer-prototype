.. _kotaemon_llms_prompts:

Prompts Module
==============

This module provides classes and utilities to define, manage, and populate prompt templates in a structured manner.

Contents:
---------

.. toctree::
   :maxdepth: 2
   :caption: Prompts Module Contents

   base
   template

Module Overview
---------------

The `prompts` folder includes the following files:

- **`base.py`**:
  - Defines the `BasePromptComponent` class, which serves as a foundational component for managing prompts.
  - Provides methods to set, validate, and populate attributes for prompt templates.
- **`template.py`**:
  - Defines the `PromptTemplate` class for creating and populating string templates with placeholders.
  - Supports strict and partial population of templates and concatenation of templates.

Source Code
-----------

.. literalinclude:: ../../../../../../libs/kotaemon/kotaemon/llms/prompts/__init__.py
   :language: python
