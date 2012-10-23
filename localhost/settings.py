from samsonspooler.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3'
    }
}

ROOT_URLCONF = 'localhost.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'localhost.wsgi.application'
