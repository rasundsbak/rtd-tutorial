01 Welcome to the pilot course on how to use ComtradR
======================================
This project has its documentation hosted on Read the Docs: https://readthedocs.org/
This project has a GitHub repository: https://github.com/rasundsbak/rtd-tutorial/tree/3.0.y

Check out the :doc:`usage` section for further information, including
how to :ref:`installation` the project.

.. note::

   This project is under active development.
---

.. note::

   This is a test

---

01 Introduction
===============
This is a report after following a bachelor course of STV 2020 Spring term 2023, University of Oslo. This text may be used as a tutorial for using Comtrade. In the following, it will be outlined how data from the United Nations' Comtrade database [@CRANPackageComtradr] can be used to point out structural problems related to oil industry. This will be the academic example used to demonstrate both the process of data collection, as well as the processing and division of data into relevant units. While working on this project, the United Nations API delivery was modernized and changed from being facilitated for R and RStudio into Python. The ComtradR is still being maintained under the GitHib initiative of OpenSci[@muir2023; @ROpenSciOpenTools]. This project will be developed according to the progress of the technical development of the official Comtrade database. A repository on how to generate data with Python, for import to RStudio may come at a later time.

02 The research question
========================
OPEC countries, their oil export and democracy development. The statistics shown will be from the OPEC countries. Data on Trade value in Crude oil will be collected from Comtrade legacy database [@muir2023]. "Trade value" was chosen because it is the variable in this category that includes the most data. If choosing another category, the number of missing values would be larger. The development of the values of Trade value will be shown from the period 1995-2004. Then then the results of the Opec countries on a corruption index from the World Bank governance Indicators will be introduced [@kaufmann2023]. Finally, a regression analysis with corruption level as the dependent variable will be shown. The unit of analysis will be land- years. The process of restructuring the data will be shown.

03 The academic problem
=======================
We are going to look at data from the two institutions of Comtrade and World bank.

**Q1 How does the distribution of Export of Crude oil from the OPEC countries look like for the years from 1995 until today?**

**Q2 How does the available corruption index of the OPEC countries look like?**

**Q3 Is there a tendency for the OPEC countries that higher income from oil export leads to higher levels of corruption?**

In order to answer these questions, data will be taken from two sources. Firstly, numbers on trade is taken from the Comtrade database. Secondly, indicators on democracy and corruption levels are taken from the Worldwide Governance Indicators.

This project should be seen as a pedagogical example on how to extract and analyze data for political and social science, rather than real social science. The main focus here is on the technical processes, rather than the scientific value of the findings.


A good way to start up an R script
==================================

In the .R file, at the very begining::

<pre><code class="language-css">.some-box {
	width: 20px;
	height: 20px;
	background: black;
	margin-bottom: 1.5rem;
}
</code></pre>

   getwd
   setwd("/Users/ragnhildsundsbak/Documents/LearningR2023/ComtradeProjectNew")

I always start with the setwd. This is a very useful command, it is a good idea to combine it with opening the library(here)

In order to follow the process in this script, we need the following pagkages. Note that if you do not have them installed, you must use the command "install.packages("package name")::

   install.packages("comtradr")
   install.packages("rjson")

This chunk is for the activation of already downloaded packages::

   library(comtradr) 
   library(here)
   library(rjson)
   library(ggplot2)
   library(dplyr)
   library(plotly)
   library(conflicted)
   library(janitor)

Then I need to rule out the conflicts between the packages that are in use::

   conflict_scout()

   conflicts_prefer(stats::chisq.test) 
   conflicts_prefer(stats::fisher.test) 
   conflicts_prefer(dplyr::filter)
   conflicts_prefer(plotly::layout)
   conflicts_prefer(dplyr::lag)


This is a normal text paragraph. The next paragraph is a code sample::

   It is not processed in any way, except
   that the indentation is removed.

   It can span multiple lines.

This is a normal text paragraph again.



 import lumache
 lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

03 Lorem Ipsum
==============
03.01 Etiam tincidunt
---------------------
This is an ordinary paragraph.

 print 'this is a Doctest block'
this is a Doctest block

The following is a literal block::

     This is not recognized as a doctest block by
    reStructuredText.  It *will* be recognized by the doctest
    module, though!

03.02 Etiam tincidunt
---------------------

"Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit..."
"There is no one who loves pain itself, who seeks after it and wants to have it, simply because it is pain..."

This is an ordinary paragraph, introducing a block quote.

    "It is my business to know things.  That is my trade."

    -- Sherlock Holmes



04 Lorem ipsum dolor sit amet
=============================
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut eleifend augue, et pretium turpis. Fusce in tortor a tellus luctus tristique a at metus. Pellentesque in suscipit ipsum. Ut bibendum elit orci, eget efficitur mauris fringilla eget. Aliquam vitae risus lectus. Nam quis ante magna. Nunc hendrerit tellus at tortor dapibus, ut porttitor enim tincidunt. Etiam nisl purus, fermentum sit amet justo ac, lobortis congue ipsum. Cras nisl nisi, vehicula ac suscipit vitae, consectetur at ligula. Morbi faucibus dignissim dictum. Phasellus bibendum iaculis tellus, sed vehicula est luctus imperdiet. Pellentesque dictum enim est, at condimentum mauris iaculis et. Nulla posuere congue luctus. Aliquam nec sem pretium massa mollis ornare. Proin vel nulla eu dolor consequat fermentum nec et velit. Ut quis sapien non lacus pretium elementum.

01 Suspendisse consequat sagittis leo at accumsan
----------------------------------------------

02 Suspendisse consequat sagittis leo at accumsan
----------------------------------------------


05 Quisque at finibus orci
==========================
Quisque at finibus orci. Suspendisse sit amet magna rutrum nisl tincidunt eleifend. Nulla tempus turpis justo, aliquam viverra ex bibendum at. Praesent accumsan ligula in magna consequat consectetur. Morbi vestibulum tempor odio et commodo. Suspendisse potenti. Suspendisse congue vitae erat eget pellentesque. Donec imperdiet posuere dapibus. Etiam maximus sodales eros, lobortis vulputate mauris commodo ut. Maecenas iaculis sem a tempor tempus. Nulla diam nibh, lacinia non dolor ut, imperdiet aliquet augue. Aenean elit quam, mattis eu ligula a, dapibus sodales nunc. Vivamus a commodo magna, non imperdiet metus.

.. _Suspendisse consequat sagittis leo at accumsan:
Suspendisse consequat sagittis leo at accumsan
----------------------------------------------
- Suspendisse consequat sagittis leo at accumsan. 
- Donec dapibus euismod mi ac tempus. 

In.hac_habitasse() platea dictumst. 
Etiam varius nisi eu nunc fringilla ultricies. Ut sapien neque, sollicitudin sed eros id, ornare luctus mauris. Sed ac auctor lorem. Curabitur vitae justo est. Sed quis est at urna malesuada vestibulum sit amet vitae nisi. Vivamus fringilla, nisl quis maximus dignissim, felis justo pulvinar nisi, vitae scelerisque mauris nibh commodo nunc. Nunc eu est nisl. Duis luctus sed sapien eu feugiat. Suspendisse efficitur sagittis neque, non fringilla justo egestas ut. Phasellus posuere pretium est, ac sollicitudin diam egestas in.

.. _Etiam tincidunt:
Etiam tincidunt
---------------
- Etiam tincidunt: https://www.writethedocs.org/guide/writing/beginners-guide-to-docs/#id1

ex ac viverra semper, diam eros laoreet felis, vel maximus purus nunc a augue. Cras ultricies elementum enim. Praesent sed pharetra ipsum. Nullam vel risus tellus. Sed finibus risus at condimentum laoreet. Sed volutpat convallis sapien, id pharetra ante. Quisque sagittis lobortis mattis.

.. _Suspendisse vulputate est vitae nunc porta:
Suspendisse vulputate est vitae nunc porta
------------------------------------------
Suspendisse vulputate est vitae nunc porta, in tempor sem convallis. Vivamus turpis turpis, imperdiet et viverra et, sodales nec ligula. Nullam ultrices diam sed nisl imperdiet sollicitudin. Quisque id nulla dapibus, tincidunt odio vitae, euismod erat. In in aliquet libero, sed pharetra nisi. Maecenas vel erat pretium, aliquet sapien vitae, ornare neque. Aliquam facilisis, diam vel porttitor tincidunt, tortor eros molestie arcu, nec vulputate enim justo eget nulla. Nam gravida interdum ligula id convallis. Aenean suscipit auctor blandit. Maecenas iaculis lectus in neque mattis, ut hendrerit nunc imperdiet. Sed sed sem sed turpis egestas fringilla. Quisque nec est quis lacus consectetur faucibus tempor vel ex. Integer lobortis augue ac orci vestibulum egestas non blandit diam. Nulla vel lacus nec ex tempus luctus nec eget tortor. 


Contents
--------

.. toctree::

   01 Welcome to Lumache's documentation!
   01 Introduction
   02 The research question
   03 The academic problem
   04  
   05 
   04 Quisque at finibus orci
      Suspendisse consequat sagittis leo at accumsan
      Etiam tincidunt
      Suspendisse vulputate est vitae nunc porta
      
   
   

