# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

# Incase the project was not installed
import os
import sys
import time

sys.path.insert(0, os.path.abspath(".."))

# -- Project information -----------------------------------------------------

project = "Developers Resources"
copyright_first_year = "2025"
copyright_owners = "CCPBioSim"
author = "James Gebbie-Rayet"
current_year = str(time.localtime().tm_year)
copyright_year_string = (
    current_year
    if current_year == copyright_first_year
    else f"{copyright_first_year}-{current_year}"
)
copyright = f"{copyright_year_string}, {copyright_owners}. All rights reserved"
version = ""
release = ""

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autosummary",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "sphinx_copybutton",
    "myst_parser",
]

autosummary_generate = True
napoleon_google_docstring = False
napoleon_use_param = False
napoleon_use_ivar = True

source_suffix = [".rst", ".md"]
master_doc = "index"

language = "en"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "default"

# -- Options for HTML output -------------------------------------------------

html_theme = "furo"
html_title = "Developers Resources"
html_theme_options = {
"light_logo": "ccpbiosim-dark-sq.png",  # Your light mode logo file
"dark_logo": "ccpbiosim-light-sq.png",   # Your dark mode logo file
}

html_static_path = ["_static"]

# Output file base name for HTML help builder.
htmlhelp_basename = "ccpbiosim_doc"

# -- Options for LaTeX output ------------------------------------------------
latex_elements = {}
latex_documents = [
    (
        master_doc,
        "ccpbiosim.tex",
        "CCPBioSim Developers Documentation",
        "CCPBioSim",
        "manual",
    ),
]

# -- Options for manual page output ------------------------------------------
man_pages = [(master_doc, "CCPBioSim", "CCPBioSim Developers Documentation", [author], 1)]

# -- Options for Texinfo output ----------------------------------------------
texinfo_documents = [
    (
        master_doc,
        "CCPBioSim",
        "CCPBioSim Developers Documentation",
        author,
        "CCPBioSim",
        "CCPBioSim developer pages for its GitHub organisation.",
    ),
]

# -- Extension configuration -------------------------------------------------
def setup(app):
    app.add_css_file("custom.css")
