# Configuration file for the Sphinx documentation builder.

import os  # For using environment variables (optional)

# -- Project information --

project = 'AI on Cluster'
copyright = '2024'
author = 'Documentation Team'

release = '4.2'
version = '4.2.AI'

# -- General configuration --

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_copybutton',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output --

html_theme = "pyramid"

# -- Options for TODO extension --
todo_include_todos = os.getenv('SPHINX_TODO_INCLUDE_TODOS', 'False') == 'True'

# -- Options for EPUB output --
epub_show_urls = 'footnote'

# changing layout: https://sphinx-rtd-trial.readthedocs.io/en/1.1.3/theming.html
# css colours: https://www.w3schools.com/cssref/css_colors.php
