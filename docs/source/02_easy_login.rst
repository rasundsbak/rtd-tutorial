.. _02_easy_login:
02 Login to browser: Easy way
=====================
.. index:: Fox, server, A100, GPU, hardware, NVIDIA

Fox has a GPU accelerated part of the system, with four NVIDIA A100 cards each, as well as three nodes with four NVIDIA RTX 3090 cards from IFI. These systems of hardware are fit for running AI on.


How to order a job on the Fox
____________________________
When you are logged on to `the Fox <https://ood.educloud.no/>`_, move like this: from the left menu, go to Jupyter lab --> ec443 Choose one of the Nvidia GPUs from the drop down menu --> Rumtime. 1h --> Jupyter variant, Jupyter lab --> Choose Jupyter module 12.3.0. Make sure you have loaded the correct modules in the box for "Additional modules (optional)" -->  Launch. You are now in the line to get into the Jupyter lab on UiO Fox. You can get tea or coffee, and have a chat with your colleague, while you wait. The waiting time depends on how much you are asking for, when it comes to machine power and time.

.. warning:: 

  Try to get used to experiencing small technical problems like the kernel stops. These are just annoying hickups and usually don't make to much problem.

.. image:: fox_skjermbilde.png

In the additional modules (optional)::

  module load PyTorch-bundle/2.1.2-foss-2023a-CUDA-12.1.1 module load Transformers/4.39.3-gfbf-2023a


.. image:: fox_top_menu.png

.. note::

  Task 2.1: 2 mins. Explore the top menu and look into the folders. What does it look like? Familiarize yourself with the browser view of Fox. For a beginner, it is useful to learn how to copy paths and move or copy files and folders between the project area and the Home Directory.

.. note::

  Task 2.2: 2 mins. How do you copy or move files in the browser view? Hint, mark the file, and click on Move/Copy
