from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib import messages
import logging

# Create your views here.

def loginuser(request):
    return render(request, 'users/login.html')

logger = logging.getLogger(__name__)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful, Welcome")
            return redirect('login')
        else:
            logger.error(f"Form errors: {form.errors.as_json()}")
            messages.error(request, 'Please, correct the error below')
    else:
        form = CustomUserCreationForm
    return render(request, 'users/register.html', {'form' : form})

def forget_password(request):
    return render(request, 'users/forget-password.html')