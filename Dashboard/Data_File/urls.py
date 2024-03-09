from django.urls import path
from Data_File import views

urlpatterns = [
    path("",views.Home,name='home'),
    path("Display/",views.Display_Summary,name='display'),
    path("Calculated/<str:column>/",views.Calculated,name='calculated'),
]
