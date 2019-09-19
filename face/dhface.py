from django.conf import settings
from userinfo.models import Guest
from userinfo.fourrandom import generate_code
from urllib import parse
from urllib import request
import uuid
import base64
import requests
import os
import json
import time


class FaceManage():

    def face_regist(self, guest_id):
        url = "http://10.11.30.89:25000/service"
        action = "addface"
        guest = Guest.objects.filter(id=guest_id)
        faceid = int(str(guest[0].id) + generate_code())
        realname = guest[0].realname
        face_db_path = guest[0].face_picture
        face_path = "/media" + str(face_db_path)
        abs_path = settings.BASE_DIR + face_path
        with open(abs_path, 'rb') as f:
            face_base64 = base64.b64encode(f.read())
        payload = {'action': action, 'faceid': faceid, 'base64': face_base64, 'realname':realname}
        response = requests.post(url=url, data=payload)
        return response.text
        # status = eval(response.text)['status']
        # print(status)
        # if status == 0:
        #     return True
        # elif status == -1:
        #     pass
        # elif status == -2:
        #     pass
        # elif status == -3:
        #     pass
        # elif status == -4:
        #     pass
        # else:
        #     return False



