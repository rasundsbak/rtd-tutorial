.. _08_pirat:
08 Summarization
==============

We will use `LangChain <https://www.langchain.com/>`_, an open-source library for making applications with LLMs. The documents should be in your Home Directory, in a folder named "documents". We have 5 documents in pdf that contain a test search on terms terrorism and europe. When you have run this process, you may of course replace the documents with your own data.

Cell  1::

  #document_folder = 'documents'
  #document_folder = '../summarizing'
  document_folder = '../documents'
  

Cell 2::

  # Endre arbeidskatalogen til prosjektmappen
  import os
  
  # Sett brukernavnet til studentene
  username = "your username no ec"  # Studentene må endre dette til sitt faktiske brukernavn
  
  # Definer sti til prosjektmappen
  project_dir = f"/fp/projects01/ec443/{username}"
  
  # Endre arbeidskatalogen
  os.chdir(project_dir)
  print(f"Nåværende arbeidskatalog: {os.getcwd()}")

Cell 3::

  # Importer nødvendige moduler
  import sys
  import os
  
  # Sett brukernavnet til studentene
  username = "your username no ec"  # Studentene må endre dette til sitt faktiske brukernavn
  
  # Sti til ditt virtuelle miljøs site-packages
  venv_path = f'/fp/projects01/ec443/{username}/my_venv/lib/python3.9/site-packages'
  
  # Legg til stien til sys.path hvis den ikke allerede er der
  if venv_path not in sys.path:
      sys.path.append(venv_path)
  
  # Prøv å importere nødvendige pakker
  try:
      import llama_cpp
      print('llama_cpp import successful')
  except ModuleNotFoundError as e:
      print(f"Failed to import llama_cpp: {e}")
  
  try:
      import transformers
      from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig
      print('transformers import successful')
  except ModuleNotFoundError as e:
      print(f"Failed to import transformers: {e}")
  
  try:
      import torch
      print('torch import successful')
  except ModuleNotFoundError as e:
      print(f"Failed to import torch: {e}")

Cell 4::

  # Kontrollere hvilken Python executable som er i bruk
  import sys
  print(f"Python executable in use: {sys.executable}")

**The pirate example**

Cell 5::

  # Angi stien til Hugging Face cache (felles for alle)
  cache_base_path = "/fp/projects01/ec443/huggingface/cache/Llama"
  
  # Sti til den kvantiserte modellfilen
  quantized_modelfile_path = f"{cache_base_path}/Meta-Llama-3-8B-Instruct.Q5_K_M.gguf"
  
  # Importere Llama-klassen fra llama_cpp-pakken
  from llama_cpp import Llama
  
  # Initialiser modellen med riktig filsti
  lcpp_model = Llama(
      model_path=quantized_modelfile_path,  # Path to the quantized model file
      chat_format="chatml",  # Using the 'chatml' format for conversations
      n_gpu_layers=-1  # Running on CPU (no GPU layers)
  )
  
  # Lage en chat completion
  response = lcpp_model.create_chat_completion(
      messages=[
          {"role": "system", "content": "You are a pirate chatbot who always responds in pirate speak in whole sentences!"},
          {"role": "user", "content": "Who are you?"},
          {"role": "user", "content": "Tell me about your ideal boat?"},
      ],
      temperature=0.3,
  )
  
  # Print responsen
  print(response['choices'][0]['message']['content'])


**The economist example**

Cell 6::

    # Importing the Llama class from the llama_cpp package
    from llama_cpp import Llama
    
    # Angi stien til den kvantiserte modellfilen
    quantized_modelfile_path = "/fp/projects01/ec367/huggingface/cache/Llama/Meta-Llama-3-8B-Instruct.Q5_K_M.gguf"
    
    # Initialiser modell med riktig filsti
    lcpp_model = Llama(
        model_path=quantized_modelfile_path,  # Path to the quantized model file
        chat_format="chatml",  # Using the 'chatml' format for conversations
        n_gpu_layers=-1  # Running on CPU (no GPU layers)
    )
    
    # Lage en chat completion
    response = lcpp_model.create_chat_completion(
        messages=[
            {"role": "system", "content": "You are a world class economist chatbot who always responds in understandable speak in whole sentences!"},
            {"role": "user", "content": "Who are you?"},
            {"role": "user", "content": "Tell me about income equality and colonial history?"},
        ],
        temperature=0.3,
    )
    
    # Print responsen
    print(response['choices'][0]['message']['content'])

.. note::

  Task 8.1: Copy one of the prompting cells in Jupyter lab, and make your own prompt where you make your own role for the AI and ask it Who are you, and a question that you would like it to answer.

Cell inspiration for task 8.1::

    # Lage en chat completion
    response = lcpp_model.create_chat_completion(
        messages=[
            {"role": "system", "content": "You are a world class economist chatbot who always responds in understandable speak in whole sentences!"},
            {"role": "user", "content": "Who are you?"},
            {"role": "user", "content": "Tell me about income equality and colonial history?"},
        ],
        temperature=0.3,
    )


.. note::
  Task 8.2: Save your jupyter notebook in your home directory in jupyter lab, and open a new one. Check that you have ordered enough time on the Fox for the next lesson.




