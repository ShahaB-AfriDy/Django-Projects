# urls.py
from django.urls import path
from dropdownlist import views

urlpatterns = [
    path(route='', view=views.my_view, name='your_view_name'),
]
