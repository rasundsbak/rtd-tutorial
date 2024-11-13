.. _05_pirat:
05 Pirate example with .gguf format
==============

Code view::

  # 1
  !export HF_HOME=/fp/projects01/ec367/huggingface/cache

Code view::

  #2
  ! ls -lh /fp/projects01/ec367/huggingface/cache/Llama/Meta-Llama-3-8B-Instruct.Q5_K_M.ggufa

Code view::

  #3
  # renser requirements.txt for navnet på gamle filstier:
  
  import re
  
  def clean_requirements_file(input_file, output_file):
      with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
          for line in infile:
              # Fjern linjen hvis den inneholder @ file:/// eller @ /path/
              if not re.search(r'(@ file:///|@ /|@file:///|@/)', line):
                  outfile.write(line)
              else:
                  # Finn og hent pakkenavn og versjon hvis de finnes på spesifik formatt
                  match = re.match(r'([^@]+)@ .+', line)
                  if match:
                      package_name = match.group(1)
                      outfile.write(f'{package_name}\n')
                  else:
                      # Hvis match ikke finnes, behold linjen som den er
                      outfile.write(line)
  
  input_file = 'requirements.txt'
  output_file = 'cleaned_requirements.txt'
  clean_requirements_file(input_file, output_file)
  print(f"Cleaned requirements written to {output_file}")

Code view::

  #4
  # Endre arbeidskatalogen til prosjektmappen
  import os
  
  os.chdir("/fp/projects01/ec367/ragnhsu")
  print(f"Nåværende arbeidskatalog: {os.getcwd()}")
  
  Code view::
  
  #5
  # Celle 1: Import necessary packages and set up the environment
  import sys
  import os
  
  # Sti til ditt virtuelle miljøs site-packages
  venv_path = '/fp/projects01/ec367/ragnhsu/venv_transformers/lib/python3.9/site-packages'
  
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


####### kopierer fra Pirat 2.gang #########

Code view::

  #1
  !export HF_HOME=/fp/projects01/ec367/huggingface/cache

Code view::

  #2
  ! ls -lh /fp/projects01/ec367/huggingface/cache/Llama/Meta-Llama-3-8B-Instruct.Q5_K_M.ggufa

Code view::

  #3
  # renser requirements.txt for navnet på gamle filstier:
  
  import re
  
  def clean_requirements_file(input_file, output_file):
      with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
          for line in infile:
              # Fjern linjen hvis den inneholder @ file:/// eller @ /path/
              if not re.search(r'(@ file:///|@ /|@file:///|@/)', line):
                  outfile.write(line)
              else:
                  # Finn og hent pakkenavn og versjon hvis de finnes på spesifik formatt
                  match = re.match(r'([^@]+)@ .+', line)
                  if match:
                      package_name = match.group(1)
                      outfile.write(f'{package_name}\n')
                  else:
                      # Hvis match ikke finnes, behold linjen som den er
                      outfile.write(line)
  
  input_file = 'requirements.txt'
  output_file = 'cleaned_requirements.txt'
  clean_requirements_file(input_file, output_file)
  print(f"Cleaned requirements written to {output_file}")

Code view::

  #4
  # Endre arbeidskatalogen til prosjektmappen
  import os
  
  os.chdir("/fp/projects01/ec367/ragnhsu")
  print(f"Nåværende arbeidskatalog: {os.getcwd()}")

Code view::

  #5
  # Celle 1: Import necessary packages and set up the environment
  import sys
  import os
  
  # Sti til ditt virtuelle miljøs site-packages
  venv_path = '/fp/projects01/ec367/ragnhsu/venv_transformers/lib/python3.9/site-packages'
  
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
    
    
 Code view::   

  #6
  # Celle: Kontrollere hvilket Python executable som er i bruk
  import sys
  print(sys.executable)

Code view::

  #7
  # Celle 2: Kontrollere hvilken Python executable som er i bruk
  import sys
  print(f"Python executable in use: {sys.executable}")

Code view::

  #8
  # Celle 3: Endre arbeidskatalogen til prosjektmappen
  import os
  
  os.chdir("/fp/projects01/ec367/ragnhsu")
  print(f"Nåværende arbeidskatalog: {os.getcwd()}")

Code view::

  #9
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
          {"role": "system", "content": "You are a pirate chatbot who always responds in pirate speak in whole sentences!"},
          {"role": "user", "content": "Who are you?"},
          {"role": "user", "content": "Tell me about your ideal boat?"},
      ],
      temperature=0.3,
  )
  
  # Print responsen
  print(response['choices'][0]['message']['content'])

Code view::

  #10
  # Celle 8: Oppdater requirements.txt og installer pakkene
  
  # Eksporter alle installerte pakker til requirements.txt
  !pip freeze > /fp/homes01/u01/ec-ragnhsu/requirements.txt
  
  # Installer pakkene fra requirements.txt med --user flagget
  !pip install --user -r /fp/homes01/u01/ec-ragnhsu/requirements.txt

###### slutt av kopiering fra Naomi_Pirate  #########
