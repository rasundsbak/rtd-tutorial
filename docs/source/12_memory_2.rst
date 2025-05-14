.. _12 memory 2:

12 Long term memory in Json format
===================================
.. index:: conversational memory

This is a continuation from the previous setup, where the short term memory is passed on to the long term memory.

.. todo:: 

 explain more and bla bla

::
 
 # Cell 8: Define the Message and Long-Term Memory Models
 # Import necessary libraries
 import json
 from typing import List
 from pydantic import BaseModel, Field
 from datetime import datetime  # For managing timestamps
 
 class Message(BaseModel):
     """Class to represent each message in memory."""
     content: str
     timestamp: str = Field(default_factory=lambda: datetime.utcnow().isoformat())  # Automatically generate timestamp
 
 class LongTermMemory(BaseModel):
     """Class representing long-term memory for a project."""
     project_name: str = Field(..., description="Name of the research project")
     tags: List[str] = Field(default_factory=list, description="Tags related to the memory")
     memory_id: str = Field(..., description="Unique identifier for the memory")
     messages: List[Message] = Field(default_factory=list, description="Collection of messages")
     timestamp: str = Field(default_factory=lambda: datetime.utcnow().isoformat(), description="Timestamp when the memory was created or updated")
 
 def create_long_term_memory(thread_id1: str, thread_id2: str) -> LongTermMemory:
     """Create and return a long-term memory entry for the given thread IDs."""
     messages_for_long_term = []
 
     # Add the system message once
     system_message = Message(
         content="You are an expert historian who provides factual and comprehensive information."
     )
     messages_for_long_term.append(system_message)
 
     # Get messages from thread 1
     memory1 = get_memory_by_thread_id(thread_id1)
     if memory1.messages:  # Ensure there are messages to extract
         latest_ai_response1 = memory1.messages[-1]  # Get the last message (assumed to be the AI message)
         messages_for_long_term.append(Message(content=latest_ai_response1.content))
 
     # Get messages from thread 2
     memory2 = get_memory_by_thread_id(thread_id2)
     if memory2.messages:  # Ensure there are messages to extract
         latest_ai_response2 = memory2.messages[-1]  # Get the last message (assumed to be the AI message)
         messages_for_long_term.append(Message(content=latest_ai_response2.content))
 
     # Create the long-term memory instance
     long_term_memory = LongTermMemory(
         project_name="Exploration of Thomas Cavendish",
         tags=["historical", "exploration", "Cavendish"],
         memory_id="cavendish_exploration",
         messages=messages_for_long_term
     )
 
     return long_term_memory

code view 9::

 # Cell 9 - Save Short-Term Memory to Long-Term Memory
 def save_short_term_to_long_term(thread_ids: List[str], project_name: str, memory_id: str):
     """Saves the last AI message from each specified thread into long-term memory."""
     
     # Initialize an empty list for messages in long-term memory
     messages_for_long_term = []
 
     # Add the system message once
     system_message = Message(
         content="You are an expert historian who provides factual and comprehensive information."
     )
     messages_for_long_term.append(system_message)
 
     # Process each thread to get its last AI message
     for thread_id in thread_ids:
         memory = get_memory_by_thread_id(thread_id)
         
         if memory.messages:  # Ensure there are messages in the memory
             last_message = memory.messages[-1]  # Get the last message
             
             # Ensure we're getting the AI message 
             if isinstance(last_message, AIMessage):  
                 messages_for_long_term.append(Message(
                     content=last_message.content
                     # Omit the timestamp now
                 ))
 
     # Create the long-term memory instance
     long_term_memory = LongTermMemory(
         project_name=project_name,
         tags=["historical", "exploration", "Cavendish"],
         memory_id=memory_id,
         messages=messages_for_long_term
     )
 
     # Save to JSON immediately after creating long-term memory
     save_memory_to_json("cavendish_exploration.json", [long_term_memory])  # Save the data


code view 10::

# Cell 10
from typing import List
import json  # Ensure you've imported json

# Function to save long-term memory to a JSON file
def save_memory_to_json(file_path: str, memories: List[LongTermMemory]) -> None:
    """Saves a list of LongTermMemory instances to a JSON file."""
    with open(file_path, 'w') as json_file:
        # Serialize the memories using Pydantic's dict() method to avoid deprecation warnings
        json.dump([memory.dict() for memory in memories], json_file, indent=4)

# Function to load memory from a JSON file
def load_memory_from_json(file_path: str) -> List[LongTermMemory]:
    """Loads a list of LongTermMemory instances from a JSON file."""
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            # Return a list of LongTermMemory instances from the loaded data
            return [LongTermMemory(**item) for item in data]
    except FileNotFoundError:
        print(f"Error: The specified file '{file_path}' was not found.")
        return []  # Return an empty list if the file does not exist
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' could not be decoded.")
        return []  # Return an empty list if decoding fails


code view 11::
 
 # Cell 11
 threads = [
     ("thread-1", "Thomas Cavendish was the first man to intentionally circumnavigate the globe."),
     ("thread-2", "Cavendish was a chemist and physicist.")
 ]
 
 # Storing messages
 for thread_id, human_message in threads:
     memory = get_memory_by_thread_id(thread_id)  # Retrieve existing memory
     
     # Add the human message to memory
     memory.add_message(HumanMessage(content=human_message))  # Timestamps will auto-generate
     
     # Generate and add AI response based on the human message
     ai_response = get_ai_response(human_message)
     memory.add_message(AIMessage(content=ai_response))  # Timestamps will auto-generate
 
 # Save data to long-term memory
 save_short_term_to_long_term(
     thread_ids=[thread_id for thread_id, _ in threads],
     project_name="Exploration of Thomas Cavendish",
     memory_id="cavendish_exploration"
 )
 
 # Optional output for verification
 for thread_id in threads:
     messages = get_memory_by_thread_id(thread_id[0]).messages  # Access messages for the current thread
     if messages:  # Ensure there are messages to display
         latest_message = messages[-1]  # Get the latest message (assumed to be the AI message)
         # Display thread information with content
         print(f"{thread_id[0]}: {latest_message.content}")

::

 # Cell 12
 print("Data successfully saved to JSON. Summary of stored conversations:")
 for thread_id, _ in threads:  # Directly unpack each tuple
     messages = thread_memory_store[thread_id].messages  # Access messages correctly
     message_contents = [message.content for message in messages]
     print(f"{thread_id}: {message_contents}")  # Print summary of message contents

::

 # Cell 13
 # Load and show the long-term memory
 loaded_memories = load_memory_from_json("cavendish_exploration.json")
 
 if loaded_memories:  # Check if any memories were loaded
     for memory in loaded_memories:
         print(f"Project: {memory.project_name}, ID: {memory.memory_id}")
         print("Messages:")
         for message in memory.messages:
             print(f"  - {message.content}")  # Use dot notation to access message content
 else:
     print("No memories found in the JSON file.")

