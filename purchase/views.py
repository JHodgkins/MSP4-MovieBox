"""
Import render, redirect and reverse too handle url requests.
Import require post to handle post requests sent through the fromt end.
Import messages to handle displaying success and error messages.
Import settings for env variables.
Import Customer order form skeleton to apply to pass through to the template.
Import order and orderline models to pass order through to the admin section.
Import product model to have access to product details.
Import basket contents to process through Stripe payment gateway.
Import Stripe to process intents.
Importjson to handle json data dumps.
"""
import json
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
import stripe
from products.models import Product
from profiles.forms import ProfileForm
from profiles.models import UserProfile
from basket.contexts import basket_contents
from .forms import OrderForm
from .models import Order, OrderLineItem

@require_POST
def cache_purchase_data(request):
    """
    Cache the response of the checkbox of user data
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed Stripe has stopped responding. Please try again in a few minutes.')
        return HttpResponse(content=e, status=400)


def purchase(request):
    """ request basket contents and redirect if none or show order form """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        basket = request.session.get('basket', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_basket = json.dumps(basket)
            order.save()

            for item_id, item_data in basket.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()

                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your basket cannot be found in our records. ")
                    )
                    order.delete()
                    return redirect(reverse('view_basket'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('purchase_complete', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, "There appears to be no items in your basket.")
            return redirect(reverse('products'))

        current_basket = basket_contents(request)
        total = current_basket['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'town_or_city': profile.default_town_or_city,
                    'county': profile.default_county,
                    'postcode': profile.default_postcode,
                    'country': profile.default_country,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()
        
    template = 'purchase/purchase.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def purchase_complete(request, order_number):
    """
    Processes the order when a completed purchase has been made
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Profile. of current user is associated with the order placed.
        order.profile = profile
        order.save()

        # Profile information is gathered and saved
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = ProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Thank You, Your purchase was successfully completed. \
        Your purchase order number is {order_number}. A confirmation email containing \
        this information will be sent shortly to your email address. {order.email} \
            Many thanks, MovieBox Team')
    
    if 'basket' in request.session:
        del request.session['basket']

    template = 'purchase/purchase_complete.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
