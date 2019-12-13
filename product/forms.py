''' forms '''
from django import forms

from .models import Product


class ProductUpdateForm(forms.ModelForm):
    ''' form product update '''
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'price']
