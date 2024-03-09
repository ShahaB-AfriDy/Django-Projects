from django.shortcuts import render

# Create your views here.

def Service(request):
    context = {'service':"active"}
    return render(request,template_name="service.html",context=context)