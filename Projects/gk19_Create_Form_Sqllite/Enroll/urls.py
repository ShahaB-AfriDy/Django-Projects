
from django.urls import path
from Enroll.views import Home,Form_Page,Show_Data


urlpatterns = [
    path(route='',view=Home,name='home'),
    path(route='Form-page/',view=Form_Page,name='form'),
    path(route='Form-data/',view=Show_Data,name='show_data'),
]
