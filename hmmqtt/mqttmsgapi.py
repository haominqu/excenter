from django.http import HttpResponse

from machine.models import *
import hmmqtt
import json
# Create your views here.


class ReciveMessage:

    def readmessage(self, client, userdata, message):
        # message.topic
        topical = message.topic.split('/')[-1]
        out = str(message.payload.decode('utf-8'))
        msg = json.loads(out)
        mac_mode = MacSetting.objects.all()[0]
        if topical == "data":
            # 手动模式
            if mac_mode.mac_mode == 2:
                mac_detail = json.loads(msg['msgContent'])
                devID = mac_detail['devID']
                endpointNumber = mac_detail['endpoints'][0]['endpointNumber']
                attributeValue = mac_detail['endpoints'][0]['clusters'][0]['attributes'][0]['attributeValue']
                mac = Machine.objects.filter(mac_devID=devID)
                if mac:
                    ControlMac.objects.filter(mac=mac,endpointnum=endpointNumber).update(mac_status=attributeValue)
                # if mac_detail['type'] == '19':
                # print(msg)
            # 自动模式
            elif mac_mode.mac_mode == 1:
                # 更新数据
                mac_detail = json.loads(msg['msgContent'])
                devID = mac_detail['devID']
                endpointNumber = mac_detail['endpoints'][0]['endpointNumber']
                attributeValue = mac_detail['endpoints'][0]['clusters'][0]['attributes'][0]['attributeValue']
                mac = Machine.objects.filter(mac_devID=devID,mac_ctype=0)
                if mac:
                    ControlMac.objects.filter(mac_id=mac[0].id, endpointnum=endpointNumber).update(mac_status=attributeValue)

        elif topical == "alarm":

            if mac_mode.mac_mode == 2:
                mac_detail = json.loads(msg['msgContent'])
                devID = mac_detail['devID']
                endpointNumber = mac_detail['endpoints'][0]['endpointNumber']
                attributeValue = mac_detail['endpoints'][0]['clusters'][0]['attributes'][0]['attributeValue']
                mac = Machine.objects.filter(mac_devID=devID)
                if mac:
                    ControlMac.objects.filter(mac=mac, endpointnum=endpointNumber).update(mac_status=attributeValue)
                # if mac_detail['type'] == '62':
                # 判断自动手动
            elif mac_mode.mac_mode == 1:
                mac_detail = json.loads(msg['msgContent'])
                devID = mac_detail['devID']
                endpointNumber = mac_detail['endpoints'][0]['endpointNumber']
                attributeValue = mac_detail['endpoints'][0]['clusters'][0]['attributes'][0]['attributeValue']
                # 获取当前触发设备
                macv = Machine.objects.filter(mac_devID=devID)
                # 判断设备是否为触发mac_ctype 0感应设备，1触发设备
                if macv[0].mac_ctype == 0:
                    macs = ControlMac.objects.filter(mac__scene=macv[0].scene, mac__mac_ctype=1)
                    if attributeValue == '0':
                        # 修改触发设备状态
                        n = ControlMac.objects.filter(mac_id=macv[0].id)
                        n.update(mac_status=1)
                        macs.update(mac_status=1)
                        for m in macs:
                            hmmqtt.mqttctlapi.LampAPI().lamp_on(m.mac.id)
                    else:
                        # 次感应器状态回复
                        ControlMac.objects.filter(mac_id=macv[0].id).update(mac_status=0)
                        # 查看其他感应器
                        n_mac = ControlMac.objects.filter(mac__scene=macv[0].scene, mac__mac_ctype=0, mac_status=1)
                        print(len(n_mac))
                        if not n_mac:
                            macs.update(mac_status=0)
                            for m in macs:
                                print('@@', m.mac.id)
                                hmmqtt.mqttctlapi.LampAPI().lamp_off(m.mac.id)

        return True