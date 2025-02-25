.. _27 preparations:
Preparing for Slurm and Batch
==============================
.. index:: slurm batch virtual environment

If you have done all the steps until this chapter, you have gotten used to writing puthon code, and you are readu for the next step. Once we are finished developing the AI-process, we are going to convert our .ipynb files to .py files. A JupyterLab session reserves a GPU all the time, also when you’re not running computations. This is the reason why it is desirable that we save and export the notebook into an executable script. Sbatch submits a batch script to Slurm. This allows the job to wait in a queue until the resources become available. We can use a lot of the code that we already have. However, some preparations before we enter into the new working method is useful.


Terminal view 4::

   # change into the right subdirectory
   cd /fp/projects01/ec443
   
   # make a directory at ec443, where you plan to have your working files
   mkdir **[your username at uio]**

**Be sure to read the details and put in your username before you copy and paste!**

Terminal view 5::

   # making a virtual env for python packages
   python -m venv /fp/projects01/ec443/**[your username at uio]**/my_venv
   
Terminal view 6::

   # Aktivér ditt venv
   source /fp/projects01/ec443/**[your username at uio)**/my_venv/bin/activate
