from rest_framework.views import APIView

from django.http import JsonResponse

from hmmqtt.mqttctlapi import *

from .models import *
from .serializers import *

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


class ControllMachine(APIView):
    """
    desc:可控设备
    """

    def get(self, request):
        """
        desc:可控设备列表
        :param request:触发是可控设备
        :return:
        """
        control_mac = ControlMac.objects.filter(mac__mac_ctype=1)
        print(control_mac)
        machine_se = ControlMacSerializer(control_mac, many=True)
        machine_data = machine_se.data
        result = True
        data = machine_data
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})


class SensorMachine(APIView):
    """
    感应器设备
    """

    def get(self, request):
        """
        desc:感应器设备列表
        :param request:数据是感应器设备
        :return:
        """
        machine = Machine.objects.filter(mac_ctype=2)
        machine_se = MachineSerializer(machine, many=True)
        machine_data = machine_se.data
        result = True
        data = machine_data
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})
