Component Module
================

The `component` module defines the foundational `BaseComponent` class and provides utilities for creating and managing pipeline components.

Overview
--------

The `BaseComponent` class serves as the base for all pipeline components. It ensures:
- **Auto caching and logging**.
- **Support for multiple input types** (e.g., `str`, `Document`, `List[str]`, `List[Document`]).
- **Single output type enforcement**, making outputs as generic as possible.

Re-exported Utilities:
- **`Param`**: Utility for defining configurable parameters.
- **`Node`**: Represents a node in the pipeline.
- **`lazy`**: Delays computation or initialization until needed.

BaseComponent Class
-------------------

**Class Definition**
This class is used to build pipeline components with features like caching, logging, and deployment support.

.. code-block:: python

    class BaseComponent(Function):
        """A component is a class that can be used to compose a pipeline.

        !!! tip "Benefits of component"
            - Auto caching, logging
            - Allow deployment

        !!! tip "For each component, the spirit is"
            - Tolerate multiple input types, e.g. str, Document, List[str], List[Document]
            - Enforce single output type. Hence, the output type of a component should be
        as generic as possible.
        """
        ...

### **Attributes and Methods**

#### inflow
Represents an upstream component in the pipeline.

.. code-block:: python

    inflow = None

---

#### flow(self)
Connects to the upstream `inflow` component and invokes its `flow()` method. Ensures the inflow is an instance of `BaseComponent`.

.. code-block:: python

    def flow(self):
        if self.inflow is None:
            raise ValueError("No inflow provided.")

        if not isinstance(self.inflow, BaseComponent):
            raise ValueError(
                f"inflow must be a BaseComponent, found {type(self.inflow)}"
            )

        return self.__call__(self.inflow.flow())

---

#### set_output_queue(self, queue)
Sets an output queue for reporting results and propagates it to downstream components.

.. code-block:: python

    def set_output_queue(self, queue):
        self._queue = queue
        for name in self._ff_nodes:
            node = getattr(self, name)
            if isinstance(node, BaseComponent):
                node.set_output_queue(queue)

---

#### report_output(self, output: Optional[Document])
Reports the output of the component to the designated queue.

.. code-block:: python

    def report_output(self, output: Optional[Document]):
        if self._queue is not None:
            self._queue.put_nowait(output)

---

#### invoke(self, *args, **kwargs) -> Document | list[Document] | None
Placeholder for synchronous invocation of the component.

.. code-block:: python

    def invoke(self, *args, **kwargs) -> Document | list[Document] | None:
        ...

---

#### ainvoke(self, *args, **kwargs) -> Document | list[Document] | None
Placeholder for asynchronous invocation of the component.

.. code-block:: python

    async def ainvoke(self, *args, **kwargs) -> Document | list[Document] | None:
        ...

---

#### stream(self, *args, **kwargs) -> Iterator[Document] | None
Placeholder for synchronous streaming of outputs.

.. code-block:: python

    def stream(self, *args, **kwargs) -> Iterator[Document] | None:
        ...

---

#### astream(self, *args, **kwargs) -> AsyncGenerator[Document, None] | None
Placeholder for asynchronous streaming of outputs.

.. code-block:: python

    def astream(self, *args, **kwargs) -> AsyncGenerator[Document, None] | None:
        ...

---

#### run(self, *args, **kwargs)
An abstract method that must be implemented by subclasses to define the core functionality of the component.

.. code-block:: python

    @abstractmethod
    def run(
        self, *args, **kwargs
    ) -> Document | list[Document] | Iterator[Document] | None | Any:
        """Run the component."""
        ...

---

Utilities
---------

The following utilities are re-exported from `theflow`:

- **Param**: Utility for defining configurable parameters.
- **Node**: Represents a node in the pipeline.
- **lazy**: Delays computation or initialization until needed.

.. code-block:: python

    from theflow import Function, Node, Param, lazy
    __all__ = ["BaseComponent", "Param", "Node", "lazy"]

