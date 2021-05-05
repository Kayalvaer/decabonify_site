from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def reload_on_save(sender, instance, created, **kwargs):
    """
    Updates total amount on each addition of an 
    item to the order
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def reload_on_delete(sender, instance, **kwargs):
    """
    Updates total amount on each deletion 
    from the order
    """
    print('delete signal activated!') 
    instance.order.update_total()