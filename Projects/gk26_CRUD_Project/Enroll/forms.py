from django import forms

from Enroll.models import Student

class Student_Form(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['Name',"Email","Password"]
        # labels = {"Name:":"Name Enter","Email":"Email Enter","Password":"Password"}
        # label_suffixs = {":":""}
        widgets = {"Name":forms.TextInput(attrs={'class':'form-control'}),
                   "Email":forms.EmailInput(attrs={'class':'form-control'}),
                   "Password":forms.PasswordInput(render_value=True,attrs={'class':'form-control'})}

        