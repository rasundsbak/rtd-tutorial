# Configuration file for the Sphinx documentation builder.

# -- Project information --

project = 'KI på Klynge'
copyright = '2026, KI gruppen på UB'
author = 'Ragnhild Sundsbak, Erik Winge'

release = '5.0'
version = '5.0.no'

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
    "sphinx_design",
    'myst_nb',
    'sphinx_togglebutton',
]

togglebutton_selector = '.admonition.dropdown, .toggle, .sd-dropdown'
# Denne er til nbsphinx nbsphinx_execute = 'never'

source_suffix = {
    '.rst': 'restructuredtext',
    '.ipynb': 'myst-nb',
}

# new suggestion by chat GPT January 2026
# not enabled: "linkify",

myst_enable_extensions = [
    "colon_fence",  # enables ```{note} and other directive fences
    "attrs_block",  # allows :class: dropdown on blocks
    "deflist",
    "substitution",
    "tasklist",
]

nb_execution_mode = "off"

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

# intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
exclude_patterns = []

# -- Master document --

master_doc = 'index'

# -- Options for HTML output --

html_theme = 'sphinx_rtd_theme'

# -- Options for TODO extension --

todo_include_todos = False

# -- Options for EPUB output --
epub_show_urls = 'footnote'

# changing layout: https://sphinx-rtd-trial.readthedocs.io/en/1.1.3/theming.html
# css colours: https://www.w3schools.com/cssref/css_colors.php
# Konvertering .rst til .ipynb
# Skru av når konvertering er utført
# Konvertering med extension = 'sphinxcontrib.jupyter',
# Konfigurasjon for sphinxcontrib-jupyter:
#jupyter_kernels = {
#    "python3": {
#        "name": "python3",
#        "display_name": "Python 3",
#        "language": "python",
#    }
#}