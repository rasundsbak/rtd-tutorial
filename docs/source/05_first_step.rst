.. _05 first_step:

05 First step
=======
.. index:: noko

code view::

  #1
  # Endre arbeidskatalogen til prosjektmappen
  
  !export HF_HOME=/fp/projects01/ec367/huggingface/cache
  
  code view::
  
    ! ls -lh /fp/projects01/ec367/huggingface/cache/Llama/Meta-Llama-3-8B-Instruct.Q5_K_M.gguf


code view::

  # Endre arbeidskatalogen til prosjektmappen
import os

os.chdir("/fp/projects01/ec367/palml1")
print(f"Nåværende arbeidskatalog: {os.getcwd()}")

code view:: 

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


code view::

  import sys
  import os
  
  # Sti til ditt virtuelle miljøs site-packages
  #venv_path = '/fp/projects01/ec367/palml1/venv_transformers/lib/python3.9/site-packages'
  venv_path = '/fp/projects01/ec367/palml1/myenv'
  
  # Legg til stien til sys.path
  if venv_path not in sys.path:
      sys.path.append(venv_path)
  
  # Prøv å importere llama_cpp etter å ha lagt til stien
  try:
      import llama_cpp
      print('llama_cpp import successful')
  except ModuleNotFoundError as e:
      print(f"Failed to import llama_cpp: {e}")
  
  # Importere andre nødvendige pakker som transformers
  try:
      from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig
      print('transformers import successful')
  except ModuleNotFoundError as e:
      print(f"Failed to import transformers modules: {e}")
