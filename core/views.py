from django.shortcuts import render
from jobs.models import JobPosting, EmployerProfile

# Create your views here.
def homepage(request):
    return render(request, 'core/index.html')

def hiring_companies(request):
    return render(request, 'core/hiring-company.html')

def browse_jobs(request):
    jobpost_listings = JobPosting.objects.all().order_by('-created_at')
    return render(request, 'core/browse-jobs.html', {'jobpost_listings': jobpost_listings})

def custom404(request, exception):
    return render(request, 'core/404.html', status=404)