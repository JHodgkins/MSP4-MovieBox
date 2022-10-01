""" import path and views to route address to frontend """
from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_details, name='product_details'),
    path('edit_movie/<int:product_id>/', views.edit_movie, name='edit_movie'),
    path('delete_movie/<int:product_id>/', views.delete_movie, name='delete_movie'),
    path('add_movie/', views.add_movie, name='add_movie'),
]
