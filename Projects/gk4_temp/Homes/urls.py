

from django.urls import path
from Homes.views import Home_Index,About

urlpatterns = [
    path('',Home_Index),
    path('About/',About),
]