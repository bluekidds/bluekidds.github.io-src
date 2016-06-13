#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Fu-Chun Hsu'
SITENAME = u'DÉCARE'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# STATIC_OUT_DIR requires pelican 3.3+.
STATIC_PATHS = ['images', 'figures', 'downloads', 'favicon.png']
CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

THEME = '../pelican-octopress-theme'

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal']


# Blogroll
LINKS = (('Fongfu', 'http://fongfu.com.tw/'),
         ('Python.org', 'http://python.org/'),
         )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
