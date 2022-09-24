"""
post_save and post_delete to save and delete when recieving a signal.
Import recieiver so that data can be rieved from the admin dashboard.
Import model LineItemOrder so fields can be interacted with.
"""
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update the line item order total when saved.
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Updates the line item when an item is deleted using the admin dashoard.
    """
    instance.order.update_total()
