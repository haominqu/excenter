# restful API
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings

# django
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from django.utils.decorators import method_decorator

# selfproject
from userinfo.models import *
from .permissions import *
from .serializers import *
from userinfo.permissions import *

# base
import logging

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