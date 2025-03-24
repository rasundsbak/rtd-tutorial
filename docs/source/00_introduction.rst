.. _00_introduction:

Kjøring av store språkmodeller på Fox, en introduksjon
==========================================================

.. index:: LLM, large language models, språkmodeller, HPC, tungregningsklynge

Dette er et instoduksjonskurs hvor du lærer å kjøre store språkmodeller på on the UiO sin tungregningsklynge Fox. Store språkmodeller som ChatGPT, er trenet til å generere ordsekvenser basert på kontekst, som når de fullfører setningen. For eksempel, hvis bi begynner med "kyllingen krysset veien", kan en mulig fullføring være "for å finne mat" eller "komme over på den andre siden". For å lære mer om hvordan språkmodeller trenes, anbefaler vi å se youtube videoene `Intro to Large Language Models <https://www.youtube.com/watch?v=zjkBMFhNj_g>`_ og `Deep Dive into LLMs like ChatGPT <https://www.youtube.com/watch?v=7xTGNNLPyMI>`_ av Andrej Karpathy.

I dette kurset bruker vi Python programmering til å kjøre språkmodellene. Det er derfor nødvendig å ha grunnleggende programmeringskunnskaper. Hvis programmering er nytt for deg, anbefaler vi at du programmerer litt før du kommer på kurs. Eksempelvis kurset `Plotting and Programming in Python <https://swcarpentry.github.io/python-novice-gapminder/>`_, som avholdes av Senter for Digital Forskningsstøtte (DSC), ved Universitetsbiblioteket, UiO.

Kurset består av fem kapitler. I :doc:`intersphinx` Getting Started, we log on to Fox. You will need a user account at the University of Oslo and a smart phone or other means of using two factor authentication (2FA).


In Installing Software, we install the software that we will need for this course.

In Querying LLMs (Chatbots), we learn to load and query basic LLMs.

In Summarization, we use LLMs for making shorter summaries of documents.

In Retrieval-Augmented Generation, we build an application for doing Retrieval-Augmented Generation based on a set of documents.
