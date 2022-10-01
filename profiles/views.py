"""
Import render to pass template files to be rendered
to the frontend.
Immport get object or 404 to handle requests that return null.
Import messages to show error messages to users.
Import user profile model so userr data can be accessed.
Import profile form to access profile data.
"""
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from purchase.models import Order
from .models import UserProfile
from .forms import ProfileForm

def profile(request):
    """
    View to display registered user profile to the frontend.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile information \
                was successfully updated')
        else:
            messages.error(request, 'Unfortunately the update \
                faile, Please ensure all required fields are \
                    filled out correctly.')
    else:
        form = ProfileForm(instance=profile)
    orders = profile.orders.all()
    template = 'profiles/user_profile.html'
    context = {
        'profile': profile,
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)

def order_history(request, order_number):
    """
    Retrieve past purchases and return to template, used
    within the profile section for a customer to view
    previous purchases.
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'You are viewing a previous confirmed order, {order_number}.'
    ))

    template = 'purchase/purchase_complete.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
