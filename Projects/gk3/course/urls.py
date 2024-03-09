
from django.urls import path
# from views import Studend_Course_Detail,Student_Course
# from . import views
from course import views
urlpatterns = [
    path('Student_Course/',views.Student_Course),
    path('Student_Course_Detail/',views.Student_Course_Detail),
]