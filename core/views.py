from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'core/index.html')

def hiring_companies(request):
    return render(request, 'core/hiring-company.html')