from django.http import HttpResponse

from machine.models import *
import hmmqtt
import json
from userinfo.views import *
# Create your views here.
import time
a={}
b={}
b["32DCD418004B1200"]=123
i=0
class ReciveMessage:

    def ac(self,arg,argc,argsql):

        if argc in b.keys():

            if a[argc] != b[argc]:
                b[argc] = a[argc]
            else:
                argsql.update(mac_status=0)
                for m in arg:
                    hmmqtt.mqttctlapi.LampAPI().lamp_off(m.mac.id)
        else:
            b[argc] = 123

    def readmessage(self, client, userdata, message):
        # message.topic

        topical = message.topic.split('/')[-1]
        out = str(message.payload.decode('utf-8'))
        msg = json.loads(out)
        print(topical)
        print(msg)
        mac_mode = MacSetting.objects.all()[0]
        if topical == "data":
            # 手动模式
            if mac_mode.mac_mode == 2:
                print("&&&&!!!!!!!!!!!!!!!!!!!!!!!")
                mac_detail = json.loads(msg['msgContent'])
                devID = mac_detail['devID']
                thire_type = mac_detail['type']
                print(thire_type)
                if thire_type == "17":
                    endpointNumber2 = mac_detail['endpoints'][1]['endpointNumber']
                    attributeValue2 = mac_detail['endpoints'][1]['clusters'][0]['attributes'][0]['attributeValue']
                    mac2 = Machine.objects.filter(mac_devID=devID)

                    if mac2:
                        now_mc2 = ControlMac.objects.filter(mac=mac2[1], endpointnum=endpointNumber2)
                        print(len(now_mc2))
                        print(attributeValue2)
                        now_mc2.update(temperature=attributeValue2)
                    # if mac_detail['type'] == '19':
                    backdatat = {}
                    backdatat["mac_id"] = now_mc2[0].mac.id
                    backdatat["mac_sty"] = now_mc2[0].mac.mac_type
                    backdatat['mac_st'] = now_mc2[0].temperature
                    backdatat['mac_kind'] = "hu"
                    backdatat['mac_type'] = '2'
                    print(backdatat["mac_sty"])
                    print("%%%%")
                    send_web_msg('', "$$$$")
                    send_web_msg('', str(backdatat).replace('\'', '\"'))

                    endpointNumber = mac_detail['endpoints'][0]['endpointNumber']
                    attributeValue = mac_detail['endpoints'][0]['clusters'][0]['attributes'][0]['attributeValue']
                    mac = Machine.objects.filter(mac_devID=devID)
                    if mac:

                        now_mc = ControlMac.objects.filter(mac=mac[0],endpointnum=endpointNumber)
                        now_mc.update(temperature=attributeValue)
                    # if mac_detail['type'] == '19':
                    backdata = {}
                    backdata["mac_id"] = now_mc[0].mac.id
                    backdata["mac_sty"] = now_mc[0].mac.mac_type
                    backdata['mac_st'] = now_mc[0].temperature
                    backdata['mac_kind'] = now_mc[0].mac.kind
                    backdata['mac_type'] = '2'
                    print("@@@@@@###$$")
                    send_web_msg('', str(backdata).replace('\'', '\"'))

                if thire_type=="44":
                    endpointNumber = mac_detail['endpoints'][0]['endpointNumber']
                    attributeValue = mac_detail['endpoints'][0]['clusters'][0]['attributes'][0]['attributeValue']
                    mac = Machine.objects.filter(mac_devID=devID)
                    if mac:
                        now_mc = ControlMac.objects.filter(mac=mac[0], endpointnum=endpointNumber)
                        now_mc.update(temperature=attributeValue)
                    # if mac_detail['type'] == '19':
                    backdata = {}
                    backdata["mac_id"] = now_mc[0].mac.id
                    backdata["mac_sty"] = now_mc[0].mac.mac_type
                    backdata['mac_st'] = now_mc[0].temperature
                    backdata['mac_kind'] = now_mc[0].mac.kind
                    backdata['mac_type'] = '2'
                    print("@@@@@@###$$")
                    send_web_msg('', str(backdata).replace('\'', '\"'))

                if thire_type=="42":
                    endpointNumber = mac_detail['endpoints'][0]['endpointNumber']
                    attributeValue = mac_detail['endpoints'][0]['clusters'][0]['attributes'][0]['attributeValue']
                    mac = Machine.objects.filter(mac_devID=devID)
                    if mac:
                        now_mc = ControlMac.objects.filter(mac=mac[0], endpointnum=endpointNumber)
                        now_mc.update(temperature=attributeValue)
                    # if mac_detail['type'] == '19':
                    backdata = {}
                    backdata["mac_id"] = now_mc[0].mac.id
                    backdata["mac_sty"] = now_mc[0].mac.mac_type
                    backdata['mac_st'] = now_mc[0].temperature
                    backdata['mac_kind'] = now_mc[0].mac.kind
                    backdata['mac_type'] = '2'
                    print("@@@@@@###$$")
                    send_web_msg('', str(backdata).replace('\'', '\"'))

                if thire_type=="Ai":
                    endpointNumber = mac_detail['endpoints'][0]['endpointNumber']
                    attributeValue = mac_detail['endpoints'][0]['clusters'][1]['attributes'][0]['attributeValue']
                    mac = Machine.objects.filter(mac_devID=devID)
                    print("###########")
                    print(attributeValue)
                    # aaaayyyyyyzzzzzzcc
                    # 当前电流
                    print(int(attributeValue[0:4],16)*100)
                    # 当前功率
                    print(int(attributeValue[4:10],16)*100)
                    # 当前的累计电量
                    print(int(attributeValue[10:16],16))
                    if mac:
                        now_mc = ControlMac.objects.filter(mac=mac[0], endpointnum=endpointNumber)
                        now_mc.update(temperature=str(int(attributeValue[4:10],16)*100))
                    # if mac_detail['type'] == '19':
                    backdata = {}
                    backdata["mac_id"] = now_mc[0].mac.id
                    backdata["mac_sty"] = now_mc[0].mac.mac_type
                    backdata['mac_st'] = now_mc[0].temperature
                    backdata['mac_kind'] = now_mc[0].mac.kind
                    backdata['mac_type'] = '2'
                    print("@@@@@@###$$")
                    send_web_msg('', str(backdata).replace('\'', '\"'))



                endpointNumber = mac_detail['endpoints'][0]['endpointNumber']
                attributeValue = mac_detail['endpoints'][0]['clusters'][0]['attributes'][0]['attributeValue']
                mac = Machine.objects.filter(mac_devID=devID)
                if mac:
                    now_mc = ControlMac.objects.filter(mac=mac,endpointnum=endpointNumber)
                    now_mc.update(mac_status=attributeValue)
                # if mac_detail['type'] == '19':
                backdata = {}
                backdata["mac_id"] = now_mc[0].mac.id
                backdata["mac_sty"] = now_mc[0].mac.mac_type
                backdata['mac_st'] = now_mc[0].mac_status
                backdata['mac_kind'] = now_mc[0].mac.kind
                backdata['mac_type'] = '2'
                print("@@@@@@###$$")
                send_web_msg('', str(backdata).replace('\'', '\"'))

            # 自动模式
            elif mac_mode.mac_mode == 1:
                # 更新数据
                mac_detail = json.loads(msg['msgContent'])
                devID = mac_detail['devID']
                endpointNumber = mac_detail['endpoints'][0]['endpointNumber']
                attributeValue = mac_detail['endpoints'][0]['clusters'][0]['attributes'][0]['attributeValue']
                macv = Machine.objects.filter(mac_devID=devID)
                if macv:
                    now_mc = ControlMac.objects.filter(mac=macv,endpointnum=endpointNumber)
                    now_mc.update(mac_status=attributeValue)
                backdata = {}
                backdata["mac_id"] = now_mc[0].mac.id
                backdata["mac_sty"] = now_mc[0].mac.mac_type
                backdata['mac_st'] = now_mc[0].mac_status
                backdata['mac_kind'] = now_mc[0].mac.kind
                backdata['mac_type'] = '2'
                print("$%^&*",str(backdata))
                send_web_msg('', str(backdata).replace('\'', '\"'))
                if macv[0].mac_ctype == 0:
                    macs = ControlMac.objects.filter(mac__scene=macv[0].scene, mac__mac_ctype=1)

                    if attributeValue == '1':
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

                        if not n_mac:


                            # if a['aa'] != b['aa']:
                            #     print("*****cs")
                            #     b['aa'] = a['aa']
                            # *******************************
                            # auto close
                            from threading import Timer
                            # t = Timer(10, self.ac,[macs,devID,macs])
                            # t.start()
                            # ***********************************
                            # else:
                            #     for m in macs:
                            #         hmmqtt.mqttctlapi.LampAPI().lamp_off(m.mac.id)
                            #     print("*****")

                            # print("$$$$$$$$$$$$$$$", a['aa'])
                            # print("$$$$$$$$$$$$$$$", b['aa'])


                            # for m in macs:
                            #     hmmqtt.mqttctlapi.LampAPI().lamp_off(m.mac.id)
        elif topical == "alarm":
            print("###$%^^^",mac_mode.mac_mode)
            if mac_mode.mac_mode == 2:

                mac_detail = json.loads(msg['msgContent'])
                devID = mac_detail['devID']

                endpointNumber = mac_detail['endpoints'][0]['endpointNumber']
                attributeValue = mac_detail['endpoints'][0]['clusters'][0]['attributes'][0]['attributeValue']
                mac = Machine.objects.filter(mac_devID=devID)
                if mac:
                    now_mc = ControlMac.objects.filter(mac__mac_devID=devID, endpointnum=endpointNumber)
                    now_mc.update(mac_status=attributeValue)
                # 返回数据到前端
                backdata = {}
                backdata["mac_id"]=now_mc[0].mac.id
                backdata['mac_st']=now_mc[0].mac_status
                backdata['mac_type']='1'

                send_web_msg('',str(backdata).replace('\'','\"'))

                # if mac_detail['type'] == '62':
                # 判断自动手动
            elif mac_mode.mac_mode == 1:
                print("!!!!2")
                mac_detail = json.loads(msg['msgContent'])
                devID = mac_detail['devID']
                endpointNumber = mac_detail['endpoints'][0]['endpointNumber']
                attributeValue = mac_detail['endpoints'][0]['clusters'][0]['attributes'][0]['attributeValue']
                # 获取当前触发设备
                macv = Machine.objects.filter(mac_devID=devID)
                # 判断设备是否为触发mac_ctype 0感应设备，1触发设备
                if macv[0].mac_ctype == 0:
                    macs = ControlMac.objects.filter(mac__scene=macv[0].scene, mac__mac_ctype=1)
                    if attributeValue == '1':
                        # 修改触发设备状态
                        n = ControlMac.objects.filter(mac_id=macv[0].id)

                        n.update(mac_status=1)
                        macs.update(mac_status=1)
                        for m in macs:
                            print(m.mac.mac_type)
                            if m.mac.mac_type=="62":
                                hmmqtt.mqttctlapi.LampAPI().lamp_on(m.mac.id)
                            elif m.mac.mac_type=="Ar":
                                hmmqtt.mqttctlapi.CurtainAPI().curtain_on(m.mac.id)
                            elif m.mac.mac_type == "Af":
                                hmmqtt.mqttctlapi.AirconditionerAPI().air_on(m.mac.id)

                            a[devID]=msg['timestamp']
                    else:
                        # print("@@@@@@@@@@@@!!!!!!!!!")
                        # 次感应器状态回复
                        ControlMac.objects.filter(mac_id=macv[0].id).update(mac_status=0)
                        # 查看其他感应器
                        n_mac = ControlMac.objects.filter(mac__scene=macv[0].scene, mac__mac_ctype=0, mac_status=1)
                        print("@@@@@@@@@@@@@@$$$$$$$$$$$$$")
                        if not n_mac:
                            macs.update(mac_status=0)
                            for m in macs:
                                # print('@@', m.mac.id)
                                hmmqtt.mqttctlapi.LampAPI().lamp_off(m.mac.id)

        return True