# restful API
from rest_framework import permissions
from rest_framework_jwt.utils import jwt_decode_handler

# django
from django.utils.decorators import method_decorator
from django.http import JsonResponse

# selfproject



# 登录装饰器
def login_decorator(func):
    def token_func(request, *args, **kwargs):
        if not request.META.get("HTTP_AUTHORIZATION"):
            result = False
            data = ""
            error = "token无效"
            return JsonResponse({"result": result, "data": data, "error": error})
        token = request.META.get("HTTP_AUTHORIZATION").split(' ')
        kwargs['token'] = jwt_decode_handler(token[2])
        return func(request, *args, **kwargs)
    return token_func


class IsAdmin(permissions.BasePermission):

    @method_decorator(login_decorator)
    def has_permission(self, request, view, *args, **kwargs):
        token = kwargs['token']
        if token['role'] == 1:
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