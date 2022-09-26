"""
Import render to pass template files to be rendered
to the frontend.
"""
from django.shortcuts import render


def profile(request):
    """
    View to display registered user profile to the frontend.
    """
    template = 'profiles/user_profile.html'
    context = {}

    return render(request, template, context)
