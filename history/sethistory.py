from .models import *
from django.core.exceptions import ObjectDoesNotExist
import logging

class SetHistory:

    # userid"用户id"
    # macid"感应器id"
    # temtime"操作时间"
    # detail"操作详情"
    def setuse(self, user_id, mac_id, tem_time, use_detail):
        try:
            UseHistory.objects.create(userid=user_id,macid=mac_id,temtime=tem_time,detail=use_detail)
        except ObjectDoesNotExist as e:
            logging.warning(e)
            return False
        return True

    # temNo"感应器id"
    # temname"感应器名称"
    # temtime"温度时间"
    # temtem"温度"
    def settempracure(self,tem_No,tem_name,tem_tem):
        try:
            TemperatureHistory.objects.create(temNo=tem_No,temname=tem_name,temtem=tem_tem)
        except ObjectDoesNotExist as e:
            logging.warning(e)
            return False
        return True

    # humNo"感应器id"
    # humname"感应器名称"
    # humtime"湿度时间"
    # humtem"湿度"
    def sethumidity(self,hum_No,hum_name,hum_time,hum_tem):
        try:
            HumidityHistory.objects.create(humNo=hum_No,humname=hum_name,humtime=hum_time,humtem=hum_tem)
        except ObjectDoesNotExist as e:
            logging.warning(e)
            return False
        return True

    # coNo"感应器id"
    # coname"感应器名称"
    # cotime"CO2时间"
    # cotem"co2度"
    def setcot(self,co_No,co_name,co_tem):

        try:
            COtHistory.objects.create(coNo=co_No,coname=co_name,cotem=co_tem)
        except ObjectDoesNotExist as e:
            logging.warning(e)
            return False
        return True

    # pmNo"感应器id"
    # pmname"感应器名称"
    # pmtime"PM2.5时间"
    # pmtem"PM2.5度"
    def setpm(self,pm_No,pm_name,pm_tem):

        try:
            PMHistory.objects.create(pmNo=pm_No,pmname=pm_name,pmtem=pm_tem)
        except ObjectDoesNotExist as e:
            logging.warning(e)
            return False
        return True

    # lightNo"感应器id"
    # lightname"感应器名称"
    # lighttime"光照时间"
    # lighttem"光照强度"
    def setlight(self,light_No,light_name,light_tem):
        try:
            LigthHistory.objects.create(lightNo=light_No,lightname=light_name,lighttem=light_tem)
        except ObjectDoesNotExist as e:
            logging.warning(e)
            return False
        return True


    # electNo"感应器id"
    # electname"感应器名称"
    # electttime"时间"
    # electtem"电力使用"
    def setelect(self,electNo,electname,electtem):
        try:
            ElectHistory.objects.create(electNo=electNo,electname=electname,  electtem=electtem)
        except ObjectDoesNotExist as e:
            logging.warning(e)
            return False
        return True

    def setinvite(self):
        InviteHistory.objects.create()
        pass

