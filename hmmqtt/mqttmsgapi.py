from django.http import HttpResponse

from machine.models import *
import hmmqtt
import json
from userinfo.views import *
from history import sethistory
# Create your views here.
import time
import datetime
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
                    print(mac2[0])
                    if mac2:
                        now_mc2 = ControlMac.objects.filter(mac=mac2[0], endpointnum=endpointNumber2)
                        print(endpointNumber2)
                        print(attributeValue2)
                        now_mc2.update(temperature=attributeValue2)
                    # if mac_detail['type'] == '19':
                    # temNo"感应器id"
                    # temname"感应器名称"
                    # temtime"温度时间"
                    # temtem"温度"
                    backdatat = {}
                    backdatat["mac_id"] = now_mc2[0].mac.id
                    backdatat["mac_sty"] = now_mc2[0].mac.mac_type
                    backdatat['mac_st'] = now_mc2[0].temperature
                    backdatat['mac_kind'] = "hu"
                    backdatat['mac_type'] = '2'

                    
                    tem_No = mac2[1].id
                    tem_name = mac2[1].mac_name
                    tem_tem = attributeValue2
                    sethistory.SetHistory().sethumidity(tem_No, tem_name, tem_tem)

                    endpointNumber = mac_detail['endpoints'][0]['endpointNumber']
                    attributeValue = mac_detail['endpoints'][0]['clusters'][0]['attributes'][0]['attributeValue']
                    print("@@@@@@@@@@@@@@@@@@")
                    print(len(mac2))
                    if mac2:
                        print(endpointNumber)
                        print(attributeValue)
                        now_mc = ControlMac.objects.filter(mac=mac2[1],endpointnum=endpointNumber)
                        now_mc.update(temperature=attributeValue)

                    # if mac_detail['type'] == '19':

                    backdata = {}
                    backdata["mac_id"] = now_mc[0].mac.id
                    backdata["mac_sty"] = now_mc[0].mac.mac_type
                    backdata['mac_st'] = now_mc[0].temperature
                    backdata['mac_kind'] = now_mc[0].mac.kind
                    backdata['mac_type'] = '2'
                    print("@@@@@@###$$")
                    tem_No = mac[0].id
                    tem_name = mac[0].mac_name
                    tem_tem = attributeValue
                    sethistory.SetHistory().settempracure(tem_No, tem_name, tem_tem)

                    send_web_msg('', str(backdatat).replace('\'', '\"'))
                    send_web_msg('', str(backdata).replace('\'', '\"'))

                if thire_type=="19":
                    print("@@@@")
                    endpointNumber = mac_detail['endpoints'][0]['endpointNumber']
                    attributeValue = mac_detail['endpoints'][0]['clusters'][0]['attributes'][0]['attributeValue']
                    mac = Machine.objects.filter(mac_devID=devID)
                    print(len(mac))
                    print(mac[0].id)
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
                    # coNo"感应器id"
                    # coname"感应器名称"
                    # cotime"CO2时间"
                    # cotem"co2度"
                    lightNo = mac[0].id
                    lightname = mac[0].mac_name
                    lighttem = attributeValue
                    sethistory.SetHistory().setlight(lightNo, lightname, lighttem)



                if thire_type=="44":
                    endpointNumber = mac_detail['endpoints'][0]['endpointNumber']
                    attributeValue = mac_detail['endpoints'][0]['clusters'][0]['attributes'][0]['attributeValue']
                    mac = Machine.objects.filter(mac_devID=devID)
                    if mac:
                        now_mc = ControlMac.objects.filter(mac=mac[0], endpointnum=endpointNumber)
                        now_mc.update(temperature=attributeValue)
                    # pmNo"感应器id"
                    # pmname"感应器名称"
                    # pmtime"PM2.5时间"
                    # pmtem"PM2.5度"
                       # if mac_detail['type'] == '19':
                    backdata = {}
                    backdata["mac_id"] = now_mc[0].mac.id
                    backdata["mac_sty"] = now_mc[0].mac.mac_type
                    backdata['mac_st'] = now_mc[0].temperature
                    backdata['mac_kind'] = now_mc[0].mac.kind
                    backdata['mac_type'] = '2'
                    print("@@@@@@###$$")
                    send_web_msg('', str(backdata).replace('\'', '\"'))
                    pmNo = mac[0].id
                    pmname = mac[0].mac_name
                    pmtem = attributeValue

                    sethistory.SetHistory().setpm(pmNo, pmname, pmtem)

                if thire_type=="42":
                    print("@@@@")
                    endpointNumber = mac_detail['endpoints'][0]['endpointNumber']
                    attributeValue = mac_detail['endpoints'][0]['clusters'][0]['attributes'][0]['attributeValue']
                    mac = Machine.objects.filter(mac_devID=devID)
                    print(len(mac))
                    print(mac[0].id)
                    if mac:
                        now_mc = ControlMac.objects.filter(mac=mac[0], endpointnum=endpointNumber)
                        now_mc.update(temperature=attributeValue)
                    # coNo"感应器id"
                    # coname"感应器名称"
                    # cotime"CO2时间"
                    # cotem"co2度"
                    # if mac_detail['type'] == '19':
                    backdata = {}
                    backdata["mac_id"] = now_mc[0].mac.id
                    backdata["mac_sty"] = now_mc[0].mac.mac_type
                    backdata['mac_st'] = now_mc[0].temperature
                    backdata['mac_kind'] = now_mc[0].mac.kind
                    backdata['mac_type'] = '2'

                    send_web_msg('', str(backdata).replace('\'', '\"'))
                    coNo = mac[0].id
                    coname = mac[0].mac_name
                    cotem = attributeValue
                    sethistory.SetHistory().setcot(coNo, coname, cotem)

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
                    # lightNo"感应器id"
                    # lightname"感应器名称"
                    # lighttime"光照时间"
                    # lighttem"光照强度"
                    # if mac_detail['type'] == '19':
                    backdata = {}
                    backdata["mac_id"] = now_mc[0].mac.id
                    backdata["mac_sty"] = now_mc[0].mac.mac_type
                    backdata['mac_st'] = now_mc[0].temperature
                    backdata['mac_kind'] = now_mc[0].mac.kind
                    backdata['mac_type'] = '2'
                    print("@@@@@@###$$")
                    send_web_msg('', str(backdata).replace('\'', '\"'))
                    electNo = mac[0].id
                    electname = mac[0].mac_name
                    electtem = str(int(attributeValue[4:10], 16) * 100)
                    sethistory.SetHistory().setelect(electNo, electname, electtem)

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
                thire_type = mac_detail['type']

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
                    # temNo"感应器id"
                    # temname"感应器名称"
                    # temtime"温度时间"
                    # temtem"温度"
                    tem_No = mac2[1].id
                    tem_name = mac2[1].mac_name
                    tem_tem = attributeValue2
                    sethistory.SetHistory().sethumidity(tem_No,tem_name,tem_tem)
                    backdatat = {}
                    backdatat["mac_id"] = now_mc2[0].mac.id
                    backdatat["mac_sty"] = now_mc2[0].mac.mac_type
                    backdatat['mac_st'] = now_mc2[0].temperature
                    backdatat['mac_kind'] = "hu"
                    backdatat['mac_type'] = '2'

                    send_web_msg('', str(backdatat).replace('\'', '\"'))

                    endpointNumber = mac_detail['endpoints'][0]['endpointNumber']
                    attributeValue = mac_detail['endpoints'][0]['clusters'][0]['attributes'][0]['attributeValue']
                    mac = Machine.objects.filter(mac_devID=devID)
                    if mac:

                        now_mc = ControlMac.objects.filter(mac=mac[0],endpointnum=endpointNumber)
                        now_mc.update(temperature=attributeValue)
                    # if mac_detail['type'] == '19':
                    tem_No = mac[0].id
                    tem_name = mac[0].mac_name
                    tem_tem = attributeValue
                    sethistory.SetHistory().settempracure(tem_No, tem_name, tem_tem)

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
                    # pmNo"感应器id"
                    # pmname"感应器名称"
                    # pmtime"PM2.5时间"
                    # pmtem"PM2.5度"
                    pmNo = mac[0].id
                    pmname = mac[0].mac_name
                    pmtem = attributeValue

                    sethistory.SetHistory().setpm(pmNo, pmname, pmtem)

                if thire_type=="19":
                    print("@@@@")
                    endpointNumber = mac_detail['endpoints'][0]['endpointNumber']
                    attributeValue = mac_detail['endpoints'][0]['clusters'][0]['attributes'][0]['attributeValue']
                    mac = Machine.objects.filter(mac_devID=devID)
                    print(len(mac))
                    print(mac[0].id)
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
                    # coNo"感应器id"
                    # coname"感应器名称"
                    # cotime"CO2时间"
                    # cotem"co2度"
                    lightNo = mac[0].id
                    lightname = mac[0].mac_name
                    lighttem = attributeValue
                    sethistory.SetHistory().setlight(lightNo, lightname, lighttem)

                if thire_type=="42":
                    print("@@@@")
                    endpointNumber = mac_detail['endpoints'][0]['endpointNumber']
                    attributeValue = mac_detail['endpoints'][0]['clusters'][0]['attributes'][0]['attributeValue']
                    mac = Machine.objects.filter(mac_devID=devID)
                    print(len(mac))
                    print(mac[0].id)
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
                    # coNo"感应器id"
                    # coname"感应器名称"
                    # cotime"CO2时间"
                    # cotem"co2度"
                    coNo = mac[0].id
                    coname = mac[0].mac_name
                    cotem = attributeValue
                    sethistory.SetHistory().setcot(coNo, coname, cotem)

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
                    # lightNo"感应器id"
                    # lightname"感应器名称"
                    # lighttime"光照时间"
                    # lighttem"光照强度"
                    # if mac_detail['type'] == '19':
                    backdata = {}
                    backdata["mac_id"] = now_mc[0].mac.id
                    backdata["mac_sty"] = now_mc[0].mac.mac_type
                    backdata['mac_st'] = now_mc[0].temperature
                    backdata['mac_kind'] = now_mc[0].mac.kind
                    backdata['mac_type'] = '2'

                    send_web_msg('', str(backdata).replace('\'', '\"'))
                    electNo = mac[0].id
                    electname = mac[0].mac_name
                    electtem = str(int(attributeValue[4:10], 16) * 100)
                    sethistory.SetHistory().setelect(electNo, electname, electtem)

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
