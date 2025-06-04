from django.contrib import admin
from jobs.models import EmployerProfile, JobPosting
# Register your models here.
admin.site.register(EmployerProfile)
admin.site.register(JobPosting)