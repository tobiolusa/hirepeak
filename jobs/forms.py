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
        fields = [
            'job_title', 'description', 'experience_level',
            'salary_range', 'location', 'employment_type',
            'job_mode', 'requirement'
        ]
        widgets = {
            'job_title': forms.TextInput(attrs={
                'id': 'job_title', 'placeholder': 'e.g. Frontend Developer', 'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'id': 'description', 'rows': 6, 'placeholder': 'Describe the role...', 'class': 'form-control'
            }),
            'experience_level': forms.Select(attrs={
                'id': 'experience_level', 'class': 'chosen-select'
            }),
            'salary_range': forms.TextInput(attrs={
                'id': 'salary_range', 'placeholder': 'e.g. $2500 - $3500', 'class': 'form-control'
            }),
            'location': forms.TextInput(attrs={
                'id': 'location', 'placeholder': 'e.g. Lagos, Nigeria', 'class': 'form-control'
            }),
            'employment_type': forms.Select(attrs={
                'id': 'employment_type', 'class': 'chosen-select'
            }),
            'job_mode': forms.Select(attrs={
                'id': 'job_mode', 'class': 'chosen-select'
            }),
            'requirement': forms.Textarea(attrs={
                'id': 'requirement', 'rows': 4, 'placeholder': 'e.g. Experience with Django...', 'class': 'form-control'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].required = True
        self.fields['experience_level'].required = True
        self.fields['location'].required = True
        self.fields['employment_type'].required = True
        self.fields['job_mode'].required = True
        self.fields['salary_range'].required = False
        self.fields['requirement'].required = False
