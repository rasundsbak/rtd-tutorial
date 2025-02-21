.. _11 memory:

11 Conversational memory - work in progress
============================================
.. index:: conversational memory


Short term memory with LangGraph
-----------------------------------
The memory of the LLM depends on the context window. In our first experiment, we will just make a test using hte short term memory of Mistral. Mistral-7B-Instruct-v0.3 is the smallest and latest Large Language Model (LLM) from Mistral AI, providing a 32k context window and support for function calling. This is what sets the limit when we want to implement a simple form of memory/ chat history.
https://langchain-ai.github.io/langgraph/concepts/memory/#managing-long-conversation-history

Trim messages
--------------
The function of trimming or cleaning up messages, can be useful when we use the short term memory.
https://python.langchain.com/docs/how_to/trim_messages/

More on this
-------------
https://python.langchain.com/docs/integrations/memory/redis_chat_message_history/
https://python.langchain.com/docs/concepts/chat_history/







