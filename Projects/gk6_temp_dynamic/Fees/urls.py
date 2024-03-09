

from django.urls import path
from Fees.views import Fee_Detail

urlpatterns = [
    path(route='Fee_Detail/',view=Fee_Detail),
]