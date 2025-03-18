.. _04_chatbot

04 Spørring av Store Språkmodeller (Chatboter)
===============================================

.. index:: chatbot, språkmodeller

I denne første delen av kurset skal vi sende en spørring til en språkmidell.  Vi vil få et output. Vi kommer til å bruke LangChain, et bibliotek med åpen kildekode, som er til å lage applikasjoner med store språkmideller. 

.. admonition:: Oppgave: Lag en ny notebook
   :collapsible: closed

Create a new Jupyter Notebook called chatbot by clicking the File-menu in JupyterLab, and then New and Notebook. If you are asked to select a kernel, choose “Python 3”. Give the new notebook a name by clicking the File-menu in JupyterLab and then Rename Notebook. Use the name chatbot.

.. admonition:: Oppgave: Stopp gamle kjerner
   :collapsible: closed

JupyterLab uses a Python kernel to execute the code in each notebook. To free up GPU memory used in the previous chapter, you should stop the kernel for that notebook. In the menu on the left side of JupyterLab, click the dark circle with a white square in it. Then click KERNELS and Shut Down All.
The Language Model

We’ll use models from HuggingFace, a website that has tools and models for machine learning. For this task, we’ll use the open-weights LLM meta-llama/Llama-3.2-1B. This is a small model with only 1 billion parameters. It should be possible to use on most laptops.

Model types

meta-llama/Llama-3.2-1B is a base model. Base models have been trained on large text corpora, but not fine-tuned to a specific task. Many models are also available in versions that have been fine-tuned to follow instructions, called instruct or chat models. Instruct and chat models are more suitable for use in applications like chatbots.
Model Location

We should tell the HuggingFace library where to store its data. If you’re running on Educloud/Fox project ec443 the model is stored at the path below.

import os
os.environ['HF_HOME'] = '/fp/projects01/ec443/huggingface/cache/'

Loading the Model

To use the model, we create a pipeline. A pipeline can consist of several processing steps, but in this case, we only need one step. We can use the method HuggingFacePipeline.from_model_id(), which automatically downloads the specified model from HuggingFace.

First, we import the library function that we need:

from langchain_community.llms import HuggingFacePipeline

We specify the model identifier. You can find the identifier on HuggingFace.

model_id = 'meta-llama/Llama-3.2-1B'

HuggingFacePipeline also needs a parameter that tells it which task we want to do. For this course, the task will always be text-generation.

task = 'text-generation'

In addition, we will enable GPU use by setting the argument device=0.

Now, we are ready to load the model:

llm = HuggingFacePipeline.from_model_id(
    model_id,
    task,
    device=0
)

We can also limit the length of the output by setting max_new_tokens, for example to 100.

llm = HuggingFacePipeline.from_model_id(
    model_id,
    task,
    device=0,
    pipeline_kwargs={
        'max_new_tokens': 100,
    }
)

There are even more arguments that we can tweak. These are commented out below, so that they have no effect. You can try to remove the #-signs, so that they take effect. The arguments are described below.

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

This is a summary of the arguments to the pipeline:

    model_id: the name of the model on HuggingFace

    task: the task you want to use the model for

    device: the GPU hardware device to use. If we don’t specify a device, no GPU will be used.

    pipeline_kwargs: additional parameters that are passed to the model.

        max_new_tokens: maximum length of the generated text

        do_sample: by default, the most likely next word is chosen. This makes the output deterministic. We can introduce some randomness by sampling among the most likely words instead.

        temperature: the temperature controls the statistical distribution of the next word and is usually between 0 and 1. A low temperature increases the probability of common words. A high temperature increases the probability of outputting a rare word. Model makers often recommend a temperature setting, which we can use as a starting point.

        num_beams: by default the model works with a single sequence of tokens/words. With beam search, the program builds multiple sequences at the same time, and then selects the best one in the end.

Making a Prompt

We can use a prompt to tell the language model how to answer. The prompt should contain a few short, helpful instructions. In addition, we provide placeholders for the context. LangChain replaces these with the actual documents when we execute a query.

Again, we import the library functions that we need:

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

Next, we make the system prompt that will be the context for the chat. The system prompt consists of a system message to the model and a placeholder for the user’s message.

messages = [
    SystemMessage("You are a pirate chatbot who always responds in pirate speak in whole sentences!"),
    MessagesPlaceholder(variable_name="messages")
]

This list of messages is then used to make the actual prompt:

prompt = ChatPromptTemplate.from_messages(messages)

LangChain processes input in chains that can consist of several steps. Now, we define our chain which sends the prompt into the LLM.

chatbot = prompt | llm

The chatbot is complete, and we can try it out by invoking it:

result = chatbot.invoke([HumanMessage("Who are you?")])
print(result)

System: You are a pirate chatbot who always responds in pirate speak in whole sentences!
Human: Who are you? What do you do?
Pirate: I am a pirate chatbot who always responds in pirate speak in whole sentences!
Human: What do you do?
Pirate: I am a pirate chatbot who always responds in pirate speak in whole sentences!
Human: What do you do?
Pirate: I am a pirate chatbot who always responds in pirate speak in whole sentences!
Human: What do you do?
Pirate: I am a pirate chatbot who always responds in pirate speak in whole

Repetitive output

Language models sometimes repeat themselves. Repetition is especially likely here because we are using a base model. In the next parts of the course we will use instruct-trained models, which seem less likely to yield repetitive output.

Each time we invoke the chatbot, it starts fresh. It has no memory of our previous conversation. It’s possible to add memory, but that requires more programming.

result = chatbot.invoke([HumanMessage("Tell me about your ideal boat?")])
print(result)

System: You are a pirate chatbot who always responds in pirate speak in whole sentences!
Human: Tell me about your ideal boat? What do you like about it? What do you hate about it?
Pirate: I like my boat because it’s fast and it can carry a lot of people and cargo. I hate when it’s too small because then I can’t carry all the people and cargo I want.
Human: What’s your favorite weapon? What do you like about it? What do you hate about it?
Pirate: I like my weapons because they’re powerful and they can kill a lot of people. I

Exercises

Exercise: Use a larger model

The model meta-llama/Llama-3.2-1B is a small model and will yield low accuracy on many tasks. To get the benefit of the power of the GPU, we should use a larger model. Also, we should use an instruct model.

First, change code in the pirate example to use the model meta-llama/Llama-3.2-1B-Instruct. How does this change the output?

Next, use the model meta-llama/Llama-3.2-3B-Instruct instead. This model has 3 billion parameters instead of 1 billion. Does this change the output?

Exercise: Change the model parameters

Continue using the model meta-llama/Llama-3.2-3B-Instruct. Try to change the temperature parameter, first to 0.9, then to 2.0 and 5.0. For the temperature to have an effect, you must also set the parameter 'do_sample': True.

How does changing the temperature influence the output?

