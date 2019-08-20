from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'build_socket/(?P<user_id>[0-9]+)$', build_socket, name='build_socket'),
    url(r'staff_guest/login/$', StaffGuestLogin.as_view(), name='staff_guest_login'),
    url(r'staff_guest/logout/$', StaffGuestLogout.as_view(), name='staff_guest_logout'),
]