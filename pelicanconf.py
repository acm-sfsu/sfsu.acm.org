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
DISQUS_SITENAME = 'acm-sfsu'
GOOGLE_ANALYTICS = 'UA-48204918-1'

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
SOCIAL = (('envelope-alt','mailto:'+CONTACT_EMAIL),
          ('github', 'https://github.com/acm-sfsu'),
          ('comment','http://webchat.freenode.net/?channels=acm-sfsu'),
          ('twitter', 'http://twitter.com/acmsfsu'),)

# Social
#CONTACTS = ((,),)

#CUSTOM_MENUITEMS = ((,),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PATH = 'content'
OUTPUT_PATH = 'output'
THEME = "themes/pelican-cait"

# static paths will be copied under the same name
IMG_PATH = 'images'
GALLERY_PATH = IMG_PATH+'/gallery'
STATIC_PATHS = [IMG_PATH, ]

# to disable, comment out
FAVICON = IMG_PATH+'/icons/favicon.ico' 
#moved icon to main path until solve thumbnailer icon exception

PLUGIN_PATH = 'plugins'
PLUGINS = ['gravatar', 'gallery', 'github_activity', 'share_post', 'thumbnailer']

# THUMBNAIL_DIR is the path to the output sub directory where the thumbnails are generated
THUMBNAIL_DIR = GALLERY_PATH+'/thumbnails'
# THUMBNAIL_SIZES is a dictionary mapping name of size to size specifications.
# The generated filename will be originalname_thumbnailname.ext unless THUMBNAIL_KEEP_NAME is set.
THUMBNAIL_SIZES = {
#    'thumbnail_square': '200',
    'thumbnail_wide': '200x?',
#    'thumbnail_tall': '?x200',
}
# THUMBNAIL_KEEP_NAME is a boolean which if set puts the file with the original name in a thumbnailname folder.
THUMBNAIL_KEEP_NAME = True
# Assuming THUMBNAIL_KEEP_NAME is true, then set def thumb sizefolder. This is a path that has same name as in the thumbnail size dictionary..
DEF_THUMB_SIZE_PATH = 'thumbnail_wide'