R packages required for the prosess
===================================

The first time you install to R::

   install.packages("scales") 
   install.packages("comtradr") 
   install.packages("here") 
   install.packages("rjson") 
   install.packages("ggplot2") 
   install.packages("dplyr") 
   install.packages("plotly") 
   install.packages("conflicted") 
   install.packages("janitor") 
   install.packages("tidyverse")

After the first installation::

   library(scales) 
   library(comtradr) 
   library(here) 
   library(rjson) 
   library(ggplot2) 
   library(dplyr) 
   library(plotly) 
   library(conflicted) 
   library(janitor) 
   library(tidyverse)


.. _installation:

Technical preparations
----------------------
You need R and RStudio, the free version. The software can be found at the homepages of Posit.
https://posit.co/downloads/

R and RStudio
-------------
Downliad from the pages of Posit: https://posit.co/downloads/
You need R and RStudio for desktop. The free version. 

The package ComtradR
--------------------
Install the package::

   # install.packages("devtools")
   devtools::install_github("ropensci/comtradr@main")

You can read more on the package here: https://github.com/ropensci/comtradr/blob/main/README.md

The repository in GitHub: https://github.com/ropensci/comtradr

