
from django.urls import path
from Enroll.views import Home_Index,Data_Table

urlpatterns = [
    path(route='',view=Home_Index,name='home_index'),
    path(route='Data-Table/',view=Data_Table,name='data_table'),
]
