from django.shortcuts import render
from Calculator.forms import Math_Form
# Create your views here.

def Home(request):
    add_up = None
    if request.method == 'POST':
        math_form = Math_Form(request.POST)
        if math_form.is_valid():
            one_input = math_form.cleaned_data['one_input']
            two_input = math_form.cleaned_data['two_input']
            add_up = one_input+two_input

    else:
        math_form = Math_Form()
    return render(request,template_name='Calculator/home.html',
                  context={"math_form":math_form,"add_up":add_up})