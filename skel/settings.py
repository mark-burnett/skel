import dj_database_url
import importlib
import os


SKEL_APP_MODULE = os.environ['SKEL_APP_MODULE']


# Security settings
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False
LOG_LEVEL = 'INFO'
if os.environ.get('DEBUG'):
    DEBUG = True
    TEMPLATE_DEBUG = True
    LOG_LEVEL = 'DEBUG'

ALLOWED_HOSTS = ['*']

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Application definition
INSTALLED_APPS = [
    'django.contrib.staticfiles',

    'rest_framework',
    'django_extensions',
    'django_filters',

    SKEL_APP_MODULE,
]
if 'TEST' in os.environ:
    INSTALLED_APPS.append('django_nose')
    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'skel.urls'

WSGI_APPLICATION = 'skel.wsgi.application'

APPEND_SLASH = False


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite')
}
CONN_MAX_AGE = None


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = 'static'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# Logging configuration
LOGGING = {
    'version': 1,
    'loggers': {
        '': {
            'level': LOG_LEVEL,
        },
    },
}


# DRF Configuration
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny',),
    'PAGINATE_BY': 10,
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),

    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}


try:
    globals().update(importlib.import_module(
        '%s.settings' % SKEL_APP_MODULE).__dict__)
except ImportError:
    pass
