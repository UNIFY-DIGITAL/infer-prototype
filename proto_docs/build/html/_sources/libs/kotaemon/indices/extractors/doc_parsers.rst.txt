doc_parsers Module
==================

The `doc_parsers` module provides tools to extract specific information, such as titles and summaries, from documents using the LlamaIndex framework.

.. automodule:: kotaemon.indices.extractors.doc_parsers
   :members:
   :undoc-members:
   :show-inheritance:

Classes
-------

BaseDocParser
~~~~~~~~~~~~~
.. autoclass:: kotaemon.indices.extractors.doc_parsers.BaseDocParser
   :members:
   :undoc-members:
   :show-inheritance:

   Base class for all document parsers.

TitleExtractor
~~~~~~~~~~~~~~
.. autoclass:: kotaemon.indices.extractors.doc_parsers.TitleExtractor
   :members:
   :undoc-members:
   :show-inheritance:

   Extracts titles from documents using a LlamaIndex component.

   **Attributes:**
      - `llm`: Language model used for title extraction.
      - `nodes`: Number of nodes used for processing. Defaults to 5.

   **Methods:**
      - `_get_li_class`: Retrieves the LlamaIndex class for title extraction.

SummaryExtractor
~~~~~~~~~~~~~~~~
.. autoclass:: kotaemon.indices.extractors.doc_parsers.SummaryExtractor
   :members:
   :undoc-members:
   :show-inheritance:

   Extracts summaries from documents using a LlamaIndex component.

   **Attributes:**
      - `llm`: Language model used for summary extraction.
      - `summaries`: List of summary types (e.g., ["self"]). Defaults to ["self"].

   **Methods:**
      - `_get_li_class`: Retrieves the LlamaIndex class for summary extraction.



Source Code
-----------

Below is the full source code for the `doc_parsers` module:

.. code-block:: python

    from ..base import DocTransformer, LlamaIndexDocTransformerMixin


    class BaseDocParser(DocTransformer):
        """
        Base class for all document parsers.

        This class serves as a foundation for implementing custom document parsers
        by inheriting its functionality.
        """
        ...


    class TitleExtractor(LlamaIndexDocTransformerMixin, BaseDocParser):
        """
        Extracts the title of a document using a LlamaIndex component.

        Attributes:
            llm (optional): A language model to enhance the title extraction process.
            nodes (int, default=5): Number of nodes to consider during title extraction.
        """

        def __init__(
            self,
            llm=None,
            nodes: int = 5,
            **params,
        ):
            """
            Initialize the TitleExtractor.

            Args:
                llm: A language model for processing.
                nodes (int): Number of nodes to extract titles from.
                **params: Additional parameters for customization.
            """
            super().__init__(llm=llm, nodes=nodes, **params)

        def _get_li_class(self):
            """
            Returns the LlamaIndex class for title extraction.

            Returns:
                LlamaIndex TitleExtractor class.
            """
            from llama_index.core.extractors import TitleExtractor

            return TitleExtractor


    class SummaryExtractor(LlamaIndexDocTransformerMixin, BaseDocParser):
        """
        Extracts summaries of a document using a LlamaIndex component.

        Attributes:
            llm (optional): A language model to assist with summary extraction.
            summaries (list[str], default=["self"]): Specifies the type of summaries.
        """

        def __init__(
            self,
            llm=None,
            summaries: list[str] = ["self"],
            **params,
        ):
            """
            Initialize the SummaryExtractor.

            Args:
                llm: A language model for processing.
                summaries (list[str]): Type of summaries to generate.
                **params: Additional parameters for customization.
            """
            super().__init__(llm=llm, summaries=summaries, **params)

        def _get_li_class(self):
            """
            Returns the LlamaIndex class for summary extraction.

            Returns:
                LlamaIndex SummaryExtractor class.
            """
            from llama_index.core.extractors import SummaryExtractor

            return SummaryExtractor
