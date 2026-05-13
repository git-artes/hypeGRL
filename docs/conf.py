# Sphinx configuration for hyperbolic-grl documentation
import os, sys
sys.path.insert(0, os.path.abspath(".."))

project = "hyperbolic-grl"
copyright = "2026, Federico Larroca, Paola Bermolen, Marcelo Fiori, Sofia Perez Casulo"
author = "Federico Larroca, Paola Bermolen, Marcelo Fiori, Sofia Perez Casulo"
release = "0.1.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",       # NumPy / Google style docstrings
    "sphinx.ext.viewcode",       # links to source
    "sphinx.ext.intersphinx",    # cross-links to torch, networkx docs
    "sphinx_autodoc_typehints",
    "nbsphinx",                  # render tutorial notebooks
    "myst_parser",               # Markdown support
]

autodoc_default_options = {
    "members": True,
    "undoc-members": False,
    "show-inheritance": True,
}

napoleon_numpy_docstring = True
napoleon_google_docstring = False

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "networkx": ("https://networkx.org/documentation/stable", None),
    "torch": ("https://pytorch.org/docs/stable", None),
}

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

exclude_patterns = ["_build", "**.ipynb_checkpoints"]
nbsphinx_execute = "never"   # don't re-run notebooks on build
