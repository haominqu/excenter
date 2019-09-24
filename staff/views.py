# restful API
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings

# django
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from django.utils.decorators import method_decorator
from django.conf import settings

# selfproject
from userinfo.models import *
from .permissions import *
from .serializers import *
from userinfo.permissions import *
from userinfo.fourrandom import generate_code

# base
import logging
import time
import os
import shutil
import socket
from PIL import Image

# Create your views here.


class StaffInfo(APIView):
    """
        desc: 个人信息管理模块
    """
    permission_classes = (
        IsStaff,
    )

    @method_decorator(login_decorator)
    def get(self, request, **kwargs):
        """
        desc:个人账户查看
        :param request:
        :return:
        """
        token = kwargs['token']
        user_id = token['user_id']
        user = UserDetail.objects.filter(user_id=user_id)
        if not user:
            result = False
            data = ""
            error = "未查询到用户"
            return JsonResponse({"result": result, "data": data, "error": error})
        user_se = StaffSerializer(user[0], many=False)
        result = True
        data = user_se.data
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})

    def put(self, request, **kwargs):

        """
        desc:修改密码
        :return:
        """
        token = kwargs['token']
        user_id = token['user_id']
        new_pwd = request.data.get('new_pwd', '')
        user = UserInfo.objects.filter(id=user_id)
        if not user:
            result = False
            data = ""
            error = ""
            return JsonResponse({"result": result, "data": data, "error": error})
        try:
            user[0].update(password=new_pwd)
        except ObjectDoesNotExist as e:
            logging.warning(e)
            result = False
            data = ""
            error = ""
            return JsonResponse({"result": result, "data": data, "error": error})
        user[0].user_secret = uuid4()
        user[0].is_login = False
        user[0].save()
        result = True
        data = "密码已修改"
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})


class UploadImage(APIView):
    permission_classes = (
        IsStaff,
    )
    """
    desc:手机端,业务人员添加来宾人脸图
    """

    @method_decorator(login_decorator)
    def post(self, request, **kwargs):
        # phonesys = request.FILES.get("phonesys",'a')   # android iphone(顺90->270) wp
        phonesys = request.META.get("HTTP_PHONESYS",'a')   # android iphone(顺90->270) wp
        face_picture = request.FILES.get('myfiles', '')
        file_type = face_picture.name.split('.')[1]
        time_stamp = int(round(time.time() * 1000))
        file_name = str(time_stamp) + '.' + file_type
        f = open(os.path.join(settings.BASE_DIR, 'media', 'tempory_m', file_name), 'wb')
        for chunk in face_picture.chunks():
                f.write(chunk)
        f.close()
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        file_path = "http://" + "39.106.16.34:8001" + "/media/tempory_m/"+file_name
        im = Image.open(os.path.join(settings.BASE_DIR, 'media', 'tempory_m', file_name))
        if phonesys == "android":
            im_rotate = im.rotate(90)
            im_rotate.save(os.path.join(settings.BASE_DIR, 'media', 'tempory_m', file_name))
        elif phonesys == 'iphone':
            im_rotate = im.rotate(270)
            im_rotate.save(os.path.join(settings.BASE_DIR, 'media', 'tempory_m', file_name))
        result = True
        data = file_path
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})



class GuestManageView(APIView):
    permission_classes = (
        IsStaff,
    )

    @method_decorator(login_decorator)
    def post(self, request, *args, **kwargs):
        """
        desc:员工邀约来宾
        :param request:
        :return:
        """
        token = kwargs['token']
        staff_id = token['user_id']
        user_name = request.POST.get("user_name", "")  # 手机号
        real_name = request.POST.get("real_name", "")
        position = request.POST.get("position", "")  # 职位(允许为空)
        department = request.POST.get("department", "")  # 公司(允许为空)
        face_picture = request.POST.get("face_picture", "")
        if user_name == "" or real_name == "" or face_picture == "":
            result = False
            data = ""
            error = "来宾基础信息不能为空"
            return JsonResponse({"result": result, "data": data, "error": error})
        staff = UserInfo.objects.filter(id=staff_id)
        if not staff:
            result = False
            data = ""
            error = "员工信息有误"
            return JsonResponse({"result": result, "data": data, "error": error})
        user_name_fit = UserInfo.objects.filter(username=user_name)
        if user_name_fit:
            result = False
            data = ""
            error = "该手机已注册"
            return JsonResponse({"result": result, "data": data, "error": error})
        user_info = UserInfo()
        user_info.username = user_name
        user_info.password = user_name[-4:]
        user_info.role = 3
        user_info.uu_id = str(int(round(time.time() * 1000))) + generate_code()
        try:
            user_info.save()
        except ObjectDoesNotExist as e:
            logging.warning(e)
            result = False
            data = ""
            error = "添加失败"
            return JsonResponse({"result": result, "data": data, "error": error})
        user = UserInfo.objects.filter(id=user_info.id)
        if not user:
            user_info.delete()
        guest = Guest()
        guest.user = user_info
        guest.invite = staff[0]
        guest.realname = real_name
        face_file_name = face_picture.split('/')[-1]
        fixed_file_path = "/media/face_info/guest/"
        tempory_file_path = "/media/tempory_m/"
        abs_path = os.getcwd()
        for file in os.listdir(abs_path + tempory_file_path):
            if file != face_file_name:
                continue
            else:
                shutil.copy(os.path.join(abs_path + tempory_file_path, file),
                            os.path.join(abs_path + fixed_file_path, file))
                os.remove(os.path.join(abs_path + tempory_file_path, face_file_name))
        guest.face_picture = "/face_info/guest/" + face_file_name
        guest.position = position
        guest.department = department
        try:
            guest.save()
        except ObjectDoesNotExist as e:
            user_info.delete()
            logging.error(e)
            result = False
            data = ""
            error = "添加失败"
            return JsonResponse({"result": result, "data": data, "error": error})
        result = True
        data = "已成功邀约来宾"
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})


class GuestList(APIView):
    permission_classes = (
        IsStaff,
    )

    @method_decorator(login_decorator)
    def get(self, request, **kwargs):
        """
            desc:业务人员获取自己邀请的来宾列表
            :param request:
            :return:返回来宾角色, 来宾用户名(手机号), 来宾姓名, 邀请人, 审核状态
        """
        token = kwargs['token']
        staff_id = token['user_id']
        guest = Guest.objects.filter(user__role=3, invite_id=staff_id)
        guest_se = GuestSerializer(guest, many=True)
        guest_data = guest_se.data
        result = True
        data = guest_data
        # data = guest_info_list
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})


