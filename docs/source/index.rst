In this project, We use Sphinx to formulate our ideas: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

"
===============================================

In this documentation, you will learn how to set up your an AI process at the UiO Nvidia Cluster. The documentation belongs to a course held as a part of Digital Scholarship Days 2025. The course is for employees at the University of Oslo. If you are in our interest group, you may sign up here <https://www.ub.uio.no/english/courses-events/events/dsc/2025/digital-scholarship-days/01-run%20large%20language%20models%20through%20Educloud%20UiO>`_. AIs from Huggingface run on a Transformer architecture. The method we are going to use, Jupyter Lab is an effective way of showing what goes on behind the interface of the AI. You will learn how the language model is built, how the parameters are set, and what the output is like. We hope this will give you insight into how the AI of our times work.

.. note::

   This project is under active development.


Contents
--------

.. image:: fox.png

.. toctree::
   :maxdepth: 2

=======
   00 Preparations: Before you come
   01 This is a test
   02 Hugging face and the AIs
   03 Get an overview
   04 Log in to Educloud through SSH, in Bash/ Terminal
   05 What is a Cluster and what about the rest?
   06 Log on to Jupyter lab on demand
   07 Disk quota exceeded problem
=======



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
      
