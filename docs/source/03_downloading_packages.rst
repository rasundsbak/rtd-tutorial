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

Cell 1::

   # Location of locally downloaded models
   # %env HF_HOME=/fp/projects01/ec443/huggingface/cache/Llama
   %env HF_HOME=/fp/projects01/ec443/huggingface/cache/

Output:
env: HF_HOME=/fp/projects01/ec443/huggingface/cache/

Cell 2::

   !pip install --upgrade huggingface-hub langchain langchain-community sentence-transformers sentencepiece

Output example:
Requirement already satisfied: joblib>=1.2.0 in /cluster/software/EL9/easybuild/software/Python-bundle-PyPI/2023.06-GCCcore-12.3.0/lib/python3.11/site-packages (from scikit-learn->sentence-transformers) (1.2.0)

Requirement already satisfied: threadpoolctl>=3.1.0 in /cluster/software/EL9/easybuild/software/Python-bundle-PyPI/2023.06-GCCcore-12.3.0/lib/python3.11/site-packages (from scikit-learn->sentence-transformers) (3.1.0)

Requirement already satisfied: anyio in /cluster/software/EL9/easybuild/software/jupyter-server/2.7.2-GCCcore-12.3.0/lib/python3.11/site-packages (from httpx<1,>=0.23.0->langsmith<0.2.0,>=0.1.17->langchain) (3.7.1)

Requirement already satisfied: httpcore==1.* in ./.local/lib/python3.11/site-packages (from httpx<1,>=0.23.0->langsmith<0.2.0,>=0.1.17->langchain) (1.0.7)

Requirement already satisfied: h11<0.15,>=0.13 in ./.local/lib/python3.11/site-packages (from httpcore==1.*->httpx<1,>=0.23.0->langsmith<0.2.0,>=0.1.17->langchain) (0.14.0)

Requirement already satisfied: jsonpointer>=1.9 in ./.local/lib/python3.11/site-packages (from jsonpatch<2.0,>=1.33->langchain-core<0.4.0,>=0.3.21->langchain) (3.0.0)

...and more

Cell 3::

   from huggingface_hub import login
   login()

Output:
(image)

Copy a token from your Hugging Face tokens page and paste it below.


Immediately click login after copying your token or it might be stored in plain text in this notebook file.

Token:
​
Add token as git credential?

**Pro Tip:** If you don't already have one, you can create a dedicated 'notebooks' token with 'write' access, that you can then easily reuse for all notebooks.

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


