.. _03_downloading_packages:

03 Installering
=================

Vi kommer til å bruke LangChain, et bibliotek med åpen kildekode, som brukes til å lage 
aplikasjoner med LLMer. Vi vil bruke modeller fra HuggingFace, en nettside som har verktøy og modeller som brukes til maskinlæring.

.. tip:: Lag en ny notebook
Lag en ny Jupyter Notebook med navn "installing" by ved å klikke File-menyen i JupyterLab, og så New og Notebook. IHvis du blir spurt om å velge en kjerne (kernel), velg “Python 3”. Gi navn til notebooken ved å klikke Fil-meny i JupyterLab og deretter "Rename Notebook". Bruk navnet installing.

Vanlig programvare for store språkmodeller
--------------------------------------------

Vi installerer programvaren til LangChain og HuggingFace først. Transformers er den grunnleggende teknologien som brukes for store språkmideller, derfor installerer vi library sentence-transformers også. Modellene bruker sentencepiece biblioteket, derfor er dette også viktig.

Kode::

  !pip install --upgrade pip 
  !pip install --upgrade huggingface-hub
  !pip install --upgrade langchain
  !pip install --upgrade langchain-community langchain-huggingface
  !pip install --upgrade sentence-transformers
  !pip install --upgrade sentencepiece

Programvare til å lese tekstdokumenter
-----------------------------------------

Vi kommer til å bruke "unstructured" til å lese dokumenter. Biblioteket unstructured støtter ulike dokumentformater, som PDFer, Word filer og rene tekstdokumenter.

Kode::

  !pip install --upgrade unstructured[all-docs] langchain-unstructured

Søkeindeks
----------

Til RAG kapittelet vil vi bruke FAISS til å søke etter dokumenter lokalt på maskinen.

Kode::

  !pip install --upgrade faiss-cpu

Språkmodellen
---------------

Vi kommer til å bruke modeller fra HuggingFace, en nettside som har verktøy og modeller som brukes til maskinlæring. Vi vil bruke åpen- vektmodellen mistralai/Ministral-8B-Instruct-2410 til de fleste av våre oppgaver. Modellen har 8 milliarder parametere. Til sammenligning har en av de største språkmodellene når dette skrives, Llama 3.1, 405 milliarder parametere. Ministral-8B-Instruct-2410 har rundt 16 GB, noe som fortsatt gjør den til en ganske stor modell. For å kjøre den, må vi ha en GPU med minst 20 GB minne. Den kan også kjøres uten GPU, men da vil det ta lenger tid.

Kode::

  %env HF_HOME=/fp/projects01/ec443/huggingface/cache/

Frivillig
-----------

If you’re running one of the models that is already downloaded Educloud/Fox project ec443 the model, you can skip this step. If you’re not running on Educloud/Fox project ec443 or want to use a model that isn’t already downloaded, you’ll need to download the model.

You will need a User Access Token from HuggingFace. If you don’t already have a user account on HuggingFace, you must first sign up for one. Click the button “Sign Up” in the upper right corner on HuggingFace.

When you have logged in to HuggingFace with your user account, you can create a User Access Token giving read access by following this guide.

from huggingface_hub import login
login()
