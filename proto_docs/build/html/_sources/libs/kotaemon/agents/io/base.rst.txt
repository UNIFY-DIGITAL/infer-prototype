base.py
=======

The `base.py` module in the `kotaemon.agents.io` package defines essential building blocks for agents, including types, actions, outputs, and logging mechanisms.

Classes
-------

The following classes are defined in `base.py`:

AgentType
---------

.. automodule:: kotaemon.agents.io.base.AgentType
   :members:
   :undoc-members:
   :show-inheritance:

Enumerated types for different agent categories, such as:
- `openai`: OpenAI-based agent.
- `self_ask`: Self-ask agent.
- `react`: ReAct-based agent.
- `rewoo`: ReWoo-based agent.
- `vanilla`: A simple vanilla agent type.

**`AgentType`**: Enum representing various types of agents.

.. code-block:: python

    class AgentType(Enum):
        """
        Enumerated type for agent types.
        """
        openai = "openai"
        openai_multi = "openai_multi"
        openai_tool = "openai_tool"
        self_ask = "self_ask"
        react = "react"
        rewoo = "rewoo"
        vanilla = "vanilla"

BaseScratchPad class
--------------------

.. automodule:: kotaemon.agents.io.base.BaseScratchPad
   :members:
   :undoc-members:
   :show-inheritance:

The `BaseScratchPad` class provides functionality for managing logs and debugging.

Attributes:
~~~~~~~~~~~

- **`logger`**: The logger object used for logging messages.
- **`log`**: A list to store log messages.

Methods:
~~~~~~~~

- **`update_status`**: Updates the status of the output.
- **`thinking`**: Logs that a process is thinking.

Code Example:
~~~~~~~~~~~~~

.. code-block:: python

    class BaseScratchPad:
        """
        Base class for output handlers.
        """

        def __init__(self):
            self.logger = logging
            self.log = []

        def update_status(self, output: str, **kwargs):
            """
            Update the status of the output.
            """
            if check_log():
                self.logger.info(output)

        def thinking(self, name: str):
            """
            Log that a process is thinking.
            """
            if check_log():
                self.logger.info(f"{name} is thinking...")

AgentAction Class
-----------------

.. automodule:: kotaemon.agents.io.base.AgentAction
   :members:
   :undoc-members:
   :show-inheritance:

Represents an action taken by an agent. Attributes include:
- `tool`: The name of the tool to invoke.
- `tool_input`: Input for the tool (string or dictionary).
- `log`: Log message for the action.


The `AgentAction` class represents an action taken by an agent.

Attributes:
~~~~~~~~~~~

- **`tool`**: The tool to be invoked by the agent.
- **`tool_input`**: The input to the tool (can be a string or dictionary).
- **`log`**: Log message associated with the action.

Code Implementation:
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    @dataclass
    class AgentAction:
        """Agent's action to take.

        Args:
            tool: The tool to invoke.
            tool_input: The input to the tool.
            log: The log message.
        """

        tool: str
        tool_input: Union[str, dict]
        log: str

Usage Example:
~~~~~~~~~~~~~~

.. code-block:: python

    from kotaemon.agents.io.base import AgentAction

    action = AgentAction(
        tool="search_tool",
        tool_input={"query": "What is the capital of France?"},
        log="Invoking search_tool with query"
    )
    print(action.tool, action.tool_input, action.log)


AgentFinish Class
-----------------

.. automodule:: kotaemon.agents.io.base.AgentFinish
   :members:
   :undoc-members:
   :show-inheritance:

Represents the return value when an agent finishes execution. Attributes include:
- `return_values`: A dictionary of results.
- `log`: Log message detailing the execution.


Attributes:
~~~~~~~~~~~

- **`return_values`**: Dictionary containing the agent's return values.
- **`log`**: Log message associated with the completion of the agent's task.

Code Implementation:
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    class AgentFinish(NamedTuple):
        """Agent's return value when finishing execution.

        Args:
            return_values: The return values of the agent.
            log: The log message.
        """

        return_values: dict
        log: str

Usage Example:
~~~~~~~~~~~~~~

.. code-block:: python

    from kotaemon.agents.io.base import AgentFinish

    result = AgentFinish(
        return_values={"answer": "Paris"},
        log="Agent execution completed successfully"
    )
    print(result.return_values, result.log)

AgentOutput
-----------

.. automodule:: kotaemon.agents.io.base.AgentOutput
   :members:
   :undoc-members:
   :show-inheritance:

The `AgentOutput` class defines the structure of an agent's output. Key attributes:
- `text`: The generated text output.
- `agent_type`: Type of the agent (`AgentType` enum).
- `status`: Current status of the agent (`thinking`, `finished`, `stopped`, or `failed`).
- `error`: Optional error message if an issue occurs.

Attributes:
~~~~~~~~~~~

- **`text`**: Text output generated by the agent.
- **`type`**: Type of the output, default is `"agent"`.
- **`agent_type`**: The type of agent (based on `AgentType` enum).
- **`status`**: Status of the agent's execution (e.g., `thinking`, `finished`, `failed`).
- **`error`**: Optional error message, if any.
- **`intermediate_steps`**: Optional list of intermediate steps performed by the agent.

Code Implementation:
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    class AgentOutput(LLMInterface):
        """Output from an agent.

        Args:
            text: The text output from the agent.
            agent_type: The type of agent.
            status: The status after executing the agent.
            error: The error message if any.
        """

        model_config = ConfigDict(extra="allow")

        text: str
        type: str = "agent"
        agent_type: AgentType
        status: Literal["thinking", "finished", "stopped", "failed"]
        error: Optional[str] = None
        intermediate_steps: Optional[list] = None

Usage Example:
~~~~~~~~~~~~~~

.. code-block:: python

    from kotaemon.agents.io.base import AgentOutput, AgentType

    output = AgentOutput(
        text="The capital of France is Paris.",
        agent_type=AgentType.openai,
        status="finished",
        error=None,
        intermediate_steps=["Step 1: Retrieved knowledge", "Step 2: Generated response"]
    )
    print(output.text, output.agent_type, output.status)

Functions
---------

The following function is available:

check_log
---------

.. automodule:: kotaemon.agents.io.base.check_log
   :members:
   :undoc-members:
   :show-inheritance:

Checks if logging has been enabled by verifying the `LOG_PATH` environment variable.

Usage
-----

This module is used as a foundation for implementing agents within the `kotaemon` framework. Each class or function can be extended or utilized based on the specific agent type or use case.

