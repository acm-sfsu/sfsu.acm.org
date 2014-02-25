#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tom Spalding'
SITENAME = u'ACM at SFSU'
SITEURL = 'http://acm-sfsu.github.io'
GITHUB = 'https://github.com/acm-sfsu'
GITHUB_SITE = 'https://github.com/acm-sfsu/acm-sfsu.github.io'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# http://docs.getpelican.com/en/3.1.1/settings.html#feed-settings
FEED_ALL_ATOM = 'feeds/all.atom.xml'
#CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('ACM-SFSU Github', 'https://github.com/acm-sfsu'),
          ('ACM International', 'http://acm.org'),
          ('Computer Science Department', 'http://cs.sfsu.edu'),)

# Social widget
SOCIAL = (('github', 'https://github.com/acm-sfsu'),
          ('IRC','http://webchat.freenode.net/?channels=acm-sfsu'),
          ('twitter', 'http://twitter.com/acmsfsu'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PATH = 'content'
THEME = "themes/pelican-cait"

# static paths will be copied under the same name
IMG_PATH = 'images'
STATIC_PATHS = [IMG_PATH, ]

# to disable, comment out
FAVICON = IMG_PATH+'/icons/favicon.ico'
