from django.urls import path
from Enroll.views import Home


urlpatterns = [
    path(route='',view=Home,name='home'),
]