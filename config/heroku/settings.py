from config.common.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

ROOT_URLCONF = 'config.heroku.urls'
