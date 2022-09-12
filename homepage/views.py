""" render for rendering templates to frontend  """
from django.shortcuts import render


# Renders homepage template.
def index(request):
    """ A view to return the home page """
    return render(request, 'homepage/index.html')
