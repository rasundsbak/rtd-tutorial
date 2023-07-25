Young female Gnu
================

Young female Gnu Drinking from River
------------------------------------
Photo by `Fabrizio Frigeni: <https://unsplash.com/@ffrige>`_  
on 
`Unsplash: <https://unsplash.com/>`_
Vivamus sed lorem dolor. Donec commodo neque neque, at blandit ligula pharetra vel. Sed tempor at nisi ac egestas. Morbi sit amet pulvinar justo. Duis at arcu quis nisi rhoncus ornare a vel lectus. Suspendisse cursus, turpis posuere pellentesque rhoncus, erat turpis congue elit, ac condimentum mauris urna et orci. Cras in diam eu felis malesuada dictum. Pellentesque vitae elit non nisl ornare imperdiet. Duis tristique hendrerit finibus. Nullam non odio nisi. Nulla leo felis, fringilla ultrices tristique eget, tincidunt quis nibh. Vestibulum leo purus, auctor sed posuere a, efficitur vitae eros. 


.. image:: younggnu.jpg

.. _installation:

Installation
------------

.. image: younggnu.jpg

Water is central for all life on earth
--------------------------------------

To use Lumache, first install it using pip:

.. code-block:: console

   (.venv) $ pip install lumache

See how she enjoys it
---------------------

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


