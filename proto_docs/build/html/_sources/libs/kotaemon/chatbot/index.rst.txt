Chatbot
=======

The `kotaemon.chatbot` module provides tools for building and managing chatbot interactions. It includes foundational classes for defining chatbot behaviors, handling conversations, and integrating with LLMs.

.. toctree::
   :maxdepth: 1
   :caption: Submodules:

   base
   simple_respondent

Exports
-------

The following components are available for direct import from the `chatbot` module:

- **`BaseChatBot`**: The foundational class for defining chatbots.
- **`ChatConversation`**: A stateful conversation handler for chatbots.
- **`SimpleRespondentChatbot`**: A minimal implementation of a chatbot that wraps around an LLM.

Examples
--------

**Using a Simple Respondent Chatbot**:

.. code-block:: python

    from kotaemon.chatbot import SimpleRespondentChatbot

    chatbot = SimpleRespondentChatbot()
    response = chatbot.run(["Hello!"])
    print(response)  # Outputs: AI's response
