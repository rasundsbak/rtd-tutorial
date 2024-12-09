.. _05_hello_world
05 Chatbot
===========

.. index:: introduction, hello world,

Querying LLMs (Chatbots)
----------------------

We will use `LangChain <https://www.langchain.com/>`_, an open-source library for making applications with LLMs.

Model Location
-------------

We should tell the HuggingFace library where to store its data. If you’re running on Educloud/Fox project ec443 the model is stored at the path below.

Cell 1::

  %env HF_HOME=/fp/projects01/ec443/huggingface/cache/


We need this library function:
Cell 2::

  from langchain_community.llms import HuggingFacePipeline

Cell 3::

  llm = HuggingFacePipeline.from_model_id(
      #model_id='mistralai/Mistral-Nemo-Instruct-2407',
      model_id='meta-llama/Llama-3.2-1B',
      task='text-generation',
      device=0,
      pipeline_kwargs={
          'max_new_tokens': 100,
          #'temperature': 0.3,
          #'num_beams': 4,
          #'do_sample': True
      }
  )

Cell 3::


