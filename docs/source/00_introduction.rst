.. _00_introduction:

Kjøring av store språkmodeller på Fox, en introduksjon
==========================================================

.. index:: LLM, large language models, språkmodeller, HPC, tungregningsklynge

Dette er et instoduksjonskurs hvor du lærer å kjøre store språkmodeller på on the UiO sin `tungregningsklynge Fox <https://www.uio.no/tjenester/it/forskning/beregning/fox/index.html>`_. Store språkmodeller som ChatGPT, er trenet til å generere ordsekvenser basert på kontekst, som når de fullfører setningen. For eksempel, hvis vi begynner med "kyllingen krysset veien", kan en mulig fullføring være "for å finne mat" eller "komme over på den andre siden". For å lære mer om hvordan språkmodeller trenes, anbefaler vi å se youtube videoene `Intro to Large Language Models <https://www.youtube.com/watch?v=zjkBMFhNj_g>`_ og `Deep Dive into LLMs like ChatGPT <https://www.youtube.com/watch?v=7xTGNNLPyMI>`_ av Andrej Karpathy.

I dette kurset bruker vi Python programmering til å kjøre de store språkmodellene. Det er derfor nødvendig å ha grunnleggende programmeringskunnskaper. Hvis programmering er nytt for deg, anbefaler vi at du programmerer litt før du kommer på kurs. Eksempelvis kurset `Plotting and Programming in Python <https://swcarpentry.github.io/python-novice-gapminder/>`_, som avholdes av Senter for Digital Forskningsstøtte (DSC), ved Universitetsbiblioteket, UiO.

Kurset består av fem kapitler. I :doc:`01_easy_login`, logger vi oss på Fox. Du trenger en brukerkonto ved Universitetet i Oslo og en smarttelefon eller en annen metode til å bruke to faktor autentisering (2FA).

I :doc:`02_downloading_packages`, installerer vi programvaren som vi trenger til kurset.

I :doc:`03_chatbot`, lærer vi å laste og spørre grunnleggende språkmodeller.

I :doc:`04_summarization`, vil vi bruke modellen til å kage korte oppsummeringer av dokumenter.

I :doc:`05_rag`, bygger vi et program til å gjøre RAG, basert på en gruppe dokumenter.
