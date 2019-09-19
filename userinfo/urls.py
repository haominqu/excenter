from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'build_socket/(?P<user_id>[0-9]+)$', build_socket, name='build_socket'),
    url(r'staff_guest/login/$', StaffGuestLogin.as_view(), name='staff_guest_login'),
    url(r'staff_guest/logout/$', StaffGuestLogout.as_view(), name='staff_guest_logout'),
    url(r'alter/pwd/$', UserAlterPwd.as_view(), name='alter_pwd'),
    url(r'face/info/$', FaceInfoView.as_view(), name='face_info'),
]