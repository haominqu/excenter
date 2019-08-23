from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'getinfo/$', StaffInfo.as_view(), name='staff_info'),
    url(r'upload/image/$', UploadImage.as_view(), name='upload_image'),  # 手机端添加人脸图片
    url(r'guest/manage/$', GuestManageView.as_view(), name='upload_image'),  # 业务人员对来宾的管理:post:邀约来宾
    url(r'guest/list/$', GuestList.as_view(), name='guest_list'),  # 手机端添加人脸图片

]