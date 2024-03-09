from django.shortcuts import render
from Enroll.forms import Enroll_Froms
from Enroll.models import Student
# Create your views here.



def Home(request):
    return render(request,template_name='Enroll/home.html')



def Form_Page(request):
    if request.method == 'POST':
        enroll = Enroll_Froms(request.POST)
        if enroll.is_valid():
            # print(enroll.cleaned_data)
            data = enroll.cleaned_data
            Student.objects.create(Name=data['Name'],
                                    Email=data['Email'],Password=data['Password'])

    else:
        enroll = Enroll_Froms()

    return render(request,template_name = 'Enroll/Form.html',
                  context={'enroll':enroll})


def Show_Data(request):
    data = Student.objects.all()
    return render(request,template_name='Enroll/students_form.html',context={'Data':data})