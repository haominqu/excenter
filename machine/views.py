from rest_framework.views import APIView

from django.http import JsonResponse

from hmmqtt.mqttctlapi import *

# 保存所有接入的用户地址


# Create your views here.
class Lamp(APIView):

    def get(self, request):
        al = request.GET.get('al')
        print(al)
        if al == '1':
            LampAPI().lamp_on(1)
        else:
            LampAPI().lamp_off(1)
        return JsonResponse({"code": '', "shuju": '', "msg": 'msg'})



