from django.shortcuts import render

# Create your views here.
def Professional(request):
    context = {'professional':'active'}
    return render(request,template_name='professional.html',context=context)