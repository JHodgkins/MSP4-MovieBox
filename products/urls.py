""" import path and views to route address to frontend """
from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name='products')
]
