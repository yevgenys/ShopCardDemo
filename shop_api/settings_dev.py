from .settings import *

SECRET_KEY = 'dev_secret'
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
DEBUG = True

INSTALLED_APPS.append(
    'django.contrib.staticfiles',  # required for serving swagger ui's css/js files
)
INSTALLED_APPS.append(
    'drf_yasg',
)
