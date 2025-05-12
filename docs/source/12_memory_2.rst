.. _12 memory 2:

12 Long term memory in Json format
===================================
.. index:: conversational memory

This is a continuation from the previous setup, where the short term memory is passed on to the long term memory.

.. todo:: 

 explain more and bla bla

::
 
 # Celle 7: Importere nødvendige biblioteker
 import json
 from typing import List, Dict, Any
 from pydantic import BaseModel, Field
 
 # Definere datamodellen for langtidsminne
 class LongTermMemory(BaseModel):
     """Class representing long-term memory for a project."""
     project_name: str = Field(..., description="Name of the research project")
     tags: List[str] = Field(default_factory=list, description="Tags related to the memory")
     memory_id: str = Field(..., description="Unique identifier for the memory")
     messages: List[Dict[str, Any]] = Field(default_factory=list, description="Collection of messages")
     timestamp: str = Field(..., description="Timestamp when the memory was created or updated")

code view 10::

  # Functions to store and download from Json
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

 # Celle 4: In-memory lagring av meldinger
 thread_memory_store = {}
 
 def get_memory_by_thread_id(thread_id: str) -> List[Dict[str, Any]]:
     """Retrieve messages for a given thread ID."""
     if thread_id not in thread_memory_store:
         return []
     return thread_memory_store[thread_id].messages


code view 9::
code view 9::
code view 9::
code view 9::
code view 9::
code view 9::

