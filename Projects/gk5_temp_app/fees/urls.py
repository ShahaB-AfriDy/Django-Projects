


from django.urls import path
from fees.views import  Fee_Detail,Fee_Payment

urlpatterns = [
    path(route='Fee_Detail/',view=Fee_Detail),
    path(route='Fee_Payment/',view=Fee_Payment),
]