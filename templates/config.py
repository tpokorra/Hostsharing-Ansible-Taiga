import os

from .common import *   # noqa, pylint: disable=unused-wildcard-import

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '{{pac}}_{{user}}',
        'USER': '{{pac}}_{{user}}',
        'PASSWORD': '{{password}}',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

SECRET_KEY = "{{secretkey}}"
TAIGA_URL = "https://{{domain}}"
SITES = {
    "api": {"domain": "{{domain}}", "scheme": "https", "name": "api"},
    "front": {"domain": "{{domain}}", "scheme": "https", "name": "front"}
}

DEFAULT_PROJECT_SLUG_PREFIX = False

MEDIA_ROOT = '/home/pacs/{{pac}}/users/{{user}}/data/media'
MEDIA_URL = f"{ TAIGA_URL }/media/"
DEFAULT_FILE_STORAGE = "taiga_contrib_protected.storage.ProtectedFileSystemStorage"
THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE

STATIC_ROOT = '/home/pacs/{{pac}}/users/{{user}}/data/static'
STATIC_URL = f"{ TAIGA_URL }/static/"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
CHANGE_NOTIFICATIONS_MIN_INTERVAL = 120  # seconds

DEFAULT_FROM_EMAIL = 'noreply@{{domain}}'
EMAIL_USE_TLS = True
EMAIL_HOST = 'localhost'
EMAIL_PORT = 4587
EMAIL_HOST_USER = '{{pac}}-{{user}}'
EMAIL_HOST_PASSWORD = '{{password}}'

CELERY_ENABLED = False

from kombu import Queue  # noqa

ENABLE_TELEMETRY = False
PUBLIC_REGISTER_ENABLED = True
USER_EMAIL_ALLOWED_DOMAINS = "{{allowedDomains}}"