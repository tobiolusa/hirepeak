from django.urls import path, include 
from . import views
urlpatterns = [
    path('', views.loginuser, name="loginuser"), 
    path('register', views.register, name= "register"),
    path('forget-password', views.forget_password, name="forget-password"),
]
