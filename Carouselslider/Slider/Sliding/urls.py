from django.urls import path

from Sliding import views

urlpatterns = [
    path(route='',view=views.home,name='home'),
    path(route='about/',view=views.About,name='About'),
]
