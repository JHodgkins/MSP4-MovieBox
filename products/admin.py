""" Inport models to register them to admin area  """
from django.contrib import admin
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    """ Amend the display of product items within the admin dashboard """
    list_display = (
        'sku',
        'name',
        'category',
        'certificate',
        'no_discs',
        'price',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """ Amend the display of category items within the admin dashboard """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
