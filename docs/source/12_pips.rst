.. _12 pips:

12 Pip installations - use only if needed
=======
.. index::

code view 1::

    # Activating the Virtual Environment
    # Before starting, activate your virtual environment and start JupyterLab:
    # Replace username with your actual username.
    
    ```bash
    # Activate the virtual environment
    source /fp/projects01/ec443/username/my_venv/bin/activate

Run these cells one my one in Juputer lab:

code view 2::

  # Install ipykernel if not already installed
  pip install ipykernel
  
  # Add the virtual environment as a Jupyter kernel
  python -m ipykernel install --user --name=my_venv --display-name "Python (my_venv)"

To ensure you have all the necessary packages installed in your virtual environment, run the following cells to install them within the Jupyter Notebook.
code view 3::

  # Setting Up the Environment in Jupyter Notebook
  # Install transformers
  !pip install transformers==4.45.0

code view 4::

  # Install PyTorch
  !pip install torch==2.0.0

code view 5::

  # Install PyMuPDF
  !pip install PyMuPDF==1.24.12

code view 6::

  # Install regex
  !pip install regex

code view 7::

  # Install TQDM
  !pip install tqdm==4.66.5

code view 8::

  # Install datasets
  !pip install datasets==3.0.1

code view 9::

  # Install sentence-transformers
  !pip install sentence-transformers>=3.2.0
