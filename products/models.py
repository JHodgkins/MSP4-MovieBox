""" import models for database tables  """
from django.db import models


class Category(models.Model):
    """ Define the db schema for the product categories """

    class Meta:
        """ Change name represented in the admin panel """
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """ return the name as a string  """
        return self.name

    def get_friendly_name(self):
        """ return the friendly name as a string  """
        return self.friendly_name


class Product(models.Model):
    """ Define the products database schema  """
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    actors = models.CharField(max_length=254, null=True, blank=True)
    directed_by = models.CharField(max_length=254, null=True, blank=True)
    certificate = models.CharField(max_length=5, null=True, blank=True)
    no_discs = models.CharField(max_length=50, null=True, blank=True)
    duration = models.CharField(max_length=50, null=True, blank=True)
    imdbrating = models.DecimalField(
        max_digits=6, decimal_places=1, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
