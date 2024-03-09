from django.urls import path

from core.views import About,Home_Index


urlpatterns = [
    path(route='',view=Home_Index,name='home'),
    path(route='About/',view=About,name='about'),
]