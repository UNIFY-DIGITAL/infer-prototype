Tavily Web Search
=================

The `tavily_web_search.py` module provides functionality to fetch and retrieve data from the web using the Tavily API. It defines the `WebSearch` class, which processes web search queries and returns structured results as `RetrievedDocument` objects.

Class Overview
--------------

**`WebSearch`**

The `WebSearch` class is a component designed to query the Tavily API and process web search results into retrievable documents.

### Methods

#### `run`

**Description:**  
The `run` method sends a query string to the Tavily API, fetches web results, and processes them into a structured document format.

**Parameters:**
- `text (str)`: The query text for the web search.
- `*args, **kwargs`: Additional arguments for extended functionality.

**Returns:**
- `list[RetrievedDocument]`: A list of retrieved documents containing structured web results.

**Raises:**
- `ValueError`: If the `TAVILY_API_KEY` is not provided.
- `ImportError`: If the `tavily-python` package is not installed.

---

#### `generate_relevant_scores`

**Description:**  
This method is a placeholder for processing and assigning scores to the retrieved documents based on their relevance.

**Parameters:**
- `text (str)`: The query text.
- `documents (list[RetrievedDocument])`: The list of documents to score.

**Returns:**
- `list[RetrievedDocument]`: The scored list of documents.

---

Code Example
------------

Below is the implementation of the `WebSearch` class:

.. code-block:: python

    from decouple import config

    from kotaemon.base import BaseComponent, RetrievedDocument

    TAVILY_API_KEY = config("TAVILY_API_KEY", default="")


    class WebSearch(BaseComponent):
        """WebSearch component for fetching data from the web
        using Jina API
        """

        def run(
            self,
            text: str,
            *args,
            **kwargs,
        ) -> list[RetrievedDocument]:
            if TAVILY_API_KEY == "":
                raise ValueError(
                    "This feature requires TAVILY_API_KEY "
                    "(get free one from https://app.tavily.com/)"
                )

            try:
                from tavily import TavilyClient
            except ImportError:
                raise ImportError(
                    "Please install `pip install tavily-python` to use this feature"
                )

            tavily_client = TavilyClient(api_key=TAVILY_API_KEY)
            results = tavily_client.search(
                query=text,
                search_depth="advanced",
            )["results"]
            context = "\n\n".join(
                "###URL: [{url}]({url})\n\n{content}".format(
                    url=result["url"],
                    content=result["content"],
                )
                for result in results
            )

            return [
                RetrievedDocument(
                    text=context,
                    metadata={
                        "file_name": "Web search",
                        "type": "table",
                        "llm_trulens_score": 1.0,
                    },
                )
            ]

        def generate_relevant_scores(self, text, documents: list[RetrievedDocument]):
            return documents

---

**Notes:**  
- Ensure you have a valid `TAVILY_API_KEY` to use this component.  
- Install the `tavily-python` library using `pip install tavily-python` to enable this feature.

