
from django import forms

class My_Form(forms.Form):
    Email = forms.EmailField(max_length=30 ,label="Email  ")
    Password = forms.CharField(widget=forms.PasswordInput())
