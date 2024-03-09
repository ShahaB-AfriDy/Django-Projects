from django.urls import path
from Fees.views import Fees_info


urlpatterns = [
    path(route='Fees-info/',view=Fees_info,name='fees'),
]