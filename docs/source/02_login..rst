.. _02 login:
02 Login to browser and Terminal
=====================
.. index:: Fox, server, cuda, A100, GPU, hardware

`Here <https://www.uio.no/english/services/it/research/platforms/edu-research/help/fox/system-overview.md>`_, you may read more about the technical specifications on Fox. Most important from this page, is that Fox has a GPU accelerated part of the system, with four NVIDIA A100 cards each, as well as three nodes with four NVIDIA RTX 3090 cards from IFI. These systems of hardware are fit for running AI on.

Log in to Fox and Educloud in the browser
-----------------------------------------
When you are logged on to the Fox, move like this: frol the left menu, go to Jupyter lab --> ec-[your group number] Choose one of the Nvidia GPUs from the drop down menu --> Rumtime. 1h --> Jupyter variant, Jupyter lab --> (You need not choose jupyter modile, as the last version is pre selected) -->  Launch. You are now in the line to get into the Jupyter lab on UiO Fox. You can get tea or coffee, and have a chat with your cilleague, while you wait.


At the Fox server, you have your own storage space. There is also a common space for the group on the server. This is where the AIs are located, and where the AI will be temporarily cached when you download it from Huggingface. In order to get the AI to work in Jupyter lab, it is essential that you set up the paths in the right way. Take a look around, and see if you can think of a good way to organize your project. 

.. note::

   First task: Visit Huggingface and search for google/Pegasus. What do you see? Switch the search to meta-llama/Llama-3.1-8B-Instruct and read. Is this a model that you can find at Fox? What format is it in? Find the format of the Llama AI at Fox, and google it, in order to find out more about this dataformat.



Log in to Fox and Educloud through SSH, in Bash or Terminal
-------------------------------------------------

.. index:: login, ssh, bash, terminal


Open the Command prompt (PC) or Terminal. Log in to Fox using ssh. You may find more information on the USIT page `Fox Account Creation and Login (SSH) <https://www.uio.no/english/services/it/research/platforms/edu-research/help/fox/account-login.md>`_

Terminal view 1::
   
   Last login: Sat Nov  2 10:51:34 on console
   (base) navnesenmaskin@eduroam-193-157-163-121 ~ %



Terminal view 2::
   
   Last login: Sat Nov  2 10:51:34 on console
   (base) navnesen@eduroam-193-157-163-121 ~ % ssh ec-navnesen@fox.educloud.no
   (ec-navnesen@fox.educloud.no) One-Time_Code: 



Terminal view 3::

   Welcome to FOX

      "'~-.       .-~'"
      |   .'"""""'.   |
      \`_"         "_'/
       )             (
       /   0     0   \
      <               >
    .< __.-'. _ .'-.__ >.
      "-.._  (#)  _..-"
           `-:_:-'
   The HPC Cluster in Educloud


# Lag en mappe for pip-arbeidsfiler, for eksempel pip_cache
mkdir -p /fp/projects01/ec367/ragnhsu/pip_cache


# Sett opp miljøvariabler i din shell init fil (f.eks. .bashrc eller .bash_profile)
echo 'export PATH=/fp/projects01/ec367/ragnhsu/pip_cache/bin:$PATH' >> ~/.bashrc
echo 'export PIP_CACHE_DIR=/fp/projects01/ec367/ragnhsu/pip_cache' >> ~/.bashrc
echo 'export PIP_TARGET=/fp/projects01/ec367/ragnhsu/pip_cache' >> ~/.bashrc

# Bruk de nåværende variablene i sesjonen din
source ~/.bashrc

# Aktivér ditt venv
source /fp/projects01/ec367/ragnhsu/venv_transformers/bin/activate

# Installer transformers og torch i venv
pip install transformers
pip install torch




