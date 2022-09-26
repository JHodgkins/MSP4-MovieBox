"""
Import path to handle routes.
Import views to recieve the view template to view.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile')
]
