.. _28 problem solving:

28 Problem solving
=====================
.. index::

code view 1::

  !pip install --upgrade pip

code view 2::

  # reset the main to match the main
  # local changes will be removed 
  # use only if you have backup on the changes you want to keep
  git reset --hard origin/main


code view 3::

  # fetch and downnoad content from the remote repository, and update on your local
  git pull

code view 4::

  # See what is changed:
  git log --oneline

code view 5::

  # Where are my kernels?
  $ jupyter kernelspec list

  Available kernels:
    llm        /fp/homes01/u01/[your username]/.local/share/jupyter/kernels/llm
    python3    /cluster/software/EL9/easybuild/software/jupyter-server/2.14.0-GCCcore-13.2.0/share/jupyter/kernels/python3


code view 6::

  # Setting up the remote again (use if it does not respind to the reset for instance):
  git remote add origin https://github.com/uio-library/LLM-course.git


code view 7::

  # fetch and merge updates
  git fetch origin
  git merge origin/main


code view 8::

  # alternative to above
  git pull origin main

code view 9::
