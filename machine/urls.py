from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'lamp/', Lamp.as_view(), name='lamp'),

]
