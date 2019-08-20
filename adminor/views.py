# restful API
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings

# django
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

# self_project
from userinfo.models import UserInfo, Guest, UserDetail
from django.contrib.auth.hashers import check_password
from userinfo.serializers import GuestSerializer, StaffSerializer, UserSerializer

# base
import logging

# Create your views here.

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
        if user:
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user[0])
            payload['role'] = user[0].role
            token = jwt_encode_handler(payload)
            user[0].user_secret = token
            user.save()
            result = True
            data = token
            error = ""
            return JsonResponse({"result": result, "data": data, "error": error})


class AdminView(APIView):
    """管理员对于人员的管理"""

    def post(self, request):
        """
        管理员进行添加员工:包括手机号, 姓名, 员工编号, 职位, 所属部门, 人脸
        密码默认手机号后4位,
        员工默认状态未激活
        :param request:
        :return:
        """
        user_name = request.POST.get("user_name", "")  # 手机号
        real_name = request.POST.get("real_name", "")
        start_code = request.POST.get("start_code", "")
        position = request.POST.get("position", "")
        department = request.POST.get("department", "")
        face_picture = request.FILES.get('face_picture', '')
        if user_name == "" or real_name == "" or start_code == "" or position == "" or department == "" or face_picture == "":
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
        user_info.password = user_name[-4: -1]
        user_info.role = 2
        user_detail = UserDetail()
        user_detail.user = user_info
        user_detail.realname = real_name
        user_detail.start_code = start_code
        user_detail.position = position
        user_detail.department = department
        user_detail.face_picture = face_picture
        try:
            user_info.save()
            user_detail.save()
        except ObjectDoesNotExist as e:
            logging.error(e)
            result = False
            data = ""
            error = "添加失败"
            return JsonResponse({"result": result, "data": data, "error": error})
        result = True
        data = ""
        error = "添加成功"
        return JsonResponse({"result": result, "data": data, "error": error})

    def put(self, request):
        """
        管理员重置用户密码
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        user_id = request.data.get('user_id')
        new_pwd = request.data.get('new_pwd')
        if user_id == "" or new_pwd == "":
            result = False
            data = ""
            error = "用户信息不能为空"
            return JsonResponse({"result": result, "data": data, "error": error})
        try:
            UserInfo.objects.filter(id=user_id).update(password=new_pwd)
        except ObjectDoesNotExist as e:
            logging.warning(e)
            result = False
            data = ""
            error = "密码修改失败"
            return JsonResponse({"result": result, "data": data, "error": error})
        result = True
        data = "密码已重置"
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})


class GuestList(APIView):

    def get(self, request):
        """
            desc:管理员获取所有来宾列表
            :param request:
            :return:返回来宾角色, 来宾用户名(手机号), 来宾姓名, 邀请人, 审核状态
        """
        guest = Guest.objects.filter(user__role=3)
        guest_se = GuestSerializer(guest, many=True)
        guest_data = guest_se.data
        result = True
        data = guest_data
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})


class StaffList(APIView):

    def get(self, request):
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

    def put(self, request):
        """
        desc: 管理员进行员工账号激活、停用
        :param request:
        :return:
        """
        staff_id = request.data.get("staff_id", "")
        is_active = request.data.get("is_active", "")
        staff = UserInfo.objects.filter(id=staff_id)
        if not staff:
            result = False
            data = ""
            error = "员工信息错误"
            return JsonResponse({"result": result, "data": data, "error": error})
        try:
            staff[0].is_active = is_active
            staff.save()
        except ObjectDoesNotExist as e:
            logging.warning(e)
        result = True
        data = ""
        error = "状态更改成功"
        return JsonResponse({"result": result, "data": data, "error": error})


class AdminInfo(APIView):

    def get(self, request, **kwargs):
        """
        desc:管理员个人信息
        :param request:
        :return:
        """
        token = kwargs['token']
        admin_id = token['user_id']
        admin = UserInfo.objects.filter(id=admin_id)
        if not admin:
            result = False
            data = ""
            error = ""
            return JsonResponse({"result": result, "data": data, "error": error})
        admin_se = UserSerializer(admin, many=False)
        admin_data = admin_se.data
        result = False
        data = admin_data
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})


