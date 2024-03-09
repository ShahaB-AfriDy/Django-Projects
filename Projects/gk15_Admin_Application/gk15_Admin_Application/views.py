from django.shortcuts import render

# Create your views here.

def Admin_Page(request):
    return render(request,template_name="Admin_page.html")