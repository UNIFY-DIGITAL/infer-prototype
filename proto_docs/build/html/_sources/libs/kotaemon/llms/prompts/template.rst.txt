.. _kotaemon_llms_prompts_template:

Prompt Template Module
======================

This module defines the `PromptTemplate` class, which provides a structured way to manage and populate prompt templates with placeholders.

Class Overview
--------------

`PromptTemplate`
~~~~~~~~~~~~~~~~
.. autoclass:: PromptTemplate
   :members:
   :undoc-members:
   :show-inheritance:

Details
-------

The `PromptTemplate` class allows defining, validating, and populating templates for prompts. It supports strict validation of placeholders and partial or full population.

**Attributes**:
- `template`: The string template containing placeholders.
- `placeholders`: A set of valid placeholder names extracted from the template.

**Methods**:
- **`check_missing_kwargs(**kwargs)`**:
  - Validates that all placeholders in the template have corresponding values.
  - Raises `ValueError` if any placeholders are missing.
- **`check_redundant_kwargs(**kwargs)`**:
  - Warns about extra keys provided in `kwargs` that are not placeholders in the template.
- **`populate(safe=True, **kwargs)`**:
  - Fully populates the template with the provided keyword arguments.
  - Raises `ValueError` if required placeholders are missing.
- **`partial_populate(**kwargs)`**:
  - Partially populates the template, leaving placeholders without provided values as they are.
- **`__add__(other)`**:
  - Concatenates the current template with another `PromptTemplate` object to create a new template.

**Usage Workflow**:
1. Create a `PromptTemplate` object with a string template.
2. Use `populate` to strictly fill all placeholders or `partial_populate` to partially fill them.
3. Validate placeholder usage with `check_missing_kwargs` and `check_redundant_kwargs`.

**Error Handling**:
- Raises `ValueError` for:
  - Invalid placeholder names.
  - Missing required placeholders during population.
- Issues warnings for redundant placeholder keys.

**Example**:
```python
template = PromptTemplate("Hello, {name}! You have {count} new messages.")
template.populate(name="Alice", count=5)
# Output: "Hello, Alice! You have 5 new messages."
