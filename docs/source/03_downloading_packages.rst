.. _03_downloading_packages:

03 Installing software
========================

We’ll use `LangChain <https://www.langchain.com/>`_, an open-source library for making applications with LLMs. We’ll use models from `HuggingFace <https://huggingface.co/>`_, a website that has tools and models for machine learning.

.. admonition:: Exercise: Create a new notebook
   :collapsible: closed

  Create a new Jupyter Notebook called ``installing`` by clicking the File-menu in JupyterLab, and then New and Notebook. If you are asked to select a kernel, choose “Python 3”. Give the new notebook a name by clicking the File-menu in JupyterLab and then clicking Rename Notebook. Use the name ``installing``.

.. warning ::

  If you usually work with `virtual environments <https://docs.python.org/3/library/venv.html>`_ on Fox, you should setup and activate a virtual environment before you continue, see Bonus: Virtual Environments. If you haven’t heard of virtual environments, you can continue without using virtual environments.

Python packages
----------------

We will use the python package manager ``pip`` for installing software. ``pip`` installs software from the `Python Package Index <https://pypi.org/>`_. First, we update pip to the newest version::

  pip install --upgrade pip

General LLM software
---------------------
Huggingface hub provides publicly available LLMs. `Langchain <https://python.langchain.com/docs/introduction/>`_ provides a framework for developing LLMs, and can be integrated with a number of packages and software.::

  pip install --upgrade huggingface-hub httpx

Packages working with LangChain and HuggingFace::

  pip install --upgrade langchain langchain-community langchain-huggingface

Transformers is the basic technology used in large language models. We install the library ``sentence-transformers``::

   pip install --upgrade sentence-transformers.

The `sentencepiece library <https://github.com/google/sentencepiece/blob/master/README.md>`_ is an unsupervised text tokenizer and detokenizer. It implements sub-word units, and is independent from languages.::

   pip install --upgrade sentencepiece

Software for Reading Text Documents
---------------------------------------

`Unstructured <https://github.com/Unstructured-IO/unstructured/blob/main/README.md>`_ provides software for reading text documents in various formats. The data processing will be more streamlined.::

  pip install --upgrade unstructured[all-docs] langchain-unstructured

Search index
-------------
The `FAISS <https://faiss.ai/>`_ package is used in the :doc:`10_rag` chapter for searching for documents. This package is about searching, clustering and parameter tuning::

  pip install --upgrade faiss-cpu

Model location
-----------------
We tell the system where the model is located. If you run on ec443, the models from Huggingface are already downloaded for you::

  %env HF_HOME=/fp/projects01/ec443/huggingface/cache/

.. admonition:: Optional
   :collapsible: closed

If you run on your own, or want to download a model that is not previously used by the group, you will need to make an account at Huggingface, and store the token you get. Your token can be found under your profile, in the right side of the top menu: "access tokens". For the gated models, you need to apply, before you can download. Your token should be stored in a safe place, and not shared with anyone.

Cell for entering your HF token::

  from huggingface_hub import login
  login()
