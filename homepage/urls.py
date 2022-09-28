"""
Path: Handle routes to views
views: Handle the view of the template
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='homepage'),
    path('test/', views.all_products, name='products'),
]
