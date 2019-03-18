from .base import *

DEBUG = True

ALLOWED_HOSTS = []

WSGI_APPLICATION = 'config.wsgi.dev.application'

INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# debug toolbar setting
INTERNAL_IPS = ('127.0.0.1',)

# celery setting
CELERY_BROKER_URL = 'redis://localhost:6379/0'
# CELERY_TASK_SERIALIZER = "json"
# CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
