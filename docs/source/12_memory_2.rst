.. _12 memory:

11 Long term memory in Json format
===================================
.. index:: conversational memory


::
 
 # Celle 1
 %env HF_HOME=/fp/projects01/ec443/huggingface/cache/

code view 3::

  # Celle 3
  from transformers import AutoModelForCausalLM, AutoTokenizer  
  model_id = 'mistralai/Mistral-7B-Instruct-v0.3'
  task = 'text-generation'

code view 4::

  # Initialize the pipeline with additional parameters
  # Recommended parameters for Mistral 7B Instruct v0.3 Median values from users on OpenRouter
  # 0.0 values removed
  # "Simplicity :)"

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

code view 5::

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


code view 6::

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


code view 7::

  # Using thread-1 for a human message
  thread_id1 = "thread-1"
  memory1 = get_memory_by_thread_id(thread_id1)
  memory1.add_message(HumanMessage(
      content="""Thomas Cavendish was the first man to intentionally circumnavigate the globe, 
                 from 1587 to 1592. He raided many Spanish towns and ships."""
  ))

code view 8::

  # Using thread-2 for a human message
  thread_id2 = "thread-2"
  memory2 = get_memory_by_thread_id(thread_id2)
  memory2.add_message(HumanMessage(content="Thomas Cavendish was a cat."))

code view 9::
  
  # Print the memory for thread-1, excluding system messages
  print(f"Memory for {thread_id1}: {get_non_system_messages(thread_id1)}")


code view 10::
  
  # Print the memory for thread-2, excluding system messages
  print(f"Memory for {thread_id2}: {get_non_system_messages(thread_id2)}")

code view 11::

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

code view 12::
 
 # Print the memory for thread-2, excluding system messages
 print(f"Memory for {thread_id2}: {get_non_system_messages(thread_id2)}")

code view 9::
code view 9::
code view 9::
code view 9::
code view 9::
code view 9::
code view 9::
code view 9::
code view 9::

