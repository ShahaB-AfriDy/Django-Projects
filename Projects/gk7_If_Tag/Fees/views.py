from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Home_Index(request):
    return render(request,'index.html')

def Tags_Values(request):
    Data = {"Names":['Ali',"Shahab","Manha","Aqsa"],
            "Registration":["CS12","SE38","PY47","ES98"],
            "Marks":[11,78,74,56],
            "Gender":['Male',"Male","Female",'Female']}
    return render(request,'Tag_Values.html',context={'Data':Data})