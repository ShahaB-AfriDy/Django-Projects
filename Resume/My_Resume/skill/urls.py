from django.urls import path
from skill import views

urlpatterns = [
    path(route='skill/',view=views.Skill,name='skill'),
]