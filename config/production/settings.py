from config.common.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/srv/www/spooler.arbitrarion.com/db.sqlite3'
    }
}

STATIC_ROOT = '/srv/www/spooler.arbitrarion.com/static/'
MEDIA_ROOT = '/srv/www/spooler.arbitrarion.com/media/'

ROOT_URLCONF = 'config.production.urls'
