from django import forms


class Enroll_Froms(forms.Form):
    Name = forms.CharField()
    Email = forms.EmailField()
    Password = forms.CharField(widget=forms.PasswordInput)
