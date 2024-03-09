from django.shortcuts import render

# Create your views here.

def Fees_info(request):
    return render(request,template_name='Fees/fees.html')