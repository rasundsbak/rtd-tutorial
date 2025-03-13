.. _03_downloading_packages:

03 Installering
=================

We’ll use LangChain, an open-source library for making applications with LLMs. We’ll use models from HuggingFace, a website that has tools and models for machine learning.

Exercise: Create new notebook

Create a new Jupyter Notebook called installing by clicking the File-menu in JupyterLab, and then New and Notebook. If you are asked to select a kernel, choose “Python 3”. Give the new notebook a name by clicking the File-menu in JupyterLab and then clicking Rename Notebook. Use the name installing.
General LLM Software

We will install LangChain and HuggingFace software first. Transformers is the basic technology used in large language models, so we install the library sentence-transformers as well. Models use the sentencepiece library, so we’ll need that as well.

!pip install --upgrade pip 
!pip install --upgrade huggingface-hub
!pip install --upgrade langchain
!pip install --upgrade langchain-community langchain-huggingface
!pip install --upgrade sentence-transformers
!pip install --upgrade sentencepiece

Software for Reading Text Documents

We will use unstructured for reading documents. Unstructured supports different document formats, like PDFs, Word files and plain text documents.

!pip install --upgrade unstructured[all-docs] langchain-unstructured

Search Index

For the RAG chapter we will use FAISS to search for documents.

!pip install --upgrade faiss-cpu

The Language Model

We’ll use models from HuggingFace, a website that has tools and models for machine learning. We’ll use the open-weights LLM mistralai/Ministral-8B-Instruct-2410 for most of our tasks. This model has 8 billion parameters. For comparison, one of the largest LLMs at the time of writing is Llama 3.1, with 405 billion parameters. Still, Ministral-8B-Instruct-2410 is around 16 GB, which makes it a quite large model. To run it, we must have a GPU with at least 20 GB memory. It can also be run without a GPU, but that will be much slower.

%env HF_HOME=/fp/projects01/ec443/huggingface/cache/

Optional

If you’re running one of the models that is already downloaded Educloud/Fox project ec443 the model, you can skip this step. If you’re not running on Educloud/Fox project ec443 or want to use a model that isn’t already downloaded, you’ll need to download the model.

You will need a User Access Token from HuggingFace. If you don’t already have a user account on HuggingFace, you must first sign up for one. Click the button “Sign Up” in the upper right corner on HuggingFace.

When you have logged in to HuggingFace with your user account, you can create a User Access Token giving read access by following this guide.

from huggingface_hub import login
login()
