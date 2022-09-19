""" 
import redirect so a url can be saved and a user can be redirected to this url.
import render for rendering templates to frontend
"""
from django.shortcuts import redirect, render


# Renders basket template.
def view_basket(request):
    """ A view to return the basket view """
    return render(request, 'basket/basket.html')


def add_to_the_basket(request, item_id):
    """ Add an item to the basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    
    return redirect(redirect_url)
    