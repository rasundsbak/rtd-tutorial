.. _05_hello_world
05 Chatbot
===========

.. index:: introduction, hello world,

Querying LLMs (Chatbots)
----------------------

We will use `LangChain <https://www.langchain.com/>`_, an open-source library for making applications with LLMs.

Cell 1::

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
