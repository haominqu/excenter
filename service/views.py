# restful API
from rest_framework.views import APIView

# django
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

# self_project
from .models import DhuiFace

# base
import logging

# Create your views here.


# 达辉人脸http api
class DhuiView(APIView):

    def post(self, request):
        action = request.POST.get("action", "")
        faceid = request.POST.get("faceid", "")
        base64 = request.POST.get("base64", "")
        print(base64)
        if action == "" or faceid == "" or base64 == "":
            result = False
            data = ""
            error = ""
            return JsonResponse({"result": result, "data": data, "error": error})
        # try:
        #     DhuiFace.objects.create(action=action, faceid=faceid, base64=base64)
        # except ObjectDoesNotExist as e:
        #     logging.warning(e)
        #     result = False
        #     data = ""
        #     error = ""
        #     return JsonResponse({"result": result, "data": data, "error": error})
        status = 0
        msg = "人脸注册成功"
        return JsonResponse({"status": status, "msg": msg})

