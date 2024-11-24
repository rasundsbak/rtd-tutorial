.. _11 pegasus_continued:

11 Pegasus continued
==============
.. index::

We are going to connect the model to our documents. You had the overview over the paths in the previous chapter. You are prepared for connecting the model to your documents. This process is a continuation of the previous chapter. Use the same ipynb file. This chapter has some error search in it. This might be good to know for later.


code view 1::
  # får rar feilmelding "expendable segments", vil sjekke torch versjon.
  import torch
  print(torch.__version__)


code view 1::

  import torch
  print(torch.__version__)  # Should show: 2.0.0+cu117
  
  import torchvision
  print(torchvision.__version__)  # Should show: 0.15.1+cu117

code view 1::

  # Import necessary libraries
  import os
  from transformers import pipeline, PegasusForConditionalGeneration, PegasusTokenizer
  import fitz  # PyMuPDF for PDF conversion, if needed
  import torch
  
  # Define a unique cache directory for the Pegasus-XSum project
  project_cache_dir = "/fp/projects01/ec443/huggingface/cache/Pegasus_XS"
  
  # Create the directory if it does not exist
  os.makedirs(project_cache_dir, exist_ok=True)
  
  # Set environment variables
  os.environ["HF_HOME"] = project_cache_dir
  
  # Confirm that the environment variables are set correctly
  print("HF_HOME:", os.getenv("HF_HOME"))
  
  # Check if GPU is available
  print("Is GPU available?:", torch.cuda.is_available())

code view 1::

  import torch
  
  # Check if GPU is available
  if torch.cuda.is_available():
      num_gpus = torch.cuda.device_count()  # Store the number of GPUs in a variable
      print(f"Number of GPUs: {num_gpus}")
  
      if num_gpus > 0:  # Check if there is at least one GPU
          for i in range(num_gpus):
              print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
              print(f"Memory Allocated (MB): {torch.cuda.memory_allocated(i) / 1024 ** 2:.2f}")
              print(f"Memory Cached (MB): {torch.cuda.memory_reserved(i) / 1024 ** 2:.2f}")
  else:
      print("No GPU available")


code view 1::

  # Count words in the folder CleanTests
  import os
  
  # Specify the folder for text files
  cleantexts_folder = "/fp/projects01/ec443/clean_env/clean_texts"
  
  def read_text_file(file_path):
      """Reads the content of a text file and returns it as a string."""
      with open(file_path, "r", encoding="utf-8") as file:
          return file.read()
  
  def count_words_in_text(text):
      """Counts the number of words in a given text."""
      words = text.split()
      return len(words)
  
  # Dictionary to store the word count per file
  txt_word_counts = {}
  
  # Iterate through each text file in cleantexts_folder
  for filename in os.listdir(cleantexts_folder):
      if filename.endswith(".txt"):
          file_path = os.path.join(cleantexts_folder, filename)
          try:
              # Read text from the file
              text = read_text_file(file_path)
              
              # Count the number of words in the text
              word_count = count_words_in_text(text)
              
              # Store the result in the dictionary
              txt_word_counts[filename] = word_count
              
          except Exception as e:
              print(f"An error occurred processing {filename}: {e}")
  
  # Print the aggregated result in sorted order
  print("\nWord counts for all text files:")
  for filename, word_count in sorted(txt_word_counts.items()):
      print(f"{filename}: {word_count} words")

code view 1::
  
  # Generate summaries for all documents in the "documents" folder
  
  # Import necessary libraries
  import os
  import re
  import fitz  # PyMuPDF for PDF conversion
  from transformers import PegasusForConditionalGeneration, AutoTokenizer
  import torch
  
  # Specify your username
  username = "ec-something"  # <--- Replace "ec-something" with your actual username
  
  # Define a unique cache directory for the Pegasus-XSum project
  project_cache_dir = f"/fp/projects01/ec443/huggingface/cache/Pegasus_XS"
  
  # Create the directory if it doesn't already exist
  os.makedirs(project_cache_dir, exist_ok=True)
  
  # Set environment variables
  os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"
  os.environ["HF_HOME"] = project_cache_dir
  
  # Confirm that the environment variables are set correctly
  print("PYTORCH_CUDA_ALLOC_CONF:", os.getenv("PYTORCH_CUDA_ALLOC_CONF"))
  print("HF_HOME:", os.getenv("HF_HOME"))
  
  # Specify the model name
  model_name = "google/pegasus-xsum"
  
  # Download the model and tokenizer (if not already done)
  model = PegasusForConditionalGeneration.from_pretrained(model_name)
  tokenizer = AutoTokenizer.from_pretrained(model_name)
  
  # Check if GPU is available and set the device
  device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
  model.to(device)
  
  # Function to convert PDF to text
  def convert_pdf_to_text(pdf_path):
      """Converts PDF files to text."""
      doc = fitz.open(pdf_path)
      text = ""
      for page in doc:
          text += page.get_text()
      return text
  
  # Function to remove ISSN numbers, DOIs, and technical headers from the text
  def clean_text(text):
      """Removes ISSN numbers, DOIs, technical headers (TABLE, FIGURE), and excludes the reference list from the text."""
      text = re.sub(r'\bISSN\s\d{4}-\d{3}[\dX]\b', '', text, flags=re.IGNORECASE)
      text = re.sub(r'https?://doi\.org/[^\s]+', '', text, flags=re.IGNORECASE)
      text = re.sub(r'\bTABLE\s\d+\.?\s*\..*', '', text, flags=re.IGNORECASE)
      text = re.sub(r'\bFIGURE\s\d+\.?\s*\..*', '', text, flags=re.IGNORECASE)
      references_start = text.lower().find("references")
      if references_start != -1:
          text = text[:references_start].strip()
      return text
  
  # Function to generate a summary
  def generate_summary(text, model, tokenizer, summary_percentage=0.4, num_beams=10, length_penalty=0.3, no_repeat_ngram_size=2):
      """Generates summaries using the Pegasus model with adjustable parameters."""
      num_tokens = len(tokenizer.encode(text, truncation=True, padding=True))
      target_length = int(num_tokens * summary_percentage)
      max_length = target_length
      min_length = int(target_length * 0.9)
      # Tokenization
      tokens = tokenizer(text, truncation=True, padding="longest", return_tensors="pt").to(device)
      # Generation
      summary_ids = model.generate(tokens.input_ids,
                                   max_length=max_length, 
                                   num_beams=num_beams, 
                                   length_penalty=length_penalty, 
                                   min_length=min_length,
                                   no_repeat_ngram_size=no_repeat_ngram_size, 
                                   early_stopping=False)
      summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
      return summary
  
  # Specify the folder for PDF documents and the output folder for summaries
  documents_folder = f"/fp/homes01/u01/{username}/documents"
  summaries_folder = f"/fp/homes01/u01/{username}/summaries_x"
  
  # Create the summaries folder if it doesn't already exist
  os.makedirs(summaries_folder, exist_ok=True)
  
  # Process each PDF file in the documents_folder
  for filename in os.listdir(documents_folder):
      if filename.endswith(".pdf"):
          file_path = os.path.join(documents_folder, filename)
          try:
              # Convert PDF to text
              pdf_text = convert_pdf_to_text(file_path)
              
              # Clean the text to remove ISSN numbers, DOIs, technical headers, and reference list
              cleaned_text = clean_text(pdf_text)
              
              # Generate a summary for the main text
              summary = generate_summary(cleaned_text, model, tokenizer, summary_percentage=0.4)  # Here we increase to 40%
              
              # Save the summary as a single .txt file in summaries_folder
              summary_filename = os.path.splitext(filename)[0] + "_summary.txt"
              summary_path = os.path.join(summaries_folder, summary_filename)
              
              with open(summary_path, "w", encoding="utf-8") as summary_file:
                  summary_file.write("Main Text Summary:\n" + summary + "\n\n")
              
              print(f"Generated summary for {filename}")
          except Exception as e:
              print(f"An error occurred processing {filename}: {e}")
  
  print("All summaries have been generated.")

This cell is heavy for beginners but well-structured documentation and in-line comments make it comprehensible. Chunking is essential given the document sizes, ensuring that the Pegasus model processes the text effectively.

code view 1::

  # Generate summaries for all documents in the "documents" folder
  
  # Import necessary libraries
  import os
  import re
  import fitz  # PyMuPDF for PDF conversion
  from transformers import PegasusForConditionalGeneration, AutoTokenizer
  import torch
  
  # Define your username
  username = "ec-something"  # <--- Replace "ec-something" with your actual username
  
  # Define a unique cache directory for the Pegasus-XSum project
  project_cache_dir = f"/fp/projects01/ec443/huggingface/cache/Pegasus_XS"
  
  # Create the directory if it doesn't already exist
  os.makedirs(project_cache_dir, exist_ok=True)
  
  # Set environment variables
  os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"
  os.environ["HF_HOME"] = project_cache_dir
  
  # Confirm that the environment variables are set correctly
  print("PYTORCH_CUDA_ALLOC_CONF:", os.getenv("PYTORCH_CUDA_ALLOC_CONF"))
  print("HF_HOME:", os.getenv("HF_HOME"))
  
  # Specify the model name
  model_name = "google/pegasus-xsum"
  
  # Download the model and tokenizer (if not already done)
  model = PegasusForConditionalGeneration.from_pretrained(model_name)
  tokenizer = AutoTokenizer.from_pretrained(model_name)
  
  # Check if GPU is available and set the device
  device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
  model.to(device)
  
  # Define summary parameters
  summary_parameters = {
      "summary_percentage": 0.4,  # Percentage of text to use for summary
      "num_beams": 10,            # Number of beams for beam search
      "length_penalty": 0.3,      # Length penalty
      "no_repeat_ngram_size": 2   # No repeated n-grams
  }
  
  # Function to convert PDF to text
  def convert_pdf_to_text(pdf_path):
      """Converts PDF files to text."""
      doc = fitz.open(pdf_path)
      text = ""
      for page in doc:
          text += page.get_text()
      return text
  
  # Function to remove ISSN numbers, DOIs, and technical headers from text
  def clean_text(text):
      """Removes ISSN numbers, DOIs, technical headers (TABLE, FIGURE), and excludes the reference list from the text."""
      text = re.sub(r'\bISSN\s\d{4}-\d{3}[\dX]\b', '', text, flags=re.IGNORECASE)
      text = re.sub(r'https?://doi\.org/[^\s]+', '', text, flags=re.IGNORECASE)
      text = re.sub(r'\bTABLE\s\d+\.?\s*\..*', '', text, flags=re.IGNORECASE)
      text = re.sub(r'\bFIGURE\s\d+\.?\s*\..*', '', text, flags=re.IGNORECASE)
      references_start = text.lower().find("references")
      if references_start != -1:
          text = text[:references_start].strip()
      return text
  
  # Function to split text into chunks
  def chunk_text(text, chunk_size=1024):
      """Splits the text into smaller chunks of a given size."""
      text_chunks = []
      for i in range(0, len(text), chunk_size):
          text_chunks.append(text[i:i + chunk_size])
      return text_chunks
  
  # Function to generate a summary
  def generate_summary(text, model, tokenizer, params):
      """Generates summaries using the Pegasus model with adjustable parameters."""
      summary_percentage = params["summary_percentage"]
      num_beams = params["num_beams"]
      length_penalty = params["length_penalty"]
      no_repeat_ngram_size = params["no_repeat_ngram_size"]
      
      # Split the text into chunks if necessary
      text_chunks = chunk_text(text)
      summaries = []
      
      for chunk in text_chunks:
          num_tokens = len(tokenizer.encode(chunk, truncation=True, padding=True))
          target_length = int(num_tokens * summary_percentage)
          max_length = target_length
          min_length = int(target_length * 0.9)
          
          # Tokenization
          tokens = tokenizer(chunk, truncation=True, padding="longest", return_tensors="pt").to(device)
          
          # Generation
          summary_ids = model.generate(tokens.input_ids,
                                       max_length=max_length, 
                                       num_beams=num_beams, 
                                       length_penalty=length_penalty, 
                                       min_length=min_length,
                                       no_repeat_ngram_size=no_repeat_ngram_size, 
                                       early_stopping=True)
          chunk_summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
          summaries.append(chunk_summary)
      
      return " ".join(summaries)
  
  # Specify the folder for PDF documents and the output folder for summaries
  documents_folder = f"/fp/homes01/u01/{username}/documents"
  summaries_folder = f"/fp/homes01/u01/{username}/summaries_2"
  
  # Create the summaries folder if it doesn't already exist
  os.makedirs(summaries_folder, exist_ok=True)
  
  # Process each PDF file in the documents_folder
  for filename in os.listdir(documents_folder):
      if filename.endswith(".pdf"):
          file_path = os.path.join(documents_folder, filename)
          try:
              # Convert PDF to text
              pdf_text = convert_pdf_to_text(file_path)
              
              # Clean the text to remove ISSN numbers, DOIs, technical headers, and reference list
              cleaned_text = clean_text(pdf_text)
              
              # Generate a summary for the main text
              summary = generate_summary(cleaned_text, model, tokenizer, summary_parameters)
              
              # Save the summary as a single .txt file in summaries_folder
              summary_filename = os.path.splitext(filename)[0] + "_summary.txt"
              summary_path = os.path.join(summaries_folder, summary_filename)
              
              with open(summary_path, "w", encoding="utf-8") as summary_file:
                  summary_file.write("Main Text Summary:\n" + summary + "\n\n")
              
              print(f"Generated summary for {filename}")
          except Exception as e:
              print(f"An error occurred processing {filename}: {e}")
  
  print("All summaries have been generated.")

.. note::

  Task 11:1: Use copy cell in jupyter lab in order to get e a copy of the summarization cell. Change some of the parameters, and see if the output changes. Remember to change the values of the "documents" path before you run and generate new output. See cell below for illustration.

code view 1::

  # Specify the folder for PDF documents and the output folder for summaries
  documents_folder = f"/fp/homes01/u01/{username}/documents"
  summaries_folder = f"/fp/homes01/u01/{username}/summaries_2"

code view 1::

  # Congratulations. You have now finishes the workshop
  # on how to Run large language models (LLM) through Educloud UiO
  # We hope to see you again!
