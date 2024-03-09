
from django.urls import path,register_converter

from Enroll.views import Home,Show_Data,Delete_Data,Deleted_Data
from Enroll.converters import Four_Digits

# register Four Digits and dddd 

# register_converter(Four_Digits,'dddd')

# urlpatterns = [
#     path(route='Home/<dddd:random_digits>/',view=Home,name="Home"),
# ]


urlpatterns = [
    path(route='',view=Home,name="Home"),
    path(route='Show-Data/',view=Show_Data,name="Show-Data"),
    path(route='Deleting-Data/',view=Delete_Data,name="Deleting-Data"),
    path(route='Deleted-Data/<int:Id>/',view=Deleted_Data,name="Deleted-Data"),
]