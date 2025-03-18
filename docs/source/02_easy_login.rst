.. _02_easy_login:

02 Oppstart
============
.. index:: Fox, server, A100, GPU, hardware, NVIDIA

Vi skal kjøre programmene via tjenesten Educloud On Demand. (Educloud On Demand er en del av Universitetet i Oslo sin databehandlingsplattform Educloud Research.) Educloud On Demand kjører i din nettleser, og du behøver ikke innstallere noen ekstra programmer på din maskin.

Tilgang
--------
For å logge inn, må du søke medlemsskap i Educloud project ec443. Hvordan du gjør det, kommer an på om du allerede har en aktiv konto på Educloud.

Hvis du har en konto, kan du søke om medlemsskap i Educloud prosjektet ec443. Søk gjennom å følge denne veiledningen: Søk om tilgang til et eksisterende Educloud Research-prosjekt.

Hvis du ikke har en konto, må du lage en. Utfør punkt 1b, 2 and 3 i denne veiledningen: Førstegangsoppsett av Educloud Research. I punkt 1b fører du opp prosjekt ec443.

Innlogging
-----------
Logg inn i Educloud On Demand med ditt Educloud brukernavn og passord.

.. note:: Ditt brukernavn i Educloud er forskjellig fra ditt vanlige UiO brukernavn. Educloud brukernavn starter alltid med de tre bokstavene “ec-“. Educloud also has its own, separate two-factor identification (2FA) codes.

Oppstart med JupyterLab
-------------------------
Etter du har logget inn, kan du se Educlouds instrumentpanel. Klikk på JupyterLab, for å konfigurere sesjonen.

I feltet “Choose the Educloud project to run under:”, you should select ec443.

I feltet “Choose resources:”, bør du velge “GPU (1x Nvidia MIG 20G VRAM, 24 CPU cores, 100GB RAM)”.

I feltet “Runtime (in hours)” velg gjerne 1 t av gangen. Prøv å unngå å reservere en GPU lenger enn nødvendig, fordi GPUer er begrensede, delte ressurser.

I feltet “Choose Jupyter module (required)” bør du velge “4.2.0-GCCcore-13.2.0”.

De andre feltene skal ikke fylles ut. Oppsettet ditt skal se ut som bildet under.

.. image:: jupyter_lab_mig.png

Start JupyterLab ved å klikke på den brå “Launch” knappen nederst i skjemaet. Dette lager en jobb som blir sendt til køen. Når de påkrevde ressursene er tilgjengelige, starter jobben din opp.

Når jobben har startet, klikk på “Connect to Jupyter” for å åpne JupyterLab.

.. dropdown:: Valgfri OCR Støtte
    
    Du kan legge til støtte for `Optical Character Recognition (OCR) <https://en.wikipedia.org/wiki/Optical_character_recognition>`_. OCR lar deg konvertere bilder til tekst. Last inn modulen ``tesseract/5.3.4-GCCcore-12.3.0`` ved å legge den til i feltet “Additional modules”. Du må også endre  “Choose Jupyter module (required)” til “4.0.5-GCCcore-12.3.0”, slik at versjonene matcher. 

.. image:: jupyter_lab_tesseract.png


Oppgaver
---------
.. tip:: dokumentmappe i Jupyter lab grensesnitt

    Du trenger en mappe til å lagre dokumentene dine på Educloud. Når du åpner JupyterLab, vil du få filmenyen til venstre. Den peker til ditt Home directory som du finner igjen på Educlou. Her kan du lagre filene dine. Hvis du ikke allerede har en mappe som kalles “documents”, lag en. For å lage en ny mappe, klikk den grå , click the gray “New Folder” knappen i toppmenyen. Nå dukker det en ny mappe opp på listen, med forslag til navn “Untitled Folder”. Skriv “documents” istedenfor “Untitled Folder” og trykk enter på ditt eget tastatur for å lagre.

.. tip:: laste opp filer med Educloud grensesnitt

    Du kan laste opp dokumenter som du ønsker å jobbe med på Fox. Prøv å unngå dokumenter som inneholder sensitive data. Vi anbefaler å teste med offentlig tilgjengelige dokumenter som kun inneholder grønne data.
