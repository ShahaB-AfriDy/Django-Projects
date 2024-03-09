from django.shortcuts import render

# Create your views here.

def Home_Index(request):
    return render(request,template_name="Enroll/home.html")


def Enroll_Info(request):
    return render(request,template_name="Enroll/Enroll.html")