.. _01_downloading_packages: to your new venv

01 Downloading packages to venv
===================================

.. index:: something

Vi skal laste ned alle pakkene i venv. Til dette bruker vi et dokument som ligger i en fellesmappe her: 

**/fp/projects01/ec443/clean_env**

**Kjør denne**
Terminal view 1::

   import subprocess
   import sys
   
   # Bytt ut '[your_username]' med ditt faktiske brukernavn. 
   username = "[your_username]"
   
   # Angi stien til aktiveringsskriptet for det virtuelle miljøet
   venv_activate_path = f"/fp/projects01/ec443/{username}/my_venv/bin/activate"
   
   # Funksjon for å aktivere det virtuelle miljøet
   def activate_venv(activate_path):
       try:
           subprocess.run(["bash", "-c", f"source {activate_path} && echo 'Virtuelt miljø aktivert.'"], check=True)
       except subprocess.CalledProcessError as e:
           print(f"En feil oppsto ved aktivering av det virtuelle miljøet: {e}")
   
   # Kall funksjonen for å aktivere det virtuelle miljøet
   activate_venv(venv_activate_path)


**Deretter kjører du denne**
Terminal view 2::

   import subprocess
   import sys
   
   # Funksjon for å installere avhengigheter fra requirements.txt
   def install_requirements(requirements_path):
       try:
           # Installerer pakker fra requirements.txt
           subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_path])
           print("Alle avhengigheter er installert.")
       except subprocess.CalledProcessError as e:
           print(f"En feil oppsto ved installasjon av avhengigheter: {e}")
   
   # Sti til requirements.txt
   requirements_path = "/fp/projects01/ec443/clean_env/cleaned_requirements_2.txt"
   
   # Kaller funksjonen for å installere avhengigheter
   install_requirements(requirements_path)
   
   # Inni requirements.txt, triton==2.0.0  # Endret til kompatibel versjon




.. todo:: 
   todo 5.1: Hver bruker må installere de rette pakkene i sitt miljø som heter `my_env`. Pakkene ligger definert i `cleaned_requirements_2.txt` filen som befinner seg her: `/fp/projects01/ec443/clean_env`.

.. toctree::
   :maxdepth: 1
   :caption: Table of Contents
   :titlesonly:

   00_preparations
   01_downloading_packages
   02_ai_board
   03_parameters
   04_hello_world
   05_login
   06_jotain
   07_pirat
   08_pegasus
   09_algo
   10_alami
   11_juoga
   21_elastic_search
   22_disk_quota
   30_todo


