from django.shortcuts import render

# Create your views here.

def Fees_Detail(request):
    return render(request,template_name='Fees_Detail.html')