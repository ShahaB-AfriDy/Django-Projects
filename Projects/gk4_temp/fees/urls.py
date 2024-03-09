
from django.urls import path
from fees.views import Fee_Detail,Fee_Payment

urlpatterns = [
    path('Fees_Detail/',Fee_Detail),
    path('Fees_Payment/',Fee_Payment),
]