from django.urls import path
from Main import views

urlpatterns = [
    path(route='',view=views.home,name='home'),
]
