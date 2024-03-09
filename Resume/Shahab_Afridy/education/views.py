from django.shortcuts import render

# Create your views here.

def Education(request):
    context = {'education':'active'}
    return render(request,template_name='education.html',context=context)
