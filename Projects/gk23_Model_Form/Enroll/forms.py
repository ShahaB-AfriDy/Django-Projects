
from django import forms
from Enroll.models import Student


class Student_From(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('Id',"Name","Reg_No","Email","Password")
        lebals = {"Name":"Name","Password":"Password"}
        widgets = {"Password":forms.PasswordInput}