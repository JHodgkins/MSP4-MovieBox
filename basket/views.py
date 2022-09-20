"""
import redirect so a url can be saved and a user can be redirected to this url.
Import reverse to handle when rturning to a url..
import render for rendering templates to frontend.
import HttpResponse to handle errors returned through JavaScript.
"""
from django.shortcuts import redirect, reverse, render, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product

# Renders basket template.
def view_basket(request):
    """ A view to return the basket view """
    return render(request, 'basket/basket.html')


def add_to_the_basket(request, item_id):
    """ Add an item to the basket """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['basket'] = basket

    return redirect(redirect_url)


def update_basket(request, item_id):
    """ Updates the quantity of an item in the basket """

    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop(item_id)

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_the_basket(request, item_id):
    """ Removes an item in the basket """
    try:
        if 'remove' in request.POST:
        
            basket = request.session.get('basket', {})
            basket.pop(item_id)

            request.session['basket'] = basket
            return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
