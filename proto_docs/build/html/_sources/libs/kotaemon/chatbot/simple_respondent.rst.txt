Simple Respondent
=================

The `kotaemon.chatbot.simple_respondent` module provides a minimal chatbot implementation.

Classes
-------

SimpleRespondentChatbot
~~~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: kotaemon.chatbot.simple_respondent.SimpleRespondentChatbot
   :members:
   :undoc-members:
   :show-inheritance:

   **Overview**:
   - A simple chatbot that wraps around a chat LLM.
   - Requires a `ChatLLM` instance to process history and generate responses.


Source Code
------------
The following is the source code for the `simple_respondent.py` module:

.. code-block:: python
    
    from ..llms import ChatLLM
    from .base import BaseChatBot


    class SimpleRespondentChatbot(BaseChatBot):
        """Simple text respondent chatbot that essentially wraps around a chat LLM"""

        llm: ChatLLM

        def _get_message(self) -> str:
            return self.llm(self.history).text


Usage
-----

**Example**:

.. code-block:: python

    from kotaemon.chatbot.simple_respondent import SimpleRespondentChatbot
    from kotaemon.llms import ChatLLM

    # Create a ChatLLM instance (example configuration)
    llm = ChatLLM()

    # Initialize the chatbot
    chatbot = SimpleRespondentChatbot(llm=llm)

    # Process a query
    response = chatbot.run(["Hello!"])
    print(response)  # Output: "Hi, how can I assist you?"
