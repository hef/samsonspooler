from config.common.settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

ROOT_URLCONF = 'config.herouk.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'config.heroku.wsgi.application'
