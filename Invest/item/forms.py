from django import forms
from django.forms import inlineformset_factory

from .models import Item, Reviews, ReviewsImages


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'city',
                  'required_investment', 'profit_per_month', 'user', 'category']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['rating', 'text']

class ReviewImageForm(forms.ModelForm):
    class Meta:
        model = ReviewsImages
        fields = ('image',)