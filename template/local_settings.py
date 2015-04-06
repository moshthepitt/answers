import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# sites
SITE_ID = 1

# change the secret key
SECRET_KEY = 'hwokhV3;N5"E\=vV(t&_D@Yxn>CwPpuB=P\Qt8xF#j@E6)Q3:4.:@$+ox[Z!lQR'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Emails
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
DEFAULT_FROM_EMAIL = 'Hello World <hello@example.com>'


# static
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
STATIC_ROOT = '/static/'
STATIC_URL = '/static/'

# media
MEDIA_ROOT = '/media/'
MEDIA_URL = '/media/'

# CACHE
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# HAYSTACK
# HAYSTACK_CONNECTIONS = {
#     'default': {
#         'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
#         'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
#         'STORAGE': 'file',
#         'POST_LIMIT': 128 * 1024 * 1024,
#         'INCLUDE_SPELLING': True,
#         'BATCH_SIZE': 1000,
#     },
# }

# DEBUG
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CRISPY_FAIL_SILENTLY = not DEBUG

ALLOWED_HOSTS = []
