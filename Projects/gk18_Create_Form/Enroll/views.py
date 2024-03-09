from django.shortcuts import render
from Enroll.forms import Enroll_Froms
# Create your views here.



def Home(request):
    enroll = Enroll_Froms()
    return render(request,template_name='Enroll/home.html',
                  context={'enroll':enroll})

def Form_Page(request):
    enroll = Enroll_Froms()
    return render(request,template_name = 'Enroll/Form.html',
                  context={'enroll':enroll})