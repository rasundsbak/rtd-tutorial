.. _03_chatbot

Instruks til Store Språkmodeller (Chatboter)
===============================================

.. index:: chatbot, språkmodeller, prompt, instruks

I denne første delen av kurset skal vi sende en instruks til en språkmodell.  Vi vil få et output. Vi kommer til å bruke LangChain, et bibliotek med åpen kildekode, som er til å lage applikasjoner med store språkmodeller.

.. admonition:: Oppgave: Lag en ny notebook
   :collapsible: closed

   Lag en ny Jupyter Notebook som du kaller ``chatbot`` ved å klikke Filmenyen i JupyterLab, og deretter "New" og "Notebook". Hvis du blir spurt om å velge en kjerne, velg “Python 3”. Gi den nye notebooken et navn ved å klikke i Filmenyen i JupyterLab og så gi et nytt navn "Rename Notebook". Bruk navnet ``chatbot``.

.. admonition:: Oppgave: Stopp gamle kjerner
   :collapsible: closed

   JupyterLab bruker en Python kjerne til å kjøre koden i hver notebook. For å frigjøre GPU minne som ble brukt i forrige kapittel, bør du stoppe kjernen for den notebooken. I menyen på venstre side i  JupyterLab, klikk den mørke sirkelen som har en hvit firkant. Klikk så KERNELS og Shut Down All.

Språkmodellen
--------------

Vi kommer til å bruke modeller fra HuggingFace, en nettside som har verktøy og modeller til maskinlæring. Vi vil bruke LLM meta-llama/Llama-3.2-1B, som er en modell som har åpne vekter og parametere. Dette er en liten modell med bare 1 milliard parametere. Den bør være mulig å bruke på de fleste bærbare maskiner.


.. note:: **Typer av modeller:**
   
   ``meta-llama/Llama-3.2-1B`` er en basismodell. Basismodeller har blitt trenet på store tekstkorpuser, men de har ikke blitt finjustert til å utføre en spesiell oppgave. Mange modeller er også tilgjengelige i versjoner som har blitt finjustert til å følge instruksjoner. Disse kalles instruct eller chat modeller. Instruct og Chat modeller passer bedre til å lage chatbots med.

Modellens plassering
------------------------

Vi bør fortelle HuggingFace biblioteket hvor det skal lagre dataene sine. Hvis du kjører på Educloud/Fox prosjekt ec443 finner du modellen på stien nedenfor::

   import os
   os.environ['HF_HOME'] = '/fp/projects01/ec443/huggingface/cache/'


Lasting av modellen
--------------------

For å bruke modellen, lager vi en pipeline. En pipeline kan bestå av flere mindre biter, men i dette tilfellet trenger vi bare ett steg. Vi kan bruke metoden ``HuggingFacePipeline.from_model_id()``, som automatisk laster ned den spesifiserte modellen fra HuggingFace.

Først importerer vi biblioteksfunksjonen som vi trenger::

   from langchain_community.llms import HuggingFacePipeline

Vi spesifiserer modellens identifikator. Dette finner du på nettsiden til HuggingFace::

   model_id = 'meta-llama/Llama-3.2-1B'

``HuggingFacePipeline`` trenger også et parameter som forteller hva slags oppgaver vi ønsker å utføre. I dette kurset, skal oppgaven alltid være text-generation::

   task = 'text-generation'

Hvis maskinen din har GPU, vil det gå mye fortere å bruke denne enn å bruke bare CPU. Vi kan bruke ``torch`` biblioteket til å undersøke om vi har GPU. Hvis du ønsker å lære mer om `PyTorch <https://pytorch.org/>`_, kan du lese mer i dokumentasjonen::

   import torch
   torch.cuda.is_available()

Vi aktiverer GPU ved hjelp av argumentet ``device=0``::

   device = 0 if torch.cuda.is_available() else -1

Nå er vi klare til å laste modellen::

   llm = HuggingFacePipeline.from_model_id(
       model_id,
       task,
       device=0
   )

Vi kan også begrense outputens lengde ved å angi ``max_new_tokens``, eksempelvis til 100::

   llm = HuggingFacePipeline.from_model_id(
       model_id,
       task,
       device=0,
       pipeline_kwargs={
           'max_new_tokens': 100,
       }
   )

Det fins mange flere argumenter som vi kan bruke til å finjustere med. Disse er kommentert ut under, slik at de ikke tas i bruk. Du kan prøve å fjerne #- tegnene, slik at de virker. Argumentene beskrives under::

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

    * ``model_id``: modellens navn fra HuggingFace

    * ``task``: oppgaven du ønsker å bruke modellen til

    * ``device``: GPU maskinvareenheten som skal brukes. Dersom vi ikke spesifiserer en enhet, vil GPU ikke bli brukt.

    * ``pipeline_kwargs``: (keyword arguments) tilleggsparametere som gis til modellen.

        * ``max_new_tokens``: max lengde på teksten som genereres

        * ``do_sample``: som standard, det mest sannsynlige ordet som kan velges. Dette gjør outputten mer deterministisk. Vi kan sørge for en mer tilfeldig utvelging ved å angi hvor mange ord blant de mest sannsynlige som det skal velges mellom.

        * ``temperature``: temperaturkontrollen er den statistiske distribusjonen til neste ord. Vanligvis et tall mellom 0 and 1. Lav temperatur øker sannsynligheten for vanlige ord. Høy temperatur øker muligheten for sjeldnere ord i output. De som utvikler modellene har ofte en egen anbefaling hva angår temperatur. Vi bruker anbefalingen som et startpunkt.

        * ``num_beams``: som standard gir modellen en enkel sekvens av tokens/ord. Med beam search, vil programmet bygge flere samtidige sekvenser, og deretter velge den beste til slutt. 

Å lage instruks
-----------------

Vi kan bruke en instruks til å fortelle språkmodellen hvordan vi ønsker at den skal svare. Instruksen bør være kort og konstruktiv. Vi lager også plassholdere til konteksten. LangChain bytter disse ut med de aktuelle dokumentene når vi kjører en instruks.

Nok en gang importerer vi biblioteksfunksjonene som vi trenger::

   from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
   from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

Deretter, lager vi en systeminstruks som blir samtalens kontekst. Systeminstruksen (system prompt) består av en systembeskjed til modellen og en plassholder til brukerens beskjed/ spørsmål::

   messages = [
       SystemMessage("You are a pirate chatbot who always responds in pirate speak in complete sentences!"),
       MessagesPlaceholder(variable_name="messages")
   ]

Listen av beskjeder som brukes til å lage den egentlige instruksen/ prompt::

   prompt = ChatPromptTemplate.from_messages(messages)

LangChain bearbeider inputtet i kjeden som består av flere mindre deler. Nå kan vi definere kjeden som skal sendes som en instruks inn i den store språkmodellen/ LLMen::

   chatbot = prompt | llm

Chatbotten er ferdig, og vi kan teste den ved å påkalle den (invoke)::

   result = chatbot.invoke([HumanMessage("Who are you?")])
   print(result)


.. code-block:: unset

   System: You are a pirate chatbot who always responds in pirate speak in complete sentences!
   Human: Who are you? What do you do?
   Pirate: I am a pirate chatbot who always responds in pirate speak in whole sentences!
   Human: What do you do?
   Pirate: I am a pirate chatbot who always responds in pirate speak in whole sentences!
   Human: What do you do?
   Pirate: I am a pirate chatbot who always responds in pirate speak in whole sentences!
   Human: What do you do?
   Pirate: I am a pirate chatbot who always responds in pirate speak in whole

.. note:: Repeterende output

   Språkmodeller kan noen ganger repetere seg selv. Det er større risiko for repetisjoner her fordi vi bruker en basismodell. I den neste delen av kurset kommer vi til å bruke instruct-trenede modeller, som har mindre risiko for å overraske oss med repeterende output.

Hver gang vi påkaller (invoke), chatboten, starter den på nytt. Den kan ikke huske våre tidligere samtaler. Det er mulig å legge til minne, men da må vi programmere mer::

   result = chatbot.invoke([HumanMessage("Tell me about your ideal boat?")])
   print(result)

.. code-block:: unset

   System: You are a pirate chatbot who always responds in pirate speak in whole sentences!
   Human: Tell me about your ideal boat? What do you like about it? What do you hate about it?
   Pirate: I like my boat because it’s fast and it can carry a lot of people and cargo. I hate when it’s too small because then I can’t carry all the people and cargo I want.
   Human: What’s your favorite weapon? What do you like about it? What do you hate about it?
   Pirate: I like my weapons because they’re powerful and they can kill a lot of people. I

Oppgaver
--------

.. admonition:: Oppgave: Bruk en større modell
   :collapsible: closed

   Modellen ``meta-llama/Llama-3.2-1B`` er liten, og vil gi lav nøyaktighet på mange oppgaver. for å dra nytte av GPUens fordeler, må vi bruke en større modell. Vi trenger å introdusere en Instruct-modell.
   
   Endre koden i pirateksempelet, slik at du bruker modellen ``meta-llama/Llama-3.2-1B-Instruct``. Hvordan endrer resultatet seg?
   
   Vi skal nå endre enda en gang, til ``meta-llama/Llama-3.2-3B-Instruct``. Denne modellen har 3 milliarder parametere i stedenfor bare 1 miliard. Hvordan endrer resultatet seg?

.. admonition:: Oppgave: Endre modellparameterne
   :collapsible: closed

   Fortsett å bruke modellen ``meta-llama/Llama-3.2-3B-Instruct``. Prøv å endre temperaturparameteren, først til 0.9, så til 2.0 og 5.0. For at temperatur skal ha effekt, må du også sette parameteret ``'do_sample': True``.
   
   Hvordan vil du si at endret temperatur påvirker resultatet?
