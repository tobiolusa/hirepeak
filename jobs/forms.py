from django import forms
from .models import EmployerProfile, JobPosting

class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        fields = '__all__'

class JobPostingForm(forms.ModelForm):
    class Meta: 
        model = JobPosting 
        fields = '__all__'