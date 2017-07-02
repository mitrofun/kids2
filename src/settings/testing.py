# -*- coding: utf-8 -*-

from .base import *  # noqa

DEBUG = False

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
    }
}

RQ_QUEUES = {
    'default': {
        'HOST': 'redis',
        'PORT': '6379',
        'DB': 0,
        'DEFAULT_TIMEOUT': 600,
    }
}
