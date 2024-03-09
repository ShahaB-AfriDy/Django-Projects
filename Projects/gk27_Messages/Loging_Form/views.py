from django.shortcuts import render
from Loging_Form.forms import My_Login_From
from django.contrib import messages
from Loging_Form.models import Login_Model

# Create your views here.

def Logins(request):
    if request.method == 'POST':
        login_form = My_Login_From(request.POST)
        if login_form.is_valid():
            User_form = login_form.cleaned_data['User']
            Password_form = login_form.cleaned_data['Password']
            
            # Check if a user with the provided username exists in the database
            try:
                User_model = Login_Model.objects.get(User=User_form)
                if User_model.Password == Password_form:
                    messages.success(request=request, message= F'{User_form.title()} Successfully logged in')
                    # Redirect to a success page or perform further actions
                else:
                    messages.error(request=request, message='Incorrect password')
            except Login_Model.DoesNotExist:
                messages.error(request=request, message='User does not exist')
        else:
            messages.error(request=request, message='Invalid data')
    else:
        login_form = My_Login_From()

    return render(request, template_name='Login_From/login.html', context={'login_form': login_form})




def All_Users(request):
    data = Login_Model.objects.all()
    return render(request,template_name='Login_From/users.html',
                  context={'data':data,'d':'Testig data'})