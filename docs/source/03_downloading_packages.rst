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

Output:
Requirement already satisfied: joblib>=1.2.0 in /cluster/software/EL9/easybuild/software/Python-bundle-PyPI/2023.06-GCCcore-12.3.0/lib/python3.11/site-packages (from scikit-learn->sentence-transformers) (1.2.0)
Requirement already satisfied: threadpoolctl>=3.1.0 in /cluster/software/EL9/easybuild/software/Python-bundle-PyPI/2023.06-GCCcore-12.3.0/lib/python3.11/site-packages (from scikit-learn->sentence-transformers) (3.1.0)
Requirement already satisfied: anyio in /cluster/software/EL9/easybuild/software/jupyter-server/2.7.2-GCCcore-12.3.0/lib/python3.11/site-packages (from httpx<1,>=0.23.0->langsmith<0.2.0,>=0.1.17->langchain) (3.7.1)
Requirement already satisfied: httpcore==1.* in ./.local/lib/python3.11/site-packages (from httpx<1,>=0.23.0->langsmith<0.2.0,>=0.1.17->langchain) (1.0.7)
Requirement already satisfied: h11<0.15,>=0.13 in ./.local/lib/python3.11/site-packages (from httpcore==1.*->httpx<1,>=0.23.0->langsmith<0.2.0,>=0.1.17->langchain) (0.14.0)
Requirement already satisfied: jsonpointer>=1.9 in ./.local/lib/python3.11/site-packages (from jsonpatch<2.0,>=1.33->langchain-core<0.4.0,>=0.3.21->langchain) (3.0.0)
Requirement already satisfied: mypy-extensions>=0.3.0 in ./.local/lib/python3.11/site-packages (from typing-inspect<1,>=0.4.0->dataclasses-json<0.7,>=0.5.7->langchain-community) (1.0.0)
Requirement already satisfied: MarkupSafe>=2.0 in /cluster/software/EL9/easybuild/software/Python-bundle-PyPI/2023.06-GCCcore-12.3.0/lib/python3.11/site-packages (from jinja2->torch>=1.11.0->sentence-transformers) (2.1.3)
Requirement already satisfied: sniffio>=1.1 in /cluster/software/EL9/easybuild/software/jupyter-server/2.7.2-GCCcore-12.3.0/lib/python3.11/site-packages (from anyio->httpx<1,>=0.23.0->langsmith<0.2.0,>=0.1.17->langchain) (1.3.0)
Using cached packaging-24.2-py3-none-any.whl (65 kB)
Installing collected packages: packaging
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
datasets 3.1.0 requires requests>=2.32.2, but you have requests 2.31.0 which is incompatible.
Successfully installed packaging-24.2
...and more

Cell 3::

Output:


Cell 4::

Output:

Cell 5::


Cell 6::
   


Cell 7::
