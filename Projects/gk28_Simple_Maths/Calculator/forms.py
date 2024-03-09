from django import forms

class Math_Form(forms.Form):
    one_input = forms.IntegerField()
    two_input = forms.IntegerField()
    display_field = forms.Textarea()
    
