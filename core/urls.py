from django.urls import path, include 
from . import views
urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('hiring-companies/', views.hiring_companies, name="hiring_companies"),
    path('browse-jobs', views.browse_jobs, name="browse-jobs"),
       
]
