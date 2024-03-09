from django.shortcuts import render,HttpResponseRedirect
from Enroll.forms import Student_From
from Enroll.models import Student

# Create your views here.

def Home(request):
    if request.method == 'POST':
        my_form = Student_From(request.POST)
        if my_form.is_valid():
            Id = my_form.cleaned_data['Id']
            Name = my_form.cleaned_data['Name']
            Reg_No = my_form.cleaned_data['Reg_No']
            Email = my_form.cleaned_data['Email']
            Password = my_form.cleaned_data['Password']
            student = Student(Id=Id,Name=Name,Reg_No=Reg_No,Email=Email,Password=Password)
            student.save()
            return HttpResponseRedirect('/Show-Data/')
    else:
        my_form = Student_From()

    return render(request,template_name='Enroll/Home.html',
                  context={'my_form':my_form})



def Show_Data(request):
    student_data = Student.objects.all()
    return render(request,template_name='Enroll/Show_Data.html',
                  context={"student_data":student_data})


def Delete_Data(request):
    student_data = Student.objects.all()
    return render(request,template_name="Enroll/Deleting_Data.html",
                  context={"student_data":student_data})

def Deleted_Data(request,Id):
    if request.method == 'POST':
        Id = Student.objects.get(pk=Id)
        Id.delete()
    return HttpResponseRedirect('/Deleting-Data/')