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

Library function for prompts
Cell 4::

  from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
  from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

Cell 5::

  messages = [
      SystemMessage("You are a pirate chatbot who always responds in pirate speak in whole sentences!"),
      MessagesPlaceholder(variable_name="messages")
  ]

Cell 6::

  prompt = ChatPromptTemplate.from_messages(messages)

LangChain processes input in chains that can consist of several steps. Now, we define our chain which sends the prompt into the LLM.

Cell 7::

  chatbot = prompt | llm

The chatbot is complete, and we can try it out by invoking it:

Cell 8::

  result = chatbot.invoke([HumanMessage("Who are you?")])
  print(result)

Cell 9::

  result = chatbot.invoke([HumanMessage("Tell me about your ideal boat?")])
  print(result)





