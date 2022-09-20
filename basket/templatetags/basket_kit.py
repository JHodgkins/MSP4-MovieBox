""" import template so item can be used in any template page """
from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ returns the price of a movie times the quantity to
    give a sutotal """
    return price * quantity
