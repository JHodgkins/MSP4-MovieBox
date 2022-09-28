""" render for rendering templates to frontend  """
from django.shortcuts import render
from products.models import Product


# Renders homepage template.
def index(request):
    """ A view to return the home page """
    return render(request, 'homepage/index.html')


def all_products(request):
    """ Return all products including sorting and search results """
    products = Product.objects.all()
    template = 'homepage/test.html'
    context = {
        'products': products,
    }
    return render(request, template, context)
