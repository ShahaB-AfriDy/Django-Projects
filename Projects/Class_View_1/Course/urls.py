from django.urls import path
from Course import views


urlpatterns = [
    path(route="Fun_Home/",view=views.Fun_Home,name="Fun_Home"),
    path(route="Cl_Home/",view=views.Class_Home.as_view(),name="Cl_Home"),
]
