.. _01_easy_login:

Oppstart
==========

.. index:: Fox, server, A100, GPU, hardware, NVIDIA

Vi skal kjøre programmene via tjenesten `Educloud On Demand <https://www.uio.no/tjenester/it/forskning/beregning/open-on-demand/>`_. (Educloud On Demand er en del av Universitetet i Oslo sin databehandlingsplattform `Educloud Research <https://www.uio.no/tjenester/it/forskning/plattformer/edu-research/index.html/>`_.) Educloud On Demand kjører i nettleseren, og du behøver ikke å innstallere noen ekstra programmer.

Tilgang
--------
For å logge inn, må du søke medlemsskap i Educloud project ec443. Hvordan du gjør det, kommer an på om du allerede har en aktiv konto på Educloud.

    * Hvis du har en konto, kan du søke om medlemsskap i Educloud prosjektet ec443. Følg denne veiledningen: `Søk om tilgang til et eksisterende Educloud Research-prosjekt <https://www.uio.no/tjenester/it/forskning/plattformer/edu-research/hjelp/sok-medlemskap-prosjekt.html>`_.

    * Hvis du ikke har en konto, må du lage en. Utfør punkt 1b, 2 and 3 i denne veiledningen: `Førstegangsoppsett av Educloud Research <https://www.uio.no/tjenester/it/forskning/plattformer/edu-research/hjelp/kom-i-gang-med-educloud.html>`_. I punkt 1b fører du opp prosjekt ec443.

Innlogging
-----------
Logg inn i `Educloud On Demand <https://ondemand.educloud.no>`_ med ditt Educloud brukernavn og passord.

.. note:: Ditt brukernavn i Educloud er forskjellig fra det vanlige UiO brukernavnet. Educloud brukernavn starter alltid med de tre tegnene “ec-“. Educloud har også en egen to-faktor autentisering (2FA).

Oppstart med JupyterLab
-------------------------
Etter du har logget inn, kan du se `Educlouds instrumentpanel <https://ondemand.educloud.no/pun/sys/dashboard>`_. Klikk på `JupyterLab <https://ondemand.educloud.no/pun/sys/dashboard/batch_connect/sys/fox-ood-jupyter/session_contexts/new>`_, for å konfigurere sesjonen. Gruppe ec443 har en reservasjon for 31. mars 2025: **Velg Jupyter (ML node users )**.

   * I feltet “Choose the Educloud project to run under:”, velger du ec443.

   * I feltet “Choose resources:”, bør du velge “GPU (1x Nvidia A100, 40GB, 24 CPU cores, 250GB RAM)”.

   * I feltet “Runtime (in hours)” kan du velge 1 t av gangen. Prøv å unngå å reservere en GPU lenger enn nødvendig, fordi GPUer er begrensede, delte ressurser.

   * I feltet “Choose Jupyter module (required)” bør du velge “4.2.0-GCCcore-13.2.0”.

De andre feltene skal ikke fylles ut. Oppsettet ditt skal se ut som bildet under.

.. image:: ml_node_users.png

Start JupyterLab ved å klikke på den blå “Launch” knappen nederst i skjemaet. Dette lager en jobb som blir sendt til køen. Når de påkrevde ressursene er tilgjengelige, starter jobben din opp.

Når jobben har startet, klikk på “Connect to Jupyter” for å åpne JupyterLab.

.. dropdown:: Valgfri OCR Støtte
    
    Du kan legge til støtte for `Optisk tegngjenkjenning (OCR) <https://no.wikipedia.org/wiki/Optisk_tegngjenkjenning>`_. OCR lar deg konvertere bilder til tekst. Last inn modulen ``tesseract/5.3.4-GCCcore-12.3.0`` ved å legge den til i feltet “Additional modules”. Du må også endre  “Choose Jupyter module (required)” til “4.0.5-GCCcore-12.3.0”, slik at versjonene matcher. 

    .. image:: jupyter_lab_tesseract.png


Oppgaver
---------

.. admonition:: Oppgave: Dokumentmappe i Jupyter lab grensesnitt
   :collapsible: closed

   Du trenger en mappe til å lagre dokumentene dine på Educloud. Når du åpner JupyterLab, vil du få filmenyen til venstre. Den peker til ditt hjemmeområde/ home directory som du finner igjen på Educloud. Her kan du lagre filene dine. Hvis du ikke allerede har en mappe som kalles “documents”, lag en. For å lage en ny mappe, klikk den grå , “New Folder” knappen i toppmenyen. Nå dukker det en ny mappe opp på listen, med forslag til navn “Untitled Folder”. Skriv “documents” istedenfor “Untitled Folder” og trykk enter på tastaturet for å lagre.


.. admonition:: Frivillig oppgave: Laste opp filer med Educloud grensesnitt
   :collapsible: closed

   Du kan laste opp dokumenter som du ønsker å jobbe med på Fox. Prøv å unngå dokumenter som inneholder sensitive data. Vi anbefaler å teste med offentlig tilgjengelige dokumenter som kun inneholder `grønne data <https://www.uio.no/tjenester/it/sikkerhet/lsis/tillegg/lagring/infoklasser.html>`_.

   Velg folderen "dokumenter" som du etablerte på ditt hjemmeområde i forrige oppgave. Velg den blå opplastingsknappen fra toppmenyen. Deretter velger du “browse files” og velger etpar filer til opplasting. Til slutt velger du den grønne "Upload x files" knappen i nedre venstre hjørne.
