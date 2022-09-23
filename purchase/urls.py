"""
Path: Handle routes to views
views: Handle the view of the template
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.purchase, name='purchase'),
    path('purchase_complete/<order_number>', views.purchase_complete, name='purchase_complete'),
]
