
from django import forms

class My_Form(forms.Form):
    
    Digit_Field = forms.CharField(max_length=10,label='')