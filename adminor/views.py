# restful API
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings

# django
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from django.conf import settings

# self_project
from userinfo.models import UserInfo, Guest, UserDetail
from django.contrib.auth.hashers import check_password, make_password
from .serializers import StaffSerializer, GuestSerializer
from userinfo.permissions import IsAdmin, login_decorator
from excenteron.settings import BASE_URL
from machine.models import *
from userinfo.fourrandom import generate_code

# base
import logging
import time
import os
import shutil

# Create your views here.

class IndexView(APIView):
    def get(self, request):
        """
        desc:首页数据展示
        :param request:
        :return:
        """
        machines = Machine.objects.filter(mac_ctype=2)
        mac_list = []
        for machine in machines:
            data = {}
            con_mac = ControlMac.objects.filter(mac=machine)
            if not con_mac:
                result = False
                data = ""
                error = ""
                return JsonResponse({"result": result, "data": data, "error": error})
            data["mac"] = machine.mac_name
            data["kind"] = machine.kind
            data["sta"] = con_mac[0].temperature
            mac_list.append(data)
        result = True
        data = mac_list
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})


class AdminLogin(APIView):

    """
        desc:管理员登录
    """

    def post(self, request):
        """
        desc:实现管理员登录
        :param request:
        :return:
        """
        user_name = request.POST.get("user_name", "")
        password = request.POST.get("password", "")
        if user_name == "" or password == "":
            result = False
            data = ""
            error = "用户名密码不能为空"
            return JsonResponse({"result": result, "data": data, "error": error})
        user = UserInfo.objects.filter(username=user_name)
        if not user:
            result = False
            data = ""
            error = "未查询到用户"
            return JsonResponse({"result": result, "data": data, "error": error})
        is_pwd = check_password(password, user[0].password)
        if not is_pwd:
            result = False
            data = ""
            error = "用户名密码不正确"
            return JsonResponse({"result": result, "data": data, "error": error})
        if user[0].role != int(1):
            result = False
            data = ""
            error = "不是管理员"
            return JsonResponse({"result": result, "data": data, "error": error})
        if user:
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user[0])
            payload['role'] = user[0].role
            token = jwt_encode_handler(payload)
            user[0].user_secret = token
            user[0].is_login = True
            user[0].save()
            data = {}
            data['token'] = token
            data['avatar'] = BASE_URL+"/media/avatar/guide_manage.jpg"
            result = True
            data = data
            error = ""
            return JsonResponse({"result": result, "data": data, "error": error})


class UploadImage(APIView):
    permission_classes = (
        IsAdmin,
    )

    @method_decorator(login_decorator)
    def post(self, request, *args, **kwargs):
        face_picture = request.FILES.get('face_picture', '')
        print(face_picture)
        print(type(face_picture))
        file_type = face_picture.name.split('.')[1]
        time_stamp = int(round(time.time() * 1000))
        file_name = str(time_stamp) + '.' + file_type
        f = open(os.path.join(settings.BASE_DIR, 'media', 'tempory', file_name), 'wb')
        for chunk in face_picture.chunks():
            f.write(chunk)
        f.close()
        file_path = settings.BASE_URL+"/media/tempory/"+file_name
        result = True
        data = file_path
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})


class StaffManageView(APIView):
    """管理员对于人员的管理"""
    permission_classes = (
        IsAdmin,
    )

    @method_decorator(login_decorator)
    def post(self, request, **kwargs):
        """
        管理员进行添加员工:包括手机号, 姓名, 员工编号, 职位, 所属部门, 人脸
        密码默认手机号后4位,
        员工默认状态未激活
        :param request:
        :return:
        """
        user_name = request.POST.get("user_name", "")  # 手机号
        real_name = request.POST.get("real_name", "")
        staff_code = request.POST.get("staff_code", "")
        position = request.POST.get("position", "")
        department = request.POST.get("department", "")
        face_picture = request.POST.get('face_picture', '')
        if user_name == "" or real_name == "" or staff_code == "" or position == "" or department == "" or face_picture == "":
            result = False
            data = ""
            error = "员工基本信息不能为空"
            return JsonResponse({"result": result, "data": data, "error": error})
        user_name_fit = UserInfo.objects.filter(username=user_name)
        if user_name_fit:
            result = False
            data = ""
            error = "该手机已注册"
            return JsonResponse({"result": result, "data": data, "error": error})
        user_info = UserInfo()
        user_info.username = user_name
        password = make_password(user_name[-4: ], None, 'pbkdf2_sha256')
        user_info.password = password
        user_info.role = 2
        user_info.uu_id = str(int(round(time.time() * 1000))) + generate_code()
        try:
            user_info.save()
        except ObjectDoesNotExist as e:
            logging.error(e)
            result = False
            data = ""
            error = "添加失败"
            return JsonResponse({"result": result, "data": data, "error": error})
        user_detail = UserDetail()
        user_detail.user = user_info
        user_detail.realname = real_name
        user_detail.staff_code = staff_code
        user_detail.position = position
        user_detail.department = department
        face_file_name = face_picture.split('/')[-1]
        fixed_file_path = "/media/face_info/staff/"
        tempory_file_path = "/media/tempory/"
        abs_path = os.getcwd()
        for file in os.listdir(abs_path + tempory_file_path):
            if file != face_file_name:
                continue
            else:
                shutil.copy(os.path.join(abs_path + tempory_file_path, file),
                            os.path.join(abs_path + fixed_file_path, file))
                os.remove(os.path.join(abs_path + tempory_file_path, face_file_name))
        user_detail.face_picture = "/face_info/staff/" + face_file_name
        try:
            user_detail.save()
        except ObjectDoesNotExist as e:
            user_info.delete()
            logging.error(e)
            result = False
            data = ""
            error = "添加失败"
            return JsonResponse({"result": result, "data": data, "error": error})
        result = True
        data = ""
        error = "添加成功"
        return JsonResponse({"result": result, "data": data, "error": error})

    @method_decorator(login_decorator)
    def delete(self, request, *args, **kwargs):
        staff_id = request.data.get('staff_id', '')
        if staff_id == "":
            result = False
            data = ""
            error = ""
            return JsonResponse({"result": result, "data": data, "error": error})
        user = UserInfo.objects.filter(id=staff_id)
        if not user:
            result = False
            data = ""
            error = ""
            return JsonResponse({"result": result, "data": data, "error": error})
        try:
            user[0].delete()
        except ObjectDoesNotExist as e:
            logging.warning(e)
            result = False
            data = ""
            error = "删除失败"
            return JsonResponse({"result": result, "data": data, "error": error})
        result = True
        data = ""
        error = "删除成功"
        return JsonResponse({"result": result, "data": data, "error": error})



class StaffList(APIView):
    permission_classes = (
        IsAdmin,
    )

    @method_decorator(login_decorator)
    def get(self, request, *args, **kwargs):
        """
        desc:管理员获取员工列表
        :param request:
        :return:返回员工角色, 姓名, 用户名(手机号), 编号, 职位, 部门, 激活
        """
        staff = UserDetail.objects.filter(user__role=2)
        staff_se = StaffSerializer(staff, many=True)
        staff_data = staff_se.data
        result = True
        data = staff_data
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})


class AccountActive(APIView):
    permission_classes = (
        IsAdmin,
    )

    @method_decorator(login_decorator)
    def post(self, request, *args, **kwargs):
        """
        desc: 管理员进行员工账号激活、锁定
        :param request:
        :return:
        """
        staff_id = request.POST.get("user_id", "")
        is_active = request.POST.get("is_active", "")
        if staff_id == "" or is_active == "":
            result = False
            data = ""
            error = ""
            return JsonResponse({"result": result, "data": data, "error": error})
        staff = UserInfo.objects.filter(id=staff_id)
        if not staff:
            result = False
            data = ""
            error = "员工信息错误"
            return JsonResponse({"result": result, "data": data, "error": error})
        try:
            staff[0].is_active = is_active
            staff[0].save()
        except ObjectDoesNotExist as e:
            logging.warning(e)
        result = True
        data = ""
        error = "状态更改成功"
        return JsonResponse({"result": result, "data": data, "error": error})


class GuestList(APIView):
    permission_classes = (
        IsAdmin,
    )

    @method_decorator(login_decorator)
    def get(self, request, *args, **kwargs):
        """
            desc:管理员获取所有来宾列表
            :param request:
            :return:返回来宾角色, 来宾用户名(手机号), 来宾姓名, 邀请人, 审核状态
        """
        guest = Guest.objects.filter(user__role=3, audit_status=0)
        guest_se = GuestSerializer(guest, many=True)
        guest_data = guest_se.data
        result = True
        data = guest_data
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})


class GuestAudit(APIView):
    permission_classes = (
        IsAdmin,
    )

    @method_decorator(login_decorator)
    def post(self, request, *args, **kwargs):
        """
        desc: 管理员对来宾信息进行审核
        :param request:
        :return:
        """
        guest_id = request.POST.get("guest_id", "")
        is_audit = request.POST.get("is_audit", "")
        if guest_id == "" or is_audit == "":
            result = False
            data = ""
            error = ""
            return JsonResponse({"result": result, "data": data, "error": error})
        guest = Guest.objects.filter(user_id=guest_id)
        if not guest:
            result = False
            data = ""
            error = "来宾信息错误"
            return JsonResponse({"result": result, "data": data, "error": error})
        try:
            guest[0].audit_status = is_audit
            guest[0].save()
        except ObjectDoesNotExist as e:
            logging.warning(e)
            result = False
            data = ""
            error = "审核失败"
            return JsonResponse({"result": result, "data": data, "error": error})
        result = True
        data = ""
        error = "审核通过"
        return JsonResponse({"result": result, "data": data, "error": error})


class GuestIsAuditList(APIView):
    permission_classes = (
        IsAdmin,
    )

    @method_decorator(login_decorator)
    def get(self, request, *args, **kwargs):
        """
            desc:管理员获取已被审核通过的来宾列表
            :param request:
            :return:返回来宾角色, 来宾用户名(手机号), 来宾姓名, 邀请人, 审核状态
        """
        guest = Guest.objects.filter(user__role=3, audit_status=1)
        guest_se = GuestSerializer(guest, many=True)
        guest_data = guest_se.data
        result = True
        data = guest_data
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})


class GuestActive(APIView):
    permission_classes = (
        IsAdmin,
    )

    @method_decorator(login_decorator)
    def post(self, request, *args, **kwargs):
        """
        desc: 管理员进行员工账号激活、锁定
        :param request:
        :return:
        """
        guest_id = request.POST.get("user_id", "")
        is_active = request.POST.get("is_active", "")
        if guest_id == "" or is_active == "":
            result = False
            data = ""
            error = ""
            return JsonResponse({"result": result, "data": data, "error": error})
        guest = UserInfo.objects.filter(id=guest_id)
        if not guest:
            result = False
            data = ""
            error = "来宾信息错误"
            return JsonResponse({"result": result, "data": data, "error": error})
        try:
            guest[0].is_active = is_active
            guest[0].save()
        except ObjectDoesNotExist as e:
            logging.warning(e)
            result = False
            data = ""
            error = "状态更改失败"
            return JsonResponse({"result": result, "data": data, "error": error})
        result = True
        data = ""
        error = "状态更改成功"
        return JsonResponse({"result": result, "data": data, "error": error})


class AccountInPwdView(APIView):
    # permission_classes = (
    #     IsAdmin,
    # )

    # @method_decorator(login_decorator)
    def put(self, request):
        """
        管理员重置用户密码
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        user_id = request.data.get('user_id')
        if user_id == "":
            result = False
            data = ""
            error = "用户信息不能为空"
            return JsonResponse({"result": result, "data": data, "error": error})
        user = UserInfo.objects.filter(id=user_id)
        if not user:
            result = False
            data = ""
            error = ""
            return JsonResponse({"result": result, "data": data, "error": error})
        re_password = user[0].username[-4:-1]
        try:
            user.update(password=re_password)
        except ObjectDoesNotExist as e:
            logging.warning(e)
            result = False
            data = ""
            error = "密码重置失败"
            return JsonResponse({"result": result, "data": data, "error": error})
        result = True
        data = "密码已重置"
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})








