from django.urls import path
from Course.views import Course_info


urlpatterns = [
    path(route='Course-info/',view=Course_info,name='course'),
]