.. _05_chatbot
05 Chatbot
===========

.. index:: chatbot, pipeline

Querying LLMs (Chatbots)
----------------------

We will use `LangChain <https://python.langchain.com/docs/introduction/>`_, an open-source library for making applications with LLMs. Whenever you see the name of a package in an error message or in a tutorial, and you want to know more about it, you may google the name of the package. Sometimes you will have to look around a bit, but it might help you to add the word "documentation" for better results.

Model Location
-------------

We should tell the HuggingFace library where to store its data. If you’re running on Educloud/Fox project ec443 the model is stored at the path below.

We enter the location of the model. You should navigate to this location in the browser interface, and have a look at the models.

Cell 4::

  %env HF_HOME=/fp/projects01/ec443/huggingface/cache/

We are importing a module from the library. This allows us to set up a pipeline that can perform tasks such as text generation from the model.

Cell 5::
  
  from langchain_huggingface.llms import HuggingFacePipeline

Cell 6::

  model_id = 'mistralai/Mistral-7B-Instruct-v0.3'

Cell 7::

  task = 'text-generation'

Now, we are going to build up a pipeline. You do not need to run this cell yet. We are going to add some arguments.
Cell 8::
  
    llm = HuggingFacePipeline.from_model_id(
      model_id,
      task,
      device=0
  )

Cell 9::
  llm = HuggingFacePipeline.from_model_id(
      model_id,
      task,
      device=0,
      pipeline_kwargs={
          'max_new_tokens': 100,
      }
  )

Cell 10::

  task = 'text-generation'

Cell 11::

  task = 'text-generation'

Cell 12::

  task = 'text-generation'

Cell 13::

  task = 'text-generation'

Cell 14::

  task = 'text-generation'

.. note::

   Task 3.2: Copy the cell above and change the temperature to 10.0. Run the cell.
