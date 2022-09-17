"""
import render to render page and get object or 404 to handle if no item
found when requested.
import Products so the products can be viewed on the froneend
"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Category


def all_products(request):
    """ Return all products including sorting and search results """
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ Return a single product using its id """
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)
