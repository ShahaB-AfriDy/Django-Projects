
from django.shortcuts import render


def Home_Index(request):
    return render(request,template_name='index.html')

def Show_Image(request):
    return render(request,template_name='show_image.html')

