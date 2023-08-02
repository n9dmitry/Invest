from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# from Invest.reg.models import Profile


class RegistrationForm(UserCreationForm):
    interest = forms.ChoiceField(label='Меня больше интересует:', widget=forms.RadioSelect, choices=[('И', 'Инвестиции'), ('П', 'Привлечение денег в свои проекты')])
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Пароль повторно', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'name', 'interest', 'password1', 'password2')

    # def save(self, commit=True):
    #     user = super().save(commit=commit)
    #     profile = Profile(user=user)
    #     if commit:
    #         profile.save()
    #
    #     return user
