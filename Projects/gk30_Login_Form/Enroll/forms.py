
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class Signup_Form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
