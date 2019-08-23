import os, sys
import django

# input mqtt for mqtt server
import paho.mqtt.client as mqtt
# use thread for a lient
from threading import Thread
# from app名 import models
from .mqttmsgapi import ReciveMessage
from machine.models import *
import time
import json

os.environ.setdefault('DJANGO_SETTING_MODULE', 'excenteron.settings')
django.setup()


def on_connect(client, userdata, flag, respons_code):
    if respons_code == 0:
        print('Connection Succeed!')
    else:
        print('Connect Error status {0}'.format(respons_code))
    subscribe('gw/third/#',2)


def on_message(client, userdata, msg):

    # print('@@@@@@@',out)
    # if msg.topic == 'gw/third/#':
    #     print(out)
    ReciveMessage().readmessage(client, userdata, msg)


def publish(hm_topic,hm_payload,hm_status):
    if hm_status == '':
        hm_status=2
    client.publish(hm_topic,hm_payload,hm_status)


def subscribe(hm_topic,hm_qos):
    client.subscribe(hm_topic, qos=2)


def mqttfunction():
    global client
    client.loop_forever(retry_first_connection=True)


# class ReciveMessage:
#     def readmessage(self, client, userdata, message):
#         # message.topic
#         topical = message.topic.split('/')[-1]
#         out = str(message.payload.decode('utf-8'))
#         msg = json.loads(out)
#         mac_mode = MacSetting.objects.all()[0]
#         if topical == "data":
#             # 手动模式
#
#             mac_detail = json.loads(msg['msgContent'])
#             devID = mac_detail['devID']
#             endpointNumber = mac_detail['endpoints'][0]['endpointNumber']
#             attributeValue = mac_detail['endpoints'][0]['clusters'][0]['attributes'][0]['attributeValue']
#
#             mac = Machine.objects.filter(mac_devID=devID)
#             if mac:
#                 ControlMac.objects.filter(mac=mac,endpointnum=endpointNumber).update(mac_status=attributeValue)
#             # if mac_detail['type'] == '19':
#             print(msg)
#         # 自动模式
#
#
#
#         elif topical == "alarm":
#             if mac_mode.mac_mode == 2:
#                 mac_detail = json.loads(msg['msgContent'])
#                 devID = mac_detail['devID']
#                 endpointNumber = mac_detail['endpoints'][0]['endpointNumber']
#                 attributeValue = mac_detail['endpoints'][0]['clusters'][0]['attributes'][0]['attributeValue']
#                 mac = Machine.objects.filter(mac_devID=devID)
#                 if mac:
#                     ControlMac.objects.filter(mac=mac, endpointnum=endpointNumber).update(mac_status=attributeValue)
#                 # if mac_detail['type'] == '62':
#             elif mac_mode.mac_mode == 1:
#                 mac_detail = json.loads(msg['msgContent'])
#                 devID = mac_detail['devID']
#                 endpointNumber = mac_detail['endpoints'][0]['endpointNumber']
#                 attributeValue = mac_detail['endpoints'][0]['clusters'][0]['attributes'][0]['attributeValue']
#                 macv = Machine.objects.filter(mac_devID=devID)
#                 if macv.mac_ctype == 1:
#                     macs = ControlMac.objects.filter(mac_scene=macv.scene,mac_mac_ctype=1)
#                     if attributeValue == 1:
#                         macs.update(mac_status=1)
#                         for m in macs:
#                             LampAPI.lamp_on(m.mac.id)
#                         # publish(hm_topic,hm_payload,hm_status)

#
# class LampAPI:
#
#     def __hm_temp(self, gwID, devID, endpointNumber, commandId):
#         template = {"timestamp": "", "msgContent": "{\"cmd\": \"501\",\"gwID\": \""+gwID+"\",\"devID\": \""+devID+"\",\"clusterId\": 6,\"commandType\": 1,\"endpointNumber\": "+str(endpointNumber)+",\"commandId\": "+str(commandId)+"}"}
#         template = json.dumps(template)
#         return template
#
#     def __res_url(self,gwID):
#         url = 'gw/third/'+gwID+'/req'
#         return url
#
#     def lamp_on(self, mac_id):
#         machine = Machine.objects.filter(id=mac_id)[0]
#         gw_gwID = machine.gate.gw_gwID
#         payload = self.__hm_temp(gw_gwID, machine.mac_devID,machine.controlmac.endpointnum, 1)
#         api_url = self.__res_url(gw_gwID)
#         publish(api_url,payload, 2)
#         return True
#
#     def lamp_off(self, mac_id):
#         machine = Machine.objects.filter(id=mac_id)[0]
#         gw_gwID = machine.gate.gw_gwID
#         payload = self.__hm_temp(gw_gwID, machine.mac_devID,machine.controlmac.endpointnum, 0)
#         api_url = self.__res_url(gw_gwID)
#         publish(api_url, payload, 2)
#         return True
#
#
#
#



client = mqtt.Client(client_id="mqtt_hm", clean_session=False)


def mqtt_run():
    client.on_connect = on_connect
    client.on_message = on_message
    broker = '127.0.0.1'
    client.connect(broker, 1883, 62)
    client.username_pw_set('user', 'user')
    client.reconnect_delay_set(min_delay=1, max_delay=2000)
    mqttthread = Thread(target=mqttfunction)
    mqttthread.start()

# mqtt_run()
# if __name__ == "__main__":
#     mqtt_run()
#     time.sleep(10)
#     publish('hello world')
#     time.sleep(10)
#     publish('hello qhm')
