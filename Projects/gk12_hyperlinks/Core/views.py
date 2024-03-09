from django.shortcuts import render

# Create your views here.

def Home_Index(request):
    return render(request,template_name='Core/index.html',context={'hm':'/About'})

def About(request):
    return render(request,template_name='Core/about.html')

