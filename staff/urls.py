from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'getinfo/$', StaffInfo.as_view(), name='staff_info'),
    url(r'upload/image/$', UploadImage.as_view(), name='upload_image'),  # 手机端添加人脸图片
    url(r'guest/list/$', GuestList.as_view(), name='guest_list'),  # 手机端添加人脸图片

]