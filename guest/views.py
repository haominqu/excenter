# restful API
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings

# django
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist

# self_project
from userinfo.models import UserInfo
from userinfo.serializers import GuestSerializer

# base
import logging


# Create your views here.


class GuestInfo(APIView):

    """
        desc: 个人信息管理模块
    """

    def get(self, request, **kwargs):
        """
        desc:个人账户查看
        :param request:
        :return:
        """
        token = kwargs['token']
        user_id = token['user_id']
        user = UserInfo.objects.filter(id=user_id)
        if not user:
            result = False
            data = ""
            error = "未查询到用户"
            return JsonResponse({"result": result, "data": data, "error": error})
        user_se = GuestSerializer(user, many=False)
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
        try:
            UserInfo.objects.filter(id=user_id).update(password=new_pwd)
        except ObjectDoesNotExist as e:
            logging.warning(e)
            result = False
            data = ""
            error = "密码修改失败"
            return JsonResponse({"result": result, "data": data, "error": error})
        result = True
        data = "密码已修改"
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})
