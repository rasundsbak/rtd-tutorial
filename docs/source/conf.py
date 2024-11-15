# Configuration file for the Sphinx documentation builder.

import os

# -- Project information --

project = 'Lumache'
copyright = '2021'
author = 'Ragnhild'

release = '0.1'
version = '0.1.0'

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

# Innstillinger for Intersphinx
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output --
html_static_path = ['_static']

# Bruk pyramid-tema
html_theme = "pyramid"

# -- Options for EPUB output --
epub_show_urls = 'footnote'

# -- Options for TODO extension --
todo_include_todos = True
# todo_include_todos = False

# Tilpasse sidebar innhold for alle sider
html_sidebars = {
    '**': [
        'globaltoc.html',  # Global table of contents
        'relations.html',  # Previous/next navigation
        'searchbox.html',  # Search box
    ]
}

# Ekstra oppsett for tilpasninger
def setup(app):
    app.add_css_file('custom.css')
    app.add_js_file('custom.js')
