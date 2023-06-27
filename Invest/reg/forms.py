from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class LoginForm(forms.Form):
#     username = forms.CharField(label='Имя пользователя')
#     password = forms.CharField(widget=forms.PasswordInput, label='Пароль')

class RegistrationForm(UserCreationForm):
    
    role = forms.ChoiceField(widget=forms.RadioSelect, choices=[('I', 'Investor'),('A', 'Applicant')])
    password2 = forms.PasswordInput()

    class Meta():
        model = User
        fields = ('email','role','password1','password2')


    def clean_password2(self):
        cleaned_data = self.cleaned_data

        password = cleaned_data['password1']
        password2 = cleaned_data['password2']
        print(password)
        if  password or  password2 or password != password2:

            raise forms.ValidationError("Пароли не совпадают")

        return cleaned_data