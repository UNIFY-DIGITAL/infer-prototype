.. _kotaemon_llms_prompts_base:

Base Prompt Module
==================

This module defines the `BasePromptComponent`, a foundational class for working with prompts and templates in a structured way.

Class Overview
--------------

`BasePromptComponent`
~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: BasePromptComponent
   :members:
   :undoc-members:
   :show-inheritance:

Details
-------

The `BasePromptComponent` class provides mechanisms to define, validate, and populate prompts using a `PromptTemplate`.

**Attributes**:
- `template`: A `str` or `PromptTemplate` object that defines the structure of the prompt.

**Methods**:
- **`set_value(**kwargs)`**:
  - Sets values for attributes in the component.
  - Validates the provided keyword arguments against the template.
- **`run(**kwargs)`**:
  - Populates the prompt template with the given values and returns a `Document` object.
  - Checks for unset placeholders and unsupported value types.
- **`flow()`**:
  - Executes the `__call__` method to run the component.
- **Private Utility Methods**:
  - `__check_redundant_kwargs(**kwargs)`: Validates if any unused keyword arguments are provided.
  - `__check_unset_placeholders()`: Ensures all placeholders in the template are set.
  - `__validate_value_type(**kwargs)`: Checks if the values are of supported types.
  - `__set(**kwargs)`: Updates attributes with validated values.
  - `__prepare_value()`: Prepares values for populating the template.

**Usage Workflow**:
1. Define a `PromptTemplate` with placeholders.
2. Create a `BasePromptComponent` instance with the template and other attributes.
3. Use the `run` method to populate the template with values and return the result as a `Document`.

**Error Handling**:
- Raises `ValueError` for:
  - Unset placeholders in the template.
  - Unsupported types for attribute values.
  - Redundant keyword arguments not defined in the template.

Source Code
-----------

.. literalinclude:: ../../../../../../libs/kotaemon/kotaemon/llms/prompts/base.py
   :language: python
   :linenos:
