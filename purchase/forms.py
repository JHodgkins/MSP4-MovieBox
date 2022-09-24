"""
Import forms into file.
Import order model.
"""
from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """ Construct fields required on the customer form """
    class Meta:
        """
        meta handles the fields to show on the form from
        the order model
        """
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Set the placeholders on fields and the class on
        the Stripe widget field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone or Mobile Number',
            'street_address1': 'Street Address Line 1',
            'street_address2': 'Street Address Line 2',
            'town_or_city': 'City Town or Village',
            'postcode': 'Postal Code',
            'county': 'County',
            'country': 'Country',
        }
        
        self.fields['full_name'].widget.attrs['autofocus'] = False
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
