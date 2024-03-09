
from django.urls import path
from projects import views

urlpatterns = [
    path('projects/',views.Projects,name='projects'),
]
