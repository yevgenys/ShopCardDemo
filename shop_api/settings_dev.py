import os

from .settings import *

SECRET_KEY = 'dev_secret'
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
DEBUG = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'shop_api',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': DB_HOST,
        'PORT': '5432'
    }
}

INSTALLED_APPS.append('django.contrib.staticfiles')
INSTALLED_APPS.append('drf_yasg')

# Swagger setup
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
TEMPLATES.append(
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
)
