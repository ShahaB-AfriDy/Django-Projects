from django.shortcuts import render

# Create your views here.

def Home_Index(request):
    return render(request,template_name='index.html')

def About(request):
    return render(request,template_name='about.html')
