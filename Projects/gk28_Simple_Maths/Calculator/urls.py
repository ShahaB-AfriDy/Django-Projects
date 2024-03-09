from django.urls import path
from Calculator.views import Home

urlpatterns = [
    path(route='',view=Home,name='Home'),
]
