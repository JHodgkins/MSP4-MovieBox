"""
Path: Handle routes to views
views: Handle the view of the template
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_basket, name='view_basket'),
]
