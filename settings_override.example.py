DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SECRET_KEY = ''  # Get this from another developer

LOCAL_INSTALLED_APPS = ()
LOCAL_MIDDLEWARE_CLASSES = ()

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'healtharoundme',
        'USER': 'healtharoundme',
        'PASSWORD': 'healtharoundme',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
POSTGIS_VERSION = ( 2, 1 )
