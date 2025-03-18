.. _04_chatbot

04 Spørring av Store Språkmodeller (Chatboter)
===============================================

.. index:: chatbot, språkmodeller

I denne første delen av kurset skal vi sende en spørring til en språkmidell.  Vi vil få et output. Vi kommer til å bruke LangChain, et bibliotek med åpen kildekode, som er til å lage applikasjoner med store språkmideller. 

.. admonition:: Oppgave: Lag en ny notebook
   :collapsible: closed

Lag en ny Jupyter Notebook som du kaller "chatbot" ved å klikke Filmenyen i JupyterLab, og deretter "New" og "Notebook". Hvis du blir spurt om å velge en kjerne, velg “Python 3”. Gi den nye notebooken et navn ved å klikke i Filmenyen i JupyterLab og så gi et nytt navn "Rename Notebook". Bruk navnet "chatbot".

.. admonition:: Oppgave: Stopp gamle kjerner
   :collapsible: closed

JupyterLab bruker en Python kjerne til å kjøre koden i hver notebook. For å frigjøre GPU minne som ble brukt i forrige kapittel, bør du stoppe kjernen for den notebooken. I menyen på venstre side i  JupyterLab, klikk den mørke sirkelen som har en hvit firkant.  wKlikk så KERNELS og Shut Down All.

Språkmodellen
--------------

Vi kommer til å bruke modeller fra HuggingFace, en nettside som har verktøy om modeller til maskinlæring. Vi vil bruke LLM meta-llama/Llama-3.2-1B, som er en modell som har åpne vekter og parametere. Dette er en liten modell med bare 1 milliard parametere. Den bør være mulig å bruke på de fleste bærbare maskiner.

..note:: 
   **Typer av modeller:**  meta-llama/Llama-3.2-1B er en basismodell. Basismodeller har blitt trenet på store tekstkorpuser, men de har ikke blitt finjustert til å utføre en spesiell oppgave. Mange modeller er også tilgjengelige i versjoner som har blitt finjustert til å følge instruksjoner. Disse kalles instruct eller chat modeller. Instruct og Chat modeller passer bedre til å lage chatbots med.

Modellens plassering

Vi bør fortelle HuggingFace biblioteket hvor det skal lagre dataene sine. Hvis du kjører på Educloud/Fox prosjekt ec443 finner du modellen på stien nedenfor::

   import os
   os.environ['HF_HOME'] = '/fp/projects01/ec443/huggingface/cache/'


Lasting av modellen
--------------------

For å bruke kodellen, lager vi en pipeline. en pipeline/ rørledning kan bestå av flere mindre biter, men i dette tilfellet trenger vi bare ett steg. Vi kan bruke metoden HuggingFacePipeline.from_model_id(), som automatisk laster ned den spesifiserte modellen fra HuggingFace.

Først importerer vi biblioteksfunksjonen som vi trenger::

   from langchain_community.llms import HuggingFacePipeline

Vi spesifiserer modellens identifikator. Dette finner du på nettsiden til HuggingFace::

   model_id = 'meta-llama/Llama-3.2-1B'

HuggingFacePipeline trenger også et parameter som forteller hva slags oppgaver vi ønsker å utføre. I dette kurset, skal oppgaven alltid være text-generation::

   task = 'text-generation'

I tillegg skal vi aktivere GPU ved hjelp av argumentet device=0.

Nå er vi klare til å laste modellen::

   llm = HuggingFacePipeline.from_model_id(
       model_id,
       task,
       device=0
   )

Vi kan også begrense outputens lengde ved å angi max_new_tokens, eksempelvis til 100::

   llm = HuggingFacePipeline.from_model_id(
       model_id,
       task,
       device=0,
       pipeline_kwargs={
           'max_new_tokens': 100,
       }
   )

Det fins mange flere argumenter som vi kan bruke til å finjustere med. Disse er kommentert ut under, slik at de ikke har noen effekt. Du kan prøve å fjerne #- tegnene, slik at de virker. Argumentene beskrives under::

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

Her kommer en oppsummering av pipelinens/ rørledningens argumenter:

    ``model_id``: modellens navn fra HuggingFace

    ``task``: oppgaven du ønsker å bruke modellen til

    ``device``: GPU maskinvareenheten som skal brukes. Dersom vi ikke spesifiserer en enhet, vil GPU ikke bli brukt.

    ``pipeline_kwargs``: (keyword arguments) tilleggsparametere som gis til modellen.

        ``max_new_tokens``: max lengde på teksten som genereres

        ``do_sample``: som standard, det mest sannsynlige ordet som kan velges. Dette gjør outputten mer deterministisk. Vi kan sørge for en mer tilfeldig utvelging ved å angi hvor mange ord blant de mest sannsynlige som det skal velges mellom.

        ``temperature``: temperaturkontrollen er den statistiske distribusjonen til neste ord. Vanligvis et tall mellom 0 and 1. Lav temperatur øker sannsynligheten for vanlige ord. Høy temperatur
øker muligheten for sjeldnere ord i output. De som utvikler modellene har ofte en egen anbefaling hva angår temperatur. Vi bruker anbefalingen som et startpunkt.

        ``num_beams`: som standard gir modellen en enkel sekvens av tokens/ord. Med beam search, vil programmet bygge 
flere samtidige sekvenser, og deretter velge den beste til slutt. 

Å lage en spørring
-------------------

Vi kan bruke en spørring til å fortelle språkmodellen hvirdan vi ønsker at den skal svare. Spørringen bør inneholde etpar korte, konstruktive instruksjoner. Vi lager også plassholdere til konteksten. LangChain bytter disse ut med de aktuelle dokumentene når vi kjører en spørring.

Nok en gang importerer vi biblioteksfunksjonene som vi trenger::

   from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
   from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

Deretter, lager vi en systemspørring som blir samtalens kontekst. Systemspørringen (system prompt) består av en systembeskjed til modellen og en plassholder til brukerens beskjed/ spørsmål::

   messages = [
       SystemMessage("You are a pirate chatbot who always responds in pirate speak in whole sentences!"),
       MessagesPlaceholder(variable_name="messages")
   ]

Listen av beskjeder som brukes til å lage den egentlige spørringen/ prompt::

   prompt = ChatPromptTemplate.from_messages(messages)

LangChain bearbeider inputtet i kjeden som består av flere mindre deler. Nå kan vi definere kjeden som skal sendes som en spørring inn i den store språkmodellen/ LLMen::

   chatbot = prompt | llm

Chatbotten er ferdig, og vi kan teste den ved å påkalle den (invoke)::

   result = chatbot.invoke([HumanMessage("Who are you?")])
   print(result)


.. code-block:: unset

   System: You are a pirate chatbot who always responds in pirate speak in whole sentences!
   Human: Who are you? What do you do?
   Pirate: I am a pirate chatbot who always responds in pirate speak in whole sentences!
   Human: What do you do?
   Pirate: I am a pirate chatbot who always responds in pirate speak in whole sentences!
   Human: What do you do?
   Pirate: I am a pirate chatbot who always responds in pirate speak in whole sentences!
   Human: What do you do?
   Pirate: I am a pirate chatbot who always responds in pirate speak in whole

Repeterende output

Språkmideller kan noen ganger repetere seg selv. Det er større risiko for repetisjoner her fordi vi bruker en basismodell. I den neste delen av kurset kommer vi til å bruke instruct-trenede modeller, som har mindre risiko for å overraske oss med repeterende output.

Hver gang vi påkaller (invoke), chatboten, starter den på nytt. Den kan ikke huske våre tidligere samtaler. Det er mulig å legge til minne, men da må vi programmere mer::

   result = chatbot.invoke([HumanMessage("Tell me about your ideal boat?")])
   print(result)

.. code-block:: python

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

