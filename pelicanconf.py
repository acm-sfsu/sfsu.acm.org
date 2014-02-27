#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tom Spalding'
SITENAME = u'ACM at SFSU'
SITEURL = 'http://acm-sfsu.github.io'
GITHUB_USERNAME = 'acm-sfsu'
GITHUB = 'https://github.com/'+GITHUB_USERNAME
GITHUB_SITE = 'https://github.com/'+GITHUB_USERNAME+'/'+GITHUB_USERNAME+'.github.io'
CONTACT_EMAIL = 'acm.sfsu@gmail.com'
AUTHOR_EMAIL = CONTACT_EMAIL # default gravatar email

# Github Activity Plugin
GITHUB_ACTIVITY_FEED = 'https://github.com/'+GITHUB_USERNAME+'.atom'
GITHUB_ACTIVITY_MAX_ENTRIES = 10

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# http://docs.getpelican.com/en/3.1.1/settings.html#feed-settings
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
#CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('ACM-SFSU Github', 'https://github.com/acm-sfsu'),
          ('ACM International', 'http://acm.org'),
          ('Computer Science Department', 'http://cs.sfsu.edu'),)

# Social widget
SOCIAL = (('github', 'https://github.com/acm-sfsu'),
          ('comment','http://webchat.freenode.net/?channels=acm-sfsu'),
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

PLUGIN_PATH = 'plugins'
PLUGINS = ['gravatar', 'gallery', 'github_activity', 'share_post']