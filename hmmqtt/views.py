from django.http import HttpResponse

from .mqttbase import *

from machine.models import *
import json
# Create your views here.


class LampAPI:

    def lamp_on(self, mac_id):
        machine = Machine.objects.filter(id=mac_id)[0]
        gw_gwID = machine.gate.gw_gwID
        payload = {"timestamp": "","msgContent": "{\"cmd\": \"501\",\"gwID\": \""+gw_gwID+"\",\"devID\": \""+machine.mac_devID+"\",\"clusterId\": 6,\"commandType\": 1,\"endpointNumber\": 2,\"commandId\": 1}"}
        publish('gw/third/'+gw_gwID+'/req',json.dumps(payload), 2)
        return True

    def lamp_off(self, mac_id):
        a = {"timestamp": "","msgContent": "{\"cmd\": \"501\",\"gwID\": \"ME01121EB23\",\"devID\": \"B85B6002004B1200\",\"clusterId\": 6,\"commandType\": 1,\"endpointNumber\": 2,\"commandId\": 0}"}
        publish('gw/third/ME01121EB23/req',json.dumps(a), 2)
        return True


class CurtainAPI:

    def curtain_on(self,mac_id):
        machine = Machine.objects.filter(id=mac_id)[0]
        gw_gwID = machine.gate.gw_gwID
        payload = {"timestamp": "","msgContent": "{\"cmd\": \"501\",\"gwID\": \"" + gw_gwID + "\",\"devID\": \"" + machine.mac_devID + "\",\"clusterId\": 258,\"commandType\": 1,\"endpointNumber\": 2,\"commandId\": 1}"}
        publish('gw/third/' + gw_gwID + '/req', json.dumps(payload), 2)
        return True

    def curtain_off(self):
        return True


class AirconditionerAPI:

    def air_on(self):
        return True

    def air_off(self):
        return True
