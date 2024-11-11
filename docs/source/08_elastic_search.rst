.. _08 elastic search
Install and unpack elasticsearch
=================================

.. index:: terminal, elasticsearch


Terminal view 1::

  # Gå til rotmappen din (hvis du ikke er der)
  cd /fp/projects01/ec367/navnesen/

Terminal view 2::

  # Opprett en ny mappe for Elasticsearch
  mkdir elasticsearch
  cd elasticsearch

Terminal view 3::

  # Last ned Elasticsearch tar.gz filen
  wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.4.3-linux-x86_64.tar.gz

  # Pakk ut Elasticsearch i den nye mappen
  tar -xzf elasticsearch-8.4.3-linux-x86_64.tar.gz

  # Flytt elastisearch-8.4.3 til en enklere struktur:
  mv elasticsearch-8.4.3/* . 
