
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):

    email = forms.Emailfield()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']
    #Saca los mensajes de ayuda
    help_texts = {k:"" for k in fields}