"""
Import render, redirect and reverse too handle url requests.
Import messages to handle displaying success and error messages.
Import Customer order form skeleton to apply to pass through to the template.
"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def purchase(request):
    """ request basket contents and redirect if none or show order form """
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There appears to be no items in your basket.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'purchase/purchase.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
