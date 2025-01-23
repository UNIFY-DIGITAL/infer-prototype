# Configuration file for the Sphinx documentation builder.
project = 'Kotaemon Documentation'
copyright = '2025, Unify'
author = 'Unify'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',       # Extract docstrings from code
    'sphinx.ext.autosummary',   # Create summaries of functions/classes
    'sphinx.ext.napoleon',      # Support Google/NumPy style docstrings
    'sphinx.ext.viewcode',      # Add links to source code
    'sphinx.ext.intersphinx',   # Cross-reference with external docs
]
templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
autosummary_generate = True
show_authors = True


# Mock all possible dependencies
autodoc_mock_imports = [
    'elasticsearch',
    'elastic_transport',
    'chromadb',
    'nltk',
    'llama_index',
    'posthog',
    'theflow',
    'ktem',
    'gradio',
    'pydantic',
    'kotaemon'
]

html_theme_options = {
    'collapse_navigation': False,  # Keep navigation expanded
    'sticky_navigation': True,    # Stick the navigation bar
    'navigation_depth': 8,        # Depth of the sidebar
    'titles_only': False          # Display both titles and section contents
}

import os
import sys

# Add the root and subdirectories to the Python path
sys.path.insert(0, os.path.abspath('../../'))
sys.path.insert(0, os.path.abspath('../../libs'))
sys.path.insert(0, os.path.abspath('../../libs/kotaemon'))
sys.path.insert(0, os.path.abspath('../../libs/kotaemon/kotaemon'))
sys.path.insert(0, os.path.abspath('../../libs/ktem'))
sys.path.insert(0, os.path.abspath('../../libs/ktem/ktem'))


autodoc_typehints = "description"
warning_is_error = False
nitpick_ignore = []
