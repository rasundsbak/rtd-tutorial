.. _02_downloading_packages:

Installering
==============

Vi kommer til å bruke `LangChain <https://www.langchain.com/>`_ , et bibliotek med åpen kildekode, som brukes til å lage 
aplikasjoner med LLMer. Vi vil bruke modeller fra `HuggingFace <https://huggingface.co/>`_ , en nettside som har verktøy og modeller som brukes til maskinlæring.

.. admonition:: Oppgave: Lag en ny notebook
   :collapsible: closed

   Lag en ny Jupyter Notebook med navn ``installing`` ved å klikke Filmenyen i JupyterLab, og så "New" og "Notebook". Hvis du blir spurt om å velge en kjerne (kernel), velg “Python 3”. Gi navn til notebooken ved å klikke Filmenyen i JupyterLab og deretter "Rename Notebook". Bruk navnet ``installing``.

.. warning:: Virtuelle miljøer

   Hvis du vanligvis jobber med `virtuelle miljøer <https://docs.python.org/3/library/venv.html>`_ på Fox, bør du sette opp og aktivere et virtuelt miljø før du fortsetter. Se i `Bonus: Virtuelle miljøer`_ . Hvis du ikke har hørt om virtuelle miljøer, kan du fortsette uten å bruke virtuelle miljøer.

Pyton pakker
-------------
Vi kommer til å bruke pakkeinstallasjonsprogrammet ``pip``til å installere programvare. ``pip``installerer programvare fra `Python package index <https://pypi.org/>`_ . Først oppdaterer vi ``pip``til den nyeste versjonen::

     pip install --upgrade pip 

Vanlig programvare for store språkmodeller
--------------------------------------------

Vi installerer programvaren til LangChain og HuggingFace først. Vi bruker ``huggingface-hub`` til automatisk å laste ned modeller når dette er nødvendig::

   pip install --upgrade huggingface-hub httpx

Vi trenger flere pakker til å jobbe med LangChain og HuggingFace::

   pip install --upgrade langchain langchain-community langchain-huggingface

Transformers er den grunnleggende teknologien som brukes i store språkmodeller. Derfor installerer vi biblioteket ``sentence-transformers``::

   pip install --upgrade sentence-transformers

Noen modeller bruker ``sentencepiece biblioteket`. Derfor installerer vi dette også::

   pip install --upgrade sentencepiece

Programvare til å lese tekstdokumenter
---------------------------------------

Vi kommer til å bruke “unstructured” til å lese dokumenter. Unstructured støtter ulike dokumentformater, som PDFer, Word filer og rene tekstdokumenter::

   pip install --upgrade unstructured[all-docs] langchain-unstructured

Søkeindeks
----------

Til :doc:`05_rag` kapittelet vil vi bruke `FAISS <https://faiss.ai/>`_ til å søke etter dokumenter lokalt på maskinen::

  pip install --upgrade faiss-cpu

Språkmodellen
---------------

Vi kommer til å bruke modeller fra HuggingFace, en nettside som har verktøy og modeller som brukes til maskinlæring. Vi vil bruke åpen- vektmodellen mistralai/Ministral-8B-Instruct-2410 til de fleste av våre oppgaver. Modellen har 8 milliarder parametere. Til sammenligning har en av de største språkmodellene når dette skrives, Llama 3.1, 405 milliarder parametere. Ministral-8B-Instruct-2410 har rundt 16 GB, noe som fortsatt gjør den til en ganske stor modell. For å kjøre den, må vi ha en GPU med minst 20 GB minne. Den kan også kjøres uten GPU, men da vil det ta lenger tid.

Modellens plassering
------------------------

Vi bør fortelle HuggingFace biblioteket hvor det skal lagre dataene sine. Hvis du kjører på Educloud/Fox prosjekt ec443 finner du modellen på stien nedenfor. Dersom du kjører på din egen manskin, trenger du antakelig ikke å spesifisere modellens plassering::

   import os
   os.environ['HF_HOME'] = '/fp/projects01/ec443/huggingface/cache/'


.. admonition:: Frivillig oppgave:
   :collapsible: closed

   Hvis du kjører en av modellene som allerede er lastet ned til Educloud/Fox prosjekt ec443, kan du droppe dette. Hvis du ikke kjører på Educloud/Fox project ec443, eller du vil bruke en modell som ikke er lastet ned, må du laste den.

   Du trenger "User Access Token" fra HuggingFace. Hvis du ikke har en konto på HuggingFace, må du først registrere deg. Klikk på knappen “Sign Up” i øvre høyre hjørne på HuggingFace' nettside.

   Når du har logget inn med din krukerkonto, kan du lage et "User Access Token" som gir lesetilgang ved å følge denne guiden::

      from huggingface_hub import login
      login()

Bonus: Virtuelle miljøer
-------------------------

Som standard, vil ``pip`` kommandoen installere Python moduler eller biblioteker på din brukerprofil, der ditt standard Python miljø ligger. Hvis du bruker Python i forskjellige prosjekter med ulike biblioteker, kan det hende at prosjektene dine behøver ulike versjoner av det samme biblioteket. Du kan lage ett virtuelt miljø for hvert av dine prosjekter. Deretter installerer du alle biblioteker som hører til i ett spesifikt prosjekt i det virtuelle miljøet for det prosjektet. Det virtuelle miljøet blir ofte lagret i en mappe som heter ``venv``.

Etablering av virtuelt miljø
-------------------------------
La oss lage et virtuelt miljø til å kjøre store språkmodeller. Det kan gjøres på mange måter, men vi anbefaler å bruke pythons innebygde ``venv`` kommando::

   !python -m venv .venv

Aktivering av miljøet
-----------------------

For å aktivere det virtuelle miljøet i konsollen, kan du bruke et aktiveringsskript::

   source .venv/bin/activate

JupyterLab kjerne til miljøet
---------------------------------

FOr å bruke det virtuelle miljet i JupyterLab, må vi definere en kjerne for det miljøet::

   ! .venv/bin/python -m ipykernel install --user --name LLM --display-name "Python (LLM)"
