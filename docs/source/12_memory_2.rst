.. _12 memory 2:

12 Long term memory in Json format
===================================
.. index:: conversational memory

This is a continuation from the previous setup, where the short term memory is passed on to the long term memory.

.. todo:: 

 explain more and bla bla

::
 
 # Import the necessary libraries
 import json
 from typing import List, Dict, Any
 from pydantic import BaseModel, Field
 
 # Define the datamodel for the long term memory
 class LongTermMemory(BaseModel):
     """Class representing long-term memory for a project."""
     project_name: str = Field(..., description="Name of the research project")
     tags: List[str] = Field(default_factory=list, description="Tags related to the memory")
     memory_id: str = Field(..., description="Unique identifier for the memory")
     messages: List[Dict[str, Any]] = Field(default_factory=list, description="Collection of messages")
     timestamp: str = Field(..., description="Timestamp when the memory was created or updated")

code view 10::

  # Functions to store and upload from Json
  def save_memory_to_json(file_path: str, memories: List[LongTermMemory]) -> None:
      """Saves messages to a JSON file."""
      with open(file_path, 'w') as json_file:
          json.dump([memory.dict() for memory in memories], json_file, indent=4)
  
  def load_memory_from_json(file_path: str) -> List[LongTermMemory]:
      """Loads messages from a JSON file."""
      with open(file_path, 'r') as json_file:
          data = json.load(json_file)
          return [LongTermMemory(**item) for item in data]


code view 9::

 # Celle 4: In-memory storing of messages
 thread_memory_store = {}
 
 def get_memory_by_thread_id(thread_id: str) -> List[Dict[str, Any]]:
     """Retrieve messages for a given thread ID."""
     if thread_id not in thread_memory_store:
         return []
     return thread_memory_store[thread_id].messages


code view 9::

 from langchain_core.chat_history import BaseChatMessageHistory
 from langchain_core.messages import HumanMessage
 from typing import List
 from pydantic import BaseModel, Field

In the next step, we are taking up treads and adding names to them, so that they may become easier to find in the future::

 thread_id1 = "Cavendish"
 thread_id2 = "Circumnavigation"
 thread_id3 = "Cat"
 
 # Storing messages
 thread_memory_store[thread_id1] = InMemoryHistory()
 thread_memory_store[thread_id1].add_message(HumanMessage(content="Thomas Cavendish was the first man to intentionally circumnavigate the globe."))
 thread_memory_store[thread_id2] = InMemoryHistory()
 thread_memory_store[thread_id2].add_message(HumanMessage(content="Circumnavigation of the globe took from 1587 to 1592."))
 thread_memory_store[thread_id3] = InMemoryHistory()
 thread_memory_store[thread_id3].add_message(HumanMessage(content="Cavendish was a chemist and physicist."))

::

 # Kombiner meldinger i ett enkelt LongTermMemory objekt
 combined_memory = LongTermMemory(
     project_name="Exploration of Thomas Cavendish",
     tags=["historical", "exploration", "Cavendish"],
     memory_id="cavendish_exploration",
     messages=[{"content": message.content, "timestamp": "2023-10-25T12:00:00Z"} for thread in [thread_memory_store[thread_id1], thread_memory_store[thread_id2], thread_memory_store[thread_id3]] for message in thread.messages],
     timestamp="2023-10-25T12:00:00Z"
 )

::

 # Alternatively
 # Combining messages into a single LongTermMemory object
 combined_memory = LongTermMemory(
     project_name="Exploration of Thomas Cavendish",
     tags=["historical", "exploration", "Cavendish"],
     memory_id="cavendish_exploration",
     # Use the appropriate thread IDs
     messages=[
         {"content": message.content, "timestamp": "2023-10-25T12:00:00Z"}
         for thread_id in ["thread-1", "thread-2"]  # Ensure these contain the relevant messages
         for message in get_memory_by_thread_id(thread_id).messages
     ],
     timestamp="2023-10-25T12:00:00Z"
 ) 


code view 9::

 # Store the combined memory in one Json file. 
 save_memory_to_json("cavendish_exploration.json", [combined_memory])  

code view 9::

 # Load and show the long term memory
 loaded_memories = load_memory_from_json("cavendish_exploration.json")
 for memory in loaded_memories:
     print(f"Project: {memory.project_name}, ID: {memory.memory_id}, Messages: {memory.messages}")

code view 9::


code view 9::

