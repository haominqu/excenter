from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'getinfo/$', StaffInfo.as_view(), name='staff_info'),
]