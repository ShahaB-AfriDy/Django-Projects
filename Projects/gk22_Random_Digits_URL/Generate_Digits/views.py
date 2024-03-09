from django.shortcuts import render
from Generate_Digits.forms import My_Form

from random import randint
# Create your views here.

random_url = 1111

def Home(request,my_id=11):
    a = 1
    Flag = False
    if request.method == 'POST':
        Flag = True
        my_form = My_Form(request.POST)
        if my_form.is_valid():
            global random_url
            random_url = my_form.cleaned_data['Digit_Field']
    if Flag:
        my_form = My_Form(initial={'Digit_Field':randint(1111,9999)})  
    else:
        my_form = My_Form(initial={'Digit_Field':randint(1111,9999)}) 
    # print(random_url)
    return render(request,template_name='Generate_Digits/Home.html',
                context={'my_form':my_form,'my_id':random_url})