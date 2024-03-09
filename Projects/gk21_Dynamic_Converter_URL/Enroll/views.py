from django.shortcuts import render

# Create your views here.

def Home(request,random_digits=1122):
    return render(request,template_name='Enroll/Home.html',
                  context={'Random_numbers':random_digits})