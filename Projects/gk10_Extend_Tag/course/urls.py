
from django.urls import path
from course.views import Course_Info


urlpatterns = [
    path(route='Course-info/',view=Course_Info,name='Course_info'),
]