from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        models = User
        fields = ['email', 'username', 'first_name', 'last_name', 'account_type']