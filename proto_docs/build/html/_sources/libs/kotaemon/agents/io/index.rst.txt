io
==========

The `io` package within the `agents` submodule provides foundational components for defining agent types, managing agent outputs, and handling logging and status updates.

Submodules
----------

The following submodules are included in the `io` package:

.. toctree::
   :maxdepth: 2

   base

base module
-----------

The `base` module defines core components for agent actions, agent outputs, and logging mechanisms.

.. automodule:: kotaemon.agents.io.base
   :members:
   :undoc-members:
   :show-inheritance:

Classes and Utilities
---------------------

- **`AgentType`**: Enum representing various types of agents (e.g., `openai`, `react`, `rewoo`, etc.).
- **`BaseScratchPad`**: Manages logging, status updates, and debugging during agent execution.
- **`AgentAction`**: Represents an action to be taken by an agent, including the tool to invoke and the input.
- **`AgentFinish`**: Captures the final return values and logs when an agent completes its task.
- **`AgentOutput`**: Defines the structure of an agent's output, including text, status, error messages, and intermediate steps.

Utilities
---------

- **`check_log`**: A utility function to check if logging is enabled, based on the presence of a `LOG_PATH` environment variable.
