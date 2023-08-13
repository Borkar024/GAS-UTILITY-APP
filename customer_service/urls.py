from django.urls import path
from .views import submit_request,request_tracking


urlpatterns = [
    path('sr/',submit_request,name='sr_url'),
    path('tr/',request_tracking,name='tr_url'),
]