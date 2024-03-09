from django import forms


class Enroll_Froms(forms.Form):
    User_name = forms.CharField()
    Reg_NO = forms.CharField()
    Email = forms.EmailField()