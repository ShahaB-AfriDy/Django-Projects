from django.shortcuts import render,HttpResponseRedirect
from Enroll.forms import Signup_Form
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate,logout
# Create your views here.
#Home
def Home(request):
    return render(request=request,template_name='Enroll/home.html')

# Profile function
def Profile(request):
    if request.user.is_authenticated:
        return render(request=request,template_name='Enroll/profile.html',
                  context={"name":request.user.first_name})
    else:
        HttpResponseRedirect("/login/")

    

# loging view
def User_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_password = form.cleaned_data['password']
            user = authenticate(username=user_name,password=user_password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect("/profile/")
        else:
            messages.error(request,"Wrong crediential")
    else:
        form = AuthenticationForm()
    return render(request,template_name='Enroll/login.html',
                  context={"form":form})

# user signup
def User_Signup(request):
    if request.method == 'POST':
        form = Signup_Form(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, F"Successfully created {username}")
            form.save()
    else:
        form = Signup_Form()
    return render(request,template_name='Enroll/signup.html',
                  context={"form":form})


# Logout
def User_logout(request):
    logout(request)
    return HttpResponseRedirect("/login/")