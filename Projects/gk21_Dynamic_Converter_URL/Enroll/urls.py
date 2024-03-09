
from django.urls import path,register_converter

from Enroll.views import Home
from Enroll.converters import Four_Digits

# register Four Digits and dddd 

register_converter(Four_Digits,'dddd')

urlpatterns = [
    path(route='Home/<dddd:random_digits>/',view=Home,name="Home"),
]