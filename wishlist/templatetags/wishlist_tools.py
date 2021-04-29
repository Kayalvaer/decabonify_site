# From Code Institute Project Boutique Ado - django custom template text and filters
from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity