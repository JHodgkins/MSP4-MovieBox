"""
Import render to pass template files to be rendered
to the frontend.
Immport get object or 404 to handle requests that return null.
Import user profile model so userr data can be accessed.
"""
from django.shortcuts import render, get_object_or_404
from .models import UserProfile


def profile(request):
    """
    View to display registered user profile to the frontend.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    template = 'profiles/user_profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)
