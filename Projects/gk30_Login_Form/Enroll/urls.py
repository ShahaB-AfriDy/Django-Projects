from django.urls import path
from Enroll import views


urlpatterns = [
    path(route='',view=views.Home,name='home'),
    path(route='profile/',view=views.Profile,name='profile'),
    path(route='login/',view=views.User_login,name='user-login'),
    path(route='logout/',view=views.User_logout,name='user-logout'),
    path(route='signup/',view=views.User_Signup,name='user-signup'),
]