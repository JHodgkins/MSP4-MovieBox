"""
import render to render page and get object or 404 to handle if no item
found when requested.
import redirect and reverse to hanfle redirections of pages and rverse to
handle unidirectional urls.
Import login required to secure pages from unregisted and non admin users.
Import messages to handle alerts and actions given to users.
Import Q to handle wueries to locate search terms within page model areas.
import Lower to enable strings to be set to lowercase.
import Products so the products can be viewed on the froneend.
Import ptoductform to have access to database items for adding new movie
products.
"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """
    Return all products including sorting and search results
    """
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

# MovieBox admin area section


@login_required
def add_movie(request):
    """
    Add a movie product to the database and then direct admin to newly \
        added movie title.
    """
    # restrict view to non authorised users.
    if not request.user.is_superuser:
        messages.error(request, 'The page you requested is not available.')
        return redirect(reverse('homepage'))
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'New movie added to database, \
                this product is now live on MovieBox for customers to view.')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'There was an error, please \
                ensure all fields marked with an * have been filled out.')
    else:
        form = ProductForm()
    template = 'products/add_movie.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_movie(request, product_id):
    """
    Amend details about a movie product product on MovieBox
    """
    # restrict view to non authorised users.
    if not request.user.is_superuser:
        messages.error(request, 'The page you requested is not available.')
        return redirect(reverse('homepage'))
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Movie: {product.name} was sucessfully amended, \
                    the changess will be live on MovieBox immediately.')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(
                request, 'There was an issue with commiting these changes, \
                    ensre all required fields are filled out correctly.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are currently editing movie: \
             {product.name}')

    template = 'products/edit_movie.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)


@login_required
def delete_movie(request, product_id):
    """
    Delete a selected movie product from the frontend using its id
    """
    # restrict view to non authorised users.
    if not request.user.is_superuser:
        messages.error(request, 'The page you requested is not available.')
        return redirect(reverse('homepage'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'Movie {product.name} has been removed from \
        the MovieBox store front, if you need to re-add this product \
            please use a diffrent SKU number.')
    return redirect(reverse('products'))
