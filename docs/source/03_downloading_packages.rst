.. _03_downloading_packages:

03 Installing software
========================

We’ll use LangChain, an open-source library for making applications with LLMs. We’ll use models from HuggingFace, a website that has tools and models for machine learning.

.. admonition:: Exercise: Create a new notebook
   : collapsible: closed

  Create a new Jupyter Notebook called installing by clicking the File-menu in JupyterLab, and then New and Notebook. If you are asked to select a kernel, choose “Python 3”. Give the new notebook a name by clicking the File-menu in JupyterLab and then clicking Rename Notebook. Use the name installing.

.. warning ::

  If you usually work with virtual environments on Fox, you should setup and activate a virtual environment before you continue, see Bonus: Virtual Environments. If you haven’t heard of virtual environments, you can continue without using virtual environments.

Cell 1::

  # General LLM Software  
  !pip install --upgrade pip 
  !pip install --upgrade huggingface-hub
  !pip install --upgrade langchain
  !pip install --upgrade langchain-community langchain-huggingface
  !pip install --upgrade sentence-transformers
  !pip install --upgrade sentencepiece


Cell 2::

  # Software for reading text documents
  !pip install --upgrade unstructured[all-docs] langchain-unstructured


Cell 3::

  # Search index
  !pip install --upgrade faiss-cpu


If you run on ec443, you do not need to log into Huggingface. This is why next cell is optional. If you run on your own, or want to download a model that is not previously used by the group, you will need to make an account at Huggingface, and store the token you get. In that case you will be able to find the token under your profile, in the right side of the top menu "access tokens". For the gated models, you need to apply, before you are allowed to download. We recommend that you store your token in a safe place, and do not share it with anyone.

Cell 4::

  %env HF_HOME=/fp/projects01/ec443/huggingface/cache/

Optional cell for entering your HF token::

  from huggingface_hub import login
  login()
