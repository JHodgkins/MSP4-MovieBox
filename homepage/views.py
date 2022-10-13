"""
Import render for rendering templates to frontend
Import Product to display movie on the homepage
"""
from django.shortcuts import render
from products.models import Product


def all_products(request):
    """ Return all products including sorting and search results """
    products = Product.objects.all()
    template = 'homepage/index.html'
    context = {
        'products': products,
    }
    return render(request, template, context)
