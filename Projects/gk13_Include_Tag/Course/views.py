from django.shortcuts import render

# Create your views here.
def Course_Info(request):
    return render(request,template_name='Course/course.html')