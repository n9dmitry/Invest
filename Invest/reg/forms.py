from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class LoginForm(forms.Form):
#     username = forms.CharField(label='Имя пользователя')
#     password = forms.CharField(widget=forms.PasswordInput, label='Пароль')

class RegistrationForm(UserCreationForm):
    role = forms.ChoiceField(label='Регистрируюсь как:', widget=forms.RadioSelect, choices=[('И', 'Инвестор'), ('С', 'Соискатель')])
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Пароль повторно', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'role', 'password1', 'password2')