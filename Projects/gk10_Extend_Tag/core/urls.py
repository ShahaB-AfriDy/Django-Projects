
from django.urls import path
from core.views import Home_Index,About

urlpatterns = [
    path(route='',view=Home_Index,name="home"),
    path(route='About/',view=About,name="about"),
]