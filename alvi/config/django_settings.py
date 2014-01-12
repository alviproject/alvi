import os
import alvi

PROJECT_BASE_DIR = os.path.dirname(alvi.__file__)
BASE_DIR = os.path.dirname(PROJECT_BASE_DIR)

#TODO add warning about secret key and debug
SECRET_KEY = 'hn+-d5ox)bdr)a6+yn6+m3wazw0n2=6mi#cc839sb@=rs9=2%y'

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['localhost']


INSTALLED_APPS = (
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.debug",
    "django.core.context_processors.static",
    "alvi.context_processor",
)

ROOT_URLCONF = 'alvi.urls'

WSGI_APPLICATION = 'alvi.wsgi.application'


STATIC_URL = '/static/'
#STATICFILES_DIRS = (os.path.join(PROJECT_BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(PROJECT_BASE_DIR, '../static')

TEMPLATE_DIRS = (os.path.join(PROJECT_BASE_DIR, 'templates'),)