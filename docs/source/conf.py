# Configuration file for the Sphinx documentation builder.

# -- Project information --

project = 'AI på Kluster'
copyright = '2025, KI gruppen på UB'
author = 'Pål Lykkja, Ragnhild Sundsbak, Erik Winge'

release = '4.6'
version = '4.6.no'

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
    'sphinx.panels',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
exclude_patterns = []

# -- Master document --

master_doc = 'index'

# -- Options for HTML output --

html_theme = 'sphinx_rtd_theme'

# -- Options for TODO extension --

todo_include_todos = True

# -- Options for EPUB output --
epub_show_urls = 'footnote'

# changing layout: https://sphinx-rtd-trial.readthedocs.io/en/1.1.3/theming.html
# css colours: https://www.w3schools.com/cssref/css_colors.php
