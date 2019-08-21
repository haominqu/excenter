from rest_framework.views import APIView

from django.http import JsonResponse

from hmmqtt.mqttctlapi import *

# 保存所有接入的用户地址


# Create your views here.
class Lamp(APIView):

    def get(self, request):
        mac_id = request.GET.get('mac_id')
        if mac_id == '1':
            LampAPI().lamp_on(mac_id)
        else:
            LampAPI().lamp_off(mac_id)
        return JsonResponse({"code": '', "shuju": '', "msg": 'msg'})



