from django.shortcuts import render
from Enroll.models import Student
# Create your views here.

def Home_Index(request):
    return render(request,template_name='Enroll/index.html')


def Data_Table(request):
    data = Student.objects.all()
    return render(request,template_name='Enroll/Data_Table.html',context={'student_data':data})