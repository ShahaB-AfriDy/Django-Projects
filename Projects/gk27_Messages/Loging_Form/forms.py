from django import forms
from Loging_Form.models import Login_Model

class My_Login_From(forms.ModelForm):
    class Meta:
        model = Login_Model
        fields = ['User','Password']
        widgets = {"User":forms.TextInput(attrs={"class":'form-control'}),
            'Password':forms.PasswordInput(attrs={"class":'form-control'})}



# class My_Login_From(forms.Form):
#     User = forms.CharField(max_length=30,label='User_Name')
#     Password = forms.CharField(widget=forms.PasswordInput,max_length=30)
    