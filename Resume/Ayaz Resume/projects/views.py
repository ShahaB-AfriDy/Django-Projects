from django.shortcuts import render

# Create your views here.
def Projects(request):
    context = {'projects':'active'}
    return render(request,template_name='projects.html',context=context)