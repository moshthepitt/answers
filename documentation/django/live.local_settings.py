import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'SECRET KEY GOES HERE'

# SITES
SITE_ID = 1

ADMINS = (
    ('John Doe', 'johndoe@example.com'),
)

MANAGERS = (
    ('John Doe', 'johndoe@example.com')
)

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'DATABASE_NAME',
        'USER': 'DATABASE_USER',
        'PASSWORD': 'PASSWORD',
        'HOST': 'localhost',
        'PORT': '',                      # Set to empty string for default.
    }
}

# CACHE
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': '/var/tmp/django_cache',
#     }
# }

# CACHES = {
#    "default": {
#        "BACKEND": "redis_cache.cache.RedisCache",
#        "LOCATION": "127.0.0.1:6379:1",
#        "OPTIONS": {
#            "CLIENT_CLASS": "redis_cache.client.DefaultClient",
#        }
#    }
# }

# SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# SESSION_CACHE_ALIAS = "default"

# Media
MEDIA_ROOT = "/var/www/media/"
MEDIA_URL = 'http://example.com/media/'

# static
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = 'http://example.com/static/'
STATIC_ROOT = '/var/www/static/'
# COMPRESS_ROOT = ""

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# haystack
# HAYSTACK_CONNECTIONS = {
#     'default': {
#         'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
#         'URL': 'http://127.0.0.1:9200/',
#         'INDEX_NAME': 'haystack',
#     },
# }

# Test Email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'John Doe <johndoe@example.com>'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['example.com', 'www.example.com']
CRISPY_FAIL_SILENTLY = not DEBUG
