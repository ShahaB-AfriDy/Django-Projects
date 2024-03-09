from django.urls import path
from contact import views


urlpatterns = [
    path(route='contact/',view=views.Contact,name='contact'),
]
