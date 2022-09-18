"""
import render to render page and get object or 404 to handle if no item
found when requested.
import redirect and reverse to hanfle redirections of pages and rverse to
handle unidirectional urls.
import Products so the products can be viewed on the froneend.
Import Q to handle wueries to locate search terms within page model areas.
import Lower to enable strings to be set to lowercase.
"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category


def all_products(request):
    """ Return all products including sorting and search results """
    products = Product.objects.all()

    categories = None
    search = None
    sort = None
    direction = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'search' in request.GET:
            search = request.GET['search']
            if not search:
                messages.error(request, "You did not enter a search criteria")
                return redirect(reverse('products'))

            queries = Q(name__icontains=search) | Q(
                description__icontains=search) | Q(
                    actors__icontains=search) | Q(
                        directed_by__icontains=search)
            products = products.filter(queries)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            
            if sortkey == 'category':
                sortkey = 'category__name'
            
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': search,
        'active_categories': categories,
        'current_sorting': current_sorting,
    }
    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ Return a single product using its id """
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)
