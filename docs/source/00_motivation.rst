.. _00 motivation:
00 AIs and Scientific workflows.
==============
.. index:: chatbot, Chat GPT, workflow

At the UiO we have had access to Chat GPT since 2023. Many are using it every week. In this workshop, we will look at what goes on behind the interface of an AI. Is it possible to make reproducible research through using the open source `Transformers library <https://huggingface.co/docs/transformers/index>`_ together with state-of-the-art pretrained models from Huggingface? We want to establish common knowledge on how to use AIs on UiOs own infrastructure. We will do this through playing with the models. The aim is to learn more on the functionalities through testing. You will learn how to run AIs on the supercomputer Fox through Educloud. We are going to use the Juypyter Lab application. This is easier than running the model from the command prompt, while also making it possible to build reproducible or documentable scientific work flows. You will learn how to start up an open or available AI from a script in Jupyter Lab, and run it on the Fox NVIDIA Cluster.

UiO and the Storage Guide
----------------------
With Chat GPT from UiO you may use up to yellow data, according to the UiO Data `storage guide <https://www.uio.no/english/services/it/security/lsis/storage-guide.html>`_. Educloud is safe for up to red data. The same method as shown in this workshop might be used on black data, but in that case on a supercomputer with the name of Colossus (TSD). This will not be covered in the workshop.

The extra machine power of the supercomputer gives possibilities that you do not have on a laptop.

.. note:: Task 0.1. 2 mins.:  Visit UiO `Chat GPT <https://www.uio.no/tjenester/it/ki/gpt-uio/>`_ and enter the following: 

First task
--------
Code view::

   You are a pirate chatbot who always responds in pirate speak in whole sentences!
      1) Who are you?
      2) Tell me about your ideal boat?
