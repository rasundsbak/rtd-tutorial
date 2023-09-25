# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Download data with R'
copyright = '2023, Ragnhild'
author = 'Ragnhild'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

# this is for making the content of the "static" folder work
# from: https://stackoverflow.com/questions/44793811/change-the-colors-of-the-sphinx-read-the-docs-theme 
html_static_path = ['_static']

# from: https://stackoverflow.com/questions/44793811/change-the-colors-of-the-sphinx-read-the-docs-theme 
def setup(app):
    app.add_css_file('custom.css')

# html_theme = 'default'
# this not working
# sidebarbgcolor = 'DarkOrange'

# html_theme = 'sphinx_rtd_theme'

# default works, but not to change colour
# html_theme = 'default'
# sidebarbgcolor = '#FF8C00'
# sidebarbgcolor = 'DarkOrange'

html_theme = "pyramid"

# -- Options for EPUB output
epub_show_urls = 'footnote'

# changing layout: https://sphinx-rtd-trial.readthedocs.io/en/1.1.3/theming.html
# css colours: https://www.w3schools.com/cssref/css_colors.php
