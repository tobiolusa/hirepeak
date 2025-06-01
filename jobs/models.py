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
        return f"{self.user} hiring from {self.company_name}"
    
# class JobPost(models.Model):
#     company = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE,related_name="job_posts")
#     job_title = models.CharField(max_length=255)
#     description = models.TextField()
#     industry = models.Choices()
#     experience = models.Choices
