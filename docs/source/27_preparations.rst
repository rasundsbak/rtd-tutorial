.. _27 preparations:

27 Preparing for Slurm and Batch
===================================

.. index:: slurm batch virtual environment

If you have done all the steps until this chapter, you have gotten used to writing python code, and you are ready for the next step. Once we are finished developing the AI-process, we are going to convert our .ipynb files to .py files. A JupyterLab session reserves a GPU all the time, also when you’re not running computations. There is a better way to use the shared computer resources. We will save and export the notebook into an executable script. Sbatch submits a batch script to Slurm. This allows the job to wait in a queue until the resources become available. We can use the code that we already have. However, some preparations before we enter into the new working method is useful.

Virtual environment
--------------------

Terminal view 1::

   # change into the right subdirectory
   cd /fp/projects01/ec443
   
   # make a directory at ec443, where you plan to have your working files
   mkdir **[your username at uio]**

**Be sure to read the details and put in your username before you copy and paste!**

Terminal view 2::

   # making a virtual env for python packages
   python -m venv /fp/projects01/ec443/**[your username at uio]**/my_venv

Checking the content of an existing virtual environment
----------------------------------------------------------

Terminal view 1::

   source /fp/projects01/ec443/ragnhsu/my_venv/bin/activate
   pip list

Installing the requirements via the terminal
----------------------------------------------

Terminal view 1::

   source /fp/projects01/ec443/ragnhsu/my_venv/bin/activate

Terminal view 2::

   pip install --upgrade pip huggingface-hub langchain langchain-community langchain-huggingface sentence-transformers sentencepiece 

Terminal view 3::

   pip install --upgrade unstructured[all-docs] langchain-unstructured

Terminal view 4::

   pip install --upgrade faiss-cpu

Terminal view 5::

   deactivate






