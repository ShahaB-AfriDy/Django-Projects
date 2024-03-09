
from django.urls import path
from Enroll.views import Home,Delete_Data,Update_Data
urlpatterns = [
    path(route='',view=Home,name='Home'),
    path(route='Delete-Data/<int:id>/',view=Delete_Data,name='Delete-Data'),
    path(route='Update-Data/<int:id>/',view=Update_Data,name='Update-Data'),
]