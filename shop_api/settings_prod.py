from .settings import *

SECRET_KEY = 'django-insecure-kxrde@8eqd2iw3#gsqur6(*7h0mo8s2tqpltna5sgipot-d(qp'

# Prod hosts, for instance -> api.shop.com
ALLOWED_HOSTS = [

]

DEBUG = False


# Production database, for now both prod/dev will be using sqlite from settings.py
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


