"""
Path: Handle routes to views
views: Handle the view of the template
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_basket, name='view_basket'),
    path('add/<item_id>/', views.add_to_the_basket, name='add_to_the_basket'),
    path('update/<item_id>/', views.update_basket, name='update_basket'),
]
