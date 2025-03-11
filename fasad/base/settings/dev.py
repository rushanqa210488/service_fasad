from .base import *

SECRET_KEY='django-insecure-&rxgk9d@s0&^q%(^pnethuz4=hj=^8jx_)ga34=@#m_y47=5au'

DEBUG = True


ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



