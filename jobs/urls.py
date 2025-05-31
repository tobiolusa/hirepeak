from django.urls import path, include 
from . import views
urlpatterns = [
        path('dashboard/', views.job_dashboard, name="job_dashboard"),
        path('company-profile', views.company_profile, name="company_profile"),
        path('post-job', views.post_job, name="post_job"), 
        path('manage-job', views.manage_job, name="manage_job"),
        path('all-applicants', views.all_applicant, name="all_applicants")
]
