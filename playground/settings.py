# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os


PROJECT_BASE_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(PROJECT_BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hn+-d5ox)bdr)a6+yn6+m3wazw0n2=6mi#cc839sb@=rs9=2%y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

HOST = 'localhost'
PORT = 8000

ALLOWED_HOSTS = [HOST]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "playground.context_processor",
)

ROOT_URLCONF = 'playground.urls'

WSGI_APPLICATION = 'playground.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'data', 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(PROJECT_BASE_DIR, 'static'),)
STATIC_ROOT = 'data/static'

#django debug toolbar setting
INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False, 'HIDE_DJANGO_SQL': True, 'SHOW_TEMPLATE_CONTEXT': True}

TEMPLATE_DIRS = (os.path.join(PROJECT_BASE_DIR, 'templates'),)


LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
            },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '%s/data/log.txt' % BASE_DIR,
            'formatter': 'simple'
            },
        },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
            },
        }
    }

#TODO change in production
# make all loggers use the console.
for logger in LOGGING['loggers']:
    LOGGING['loggers'][logger]['handlers'] = ['console']

default_scenes = (
    'playground.client.scenes.LinearSearch',
    'playground.client.scenes.BoobleSort',
    'playground.client.scenes.SelectionSort',
    'playground.client.scenes.InsertionSort',
    'playground.client.scenes.MergeSort',
    'playground.client.scenes.ShellSort',
    'playground.client.scenes.BinarySearch',
    'playground.client.scenes.CreateTree',
    'playground.client.scenes.BinarySearchTree',
    'playground.client.scenes.CreateGraph',
    'playground.client.scenes.TraverseGraph',
)

#define API urls to make sure that they are the same on client and server
#url reversing was not used to make sure that no code (except settings) will be reused between client and server
API_URL_SCENE_REGISTER = 'api/scene/register'
API_URL_SCENE_SYNC = 'api/scene/sync'