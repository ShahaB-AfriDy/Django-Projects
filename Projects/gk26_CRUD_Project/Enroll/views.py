from django.shortcuts import render,HttpResponseRedirect
from Enroll.forms import Student_Form
from Enroll.models import Student
# Create your views here.


def Home(request):
    if request.method == 'POST':
        student_form = Student_Form(request.POST)
        if student_form.is_valid():
            Name = student_form.cleaned_data['Name']
            Email = student_form.cleaned_data['Email']
            Password = student_form.cleaned_data['Password']
            student = Student(Name=Name,Email=Email,Password=Password)
            student.save()
            # student_form = Student_Form()    
    else:
        student_form = Student_Form()

    student_data = Student.objects.all()
    return render(request,template_name='Enroll/home.html',
                  context={'student_form':student_form,'student_data':student_data})


# deleting the data
def Delete_Data(request,id):
    if request.method == 'POST':
        student_id = Student.objects.get(pk=id)
        student_id.delete()
    return HttpResponseRedirect("/")


def Update_Data(request,id):
    if request.method == 'POST':
        student_data = Student.objects.get(pk=id)
        student_form = Student_Form(request.POST,instance=student_data)
        if student_form.is_valid():
            # student_form.save()
            Name = student_form.cleaned_data['Name']
            Email = student_form.cleaned_data['Email']
            Password = student_form.cleaned_data['Password']
            student = Student(id=id,Name=Name,Email=Email,Password=Password)
            student.save()
            
    else:
        student_data = Student.objects.get(pk=id)
        student_form = Student_Form(instance=student_data)
    return render(request,template_name='Enroll/update_data.html',context={"student_form":student_form})
