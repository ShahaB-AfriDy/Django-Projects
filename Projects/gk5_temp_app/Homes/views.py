from django.shortcuts import render

# Create your views here.

def Home_Index(request):
    return render(request,template_name='Homes/index.html')
def About(request):
    return render(request,template_name='Homes/about.html')