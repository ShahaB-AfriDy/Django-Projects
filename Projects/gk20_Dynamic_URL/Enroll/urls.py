from django.urls import path

from Enroll.views import Home,Show_Data

urlpatterns = [
    path(route='',view=Home,name="Home"),
    path(route='show-data/<int:num>/',view=Show_Data,name="show-data"),
]