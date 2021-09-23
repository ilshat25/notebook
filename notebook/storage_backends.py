from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

# Настройки хранения статичных файлов
class StaticStorage(S3Boto3Storage):
    location = 'static'
    default_acl = 'public-read'

# Настройки хранения медиа файлов
class PublicMediaStorage(S3Boto3Storage):
    location = 'media'
    default_acl = 'public-read'
    file_overwrite = False
