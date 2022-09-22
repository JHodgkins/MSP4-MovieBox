""" import apps configuration setttings """
from django.apps import AppConfig


class PurchaseConfig(AppConfig):
    """ App configuration, ma,es the app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'purchase'

    def ready(self):
        """
        import signals into app so when a signal is recieved,
        post_save and post_delete can execute.
        """
        import purchase.signals
