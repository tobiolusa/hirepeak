from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.http import HttpResponse
import logging
from jobs.views import job_dashboard 
# Create your views here.

def loginuser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('job_dashboard')
        else:
            messages.error(request, "Invalid username or password")
            return render(request, 'users/login.html')
    return render(request, 'users/login.html')

logger = logging.getLogger(__name__)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful, Welcome")
            return redirect('loginuser')
        else:
            logger.error(f"Form errors: {form.errors.as_json()}")
            messages.error(request, 'Please, correct the error below')
    else:
        form = CustomUserCreationForm
    return render(request, 'users/register.html', {'form' : form})

def forget_password(request):
    return render(request, 'users/forget-password.html')

def logoutuser(request):
    logout(request)
    return redirect(loginuser)
def dashboard(request):
    return HttpResponse("Dashboard")