from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import users.views
from jobs.forms import EmployerProfileForm 

@login_required
def job_dashboard(request):
    return render(request, 'jobs/dashboard.html')

@login_required
def company_profile(request):
    
    if request.method == 'POST':
        form = EmployerProfileForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'jobs/dashboard-company-profile.html')

@login_required
def post_job(request):
    return render(request,'jobs/dashboard-post-job.html')

@login_required
def manage_job(request):
    return render(request,'jobs/dashboard-manage-job.html')

@login_required
def all_applicant(request):
    return render(request,'jobs/dashboard-applicants.html')