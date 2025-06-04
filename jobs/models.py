from django.db import models
from django.conf import settings

# Create your models here.
class EmployerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'account_type': 'employer'})
    company_name = models.CharField(max_length=255)
    company_email = models.EmailField(unique=True)
    industry = models.CharField(max_length=255)
    size = models.IntegerField(max_length=4)
    company_about = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255)
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField( upload_to="company_logo/", blank=True, null=True)

    def __str__(self):
        return f"{self.user} hiring {self.company_name}"
    
class JobPosting(models.Model):
    company = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE,related_name="job_posts")
    job_title = models.CharField(max_length=255)
    description = models.TextField()
    experience_level = models.CharField(max_length=100, choices=[
        ('entry_level', 'Entry-Level'),
        ('junior', 'Junior'),
        ('mid-level', 'Mid-level'),
        ('senior', 'Senior')
    ])
    salary_range = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=50, choices=[
        ('full_time', 'Full-Time'),
        ('part_time', 'Part-Time'),
        ('contract', 'Contract'),
        ('freelance', 'Freelance')
    ])
    job_mode = models.CharField(max_length=200, choices=[
        ('remote', 'Remote'),
        ('onsite', 'Onsite'),
        ('hybrid', 'Hybrid')
    ])
    requirement = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.job_title
