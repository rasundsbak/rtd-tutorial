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

Installation
------------

To use ComtradR, first install it::

   # install.packages("devtools")
   devtools::install_github("ropensci/comtradr@main")

You can read more on this package here

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

