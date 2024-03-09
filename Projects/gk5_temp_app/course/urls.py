
from django.urls import path
from course.views import  Course_Detail,Course_Offers

urlpatterns = [
    path(route='Course_Detail/',view=Course_Detail),
    path(route='Course_Offers/',view=Course_Offers),
]