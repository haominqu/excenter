# restful API
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings


# django
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import check_password, make_password
from django.http import JsonResponse
from django.utils.decorators import method_decorator

# websocket
from dwebsocket.decorators import accept_websocket
from collections import defaultdict


# selfproject
from .serializers import *
from .permissions import *

from .models import *

# base
import logging
import json

# Create your views here.


# 保存所有接入的用户地址
allconn = defaultdict(list)


def send_web_msg(user_id,msg):
    for i in allconn:
        if i != user_id:
            allconn[i].send(msg)
    return True

@accept_websocket
def build_socket(request, user_id):
    print("%%%%%%%%")
    """初始化时建立websocket连接, 保存所有连接"""
    allresult = {}
    # 获取用户信息
    userinfo = request.user
    allresult['userinfo'] = userinfo
    # 声明全局变量
    global allconn
    # 判断是不是websocket连接
    if request.is_websocket():
        # 将链接(请求？)存入全局字典中
        allconn[str(user_id)] = request.websocket
        for message in request.websocket:
            if message == "1111":
                # 将信息发至自己的聊天框
                # request.websocket.send(message)
                # 将信息发至其他所有用户的聊天框
                send_socket(message)
            elif message == 'quit':
                request.websocket.close()
                allconn.remove(request.websocket)


def send_socket(message):
    for i in allconn:
        allconn[i].send(message)
    return True




class StaffGuestLogin(APIView):
    permission_classes = (
        IsStaffGuest,
    )

    def post(self, request):
        """
        desc: 手机端登录
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
            user[0].is_login = True
            user[0].save()
            if user[0].role == int(2):
                staff = UserDetail.objects.filter(user_id=user[0].id)
                real_name = staff[0].realname
                position = staff[0].position
                department = staff[0].department
            elif user[0].role == int(3):
                guest = Guest.objects.filter(user_id=user[0].id)
                real_name = guest[0].realname
                position = guest[0].position
                department = guest[0].department
            data = dict()
            data['token'] = token
            data['role_name'] = real_name
            data['position'] = position
            data['department'] = department
            result = True
            data = data
            error = ""
            return JsonResponse({"result": result, "data": data, "error": error})


class StaffGuestLogout(APIView):

    permission_classes = (
        IsStaff,
        IsGuest,
    )

    def post(self, requset, **kwargs):
        """
        desc:手机端注销, token过期, 断开websocket
        :param requset:
        :return:
        """
        token = kwargs['token']
        user = UserInfo.objects.filter(id=token['user_id'])
        user[0].user_secret = uuid4()
        user[0].is_login = False
        user[0].save()
        result = True
        data = uuid4()
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})


class UserAlterPwd(APIView):
    def put(self, request):
        user_id = request.data.get('user_id', '')
        old_pwd = request.data.get('old_pwd', '')
        new_pwd = request.data.get('new_pwd', '')
        c_pwd = request.data.get('c_pwd', '')
        if user_id == "" or old_pwd == "" or new_pwd == "" or c_pwd == "":
            result = False
            data = ""
            error = "用户名密码不能为空"
            return JsonResponse({"result": result, "data": data, "error": error})
        user = UserInfo.objects.filter(id=user_id)
        if not user:
            result = False
            data = ""
            error = ""
            return JsonResponse({"result": result, "data": data, "error": error})
        is_pwd = check_password(old_pwd, user[0].password)
        if not is_pwd:
            result = False
            data = ""
            error = "密码错误"
            return JsonResponse({"result": result, "data": data, "error": error})
        if old_pwd != c_pwd:
            result = False
            data = ""
            error = "两次密码不一致"
            return JsonResponse({"result": result, "data": data, "error": error})
        new_pwd = make_password(new_pwd, None, 'pbkdf2_sha256')
        try:
            user[0].update(password=new_pwd)
        except ObjectDoesNotExist as e:
            logging.warning(e)
            result = False
            data = ""
            error = "密码修改失败"
            return JsonResponse({"result": result, "data": data, "error": error})
        result = True
        data = ""
        error = "密码修改成功"
        return JsonResponse({"result": result, "data": data, "error": error})














