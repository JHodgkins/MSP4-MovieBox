"""
Import forms from Django to manage form submissions.
Import product and category models to access movies stored in the database. 
"""
from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """
    Product form to hold field inputs so a superuser can 
    add a movie to MovieBox
    """
    class Meta:
        """ set the model for which fields to retrieve """
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        readable_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = readable_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'product-add-field'
