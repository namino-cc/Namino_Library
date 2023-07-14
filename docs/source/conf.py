# -*- coding: utf-8 -*-

import os

needs_sphinx = '1.3'
extensions = []
source_suffix = ['.rst']

project = u'namino_Library'
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

