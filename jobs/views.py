from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import users.views
from jobs.forms import EmployerProfileForm 
from jobs.models import EmployerProfile

@login_required
def job_dashboard(request):
    return render(request, 'jobs/dashboard.html')

@login_required
def company_profile(request):
   
    try:
        profile = EmployerProfile.objects.get(user=request.user)
    except EmployerProfile.DoesNotExist:
        profile = None

    if request.method == 'POST':
     
        form = EmployerProfileForm(request.POST, request.FILES or None, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            if not profile.user: 
                profile.user = request.user
            profile.save()
            messages.success(request, "Company Profile Saved Successfully")
            return redirect('job_dashboard')
        else:
            print("Form errors:", form.errors)
            messages.error(request, "Please correct the errors below!")
    else:
        
        form = EmployerProfileForm(instance=profile)

    return render(request, 'jobs/dashboard-company-profile.html', {'form': form})

@login_required
def post_job(request):
    return render(request,'jobs/dashboard-post-job.html')

@login_required
def manage_job(request):
    return render(request,'jobs/dashboard-manage-job.html')

@login_required
def all_applicant(request):
    return render(request,'jobs/dashboard-applicants.html')