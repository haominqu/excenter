from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'admin/login/$', AdminLogin.as_view(), name='admin_login'),           # 管理员登录(已调通)
    url(r'upload/image/$', UploadImage.as_view(), name='upload_image'),        # 添加人脸图片(已调通)
    url(r'staff/manage/$', StaffManageView.as_view(), name='staff_manage'),    # 人员管理:添加使用者(业务人员)、删除使用者(业务人员)
    url(r'staff/list/$', StaffList.as_view(), name='staff_list'),              # 人员管理:员工列表
    url(r'guest/list/$', GuestList.as_view(), name='guest_list'),              # 人员管理:来宾列表
    url(r'account/active/$', AccountActive.as_view(), name='account_active'),  # 账户管理:激活、锁定账户
    url(r'account/inpwd/$', AccountInPwdView.as_view(), name='accout_inpwd'),  # 账户管理:重置密码

]