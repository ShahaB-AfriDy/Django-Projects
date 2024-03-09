from django.urls import path
from Enroll.views import Home_Index,Enroll_Info

urlpatterns = [
    path(route='',view=Home_Index,name='home'),
    path(route='Enroll-Info/',view=Enroll_Info,name='enroll'),
]

