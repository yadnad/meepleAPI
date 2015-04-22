# -*- coding: utf-8 -*-
"""
Django settings for Meeple project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os
from os.path import join, dirname

BASE_DIR = dirname(dirname(__file__))


DEBUG = bool(os.environ.get('DJANGO_DEBUG', False))
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['127.0.0.1', '10.0.2.2', 'localhost', 'api.meeple.co']
if os.environ.get('ALLOWED_HOSTS'):
    ALLOWED_HOSTS += os.environ.get('ALLOWED_HOSTS').split(',')

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

THIRD_PARTY_APPS = (
    'crispy_forms',
    'rest_framework',
    'rest_framework_swagger',
    'django_jinja',
    'raven.contrib.django.raven_compat',
    'markdown_deux',
)


LOCAL_APPS = (
    'apps.api',
    'apps.web',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

SECRET_KEY = os.environ.get('SECRET_KEY', 'CHANGEME')

FIXTURE_DIRS = (
    join(BASE_DIR, 'fixtures'),
)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


ADMINS = (
    ("""Miha Zelnik""", 'miha.zelnik@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DATABASE_NAME', 'postgres'),
        'USER': os.environ.get('DATABASE_USER', 'postgres'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'postgres'),
        'HOST': 'localhost',
        'PORT': '',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

TEMPLATE_DIRS = (
    join(BASE_DIR, 'templates'),
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATE_DIRS,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': TEMPLATE_CONTEXT_PROCESSORS,
        },

    },
    {
        "NAME": 'jinja2',
        "BACKEND": "django_jinja.backend.Jinja2",
        'DIRS': TEMPLATE_DIRS,
        "APP_DIRS": True,
        "OPTIONS": {
            'context_processors': TEMPLATE_CONTEXT_PROCESSORS,
            "match_extension": ".jinja",
            "auto_reload": TEMPLATE_DEBUG,
        }
    },
]

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

STATIC_ROOT = join(os.path.dirname(BASE_DIR), 'staticfiles')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    join(BASE_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIA_ROOT = join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

AUTOSLUG_SLUGIFY_FUNCTION = 'slugify.slugify'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'WARNING',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}

REST_FRAMEWORK = {
    "DEFAULT_RENDER_CLASSES": (
        'rest_framework.renderers.JSONRenderer',
    ),
    'PAGINATE_BY': 25,
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '25000/day',
    },
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_VERSION': 'v1'
}

BASE_API = os.environ.get('BASE_API', '')

SWAGGER_SETTINGS = {
    "exclude_namespaces": ["root"],
}

# Keen.io
KEEN_DEBUG = bool(os.environ.get('DJANGO_DEBUG', False))
KEEN_PROJECT_ID = os.environ.get('KEEN_PROJECT_ID', '')
KEEN_WRITE_KEY = os.environ.get('KEEN_WRITE_KEY', '')
KEEN_READ_KEY = os.environ.get('KEEN_READ_KEY', '')
KEEN_CELERY = False

RAVEN_CONFIG = {
    'dsn': os.environ.get('RAVEN_KEY', ''),
}

MARKDOWN_DEUX_STYLES = {
    "default": {
        "extras": {
            "code-friendly": None,
        },
        "safe_mode": False,
    },
}

if DEBUG:
    MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INSTALLED_APPS += ('debug_toolbar', 'django_extensions',)

    INTERNAL_IPS = ('127.0.0.1', '10.0.2.2', 'localhost')

    DEBUG_TOOLBAR_CONFIG = {
        'DISABLE_PANELS': [
            'debug_toolbar.panels.redirects.RedirectsPanel',
        ],
        'SHOW_TEMPLATE_CONTEXT': True,
    }

    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
