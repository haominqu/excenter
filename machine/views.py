# restful API
from rest_framework.views import APIView

# django
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist

from hmmqtt.mqttctlapi import *

# self_project
from .models import *
from .serializers import *
from userinfo.permissions import IsAdmin, login_decorator

# base
import logging

# 保存所有接入的用户地址


# Create your views here.
class Lamp(APIView):

    def get(self, request):
        mac_id = request.GET.get('mac_id')
        mac_st = request.GET.get('mac_st')
        if mac_st == '1':
            LampAPI().lamp_on(mac_id)
        else:
            LampAPI().lamp_off(mac_id)
        return JsonResponse({"code": '', "shuju": '', "msg": 'success'})


class Curtain(APIView):

    def get(self, request):
        mac_id = request.GET.get('mac_id')
        mac_st = request.GET.get('mac_st')
        if mac_st == '1':
            CurtainAPI().curtain_on(mac_id)
        else:
            CurtainAPI().curtain_off(mac_id)
        return JsonResponse({"code": '', "shuju": '', "msg": 'success'})

class Airconditioner(APIView):

    def get(self, request):
        mac_id = request.GET.get('mac_id')
        mac_st = request.GET.get('mac_st')
        if mac_st == '1':
            print("~~~~")
            AirconditionerAPI().air_on(mac_id)
        else:
            AirconditionerAPI().air_off(mac_id)
        return JsonResponse({"code": '', "shuju": '', "msg": 'success'})



class ControllMachineM(APIView):
    """
    desc:可控设备
    """
    @method_decorator(login_decorator)
    def get(self, request, *args, **kwargs):
        """
        desc:可控设备列表
        :param request:触发是可控设备
        :return:
        """
        control_mac = ControlMac.objects.filter(mac__mac_ctype=1)
        print("@@@@", control_mac)
        machine_se = ControlMacSerializer(control_mac, many=True)
        machine_data = machine_se.data
        result = True
        data = machine_data
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})



class ControllMachine(APIView):
    """
    desc:可控设备
    """

    @method_decorator(login_decorator)
    def get(self, request, *args, **kwargs):
        """
        desc:可控设备列表
        :param request:触发是可控设备
        :return:
        """
        control_mac = Machine.objects.filter(mac_ctype=1)
        machine_se = MachineSerializer(control_mac, many=True)
        machine_data = machine_se.data
        result = True
        data = machine_data
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})


class SensorMachine(APIView):
    """
    感应器设备
    """
    permission_classes = (
        IsAdmin,
    )

    @method_decorator(login_decorator)
    def get(self, request, *args, **kwargs):
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


class AlterMachineName(APIView):
    permission_classes = (
        IsAdmin,
    )

    @method_decorator(login_decorator)
    def put(self, request, *args, **kwargs):
        """
        desc: 修改设备名
        :param request:
        :return:
        """
        machine_id = request.data.get('machine_id', '')
        machine_name = request.data.get('machine_name', '')
        if machine_id == '' or machine_name == '':
            result = False
            data = ""
            error = "用户名密码不能为空"
            return JsonResponse({"result": result, "data": data, "error": error})
        mac = Machine.objects.filter(id=machine_id)
        if not mac:
            result = False
            data = ""
            error = "设备不存在"
            return JsonResponse({"result": result, "data": data, "error": error})
        try:
            mac[0].mac_name = machine_name
            mac[0].save()
        except ObjectDoesNotExist as e:
            logging.warning(e)
            result = False
            data = ""
            error = "修改失败"
            return JsonResponse({"result": result, "data": data, "error": error})
        result = True
        data = ""
        error = "修改成功"
        return JsonResponse({"result": result, "data": data, "error": error})


class MachineActive(APIView):
    permission_classes = (
        IsAdmin,
    )

    @method_decorator(login_decorator)
    def post(self, request, *args, **kwargs):
        """
        desc: 管理员对设备激活、停用
        :param request:
        :return:
        """
        machine_id = request.POST.get("machine_id", "")
        is_active = request.POST.get("is_active", "")
        if machine_id == "" or is_active == "":
            result = False
            data = ""
            error = "信息不能为空"
            return JsonResponse({"result": result, "data": data, "error": error})
        machine = Machine.objects.filter(id=machine_id)
        if not machine:
            result = False
            data = ""
            error = "设备信息错误"
            return JsonResponse({"result": result, "data": data, "error": error})
        if int(is_active) == int(1):
            try:
                machine[0].is_active = int(is_active)
                machine[0].status = 1
                machine[0].save()
            except ObjectDoesNotExist as e:
                logging.warning(e)
                result = False
                data = ""
                error = "状态更新错误"
                return JsonResponse({"result": result, "data": data, "error": error})
        elif int(is_active) == int(2):
            try:
                machine[0].is_active = int(is_active)
                machine[0].status = 2
                machine[0].save()
            except ObjectDoesNotExist as e:
                logging.warning(e)
                result = False
                data = ""
                error = "状态更新错误"
                return JsonResponse({"result": result, "data": data, "error": error})
        else:
            result = False
            data = ""
            error = "激活参数错误"
            return JsonResponse({"result": result, "data": data, "error": error})
        result = True
        data = ""
        error = "状态更改成功"
        return JsonResponse({"result": result, "data": data, "error": error})


class MacModeView(APIView):

    def get(self, request):
        mac = MacSetting.objects.first()
        mode = mac.mac_mode
        result = True
        data = mode
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})

    def put(self, request):
        mode = request.data.get("mac_mode", "")
        if mode == "":
            result = False
            data = ""
            error = "信息不能为空"
            return JsonResponse({"result": result, "data": data, "error": error})
        mac = MacSetting.objects.first()
        mac.mac_mode = mode
        mac.save()
        result = True
        data = ""
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})


class M_Data(APIView):

    def get(self, request):
        tem = ControlMac.objects.filter(mac__kind=2)
        sd = ControlMac.objects.filter(mac__kind=3)
        gz = ControlMac.objects.filter(mac__kind=4)
        co = ControlMac.objects.filter(mac__kind=5)
        dl = ControlMac.objects.filter(mac__kind=6)
        pm = ControlMac.objects.filter(mac__kind=7)
        data = {}
        data['tem'] = tem[0].temperature
        data['sd'] = sd[0].temperature
        data['gz'] = gz[0].temperature
        data['co'] = co[0].temperature
        data['dl'] = dl[0].temperature
        data['pm'] = pm[0].temperature
        result = True
        data = data
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})


