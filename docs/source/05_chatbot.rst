.. _05_chatbot

05 Querying LLMs (Chatbots)
===========================

.. index:: chatbot, pipeline, pipeline initialization, kwargs

Querying LLMs (Chatbots)
-------------------------
We will use `LangChain <https://python.langchain.com/docs/introduction/>`_, an open-source library for making applications with LLMs. Whenever you see the name of a package in an error message or in a tutorial, you may google the name of the package. Sometimes you will have to look around a bit, but it might help on the results if you add the word "documentation". 

Transformers and Huggingface
-----------------------------
We are using models from `HuggingFace <https://huggingface.co/>`_ . Huggingface is an american company that develops tools for machine learning. They are the inventor of the Transformers library, that provides tools for downloading pretrained models. This documentation has a chapter on literature and references :doc:`29_references`, where you may find urls and information on these subjects.

Model Location
---------------
We should tell the HuggingFace LLM where to store its data. If you’re running on Educloud/Fox project ec443 the model is stored on the path below. We enter the location of the model.

Task 5.1: Navigate to the location mentioned in cell 4, and look at the models. Do you recognize any names? Are there any European AIs in the collection?

Cell 4::

  %env HF_HOME=/fp/projects01/ec443/huggingface/cache/

We are importing a module from the library. This allows us to set up a pipeline that can perform tasks such as text generation from the model.

Cell 5::
  
  from langchain_huggingface.llms import HuggingFacePipeline

Cell 6::

  model_id = 'meta-llama/Llama-3.2-1B'
  # model_id = 'mistralai/Mistral-7B-Instruct-v0.3'

Cell 7::

  task = 'text-generation'

This is the first step of building a working pipeline.

Cell 8::
  
    llm = HuggingFacePipeline.from_model_id(
      model_id,
      task,
      device=0
  )

We can add keyword arguments to the pipeline. Kwargs is a short form for additional keyword arguments. They are  passed along to the specific pipeline init.

Cell 9::

  llm = HuggingFacePipeline.from_model_id(
    model_id,
    task,
    device=0,
    pipeline_kwargs={
      'max_new_tokens': 100,
      }
  )

We can add even more arguments. In this cell they are commented out, so that they do not have a function. If you want to use them, take away the # and see what happens. Later, we are going to change the value for some of them.

Cell 10::

  llm = HuggingFacePipeline.from_model_id(
      model_id,
      task,
      device=0,
      pipeline_kwargs={
          'max_new_tokens': 100,
          #'do_sample': True,
          #'temperature': 0.3,
          #'num_beams': 4,
      }
  )

Making a prompt
---------------

Cell 11::

  from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
  from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

Cell 12::

  messages = [
    SystemMessage("You are a pirate chatbot who always responds in pirate speak in complete sentences!"),
    MessagesPlaceholder(variable_name="messages")
  ]

Cell 13::

  prompt = ChatPromptTemplate.from_messages(messages)

Cell 14::

  chatbot = prompt | llm

Cell 15::

  result = chatbot.invoke([HumanMessage("Who are you?")])
  print(result)

Cell 16::

  result = chatbot.invoke([HumanMessage("Tell me about your ideal boat?")])
  print(result)


.. note::

   Task 3.2: Copy the cell above and change the temperature to 10.0. Run the cell.



