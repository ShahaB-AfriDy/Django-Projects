
from django.urls import path
from Enroll.views import Home,Form_Page


urlpatterns = [
    path(route='',view=Home,name='home'),
    path(route='Form-page/',view=Form_Page,name='form'),
]
