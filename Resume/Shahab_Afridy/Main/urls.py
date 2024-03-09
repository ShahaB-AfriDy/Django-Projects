from django.urls import path
from Main import views

urlpatterns = [
    path(route='',view=views.home,name='home'),
    path(route='download-cv/',view=views.download_file,name='download-cv'),
]