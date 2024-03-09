
from django.urls import path
# from views import Student_Fee,Studend_Fee_Detail
# from . import views
from fees import views
urlpatterns = [
    path('Student_Fee_Detail/',views.Student_Fee_Detail),
    path('Student_Fee/',views.Student_Fee),
]