"""
Import render, redirect and reverse too handle url requests.
Import messages to handle displaying success and error messages.
Import settings for env variables.
Import Customer order form skeleton to apply to pass through to the template.
Import basket contents to process through Stripe payment gateway.
Import Stripe to process intents.
"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from basket.contexts import basket_contents
import stripe


def purchase(request):
    """ request basket contents and redirect if none or show order form """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There appears to be no items in your basket.")
        return redirect(reverse('products'))


    current_bag = basket_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()
    template = 'purchase/purchase.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
