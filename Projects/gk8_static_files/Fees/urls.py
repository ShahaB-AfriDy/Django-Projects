
from django.urls import path

from Fees.views import Fees_Detail

urlpatterns = [
    path(route='Fees-Detail/',view=Fees_Detail)
]