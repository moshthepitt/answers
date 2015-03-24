"""
Django settings for template project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mgu70)6s2vl#66ymf-iz=i8z05q==adv@6^*6^$8@p$bp8v04c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'suit',
    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.humanize',
    # custom
    'core',
    'users',
    # third party
    'allauth',
    'allauth.account',
    # 'allauth.socialaccount',
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.twitter',
    'crispy_forms',
    'debug_toolbar',
    'pagination',
    'compressor',
    'cacheops',
    'suit_redactor',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    # third party
    'pagination.middleware.PaginationMiddleware'
)


ROOT_URLCONF = 'template.urls'
WSGI_APPLICATION = 'template.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Templates
TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, 'templates'),
]

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',

    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",

    "core.context_processors.site_processor",
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend"
)

# auth and allauth settings
LOGIN_REDIRECT_URL = '/'
SOCIALACCOUNT_QUERY_EMAIL = True
EMAIL_CONFIRMATION_DAYS = 14
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'SCOPE': ['email', 'publish_stream'],
        'METHOD': 'js_sdk'  # instead of 'oauth2'
    }
}

# crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Pagination
PAGINATION_DEFAULT_PAGINATION = 20

# COMPRESSOR
COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter',
                        'compressor.filters.cssmin.CSSMinFilter']

# CACHE OPS
CACHEOPS_REDIS = {
    'host': 'localhost',  # redis-server is on same machine
    'port': 6379,        # default redis port
    'db': 2,             # SELECT non-default redis database
                         # using separate redis db or redis instance
                         # is highly recommended
    'socket_timeout': 3,
}
CACHEOPS_DEGRADE_ON_FAILURE = True
CACHEOPS = {
    # automatically cache everything
    '*.*': ('all', 60 * 10),
}

try:
    from local_settings import *
except ImportError, e:
    pass
