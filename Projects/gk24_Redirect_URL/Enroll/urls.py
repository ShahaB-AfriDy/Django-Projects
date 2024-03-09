
from django.urls import path
from Enroll.views import Home,Message

urlpatterns = [
    path(route='',view=Home,name='Home'),
    path(route='To-Message/',view=Message,name='Message'),
]