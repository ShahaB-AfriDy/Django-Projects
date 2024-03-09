from django.urls import path
from education import views
urlpatterns = [
    path(route='education/',view=views.Education,name='education'),
]
