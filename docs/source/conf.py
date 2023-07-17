# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "Namino boards library"
copyright = "2023, Namino Team"
author = "Namino Team"


needs_sphinx = '1.3'
extensions = []
source_suffix = ['.rst']

project = u'Namino_Library'
copyright = u'2023, Namino Team'
author = u'Namino Team'

master_doc = 'index'

version = u'1.0.18'
release = u'1.0.18'

language = 'en'
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
highlight_language = 'c++'
todo_include_todos = False

linkcheck_timeout = 60
linkcheck_ignore = [r'https://github.com/.+/.+/(compare|commits)/.+']

import subprocess
subprocess.call('make clean', shell=True)
subprocess.call('cd ../../doxygen ; doxygen', shell=True)
html_extra_path = ['../../doxygen/build/html']
