from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from allauth.auth.forms import SignupForm

class CustomSignupForm(SignupForm):
    account_type = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class' : 'form-group',
            'placeholder' : 'Enter username'
        })
        self.fields['email'].widget.attrs.update({
            'class' : 'form-group',
            'placeholder' : 'Enter Email'
        })
        self.fields['password1'].widget.attrs.update({
            'class' : 'form-group',
            'placeholder' : 'Password'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm password'
        })

        self.fields['account_type'].widget.attrs.update({
            'class' : 'form-group'
        })

        def save(self, request):
            user = super().save(request)
            user.account_type = self.cleaned_data['account_type']
            user.save()
            return user