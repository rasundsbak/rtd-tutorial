.. _00_preparations: Before you come:
00 Preparations: Before you come
===============
You have done this already: `Sign up <https://www.ub.uio.no/english/courses-events/events/dsc/2025/digital-scholarship-days/01-run%20large%20language%20models%20through%20Educloud%20UiO>`_ for the course.

First time users of Educloud
------------
* Download Microsoft Authenticator on your phone. It may be downloaded from App Store (iPhone) or Google Play (Android)

*  `Follow the instructions <https://www.uio.no/english/services/it/research/platforms/edu-research/help/getting-started-with-educloud.html#with-idporten>`_ for first time setup of Educloud Research.
* Apply for project membership to ec443
* send email to `Ragnhild <ragnhild.sundsbak@ub.uio.no>`_ with heading "I applied for membership in ec443"
* When project manager has approved of your application, log in to Educloud with your two factor authenticator
*  Try your setup on `Educloud on demand <https://ood.educloud.no>`_

In this tutorial, you will learn how to set up your own virtual environment at the UiO Nvidia Cluster. This repo is a part of the course held as a part of `Digital Scholarship Days 2025 <https://www.ub.uio.no/english/courses-events/events/dsc/2025/digital-scholarship-days/00-mainpage.html/>`_

Already users of Educloud
------------
Go to https://selfservice.educloud.no/ and apply for project membership under **Project membership**

Log in to through SSH, in Bash or Terminal and making your own virtual environment on ec443
-------------------------------------------------

.. index:: login, ssh, bash, terminal


Open the Command prompt (PC) or Terminal. Log in to Fox using ssh. You will need to read the information on the USIT page `Fox Account Creation and Login (SSH) <https://www.uio.no/english/services/it/research/platforms/edu-research/help/fox/account-login.md>`_

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

Remember to fill in the right details where it says [your username at uio]

Terminal view 4::

   # change into the right subdirectory
   cd /fp/projects01/ec443
   
   # make a directory at ec443, where you plan to have your working files
   mkdir **[your username at uio]**

**Be sure to read the details and put in your username before you copy and paste!**

Terminal view 5::

   # making a virtual env for python packages
   python -m venv /fp/projects01/ec443/**[your username at uio]**/my_venv
   
Terminal view 6::

   # Aktivér ditt venv
   source /fp/projects01/ec443/**[your username at uio)**/my_venv/bin/activate

.. toctree::
   :maxdepth: 1
   :caption: Table of Contents
