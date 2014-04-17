DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SECRET_KEY = ''  # Get this from another developer

LOCAL_INSTALLED_APPS = ()
LOCAL_MIDDLEWARE_CLASSES = ()

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
