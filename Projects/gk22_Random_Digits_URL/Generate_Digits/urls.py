
from django.urls import path
from Generate_Digits.views import Home,random_url

urlpatterns = [
    # path(route=F"Home/<{my_id}>/",view=Home,name='Home'),
    path(route="Home/<my_id>/",view=Home,name='Home'),
]