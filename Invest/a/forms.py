from django import forms
from .models import A

class AForm(forms.ModelForm):
    class Meta:
        model = A
        fields = ['title', 'description', 'image']