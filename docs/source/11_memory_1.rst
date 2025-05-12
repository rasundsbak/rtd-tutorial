.. _11 memory 1:

11 Setting up the memory
=========================
.. index:: conversational memory

Short term memory with LangGraph
-----------------------------------
Without adjustments, the memory of the LLM depends on the context window. In our first experiment, we will make a test using the short term memory of Mistral. Mistral-7B-Instruct-v0.3 is the smallest and latest Large Language Model (LLM) from Mistral AI, providing a 32k context window and support for function calling. This is what sets the limit when we want to implement a simple form of memory/ chat history.
https://langchain-ai.github.io/langgraph/concepts/memory/#managing-long-conversation-history

Trim messages
--------------
The function of trimming or cleaning up messages, can be useful when we use the short term memory.
https://python.langchain.com/docs/how_to/trim_messages/

More on this
-------------
https://python.langchain.com/docs/integrations/memory/redis_chat_message_history/
https://python.langchain.com/docs/concepts/chat_history/

::
 
 %env HF_HOME=/fp/projects01/ec443/huggingface/cache/

::

 pip install --upgrade --quiet langchain langchain-openai langgraph


# Adding Short term memory with LangGraph:
https://langchain-ai.github.io/langgraph/concepts/memory/#managing-long-conversation-history

I denne sammenhengen er hukommelse = modellens kontekstvindu.
Av denne grunn kan det senere gi mulighet å benytte seg av funksjonen trim_messages, der man redigerer meldingslister for å passe innenfor denne grensen.
https://python.langchain.com/docs/how_to/trim_messages/

og blabla

## Read more
# Long term and short term
https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#tool-calling

## Chat history
https://python.langchain.com/docs/concepts/chat_history/

## Capacity og bla
## Capacity
Mistral-7B-Instruct-v0. 3 is the smallest and latest Large Language Model (LLM) from Mistral AI, providing a 32k context window and support for function calling. This is what sets the limit when we want to implement a simple form of memory/ chat history.

We are using this:
https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.history.RunnableWithMessageHistory.html

Skip this? (test it)::

 import transformers
 print(transformers.__version__)

::

 from langchain_huggingface.llms import HuggingFacePipeline
 from transformers import AutoModelForCausalLM, AutoTokenizer
 model_id = 'mistralai/Mistral-7B-Instruct-v0.3'
 task = 'text-generation'

Tool calling and use of chat history may complicate the process. I have therefore decided to use the Recommended parameters for Mistral 7B Instruct v0.3 Median values from users on OpenRouter, ref: https://openrouter.ai/mistralai/mistral-7b-instruct-v0.3/parameters::

 llm = HuggingFacePipeline.from_model_id(
     model_id,
     task,
     device=0,
     pipeline_kwargs={
         'max_new_tokens': 100,
         'do_sample': True,
         'temperature': 1.0,  # Default value for balanced responses
         'top_p': 1.0,       # Default, allows full range of top choices
         'num_beams': 4,     # For beam search, optional
         'repetition_penalty': 1.4,
     }
 )


Bla og bla::

 from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

::

 from typing import List
 from pydantic import BaseModel, Field
 from langchain_core.chat_history import BaseChatMessageHistory
 from langchain_core.messages import BaseMessage, AIMessage, HumanMessage, SystemMessage

 class InMemoryHistory(BaseChatMessageHistory, BaseModel):
     """In-memory implementation of chat message history for a specific thread."""
     messages: List[BaseMessage] = Field(default_factory=list)
 
     def add_message(self, message: BaseMessage) -> None:
         """Add a single message to the history."""
         self.messages.append(message)
     
     def clear(self) -> None:
         """Clear the message history."""
         self.messages.clear()  # Consistently use clear()

::

 # Store for managing memory by thread ID
 thread_memory_store = {}

 def get_memory_by_thread_id(thread_id: str) -> InMemoryHistory:
     """Retrieve or create memory for a given thread ID, initialized with a system message if none."""
     if thread_id not in thread_memory_store:
         history = InMemoryHistory()
         system_message = SystemMessage(
             content="You are an expert historian who provides factual and comprehensive information."
         )
         history.add_message(system_message)
         thread_memory_store[thread_id] = history
     return thread_memory_store[thread_id]
 
 def get_non_system_messages(thread_id: str) -> List[str]:
     """Retrieve messages excluding system messages for display purposes."""
     return [
         message.content for message in thread_memory_store[thread_id].messages
         if not isinstance(message, SystemMessage)
     ]

::

 # Function to get AI response
 def get_ai_response(human_message: str) -> str:
     """Generate a response from the AI for the given human message."""
     response = llm.predict(human_message)  # Model call to generate response
     return response

::

 # Using thread-1 for a human message
 thread_id1 = "thread-1"
 memory1 = get_memory_by_thread_id(thread_id1)
 memory1.add_message(HumanMessage(
     content="""Thomas Cavendish was the first man to intentionally circumnavigate the globe, 
                from 1587 to 1592. He raided many Spanish towns and ships."""
 ))

::

 # Using thread-2 for a human message
 thread_id2 = "thread-2"
 memory2 = get_memory_by_thread_id(thread_id2)
 memory2.add_message(HumanMessage(content="Thomas Cavendish was a cat."))

::

 # Print the memory for thread-1, excluding system messages
 print(f"Memory for {thread_id1}: {get_non_system_messages(thread_id1)}")

::
  
 # Print the memory for thread-2, excluding system messages
 print(f"Memory for {thread_id2}: {get_non_system_messages(thread_id2)}")

::

 # Define function to clear memories for specific thread IDs
 def clear_memory_by_thread_id(thread_ids: List[str]) -> None:
     """Clear memory for given thread IDs."""
     for thread_id in thread_ids:
         if thread_id in thread_memory_store:
             memory = thread_memory_store[thread_id]
             memory.clear()
             print(f"After clearing, memory for {thread_id}: {memory.messages}")
 
 # Use this function to clear memories
 thread_ids_to_clear = ["thread-1", "thread-2"]
 clear_memory_by_thread_id(thread_ids_to_clear)

Testing if the cleanup works::
 
 # Print the memory for thread-2, excluding system messages
 print(f"Memory for {thread_id2}: {get_non_system_messages(thread_id2)}")
