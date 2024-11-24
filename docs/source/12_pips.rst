.. _12 pips:

12 Pip installations - use only if needed
=======
.. index::

code view 1::

    # Activate the virtual environment
  source /fp/projects01/ec367/username/my_venv/bin/activate
  
  # Start JupyterLab from within the virtual environment
  jupyter lab

code view 1::

  # Install ipykernel if not already installed
  pip install ipykernel
  
  # Add the virtual environment as a Jupyter kernel
  python -m ipykernel install --user --name=my_venv --display-name "Python (my_venv)"

code view 1::

  ## Setting Up the Environment in Jupyter Notebook
  
  To ensure you have all the necessary packages installed in your virtual environment, run the following cells to install them within the Jupyter Notebook.
  
  ### Step 1: Install Packages
  
  Run these cells one by one:
  
  ```python
  # Install transformers
  !pip install transformers==4.45.0

code view 1::

  # Install PyTorch
  !pip install torch==2.0.0

code view 1::

  # Install PyMuPDF
  !pip install PyMuPDF==1.24.12

code view 1::

  # Install regex
  !pip install regex

code view 1::

  # Install TQDM
  !pip install tqdm==4.66.5

code view 1::

  # Install datasets
  !pip install datasets==3.0.1

code view 1::

  # Install sentence-transformers
  !pip install sentence-transformers>=3.2.0

code view 1::


code view 1::
code view 1::
code view 1::

code view 1::
