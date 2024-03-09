

from django.urls import path
from course.views import Course_Detail,Course_Offers

urlpatterns = [
    path('Course_Detail/',Course_Detail),
    path('Course_Offers/',Course_Offers),
]