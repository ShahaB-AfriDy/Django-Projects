from django.urls import path
from service import views

urlpatterns = [
    path(route='service/',view=views.Service,name='service'),
]
