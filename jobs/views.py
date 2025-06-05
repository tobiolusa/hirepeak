from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import users.views
from jobs.forms import EmployerProfileForm, JobPostingForm
from jobs.models import EmployerProfile, JobPosting

@login_required
def job_dashboard(request):
    company = EmployerProfile.objects.get(user=request.user)
    job_count = JobPosting.objects.filter(company=company).count()
    return render(request, 'jobs/dashboard.html', {'job_count' : job_count })


@login_required
def company_profile(request):
    try:
        profile = EmployerProfile.objects.get(user=request.user)
    except EmployerProfile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        if profile is None:
            profile = EmployerProfile(user=request.user)
        form = EmployerProfileForm(request.POST, request.FILES or None, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user  # Ensure the user is set
            profile.save()
            messages.success(request, "Company Profile Saved Successfully")
            return redirect('job_dashboard')
        else:
            print("Form errors:", form.errors)
            messages.error(request, "Please correct the errors below!")
    else:
        # GET request: pass profile if it exists
        form = EmployerProfileForm(instance=profile)

    return render(request, 'jobs/dashboard-company-profile.html', {'form': form})


@login_required
def post_job(request):
    if request.method == 'POST':
        form = JobPostingForm(request.POST)
        if form.is_valid():
            job_posting = form.save(commit=False)
            job_posting.company = request.user
            job_posting.save()
            return redirect('manage-job')
    else:
        form = JobPostingForm()

    return render(request,'jobs/dashboard-post-job.html', {'form': form})

@login_required
def manage_job(request):
    return render(request,'jobs/dashboard-manage-job.html')

@login_required
def all_applicant(request):
    return render(request,'jobs/dashboard-applicants.html')