.. _02_easy_login:

02 Login to browser: Easy way
=================================
.. index:: Fox, server, A100, GPU, hardware, NVIDIA

Fox has a GPU accelerated part of the system, with four NVIDIA A100 cards each, as well as three nodes with four NVIDIA RTX 3090 cards from IFI. These systems of hardware are fit for running AI on.


How to order a job on the Fox
------------------------------

When you are logged on to `the Fox <https://ood.educloud.no/>`_, move like this: from the left menu, go to Jupyter lab --> ec443 Choose one of the Nvidia GPUs from the drop down menu --> Rumtime. 1h --> Jupyter variant, Jupyter lab --> (You need not choose jupyter module, as the last version is pre selected) -->  Launch. You are now in the line to get into the Jupyter lab on UiO Fox. The waiting time depends on how much machine power and time you are asking for.

How much machine power do I need?
----------------------------------
Some of these processes, like installing or simply punching code in Jupyter Lab, without executing it, can be done on any machine on Fox. When it comes to operations like Rag or Chatbot, it is better performed on a stronger machine with GPU.

.. image:: fox_skjermbilde.png

.. note::

  Task 2.1: Explore the top menu and look into the folders. What does it look like? Familiarize yourself with the browser view of Fox. For a beginner, it is useful to learn how to copy paths and move or copy files and folders between the project area and the Home Directory.

.. image:: fox_top_menu.png

.. note::

  Task 2.2: Look for the left menu in the browser view. Go to Home directory --> New directory (White button on second top menu) --> Directory name: documents. This is where you may store the documents for this workshop, and later your own material.


  Task 2.3: Take some, or all of the content from this path: '/fp/projects01/ec443/documents' and move it into your own documents folder that you made on your home directory.
