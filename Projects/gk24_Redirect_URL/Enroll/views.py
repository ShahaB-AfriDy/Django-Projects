from django.shortcuts import render,HttpResponseRedirect
from Enroll.forms import My_Form
# Create your views here.

my_dict = {}

def Message(request):
    return render(request,template_name="Enroll/Message.html",
                  context={'Email':my_dict['Email'],
                           'Password':my_dict['Password']})


def Home(request):
    if request.method == 'POST':
        my_form = My_Form(request.POST)
        if my_form.is_valid():
            Email = my_form.cleaned_data['Email']
            Password = my_form.cleaned_data['Password']
            my_dict['Email'] = Email
            my_dict['Password'] = Password
            return HttpResponseRedirect('/To-Message/')
    else:
        my_form = My_Form()
        
    return render(request,template_name='Enroll/Home.html',
                  context={"my_form":my_form})