from django.shortcuts import render

# Create your views here.

def Fee_Detail(request):
    return render(request,template_name='fees_detail.html')

def Fee_Payment(request):
    return render(request,template_name='fees_payment.html')