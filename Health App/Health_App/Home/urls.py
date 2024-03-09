from django.urls import path

from Home import views as vs

urlpatterns = [
    path(route='home/',view=vs.home,name='home'),
    path(route='',view=vs.index,name='index'),
]
