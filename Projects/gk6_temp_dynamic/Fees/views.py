
from django.shortcuts import render

# Create your views here.

def Fee_Detail(request):
   
    Dict_Data = {'name':'Shahab Afridy',
                 'registration':'SE1203192038',
                 'fee':124000,
                 'semester':'8th'}
    
    return render(request,template_name='fees_detail.html',
                  context=Dict_Data)