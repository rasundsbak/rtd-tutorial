.. _03 entering Fox:
02 Entering the Fox server
==================
.. index:: Fox, server, cuda, A100

The Foc is a `High performance computing cluster for Educloud research users <https://www.uio.no/english/services/it/research/hpc/fox/>`_. `Here <https://www.uio.no/english/services/it/research/platforms/edu-research/help/fox/system-overview.md>`_, you may read more about the technical specifications on Fox. Most important from this page, is that Fox has a GPU accelerated part of the system, with four NVIDIA A100 cards each, as well as three nodes with four NVIDIA RTX 3090 cards from IFI. These systems of hardware are for running the AI.


At the Fox server, you have your own storage space. There is also a common space for the group on the server. This is where the AIs are located, and where the AI will be temporarily cached when you download it from Huggingface. In order to get the AI to work in Jupyter lab, it is essential that you set up the paths in the right way. Take a look around, and see if you can think of a good way to organize your project. 

.. note::

   First task: Visit Huggingface and search for google/Pegasus. What do you see? Switch the search to meta-llama/Llama-3.1-8B-Instruct and read. Is this a model that you can find at Fox? What format is it in? Find the format of the Llama AI at Fox, and google it, in order to find out more about this dataformat. 



