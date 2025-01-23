Jina Web Search
===============

The `jina_web_search.py` module provides functionality to fetch and retrieve data from the web using the Jina API. It defines the `WebSearch` class, which is responsible for handling web search queries and processing the results into retrievable documents.

Class Overview
--------------

**`WebSearch`**

The `WebSearch` class is a component designed to query the Jina API and return web search results in the form of `RetrievedDocument` objects.

### Methods

#### `run`

**Description:**  
The `run` method sends a query string to the Jina API, fetches web results, and processes them into a structured list of documents.

**Parameters:**
- `text (str)`: The query text to search on the web.
- `*args, **kwargs`: Additional arguments for extended functionality.

**Returns:**
- `list[RetrievedDocument]`: A list of retrieved documents containing structured web results.

**Raises:**
- `ValueError`: If the `JINA_API_KEY` is not provided.
- `requests.exceptions.RequestException`: If the API request fails.

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

    import requests
    from decouple import config

    from kotaemon.base import BaseComponent, RetrievedDocument

    JINA_API_KEY = config("JINA_API_KEY", default="")
    JINA_URL = config("JINA_URL", default="https://r.jina.ai/")


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
            if JINA_API_KEY == "":
                raise ValueError(
                    "This feature requires JINA_API_KEY "
                    "(get free one from https://jina.ai/reader)"
                )

            # setup the request
            api_url = f"https://s.jina.ai/{text}"
            headers = {"X-With-Generated-Alt": "true", "Accept": "application/json"}
            if JINA_API_KEY:
                headers["Authorization"] = f"Bearer {JINA_API_KEY}"

            response = requests.get(api_url, headers=headers)
            response.raise_for_status()
            response_dict = response.json()

            return [
                RetrievedDocument(
                    text=(
                        "###URL: [{url}]({url})\n\n"
                        "####{title}\n\n"
                        "{description}\n"
                        "{content}"
                    ).format(
                        url=item["url"],
                        title=item["title"],
                        description=item["description"],
                        content=item["content"],
                    ),
                    metadata={
                        "file_name": "Web search",
                        "type": "table",
                        "llm_trulens_score": 1.0,
                    },
                )
                for item in response_dict["data"]
            ]

        def generate_relevant_scores(self, text, documents: list[RetrievedDocument]):
            return documents

---

**Notes:**  
- Ensure you have a valid `JINA_API_KEY` to use this component.  
- The Jina API URL can be modified using the `JINA_URL` environment variable.  

