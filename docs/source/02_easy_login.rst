.. _02_easy_login:

Oppstart
=========
Vi skal kjøre programmene via tjenesten Educloud On Demand. (Educloud On Demand er en del av Universitetet i Oslo sin databehandlingsplattform Educloud Research.) Educloud On Demand kjører i din nettleser, og du behøver ikke innstallere noen ekstra programmer på din maskin.

Tilgang
--------
For å logge inn, må du søke medlemsskap i Educloud project ec443. Hvordan du gjør det, kommer an på om du allerede har en aktiv konto på Educloud.

Hvis du har en konto, kan du søke om medlemsskap i Educloud prosjektet ec443. Søk gjennom å følge denne veiledningen: Søk om tilgang til et eksisterende Educloud Research-prosjekt.

Hvis du ikke har en konto, må du lage en. Utfør punkt 1b, 2 and 3 i denne veiledningen: Førstegangsoppsett av Educloud Research. I punkt 1b fører du opp prosjekt ec443.

Innlogging
-----------

Logg inn i Educloud On Demand med ditt Educloud brukernavn og passord.

.. note::

Your username on Educloud is different from your regular UiO username. Educloud usernames always start with the three characters “ec-“. Educloud also has its own, separate two-factor identification (2FA) codes.
Starting JupyterLab

After logging in, you should see the Educloud Dashboard. Click on JupyterLab on the dashboard. Here, you can configure your JupyterLab session.

    In the field “Choose the Educloud project to run under:”, you should select ec443.

    In the field “Choose resources:”, you should select “GPU (1x Nvidia MIG 20G VRAM, 24 CPU cores, 100GB RAM)”.

    In the field “Runtime (in hours)” you should enter 3, for this course. In general, avoid reserving a GPU for longer than necessary, because GPUs are limited, shared resources.

    In the field “Choose Jupyter module (required)” you should select “4.2.0-GCCcore-13.2.0”.

The other fields should be blank. Now, your setup should look like the picture below.

02 Innlogging og oversikt
===========================
.. index:: Fox, server, A100, GPU, hardware, NVIDIA

Oppstart med JupyterLab
-------------------------

Etter du har logget in, kan du se Educlouds instrumentpanel. Klikk på JupyterLab, for å konfigurere sesjonen.

    I feltet “Choose the Educloud project to run under:”, you should select ec443.

    In the field “Choose resources:”, skal du velge “GPU (1x Nvidia MIG 20G VRAM, 24 CPU cores, 100GB RAM)”.

    In the field “Runtime (in hours)” you should enter 3, for this course. In general, avoid reserving a GPU for longer than necessary, because GPUs are limited, shared resources.

    In the field “Choose Jupyter module (required)” you should select “4.2.0-GCCcore-13.2.0”.

The other fields should be blank. Now, your setup should look like the picture below.

.. image:: fox_skjermbilde.png

.. note::

  Task 2.1: Explore the top menu and look into the folders. What does it look like? Familiarize yourself with the browser view of Fox. For a beginner, it is useful to learn how to copy paths and move or copy files and folders between the project area and the Home Directory.

.. image:: fox_top_menu.png

.. note::

  Task 2.2: Look for the left menu in the browser view. Go to Home directory --> New directory (White button on second top menu) --> Directory name: documents. This is where you may store the documents for this workshop, and later your own material.


  Task 2.3: Take some, or all of the content from this path: /fp/projects01/ec443/documents, and move it into your own documents folder that you made on your own home directory.
