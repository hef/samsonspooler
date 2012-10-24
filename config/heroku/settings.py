from config.common.settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

ROOT_URLCONF = 'config.herouk.urls'
