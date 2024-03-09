# forms.py
from django import forms

class MyForm(forms.Form):
    my_choices = [
        ('1', 'Option 1'),
        ('2', 'Option 2'),
        ('3', 'Option 3'),
    ]

    my_field = forms.ChoiceField(choices=my_choices, widget=forms.Select(attrs={'class': 'form-control'}))
