from django.shortcuts import render

# Create your views here.

def Course_Detail(request):
    return render(request,template_name='course_detail.html')

def Course_Offers(request):
    return render(request,template_name='course_offers.html')

