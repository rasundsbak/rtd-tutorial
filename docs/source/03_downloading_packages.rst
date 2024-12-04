.. _03_downloading_packages:

03 Setup and downloading packages
========================

Cell 1::

   # Location of locally downloaded models
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
