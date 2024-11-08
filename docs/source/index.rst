In this project, We use Sphinx to formulate our ideas: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

Run large language models through Educloud On Demand
===============================================

Here, you will learn how to set up your own virtual environment at the new UiO Nvidia Cluster. This blog belongs to a course held as a part of Digital Scholarship Days 2025. The course is for employees at the University of Oslo. If you are in our interest group, `you may sign up here <https://www.ub.uio.no/english/courses-events/events/dsc/2025/digital-scholarship-days/01-run%20large%20language%20models%20through%20Educloud%20UiO>`_. AIs from Huggingface run on a Transformer architecture. The method we are going to use, Jupyter Lab is an effective way of showing what goes on behind the interface of the AI. You will learn how the language model is built, how the parameters are set, and what the output is like. We hope this will give you insight into how the AI of our times work.

.. note::

   This project is under active development.


Contents
--------

Welcome to Your Project Name's documentation!
==============================================


.. note::

   This project is under active development.

.. image:: fox.png

.. toctree::
   :maxdepth: 2

   00 Preparations: Before you come
   01 This is a test
   02 Hugging face and the AIs
   03 Get an overview
   04 Log in to Educloud through SSH, in Bash/ Terminal
   05 What is a Cluster and what about the rest?
   06 Log on to Jupyter lab on demand
   07 Disk quota exceeded problem
   



00 Preparations: Before you come
===============
* `Sign up <https://www.ub.uio.no/english/courses-events/events/dsc/2025/digital-scholarship-days/01-run%20large%20language%20models%20through%20Educloud%20UiO>`_ for the course.
* When you get the confirmation e-mail from the instructors, you are ready for the next step.
* Log in to Educloud with your two factor authenticator
* Download Microsoft Authenticator on your phone. It may be downloaded from App Store (iPhone) or Google Play (Android)
*  `Follow the instructions <https://www.uio.no/english/services/it/research/platforms/edu-research/help/getting-started-with-educloud.html#with-idporten>`_ for first time setup of Educloud Research.
*  Try your setup on `Educloud on demand <https://ood.educloud.no>`_


In this tutorial, you will learn how to set up your own virtual environment at the UiO Nvidia Cluster. This repo is a part of the course held as a part of `Digital Scholarship Days 2025 <https://www.ub.uio.no/english/courses-events/events/dsc/2025/digital-scholarship-days/00-mainpage.html/>`_

01 This is a test
=================
We are testing our code with Gnus. See how it jumps!

.. image:: bausenhart.jpg

02 Hugging face and the AIs
============================
"Hugging Face is a machine learning (ML) and data science platform and community that helps users build, deploy and train machine learning models." Ben Lutkevich on `Tech Target <https://www.techtarget.com/whatis/definition/Hugging-Face>`_

`Hugging face <https://huggingface.co/>`_ is a good place to start, when you want to familiarize yourself with the LLMs. However, in this course you do not need to download them, because we, the instructors have already done some of the work for you. If you want to learn, keep reading!

03 Get an overview
==================
At the Fox server, you have your own storage space. There is also a common space for the group on the server. This is where the AIs are located, and where the AI will be temporarily cached when you download it from Huggingface. In order to get the AI work in jupyter lab, it is essential that you set up the paths in the right way. Take a look around, and see if you can think of a good way to organize your project. 

.. note::

   First task: Visit Huggingface and search for googgle/Pegasus. What do you see? Switch the search to meta-llama/Llama-3.1-8B-Instruct and read. Is this a model that you can find at Fox? What format is it in? Find the format of the Llama AI at Fox, and google it, in order to find out more about this dataformat. 



04 Log in to Educloud through SSH, in Bash/ Terminal
====================================================

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


05 What is a Cluster and what about the rest?
=============================================
In this course, we speak a strange language, where we mention words like Cluster, HPC, Transformers and .ggufs like they where regular items from the grocery store. Write a list over concepts that you do not understand. Go in pairs, and discuss the concepts you want to elaborate on. Use google og UiO GPT or an encyclopedia from the library. Do not worry. A few months ago, the teachers of this course did not know what a Nvivia A100 Tensor Core GPU was, and we did not care. Now, we are used to it and interact with the A100 almost every day. When you start working with the AI, you will soon learn the most important concepts.

06 Log on to Jupyter lab on demand
==================================
When you are logged on to the Fox, move like this: frol the left menu, go to Jupyter lab --> ec-[your group number] Choose one of the Nvidia GPUs from the drop down menu --> Rumtime. 1h --> Jupyter variant, Jupyter lab --> (You need not choose jupyter modile, as the last version is pre selected) -->  Launch. You are now in the line to get into the Jupyter lab on UiO Fox. You can get tea or coffee, and have a chat with your cilleague, while you wait.



Aliquam erat volutpat. Nullam id augue rhoncus, ultrices leo non, cursus ex. Maecenas arcu tortor, gravida eu faucibus vel, eleifend varius ex. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. 
   getwd
   setwd("/Users/ragnhildsundsbak/Documents/LearningR2023/ComtradeProjectNew")
   ..

It is always start with the setwd. It is a good idea to combine it with opening the library(here). Many people prefer to use projects in RStudio. The reason why I no not, is that i feel the setwd command and "here" package gives me both better knowledge and control over my system.



If you do not know your directory, use the command "getwd". Then, copy the directory from the answer you got, and adjust it to fit the path that suits you. In the .R file, at the very begining::

   getwd
   setwd("/Users/ragnhildsundsbak/Documents/LearningR2023/ComtradeProjectNew")

It is always start with the setwd. It is a good idea to combine it with opening the library(here). Many people prefer to use projects in RStudio. The reason why I no not, is that i feel the setwd command and "here" package gives me both better knowledge and control over my system.

In order to follow the process in this script, we need the following pagkages. Note that if you do not have them installed, you must first use the command install.packages("package name"). Since this is to be done only once, I often use the # tag to make the coding turn into a comment that will not be executed.

1 Installation example::
   

   Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
   Vestibulum quis auctor mi, vel elementum arcu. 
   Donec fermentum luctus rhoncus.

2::

   Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
   Vestibulum quis auctor mi, vel elementum arcu. 
   Donec fermentum luctus rhoncus.

   Selected output console:

   > 
   > 
   > 



It is also necesary to rule out the conflicts between the packages that are in use 
3::

   Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
   Vestibulum quis auctor mi, vel elementum arcu. 
   Donec fermentum luctus rhoncus.

4::

   Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
   Vestibulum quis auctor mi, vel elementum arcu. 
   Donec fermentum luctus rhoncus.


   Selected output:

   > 
   > 
   > 
   >
   >
   > 

We are ready to start the process of getting data.






06 And even more babbelbla balubala
=============================
Sed pulvinar pellentesque arcu, sit amet iaculis augue luctus eget. Integer ut elit volutpat, mattis eros in, auctor lorem. Ut arcu nisi, condimentum vestibulum nibh nec, tincidunt aliquam odio. 
      
   
   

