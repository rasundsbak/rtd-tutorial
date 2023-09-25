R packages required for the prosess
===================================
The first time you install to R:
--------------------------------

.. code-block:: console
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

After the first installation
----------------------------

.. code-block:: console
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
Suspendisse consequat sagittis leo at accumsan
----------------------------------------------

To use Lumache, first install it using pip:

.. code-block:: console

   (.venv) $ pip install lumache

Creating recipes
----------------

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

