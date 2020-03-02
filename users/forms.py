from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()

    description = forms.Textarea()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']