"""
Django settings for healtharoundme project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.gis',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'boundaryservice',
    'corsheaders',
    'django_extensions',
    'mptt',
    'rest_framework',
    'south',
    'django_nose',  # Must come after south
    'tastypie',

    # Our apps
    'data',
    'healthdata',
)

TEMPLATE_LOADERS = (
    'jingo.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
JINGO_INCLUDE_PATTERN = r'\.jinja2'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'healtharoundme.urls'

WSGI_APPLICATION = 'healtharoundme.wsgi.application'

default_db_name = 'healtharoundme.sqlite'
default_db_path = os.path.join(BASE_DIR, default_db_name)
DATABASES = {
    'default': dj_database_url.config(
        default='spatialite:///' + default_db_path)
}
POSTGIS_VERSION = (2, 1)

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static') + '/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'south': {
            'level': 'INFO',
        }
    },

}

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.JSONPRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = r'^/api/.*$'

if 'test' not in sys.argv:
    try:
        from settings_override import *  # noqa
    except ImportError, ep:
        pass
    else:
        try:
            INSTALLED_APPS += LOCAL_INSTALLED_APPS
        except NameError:
            pass
        try:
            MIDDLEWARE_CLASSES += LOCAL_MIDDLEWARE_CLASSES
        except NameError:
            pass
else:
    SECRET_KEY = 'test_secret_key'
