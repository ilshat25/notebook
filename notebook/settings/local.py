from .base import *

# Режим отладки
DEBUG = True

# Допустимые хосты
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Настройки БД (postgresql)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': os.environ['DATABASE_HOST'],
        'PORT': os.environ['DATABASE_PORT'],
    }
}

# Расположение статичных файлов
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static/'

# Расположение меди файлов
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'
