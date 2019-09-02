# restful API
from rest_framework import permissions
from rest_framework_jwt.utils import jwt_decode_handler

# django
from django.utils.decorators import method_decorator
from django.http import JsonResponse

# self_project
from .models import UserInfo


# 登录装饰器
def login_decorator(func):
    def token_func(request, *args, **kwargs):
        token = request.META.get("HTTP_AUTHORIZATION")
        print("@@",token.split(' ')[2])
        if not token:
            result = False
            data = ""
            error = "身份已经过期，请重新登入"
            return JsonResponse({"result": result, "data": data, "error": error})
        front_token = jwt_decode_handler(token.split(' ')[2])
        user_jwt = UserInfo.objects.filter(user_secret=token.split(' ')[2])
        if not user_jwt:
            result = False
            data = ""
            error = "身份已经过期，请重新登入"
            return JsonResponse({"result": result, "data": data, "error": error})
        else:
            print("@@")
            kwargs['token'] = front_token
            print("###")
            return func(request, *args, **kwargs)

    return token_func


class IsAdminLogin(permissions.BasePermission):

    def has_permission(self, request, view):
        user_name = request.POST.get("user_name", "")
        if user_name == "":
            return False
        user = UserInfo.objects.filter(username=user_name)
        if not user:
            return False
        if user[0].role == 1:
            return True
        else:
            return False


class IsAdmin(permissions.BasePermission):

    @method_decorator(login_decorator)
    def has_permission(self, request, view, *args, **kwargs):
        token = kwargs['token']
        if token['role'] == 1:
            return True
        else:
            return False


class IsStaffGuest(permissions.BasePermission):
    def has_permission(self, request, view):
        user_name = request.POST.get("user_name", "")
        if user_name == "":
            return False
        user = UserInfo.objects.filter(username=user_name)
        if not user:
            return False
        if user[0].role == 2 or user[0].role == 3:
            return True
        else:
            return False


class IsStaff(permissions.BasePermission):

    @method_decorator(login_decorator)
    def has_permission(self, request, view, *args, **kwargs):
        token = kwargs['token']
        if token['role'] == 2:
            return True
        else:
            return False


class IsGuest(permissions.BasePermission):

    @method_decorator(login_decorator)
    def has_permission(self, request, view, *args, **kwargs):
        token = kwargs['token']
        if token['role'] == 3:
            return True
        else:
            return False