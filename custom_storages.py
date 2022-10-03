"""
Import settings to access site variables.
Import s3 boto storage to handle. collection of static files.
"""
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """ Set the default location to collect static files from css/hs """
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """ Set the media location to collect static files from. """
    location = settings.MEDIAFILES_LOCATION
