""" render for rendering templates to frontend  """
from django.shortcuts import render


# Renders basket template.
def view_basket(request):
    """ A view to return the basket view """
    return render(request, 'basket/basket.html')
