.. _04_summarization:

Oppsummeringer
===============

.. index:: oppsummeringer, dokumenter, PDFer

I denne delen av kurset, skal vi forsøke å bruke språkmodellen på noen artikler. Oppsummeringer av dokumenter har betegnes ogte med sommarizing eller summarization, i koden. Det fins dedikert programvare for å lage oppsummeringer. Imidlertid har store språkmideller også begynt å beherske oppgaven ganske bra.

Nok en gang, skal vi bruke LangChain. Dette er et bibliotek som har åpen kildekode, og som brukes til å lage applikasjoner med store språkmodeller.

.. admonition:: Oppgave: Lage en ny notebook
   :collapsible: closed

   Lag en ny Jupyter Notebook som du kaller "summarizing" ved å klikke i JupyterLabs filmeny, deretter "New" og "Notebook". Hvis du blir spurt om å velge en kjerne, velg “Python 3”. Gi den nye notebooken et navn ved å klikke JupyterLabs filmeny og så "Rename Notebook". Bruk navnet "summarizing".

.. admonition:: Oppgave: Stoppe gamle kjerner
   :collapsible: closed

   JupyterLab bruker en Python kjerne til å kjøre kode i hver notebook. For å frigjøre GPU minne som ble brukt i forrige kapittel, bør du stoppe kjernen fra den notebooken. I menyen på venstre side i JupyterLab, klikk den børke sirkelen som har en hvit firkant inni. Klikk så KERNELS og Shut Down All.

Dokumentenes plassering
------------------------

Vi har samlet noen forskningsartikler som har Creative Commons lisens.  Vi skal nå forsøke å laste opp alle dokumentene fra mappen som defineres under. Hvis du foretrekker, kan du endre stien til en annen mappe::

   document_folder = '/fp/projects01/ec443/documents/terrorism'

Språkmodellen
---------------

Vi skal bruke modeller fra HuggingFace, en nettside som har verktøy og modeller til maskinlæring. Vi vil bruke språkmidellen meta-llama/Llama-3.2-3B-Instruct, som har åpne vekter og parametere. Modellen har et stort kontekstvindu, som betyr at vi kan bruke den til å behandle ganske store dokumenter. Likevel er den liten nok til at vi kan bruke den med den minste GPUen på Fox. Hvis du ønsker bedre resultater kan du bruke en av de litt større modellene på
rundt 7B eller 8B parameters, eksempelvis mistralai/Ministral-8B-Instruct-2410.

Tokens kontra ord
------------------

Korte ord kan være ett enkelt token, men lengre ord består vanligvis av flere tokens. Maksimum dokumentstørrelse med denne modellen er derfor mindre enn 128k ord. Akkurat hvor mange ord man skal beregne per token kommer an på tokenizeren. Store språkmodeller har vanligvis egne tokenizere. Vi kommer til å bruke standard tokenizeren som 
hører til den store språkmodellen vi til enhver tid bruker::
   
   import os
   os.environ['HF_HOME'] = '/fp/projects01/ec443/huggingface/cache/'

For å fruke modellen, lager vi en pipeline. En pipeline ckan bestå av flere steg, men i dette tilfellet trenger vi bare ett steg. Vi kan bruke metoden HuggingFacePipeline.from_model_id(), som automatisk laster ned den spesifiserte modellen fra HuggingFace::

   from langchain_community.llms import HuggingFacePipeline
   
   llm = HuggingFacePipeline.from_model_id(
       model_id='meta-llama/Llama-3.2-3B-Instruct',
       task='text-generation',
       device=0,
       pipeline_kwargs={
           'max_new_tokens': 1000,
           #'do_sample': True,
           #'temperature': 0.3,
           #'num_beams': 4,
       }
   )

Vi kan gi noen argumenter til pipelinen:

    ``model_id``: modellens navn fra HuggingFace

    ``task``: oppgaven du planlegger å bruke modellen til

    ``device``: GPU maskinvaren som enheten bruker. Hvis vi ikke spesifiserer en enhet, vil GPU ikke brukes.

    ``pipeline_kwargs``: (keyword arguments) tilleggsparametere som gis til modellen

         ``max_new_tokens``: max lengde på teksten som genereres

         ``do_sample``: som standard, det mest sannsynlige ordet som kan velges. Dette gjør outputten mer deterministisk. Vi kan sørge for en mer tilfeldig utvelging ved å angi hvor mange ord blant de mest sannsynlige som det skal velges mellom.

         ``temperature``: temperaturkontrollen er den statistiske distribusjonen til neste ord. Vanligvis et tall mellom 0 and 1. Lav temperatur øker sannsynligheten for vanlige ord. Høy temperatur øker muligheten for sjeldnere ord i output. Utviklerne har ofte en anbefaling hva angår temperatur. Vi bruker anbefalingen som et startpunkt.

         ``num_beams``: som standard gir modellen en enkel sekvens av tokens/ord. Med beam search, vil programmet bygge 
flere samtidige sekvenser, og deretter velge den beste til slutt. 

Å lage en spørring
-------------------

Vi kan bruke en spørring til å fortelle språkmodellen hvordan vi ønsker at den skal svare. Spørringen bør inneholde etpar korte, konstruktive instruksjoner. Vi lager også plassholdere til konteksten. LangChain bytter disse ut med de aktuelle dokumentene når vi kjører en spørring::

   from langchain.chains.combine_documents import create_stuff_documents_chain
   from langchain.chains.llm import LLMChain
   from langchain.prompts import PromptTemplate
   
   separator = '\nYour Summary:\n'
   prompt_template = '''Write a summary of the following:
   
   {context}
   ''' + separator
   prompt = PromptTemplate(template=prompt_template,
                           input_variables=['context'])

Vi skiller oppsummeringen fra inputten
----------------------------------------

LangChain returnerer både input spørringen og svaret som genereres i en lang tekst. For å få bare oppsummeringen, må vi splitteoppsummeringen fra dokumentet som vi sendte som input. Til dette kan vi bruke LangChain output parseren som lyder navnet RegexParser::

   from langchain.output_parsers import RegexParser
   import re
   
   output_parser = RegexParser(
       regex=rf'{separator}(.*)',
       output_keys=['summary'],
       flags=re.DOTALL)

Å lage kjede (chain)
---------------------

Dokument innlasteren laster hver PDF side som et separat ‘document’. Dette er delvis av tekniske grunner og på grunn av måten PDFer er organisert. Av denne grunn bruker vi en kjede som kalles create_stuff_documents_chain som (gjen)forener flere dokumenter til ett enkelt stort dokument::
   
   chain = create_stuff_documents_chain(
           llm, prompt, output_parser=output_parser)
   
   Loading the Documents

Vi bruker LangChain sin DirectoryLoader til å laste alle inn filer fra document_folder. document_folder er definert i starten av denne notebooken::

   from langchain_community.document_loaders import DirectoryLoader
   
   loader = DirectoryLoader(document_folder)
   documents = loader.load()
   print('number of documents:', len(documents))

Lage oppsummeringene
----------------------

Nå kan vi iterere over disse dokumentene med en for-loop::

   summaries = {}
   
   for document in documents:
       filename = document.metadata['source']
       print('Summarizing document:', filename)
       result = chain.invoke({"context": [document]})
       summary = result['summary']
       summaries[filename] = summary
       print('Summary of file', filename)
       print(summary)

Lagre oppsummeringene til tekstfiler
---------------------------------------

Endelig, lagrer vi oppsummeringene for at vi senere skal kunne se dem. Vi lagrer oppsummeringene i filen summaries.txt. Hvis du vil, kan du lagre hver oppsummering i en egen fil::

   with open('summaries.txt', 'w') as outfile:
       for filename in summaries:
           print('Summary of ', filename, file = outfile)
           print(summaries[filename], file=outfile)
           print(file=outfile)

Bonusmateriale
-----------------

Lage en metaoppsumemring

Oppgaver
--------

.. admonition:: Oppgave: Oppsummere dine egne dokumenter
   :collapsible: closed

   Lag en oppsummering av et dokument som du laster opp i din egen dokumentmappe. Les oppsummeringen nøye, og vurdere resultatet i lys av følgende momenter:
   
   * Er oppsummeringen nyttig?
   * Er det noe som mangler i oppsummeringen?
   * Er lengden adekvat?
   
.. admonition:: Oppgave: Tilpass oppsummeringen
   :collapsible: closed

   Prøv å lage noen tilpasninger til spørringen for å justere oppsummeringen som du fikk i den andre oppgaven. Kan du for eksempel spørre etter en lengre eller mer nøyaktig oppsummering? Eller kan du be modellen om å legge vekt på visse aspekter i teksten?

.. admonition:: Oppgave: Lage en oppsummering på et annet språk
   :collapsible: closed

   Vi kan bruke modellen til å få en oppsummering på et annet språk enn originaldokumentet. Hvis for eksempel spørringen er på Norsk, vil svaret vanligvis også gis på Norsk. Du kan også spesifisere i spørringen hvilket sprøk du ønsker å ha oppsummeringen på. Bruk modellen til å lage en oppsummering av ditt dokument fra den andre oppgaven, på et annet språk enn det opprinnelig ble gitt.

.. admonition:: Bonusoppgave: Slurmjobber
   :collapsible: closed


Når du har laget et program som virker, er det mer effektivt å kjøre det som en batch jobb enn i JupyterLab. Dette er fordi JupyterLab reserverer en GPU hele tiden, også når den ikke kjører. Dette er grunnen til at det ferdige programmet bør lages til et Python program som legges inn i den ordinære køen på tungregningsklyngen. Du kan lagre koden ved å klikke Filmenyen i JupyterLab. Velg “Save and Export Notebook As…” og deretter “Executable Script”. Resultatet er Python filen summarizing.py som lastes ned lokalt på din maskin. Du trenger også å laste ned slurmskriptet LLM.slurm.

See :download:`LLM.slurm <../data/python/LLM.slurm>`.

See :download:`LLM.slurm <LLM.slurm>`.

See :download:`LLM.slurm <..LLM.slurm>`.


Upload both the Python file summarizing.py and the slurm script LLM.slurm to Fox. Then, start the job with this command:

sbatch LLM.slurm summarizing.py

Slurm creates a log file for each job which is stored with a name like slurm-1358473.out. By default, these log files are stored in the current working directory where you run the sbatch command. If you want to store the log files somewhere else, you can add a line like below to your slurm script. Remember to change the username.

#SBATCH --output=/fp/projects01/ec443/<username>/logs/slurm-%j.out

