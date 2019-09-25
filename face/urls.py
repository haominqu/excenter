from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'accesscontrol/dhface/$', AccessControlFaceView.as_view(), name='accesscontrol_face'),
    url(r'yiti/dhface/$', YiTiFaceView.as_view(), name='yiti_face'),
]