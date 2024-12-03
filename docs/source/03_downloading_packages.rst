.. _03_downloading_packages:
03 Setup and downloading packages
========================

Cell 1::

   # Set paths
   # It is expected that following modules are already loaded
   # module load PyTorch-bundle/2.1.2-foss-2023a-CUDA-12.1.1
   # module load Transformers/4.39.3-gfbf-2023a
   # Set the location for extra pacakages That are not provided by the modules
   # A directory with the same name as EXTRA_PACKAGES_DIR should not exist 
   # in your home directory, for best reproducibility of exercises
   import sys
   import os
   # Your home directory
   HOME_DIR=os.getenv('HOME')
   # The new directory you want to create to store the pakages
   EXTRA_PACKAGES_DIR="llm-tutorial3"
   # The location for pip install
   EXTRA_PACKAGES_PATH_PIP=HOME_DIR+"/"+EXTRA_PACKAGES_DIR
   # The location for jupyter 
   EXTRA_PACKAGES_PATH_JUPYTER=EXTRA_PACKAGES_PATH_PIP+"/lib/python3.11/site-packages/"
   
   # This is needed to inform pip 
   # to avoid reinstalling everytime, PYTHONPATH could be updated(not done here)
   os.environ['EXTRA_PACKAGES_PATH_PIP'] = EXTRA_PACKAGES_PATH_PIP
   
   
   # This is needed so that jupyter can find thr pakages
   if EXTRA_PACKAGES_PATH_JUPYTER not in sys.path:
       sys.path.append(EXTRA_PACKAGES_PATH_JUPYTER)
   
   
   # Locaiton of locally downloaded models
   HF_HOME="/fp/projects01/ec443/huggingface/cache"
   os.environ['HF_HOME'] = HF_HOME
   
   os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"
   
   
   # Angi stien til den kvantiserte modellfilen
   quantized_modelfile_path = "/fp/projects01/ec443/huggingface/cache/Llama/Meta-Llama-3-8B-Instruct.Q5_K_M.gguf"
   
   # test by printing
   print(EXTRA_PACKAGES_PATH_JUPYTER)
   ! echo $EXTRA_PACKAGES_PATH_PIP


Cell 2::

   # install the extra pakages in EXTRA_PACKAGES_PATH
   # list of pakages seperated with a space 
   #! pip install --prefix=$EXTRA_PACKAGES_PATH frontend starlette tools
   #! pip install --prefix=$EXTRA_PACKAGES_PATH_PIP PyMuPDF 
   #! pip install --user PyMuPDF

Cell 3::

   # Path to the requirements.txt file
   requirements_path = "/fp/projects01/ec443/clean_env/cleaned_requirements_2.txt"
   
   # Function to install packages from a requirements file
   def install_requirements(requirements_path, venv_path):
       subprocess.check_call([os.path.join(venv_path, "bin", "python"), "-m", "pip", "install", "-r", requirements_path])
       print("All dependencies are installed.")
   
   # Install the requirements
   install_requirements(requirements_path, venv_path)
   print("All dependencies have been installed.")
   # Inni requirements.txt, triton==2.0.0  # Endret til kompatibel versjon


Cell 4::

   #! pip install --upgrade pip
   
Cell 5::

   # Test : check from wich location the pakage is loading from
   # Here it should load from EXTRA_PACKAGES_PATH_JUPYTER
   import pymupdf as pkg
   print("PyMuPDF is loading from: "+pkg.__file__)

**Deretter kjører du denne**
Cell 6::
   
   # Install regex
   #!pip install regex
   
   # Install TQDM
   #!pip install tqdm==4.66.5
   #!pip install tqdm
   
   # Install datasets
   #! pip install datasets==3.0.1
   
   # Install sentence-transformers
   # !pip install sentence-transformers>=3.2.0

Cell 7::

   # Sjekker at alle pakker kan installeres uten problemer:
   import pymupdf
   import regex
   import tqdm
   import datasets
   import sentence_transformers
   print("All packages are successfully imported.")




