from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'users/login.html')

def register(request):
    if request.method == 'POST':
        pass
    return render(request, 'account/signup.html')

def forget_password(request):
    return render(request, 'users/forget-password.html')