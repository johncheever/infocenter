# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Roadrunner Email Help Center'
author = 'Support Team'
release = '1.0'
copyright = '2025'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode'
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']
html_theme = 'alabaster'  # or whatever theme you're using

templates_path = ['_templates']  # already usually present

html_context = {
    'meta_tag': '<meta name="msvalidate.01" content="FF8C76044EE58DBA322585596FD8260D" />'
}
