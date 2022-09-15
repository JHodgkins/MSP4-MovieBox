""" import Products so the products can be viewed on the froneend """
from django.shortcuts import render
from .models import Product, Category

def all_products(request):
    """ Return all products including sorting and search results """
    products = Product.objects.all()
    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
