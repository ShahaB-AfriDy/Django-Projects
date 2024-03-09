
from django.urls import path
from Homes.views import Home_Index,About

urlpatterns = [
    path(route='',view=Home_Index),
    path(route='About/',view=About),
]