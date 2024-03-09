from django.shortcuts import render
from django import views


# Create Functional base views here.
def Fun_Home(request):
    context = {"fun_key":"Functional View"}
    return render(request,template_name='home.html',context=context)


## ---------------------------------------------------------------------------------------
# Create Class base views here.
class Class_Home(views.View):
    def get(self,request):
        context = {"fun_key":"Class Base View"}
        return render(request,template_name='home.html',context=context)