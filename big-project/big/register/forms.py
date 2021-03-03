from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# se foloseste formularul de baza de inregistrare, oferit de
# catre interfata django, prin intermediul caruia se extrag
# informatiile introduse de catre utilizator
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

# se foloseste formularul de baza de autentificare, oferit de
# catre interfata django, prin intermediul caruia se extrag
# informatiile introduse de catre utilizator
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username","password"]