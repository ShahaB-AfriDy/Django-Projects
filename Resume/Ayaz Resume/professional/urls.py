
from django.urls import path
from professional import views

urlpatterns = [
    path('professional/',views.Professional,name='professional'),
]
