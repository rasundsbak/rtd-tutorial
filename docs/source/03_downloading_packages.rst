.. _03_downloading_packages:
03 Setup
========
New Style: Using Jupyter Notebook
-------------

.. todo:: This will change: put in new setup from workbook

Cell 1::

   import os
   import subprocess
   import sys
   
   # Specify the path to your virtual environment
   username = "your_username"  # Replace 'your_username' with the actual username
   venv_path = f"/fp/homes01/u01/{username}/my_venv"
   
   # Create the virtual environment
   subprocess.check_call([sys.executable, "-m", "venv", venv_path])
   print(f"Created new virtual environment at {venv_path}")

Cell 2::

   import subprocess
   import sys
   
   # Function to activate the virtual environment in Jupyter notebook
   def activate_venv(venv_path):
       activate_this = os.path.join(venv_path, "bin/activate_this.py")
       with open(activate_this) as f:
           exec(f.read(), {'__file__': activate_this})
   
   # Activate the virtual environment
   activate_venv(venv_path)
   print(f"Activated virtual environment at {venv_path}")

Cell 3::

   # Path to the requirements.txt file
   requirements_path = "/fp/projects01/ec443/clean_env/cleaned_requirements_2.txt"
   
   # Function to install packages from a requirements file
   def install_requirements(requirements_path, venv_path):
       subprocess.check_call([os.path.join(venv_path, "bin", "python"), "-m", "pip", "install", "-r", requirements_path])
       print("All dependencies are installed.")
   
   # Install the requirements
   install_requirements(requirements_path, venv_path)
   print("All dependencies have been installed.")
   # Inni requirements.txt, triton==2.0.0  # Endret til kompatibel versjon



03. 1 Old style - you have established a venv from commandline. Downloading packages.
--------------------------------------------------
.. index:: virtual environment, activate venv, path, requirements

Vi skal laste ned alle pakkene i venv. Til dette bruker vi et dokument som ligger i en fellesmappe her: 

**/fp/projects01/ec443/clean_env**

**Kjør denne**
Cell 1::

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
Cell 2::

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

Terminal view 3::

   !pip install --upgrade pip
