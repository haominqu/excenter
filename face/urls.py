from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'test/dhface/$', TestFaceView.as_view(), name='test_face'),
    # url(r'add/dhface/$', FaceManage.as_view(), name='face_manage'),


]