from django import forms
from .models import EmployerProfile, JobPosting

class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        exclude = ['user']
        widgets = {
            'company_name': forms.TextInput(attrs={'placeholder': 'Amazon'}),
            'company_email': forms.EmailInput(attrs={'placeholder': 'career@amazon.com'}),
            'industry': forms.TextInput(attrs={'placeholder': 'Technology'}),
            'size': forms.NumberInput(attrs={'placeholder': '50'}),
            'company_about': forms.Textarea(attrs={'placeholder': 'Describe your company...'}),
            'location': forms.TextInput(attrs={'placeholder': 'Lagos, Nigeria'}),
            'website': forms.URLInput(attrs={'placeholder': 'https://example.com'}),
        }

class JobPostingForm(forms.ModelForm):
    class Meta: 
        model = JobPosting 
        fields = '__all__'