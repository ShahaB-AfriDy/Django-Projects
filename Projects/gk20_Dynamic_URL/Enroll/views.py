from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,template_name='Enroll/Home.html')


def Show_Data(request,num=1):
    return render(request,template_name='Enroll/Show_Data.html',context={'num':num})