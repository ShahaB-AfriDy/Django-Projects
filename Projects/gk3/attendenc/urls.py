
from django.urls import path
# from views import Student_Attendence,Student_Record
# from . import views
from attendenc import views
urlpatterns = [
    path(route='Student_Attendence/',view=views.Student_Attendence),
    path(route='Student_Record/',view=views.Student_Record),
]