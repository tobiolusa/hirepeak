from django.urls import path, include 
from . import views
urlpatterns = [
    path('', views.login, name="login"), 
    path('register', views.register, name= "register"),
    path('forget-password', views.forget_password, name="forget-password"),
]
