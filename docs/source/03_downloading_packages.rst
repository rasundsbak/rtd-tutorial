.. _03_downloading_packages:

03 Startup and downloading packages
========================

In this course, we have tried to make it easy for you, through making the code available. We still have to spend some time familiarizing outselves with copying, pasting and running the code in the cells of Jupyter lab.


.. note::

  Task 3.1: Look around in Jupyter lab, and try googling subjects like "jupyter lab cheat sheet" and "run cell jupyter lab".

Jupyter lab keyboard shortcuts
---------------------

It might be useful for you to look at some `Jupyter lab shortcuts <https://gist.github.com/discdiver/9e00618756d120a8c9fa344ac1c375ac>`_

.. image:: jupyter_lab_menu.png

Hello world
--------------
.. note::

  Task 3.2: Explore the top menu of jupyter lab, and see what is behind categories like File, Edit, View and Run. How do you add or remove cells in a .ipynb document?

.. note::

  Task 3.3: Copy the content of the cell below, and run it in Jupyter lab, in an .ipynb document.


Run this Cell::

  print('Hello, world.')


.. note::

  Task 3.3: How do we run a cell in Jupyter lab? Try to find shortcut and the menues.

  Task 3.4: How do we stop a cell from running?

  Task 3.5: How do we change the content of a cell from markdown to code, and back again? What is the point with this?


This works on "small" Nvidia machines, only they have GPU. UiO: MIG and RTX
-------------------------

We are going to download packages. We have to do this the first time we are going to use the models. The second and thirs time, you may neutralice the !pip install code with a # in front of the cell.

Cell 1::

   # Make installations
   !pip install --upgrade pip huggingface-hub langchain langchain-community langchain-huggingface sentence-transformers    sentencepiece

Output:


Cell 2::

   # !pip install --upgrade unstructured[all-docs] langchain-unstructured

Output example:

Cell 3::
  
  !pip install --upgrade faiss-cpu

Output

We enter the location of the model. You should navigate to this location in the browser interface, and have a look at the models.

Cell 4::

  %env HF_HOME=/fp/projects01/ec443/huggingface/cache/

We are importing a module from the library. This allows us to set up a pipeline that can perform tasks such as text generation from the model.

Cell 5::
  
  from langchain_huggingface.llms import HuggingFacePipeline

Cell 6::

  model_id = 'mistralai/Mistral-7B-Instruct-v0.3'

Cell 7::

  task = 'text-generation'

Cell 8::

  

Cell 4::

   ! pip install llama-cpp-python

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

.. note::

   Task 3.6: Copy the cell above and change the temperature to 10.0. Run the cell.


