from django.shortcuts import render

# Create your views here.
def Home_Index(request):
    return render(request,template_name='core/index.html',context={'key_1':"Pythoner"})

def About(request):
    return render(request,template_name='core/about.html')