Retrievers
==========

The `retrievers` module contains components and utilities for retrieving data from various sources, such as web search engines and APIs. These retrievers are designed to integrate seamlessly with the `kotaemon` framework, allowing efficient data fetching and preprocessing.

Modules
-------

.. toctree::
   :maxdepth: 2
   :caption: Submodules:

   jina_web_search
   tavily_web_search

---

**Module Overview**

- **`jina_web_search.py`**  
  Fetches data from the web using the Jina API.

- **`tavily_web_search.py`**  
  Retrieves data from the web using the Tavily API, with support for advanced search depth.

---

Usage
-----

The retrievers are typically used to fetch external data that is then processed and analyzed within the `kotaemon` pipeline. Each retriever is implemented as a standalone class, providing flexibility in integration and extensibility.

