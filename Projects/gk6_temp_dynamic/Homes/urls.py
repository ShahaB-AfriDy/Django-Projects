
from django.urls import path
from Homes.views import Home_Index

urlpatterns = [
    path(route='',view=Home_Index),
]