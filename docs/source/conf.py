# Configuration file for the Sphinx documentation builder.

# -- Project information --

project = 'AI on Cluster'
copyright = '2025 Ragnhild Sundsbak in collaboration with Erik Winge and Pål Lykkja'
author = 'Ragnhild Sundsbak'

release = '5.0'
version = '5.0.en'

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
# not enabled: "linkify", "colon_fence",

myst_enable_extensions = [
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