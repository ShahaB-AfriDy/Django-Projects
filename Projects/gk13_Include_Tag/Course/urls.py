
from django.urls import path
from Course.views import Course_Info

urlpatterns = [
    path(route='Course-info/',view=Course_Info,name='course'),
]
