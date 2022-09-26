"""
Import forms into file.
Import user profile model to access user data.
"""
from django import forms
from .models import UserProfile


class ProfileForm(forms.ModelForm):
    """ Construct fields required for the user profile form """
    class Meta:
        """
        meta handles the fields to show on the form from
        the user model
        """
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Set the placeholders on fields and the class on
        the Stripe widget field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone or Mobile Number',
            'default_street_address1': 'Street Address Line 1',
            'default_street_address2': 'Street Address Line 2',
            'default_town_or_city': 'City Town or Village',
            'default_postcode': 'Postal Code',
            'default_county': 'County',
            'default_country': 'Country',
        }
        
        
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'input-profile'
            self.fields[field].label = False
