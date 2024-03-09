from django.urls import path
from Loging_Form.views import Logins,All_Users

urlpatterns = [
    path(route='',view=Logins,name='Home'),
    path(route='All-Users',view=All_Users,name='All-Users'),
]