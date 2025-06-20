.. _00_introduction:

Kjøring av store språkmodeller på Fox, en introduksjon
==========================================================

.. index:: LLM, large language models, språkmodeller, HPC, tungregningsklynge

Dette er et introduksjonskurs hvor du lærer å kjøre store språkmodeller på UiO sin `tungregningsklynge Fox <https://www.uio.no/tjenester/it/forskning/beregning/fox/index.html>`_. Store språkmodeller som ChatGPT, er trenet til å generere ordsekvenser basert på kontekst, som når de fullfører setningen. For eksempel, hvis vi begynner med "kyllingen krysset veien", kan en mulig fullføring være "for å finne mat" eller "komme over på den andre siden". For å lære mer om hvordan språkmodeller trenes, anbefaler vi å se youtube videoene `Intro to Large Language Models <https://www.youtube.com/watch?v=zjkBMFhNj_g>`_ og `Deep Dive into LLMs like ChatGPT <https://www.youtube.com/watch?v=7xTGNNLPyMI>`_ av Andrej Karpathy.


I dette kurset bruker vi Python programmering til å kjøre LLMer. (SSMer ?) Dette er grunnen til at vi forutsetter grunnleggende programmeringskunnskaper. Hvis programmering er nytt for deg, anbefaler vi at du øver litt på forhånd. Carpentry leksjonen `Plotting and Programming in Python <https://swcarpentry.github.io/python-novice-gapminder/>`_, bør tas som selvstudiom eller kurs med påmelding,

Kurset er sammensatte av fem kapitler. I :doc:`01_easy_login`, logger vi inn på Fox. Du trenger brukerkonto ved Universitetet i Oslo og en smarttelefon eller andre måter å bruke to faktor autentisering (2FA).

I :doc:`02_downloading_packages` installerer vi programvaren som vi trenger.

I :doc:`03_chatbot` lærer vi om opplasting og grunnleggende spørring av LLMer.

I :doc:`04_summarization` bruker vi LLMer til å lage korte oppsummeringer av dokumenter.

I :doc:`05_rag`, bygger vi et program som har hentingsforsterket tekstgenerering med noen dokumenter som vi har.

