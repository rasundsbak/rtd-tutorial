
.. _01 Welcome to the test suite of thid documentation:
01 Welcome to the test suite
============================
You can play with your code here, and test it. When ypu get the code to work, put the functionality into 4.2.AI.

.. index:: welcome, introduction

Squash and merge - Hva betyr det?
=========================

"Squash and merge" er en metode som brukes i versjonskontrollsystemer, som for eksempel Git, når man slår sammen ("merger") en gren inn i hovedgrenen (eller en annen gren). Den er spesielt populær i samarbeidende utviklingsprosjekter som hostes på plattformer som GitHub, GitLab, og Bitbucket.

Hva betyr "Squash and Merge"?
Når du bruker "Squash and Merge", gjøres følgende:
Squash: Alle committer fra en gren komprimeres (eller "squashes") til en enkelt commit.
Merge: Den singulære nye committen blir deretter slått sammen (merged) inn i målgrenen.

Hvorfor bruke "Squash and Merge"?
Ren historie: Ved å komprimere flere små og ofte urelaterte committer til en enkel commit, blir historikken til prosjektet renere og lettere å lese.
Opprettholder sammenheng: Sikrer at all endring fra funksjonsgrenen opprettholder sammenheng som en helhet når de legges inn i hovedgrenen.
Forhindrer rotete logg: Reduserer mengden unødvendige detaljer og bugfikser som gjør loggen rotete og vanskelig å følge.

Donec nec quam sit amet quam elementum porta.
_________________________________
In in ligula pharetra, posuere massa vitae, dignissim dui. Morbi ultrices ipsum nec velit lacinia lacinia. Pellentesque pharetra leo et nisl efficitur ornare. Proin hendrerit maximus sem et facilisis. Pellentesque faucibus volutpat mauris, sit amet fermentum leo ullamcorper et. Donec ac velit vehicula, facilisis velit non, pellentesque diam. Quisque in consequat libero. Integer sagittis lacinia mollis. Praesent varius ex rutrum turpis laoreet, vitae vulputate justo euismod. Donec congue aliquam erat, at sollicitudin erat finibus a. Sed arcu metus, semper in tempor rhoncus, posuere vitae augue. Quisque dapibus turpis placerat arcu ullamcorper, id faucibus nisi iaculis.

In hac habitasse platea dictumst
______________________________
Example clean Requirements
This code fetch information from the file requirement and clean up the old file paths
Jupyter lab 3::

  # renser requirements.txt for navnet på gamle filstier:

  import re

  def clean_requirements_file(input_file, output_file):
      with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
          for line in infile:
              # Fjern linjen hvis den inneholder @ file:/// eller @ /path/
              if not re.search(r'(@ file:///|@ /|@file:///|@/)', line):
                  outfile.write(line)
              else:
                  # Finn og hent pakkenavn og versjon hvis de finnes på spesifik formatt
                  match = re.match(r'([^@]+)@ .+', line)
                  if match:
                      package_name = match.group(1)
                      outfile.write(f'{package_name}\n')
                  else:
                      # Hvis match ikke finnes, behold linjen som den er
                      outfile.write(line)

  input_file = 'requirements.txt'
  output_file = 'cleaned_requirements.txt'
  clean_requirements_file(input_file, output_file)
  print(f"Cleaned requirements written to {output_file}")

This project has its documentation hosted on Read the Docs: https://readthedocs.org/
This project has a GitHub repository: https://github.com/rasundsbak/rtd-tutorial/tree/3.0.y

Check out the :doc:`usage` section for further information, including
how to :ref:`installation` the project.
