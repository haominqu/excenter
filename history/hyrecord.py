# django
from django.core.exceptions import ObjectDoesNotExist

# self_project
from .models import *

# base
import logging

class RecordManage():

    def AccessRecord(self, user_id, octime, detail):
        """
        desc:出入记录
        :param user_id:
        :param octime:
        :param detail:
        :return:
        """
        try:
            AccessHistory.objects.create(user_id=user_id, octime=octime, detail=detail)
        except ObjectDoesNotExist as e:
            logging.warning(e)
            return False
        return True


    def InviteRecord(self, invite_id, user_id, invitetime):
        """
        desc:邀请记录
        :param invite_id:
        :param user_id:
        :param invitetime:
        :return:
        """
        try:
            InviteHistory.objects.create(invite_id=invite_id, user_id=user_id, invitetime=invitetime)
        except ObjectDoesNotExist as e:
            logging.warning(e)
            return False
        return True


    def UseRecord(self, user_id, mac_id, temtime, detail):
        """
        desc:开关记录
        :param invite_id:
        :param user_id:
        :param invitetime:
        :return:
        """
        try:
            UseHistory.objects.create(userid=user_id, macid=mac_id, temtime=temtime, detail=detail)
        except ObjectDoesNotExist as e:
            logging.warning(e)
            return False
        return True



