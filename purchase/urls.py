"""
Path: Handle routes to views
views: Handle the view of the template
Imort webhook to handle webhooks from Stripe for the payment processing.
"""
from django.urls import path
from . import views
from .webhook import webhook


urlpatterns = [
    path('', views.purchase, name='purchase'),
    path('purchase_complete/<order_number>', views.purchase_complete, name='purchase_complete'),
    path('wh/', webhook, name='webhook'),
]
