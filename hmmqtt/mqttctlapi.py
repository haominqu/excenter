from django.http import HttpResponse

from .mqttbase import mqtt_run, publish

from machine.models import *
import json
# Create your views here.


class LampAPI:

    def __hm_temp(self, gwID, devID, endpointNumber, commandId):
        template = {"timestamp": "", "msgContent": "{\"cmd\": \"501\",\"gwID\": \""+gwID+"\",\"devID\": \""+devID+"\",\"clusterId\": 6,\"commandType\": 1,\"endpointNumber\": "+str(endpointNumber)+",\"commandId\": "+str(commandId)+"}"}
        template = json.dumps(template)
        return template

    def __res_url(self,gwID):
        url = 'gw/third/'+gwID+'/req'
        return url

    def lamp_on(self, mac_id):
        machine = Machine.objects.filter(id=mac_id)[0]
        gw_gwID = machine.gate.gw_gwID
        payload = self.__hm_temp(gw_gwID, machine.mac_devID,machine.controlmac.endpointnum, 1)
        api_url = self.__res_url(gw_gwID)
        publish(api_url,payload, 2)
        return True

    def lamp_off(self, mac_id):
        machine = Machine.objects.filter(id=mac_id)[0]
        gw_gwID = machine.gate.gw_gwID
        payload = self.__hm_temp(gw_gwID, machine.mac_devID,machine.controlmac.endpointnum, 0)
        api_url = self.__res_url(gw_gwID)
        publish(api_url, payload, 2)
        return True


class CurtainAPI:

    def __hm_temp(self, gwID, devID, endpointNumber, commandId):
        template = {"timestamp": "", "msgContent": "{\"cmd\": \"501\",\"gwID\": \""+gwID+"\",\"devID\": \""+devID+"\",\"clusterId\": 258,\"commandType\": 1,\"endpointNumber\": "+str(endpointNumber)+",\"commandId\": "+str(commandId)+"}"}
        template = json.dumps(template)
        return template

    def __res_url(self,gwID):
        url = 'gw/third/'+gwID+'/req'
        return url

    def curtain_on(self, mac_id):
        machine = Machine.objects.filter(id=mac_id)[0]
        gw_gwID = machine.gate.gw_gwID
        payload = self.__hm_temp(gw_gwID, machine.mac_devID, machine.controlmac.endpointnum, 0)
        api_url = self.__res_url(gw_gwID)
        publish(api_url, payload, 2)
        return True

    def curtain_off(self, mac_id):
        machine = Machine.objects.filter(id=mac_id)[0]
        gw_gwID = machine.gate.gw_gwID
        payload = self.__hm_temp(gw_gwID, machine.mac_devID, machine.controlmac.endpointnum, 1)
        api_url = self.__res_url(gw_gwID)
        publish(api_url, payload, 2)
        return True

    def curtain_stop(self, mac_id):
        machine = Machine.objects.filter(id=mac_id)[0]
        gw_gwID = machine.gate.gw_gwID
        payload = self.__hm_temp(gw_gwID, machine.mac_devID, machine.controlmac.endpointnum, 2)
        api_url = self.__res_url(gw_gwID)
        publish(api_url, payload, 2)
        return True


class AirconditionerAPI:

    def air_on(self):
        return True

    def air_off(self):
        return True


class ReciveMessage:

    def readmessage(self, client, message):
        return True