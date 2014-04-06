DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SECRET_KEY = ''  # Get this from another developer

LOCAL_INSTALLED_APPS = ('django_extensions', 'django_nose')
LOCAL_MIDDLEWARE_CLASSES = ()
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'healthgeist',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
